# fitnessapp
- python -m venv dev-env
- source dev-env/bin/activate
- pip install -r requirements.txt
- python manage.py runserver


- python manage.py makemigrations
- python manage.py migrate
- python manage.py migrate --run-syncdb

- ./manage.py shell
>> `user = User.objects.create(id=1, user_name="reshavabraham", first_name="Reshav", last_name="Abraham", email="reshavabraham@gmail.com")`