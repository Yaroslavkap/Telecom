
FROM registry.astralinux.ru/library/astra/ubi18-python311:latest


RUN apt update && apt install -y python3.11-venv


WORKDIR /back
COPY . /back

RUN python3 -m venv venv
RUN . venv/bin/activate && pip install --no-cache-dir -r requirements.txt

EXPOSE 8888
CMD ["sh", "-c", "echo 'Waiting 40 seconds...' && sleep 40 && venv/bin/python -u back.py"]