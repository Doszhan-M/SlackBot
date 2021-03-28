pip install -r requirements.txt
pip freeze > requirements.txt

python3 manage.py makemigrations
python3 manage.py migrate

python3 manage.py runserver


python manage.py parse

echo "hello">"hello.txt"