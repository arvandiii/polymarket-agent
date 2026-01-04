FROM python:3.9

COPY . /home
WORKDIR /home

RUN make install
CMD ["make", "run"]
