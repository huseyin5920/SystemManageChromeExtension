from flask import Flask
from constants import constants
from api import topCommandApi

app = Flask('app')
app.add_url_rule('/memory', view_func=topCommandApi.topCommandByMemory, methods=["GET"])
app.add_url_rule('/cpu', view_func=topCommandApi.topCommandByCpu, methods=["GET"])
app.add_url_rule('/listUsers', view_func=topCommandApi.topCommandListUsers, methods=["GET"])
app.add_url_rule('/currentUser', view_func=topCommandApi.topCommandByCurrentUser, methods=["GET"])
app.add_url_rule('/listByUserCpu', view_func=topCommandApi.topCommandListByUserCpu, methods=["POST"])
app.add_url_rule('/listByUserMemory', view_func=topCommandApi.topCommandListByUserMemory, methods=["POST"])

if __name__ == '__main__':
    app.run(constants.FLASK_HOST, constants.FLASK_PORT, debug=True)
