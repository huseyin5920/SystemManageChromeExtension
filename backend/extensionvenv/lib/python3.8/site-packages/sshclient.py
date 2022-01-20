#!/usr/bin/python
import json
import os
import stat
import traceback
from StringIO import StringIO
from contextlib import contextmanager

import logging
import paramiko
import time

from urlparse import urlparse

class SshClient:
    """A wrapper of paramiko.SSHClient"""
    TIMEOUT = 1

    def __init__(self, host, port=22, username=None, password=None, key=None, passphrase=None):
        """
        SshClient provides a thin wrapper around paramiko for some convienience
        
        
        :param host: the hostname to connect to , this may optionally provide a <user><:pass>@host<:port> 
        :param port: default 22
        :param username: the username to connect with
        :param password: the password to use this is required if you want to do ANY sudo commands and the user is not added to the NOPASSWD stuff in /etc/sudoers
        :param key: optional openssh key to use
        :param passphrase: the passphrase for the included key 
        """
        if username:
            self.username = username
        if password:
            self.password = password
        parsed = urlparse(host)
        if not parsed.hostname:
            parsed = urlparse("sftp://"+host)
        if parsed.username:
            self.username = parsed.username
        if parsed.password:
            self.password = parsed.password
        if parsed.port:
            port = parsed.port
        if parsed.hostname:
            host = parsed.hostname
        print self.username
        print self.password
        self.host = (host,port)
        print self.host
        if key is not None:
            # noinspection PyTypeChecker
            try:
                key = paramiko.RSAKey.from_private_key(open(key,"rb"), password=passphrase)
            except:
                try:
                    key = paramiko.RSAKey.from_private_key(StringIO(key), password=passphrase)
                except:
                    raise Exception("Unknwon Key!!!!!")

        self.key = key
        self.connect(self.host[0], self.host[1], username=self.username, password=self.password, key=key)

    def reconnect(self):
        self.connect(self.host[0],self.host[1],self.username,self.password,self.key)

    def connect(self, host, port, username, password, key=None,retries=3):
        """
        
        :param host: just the hostname portion (ie the ip address or registered hostname (DO NOT include scheme etc) 
        :param port: the port to connect to (this is usually 22)
        :param username: the username
        :param password: the password for that username
        :param key: optional instance of :py_class: paramiko.RSAKey
        :param retries: how many retries
        :return: 
        """
        logging.info("CONNECT TO: %s:%s"%(host,port))
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            self.client.connect(host, port, username=username, password=password, pkey=key, timeout=self.TIMEOUT+3-retries)
        except:
            if retries:
                time.sleep(1)
                return self.connect(host,port,username,password,key,retries-1)
            traceback.print_exc()
            raise Exception("Unable To Connect to %r:%r"%(host,port))

    def close(self):
        if self.client is not None:
            self.client.close()
            self.client = None

    def execute(self, command, sudo=False,**kwargs):
        """
        run a given comand against the remote server
        
        :param command: the shell command to run against the remote server
        :param sudo: should this command run as sudo 
        :param kwargs: any optional kwargs to pass to :py_class: paramiko.SSHClient
        :return: a dict of {out:stdout, err:stderr, retval: return_code}
        """
        feed_password = False
        logging.info("EXECUTE: %r"%(command if not sudo else "sudo "+command))
        if sudo and self.username != "root":
            command = "sudo -S -p '' %s" % command
            feed_password = self.password is not None and len(self.password) > 0
        stdin, stdout, stderr = self.client.exec_command(command,**kwargs)
        if feed_password:
            stdin.write(self.password + "\n")
            stdin.flush()
        response =  {'out': stdout.readlines(),
                'err': stderr.readlines(),
                'retval': stdout.channel.recv_exit_status()}
        if response["retval"]:
            logging.getLogger("test_log").warn("ERROR[%s] RETURNED: %r"%(response['retval'],"".join(response['err'])))
        else:
            logging.getLogger("test_log").info("STDOUT: %r"%"".join(response['out'])[-150:])
        return response
    @contextmanager
    def _get_sftp(self):
        yield paramiko.SFTPClient.from_transport(self.client.get_transport())
    def remote_write(self,remote_file_path,msg):
        """
        write a simple string into a remote file, this will always OVERWRITE the file if it already exists
        :param remote_file_path: the remote path to write to
        :param msg: the string to write
        :return: None
        """
        logging.info("writing %r => %r"%(msg,remote_file_path))
        with self._get_sftp() as sftp:
            with sftp.open(remote_file_path,"wb") as f:
                if isinstance(msg,basestring):
                    f.write(msg)
                elif hasattr(msg,"read"):
                    f.write(msg.read())
                else:
                    f.write(json.dumps(f))
    def remote_open(self,remote_file_path,open_mode):
        """
        Open a remote file for reading or writing or apending
        
        :param remote_file_path: 
        :param open_mode: 
        :return: remote file handle 
        """
        with self._get_sftp() as sftp:
            return sftp.open(remote_file_path,open_mode)
    def download_file(self,remote_path,local_path):
        """
        download a remote file to the local system
        
        :param remote_path: 
        :param local_path: 
        :return: 
        """
        logging.info("DOWNLOAD %r=>%r"%(remote_path,local_path))
        with self._get_sftp() as sftp:
            return sftp.get(remote_path,local_path)

    def remote_glob(self,remote_pattern):
        """
        equivelent to glob.glob, except on the remote filesystem
        
        :param remote_pattern: 
        :return: 
        """
        return map(lambda x:x.strip(),self.execute("ls %s"%(remote_pattern,)).get("out",[]))
    def remote_read(self,remote_path):
        """
        return the contents of a remote file(note that this will not open a file in binary mode)
        
        :param remote_path: 
        :return: 
        """
        with self._get_sftp() as sftp:
            try:
                return sftp.open(remote_path).read()
            except IOError:
                return None

    def remote_path_exists(self,remote_path):
        """
        same as :py_func: os.path.exists, except it targets a remote filesystem
         
        :param remote_path: 
        :return: boolean  
        """
        with self._get_sftp() as sftp:
            try:
                return bool(sftp.stat(remote_path))
            except:
                return False
    def upload(self,local_file_path,remote_file_path):
        """
        upload a local file to the remote filesystem. NOTE that the user MUST have the appropriate write permissions
        
        :param local_file_path: 
        :param remote_file_path: 
        :return: 
        """
        if os.path.isdir(local_file_path):
            return self.upload_dir(local_file_path,remote_file_path)
        with self._get_sftp() as sftp:
            logging.info("Upload %r=>%r" % (local_file_path, remote_file_path))
            sftp.put(local_file_path,remote_file_path)
    def upload_dir(self,local_path,remote_path):
        """
        upload a complete local directory to a remote directory
        
        :param local_path: 
        :param remote_path: 
        :return: 
        """
        with self._get_sftp() as sftp:
            try:
                sftp.mkdir(remote_path)
            except:
                print "CANNOT CREATE DIR: %r"%remote_path
            for curdir,dirs,files in os.walk(local_path):
                for file in files:
                    remote_dir =(remote_path.rstrip("/\\")+"/"+curdir.split(local_path)[-1].replace("\\","/").strip("/"))
                    try:
                        sftp.mkdir(remote_dir)
                    except:
                        #traceback.print_exc()
                        #print "CANNOT CREATE DIR: %r"%remote_dir
                        try:
                            if stat.S_ISDIR(sftp.stat(remote_dir).st_mode):
                                logging.debug("DIRECTORY '%r' EXISTS , SKIP CREATE" % remote_dir)
                        except:
                            pass
                    local_file_path,remote_file_path = os.path.join(curdir,file),remote_dir+"/"+file
                    logging.info("Upload %r=>%r" % (local_file_path, remote_file_path))
                    sftp.put(local_file_path,remote_file_path)



