FROM flask
ADD . /datgatto
WORKDIR /datgatto
CMD python database_initialize.py & python app.py