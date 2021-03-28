pip install -r requirements.txt
pip freeze > requirements.txt

python3 manage.py makemigrations
python3 manage.py migrate

python3 manage.py runserver


python manage.py parse
python3 manage.py delete

echo "hello">"hello.txt"