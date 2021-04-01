pip3 install -r requirements.txt
pip3 freeze 

python3 manage.py makemigrations
python3 manage.py migrate

python3 manage.py runserver


python3 manage.py parse
python3 manage.py delete

echo "hello">"hello.txt"

celery -A slackbot worker -l INFO

xoxb-1900575918485-1903110096709-oQuJPQ5j0uJtwg3QV6AwPwjX
wsl --shutdown