# export SECRET_KEY=bxxfcxa43xf7xd9xc6xefxf8c

# python manage.py server
export SECRET_KEY=os.environ.get
export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://dunco:dunco@localhost/pitch
export MAIL_USERNAME=aruncodunco@gmail.com
export MAIL_PASSWORD=31740141

python3.6 manage.py server