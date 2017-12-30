from celery import Celery
import subprocess,time


app = Celery('tasks',
             broker='redis://192.168.4.13',
             backend='redis://192.168.4.13')


@app.task
def add(x, y):
    print("running...", x, y)
    return x + y

@app.task
def run_cmd(cmd):
    print("run cmd ...",cmd)
    time.sleep(5)
    cmd_obj = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    return cmd_obj.stdout.read().decode("utf-8")
