FROM kubeless/python:3.6

RUN pip install kubernetes jinja2
RUN  curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.10.0/bin/linux/amd64/kubectl && \
    mv kubectl /usr/local/bin && \
    chmod a+x /usr/local/bin/kubectl

COPY . .

CMD ["python", "server.py"]

