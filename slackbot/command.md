pip3 install -r requirements.txt
pip3 freeze 

python3 manage.py makemigrations
python3 manage.py migrate

python3 manage.py runserver


python3 manage.py parse
python3 manage.py delete

echo "hello">"hello.txt"

celery -A slackbot worker -l INFO

wsl --shutdown