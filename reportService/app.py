from flask import Flask

from api import cpuUsageControlApi

app = Flask(__name__)

# JWT Config


app.add_url_rule('/report', methods=['GET'], view_func=cpuUsageControlApi.cpuRe)
app.add_url_rule('/journalctl', methods=['GET'], view_func=cpuUsageControlApi.journalctlReport)


def main():
    app.run(debug=True, use_reloader=False)


if __name__ == "__main__":

    main()