run:
	venv/bin/python project/manage.py runserver
fun:
	venv/bin/python project/manage.py runserver_socketio
migrate:
	venv/bin/python project/manage.py migrate
makemigrations:
	venv/bin/python project/manage.py makemigrations
reqs:
	venv/bin/pip install -r requirements/development.txt
gunicorn:
	cd project && gunicorn --worker-class socketio.sgunicorn.GeventSocketIOWorker project.wsgi:application &
