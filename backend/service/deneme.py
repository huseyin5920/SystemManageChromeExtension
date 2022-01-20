import subprocess, sys, re
from io import StringIO
import pandas as pd

def main(argv):
    output = subprocess.check_output(['top', "-bn1", "-o", "%CPU"])
    print(output.decode())
    match = re.match(r'^[\w\W]*?\n( +PID.*COMMAND)\n([\w\W]*)', output.decode())

            # df = pd.read_fwf(
            # StringIO(data),
            # colspecs=[(0, 7),  # PID
            #           (7, 16),  # USER
            #           (16, 20),  # PR
            #           (19, 22),  # NI
            #           (25, 32),  # VIRT
            #           (32, 39),  # RES
            #           (40, 46),  # SHR
            #           (48, 56),  # CPU
            #           (57, 61),  # MEM
            #           (61, 70),  # TIME
            #           (71, 999)],  # COMMAND
            # names=['PID', 'USER', 'PR', 'NI', 'VIRT', 'RES', 'SHR', 'CPU', 'MEM', 'TIME', 'COMMAND'])


    df = pd.read_fwf( StringIO(output.decode())
        , colspecs=[(0, 7),  # PID
                      (7, 16),  # USER
                      (16, 20),  # PR
                      (19, 22),  # NI
                      (25, 32),  # VIRT
                      (32, 39),  # RES
                      (40, 46),  # SHR
                      (48, 56),  # CPU
                      (57, 61),  # MEM
                      (61, 70),  # TIME
                      (71, 999)]
        , names=['PID', 'USER', 'PR', 'NI', 'VIRT', 'RES', 'SHR', 'CPU', 'MEM', 'TIME', 'COMMAND'])

    print(df.to_dict(orient='index'))

    return df.to_dict(orient='index')

if __name__ == '__main__':
    main(sys.argv[1:])