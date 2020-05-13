import logging
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

# if __name__ != '__main__':
#     # 如果不是直接运行，则将日志输出到 gunicorn 中
#     gunicorn_logger = logging.getLogger('gunicorn.error')
#     app.logger.handlers = gunicorn_logger.handlers
#     app.logger.setLevel(gunicorn_logger.level)
#


if __name__ == '__main__':
    app.run()
