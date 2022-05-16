cd challenge
pip3 install -r requirements.txt
docker-compose up -d
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver