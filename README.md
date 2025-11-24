SmartConsulta - Django project

Setup:
1. python -m venv venv
   venv\Scripts\activate
2. venv\Scripts\activate   (Windows) or source venv/bin/activate
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py createsuperuser
6. python manage.py runserver

Admin: http://127.0.0.1:8000/admin/  Login: use superuser
Home: http://127.0.0.1:8000/
Agendamentos (calendar): http://127.0.0.1:8000/agendamentos/
