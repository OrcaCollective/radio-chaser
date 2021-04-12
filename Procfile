release: flask db upgrade
web: gunicorn radio_chaser.app:create_app\(\) -b 0.0.0.0:$PORT -w 3
