from celery import Celery

app = Celery('tasks' , broker = "amqp://guest:guest@localhost/virhost")
