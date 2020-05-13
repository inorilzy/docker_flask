FROM python
WORKDIR /flask_application/
COPY requirements.txt /flask_application/
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
EXPOSE 8000
CMD ["gunicorn","app:app","-c","gunicorn_config.py"]