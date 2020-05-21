FROM python

RUN mkdir /src

WORKDIR /src

COPY . /src

EXPOSE 8081

CMD python ./mypython.py
