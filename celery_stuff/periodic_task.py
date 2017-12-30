from celery import Celery
from celery.schedules import crontab

app = Celery('tasks',
             broker='redis://192.168.4.13',
             backend='redis://192.168.4.13',
             include=['proj.tasks'])


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # 每10 秒执行一次.
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

    # lls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
       crontab(hour=7, minute=30, day_of_week=1),
       test.s('Happy Mondays!'),
    )


@app.task
def test(arg):
    print(arg)