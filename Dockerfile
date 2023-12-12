FROM python:3.9.17
WORKDIR /flask_service
EXPOSE 5000
COPY . .
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
ENV FLASK_DEBUG=True \
    FLASK_APP=run.py \
    FLASK_RUN_HOST=0.0.0.0 \
    FLASK_ENV=development \
    SECRET_KEY=b'#q)\\x00\xd6\x9f<iBQ\xd7;,\xe2E' \
    JWT_SECRET_KEY=b'#q)\\x00\xd6\x9f<iBQ\xd7;,\xe2E' \
    MYSQL_USER_NAME=test \
    MYSQL_USER_PASSWORD=123456 \
    MYSQL_HOSTNAME=172.17.0.1 \
    MYSQL_PORT=3306 \
    MYSQL_DATABASE_NAME=flask_test

RUN flask db migrate
RUN flask db upgrade
CMD ["flask", "run"]