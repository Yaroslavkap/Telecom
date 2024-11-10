FROM registry.astralinux.ru/library/astra/ubi18-python311:latest

RUN apt update && apt install -y python3.11-venv
RUN apt-get update && apt-get install -y postgresql-client python3.11-venv netcat-openbsd

WORKDIR /servicedb

COPY . /servicedb

RUN python3 -m venv venv
RUN . venv/bin/activate && pip install --no-cache-dir -r requirements.txt

# CMD ["sh", "-c", "echo 'Waiting 40 seconds...' && sleep 40 && venv/bin/python -u app.py"]
RUN curl -sSL https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh -o /usr/local/bin/wait-for-it && chmod +x /usr/local/bin/wait-for-it

CMD ["sh", "-c", "wait-for-it db:5432  -t 40 -- wait-for-it rabbitmq:5672  -t 40 -- venv/bin/python -u app.py"]

