FROM debian
RUN apt update -y  && apt install -y python3 python3-pip && pip3 install flask
COPY main.py /
RUN chmod +x /main.py

CMD ["/usr/bin/python3","/main.py"]