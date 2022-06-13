from challenge.celery import app


@app.task(name='add')
def add(x, y):
    return x + y