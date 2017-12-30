from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery('tasks',
             broker='redis://192.168.4.13',
             backend='redis://192.168.4.13',
             include=['proj.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()