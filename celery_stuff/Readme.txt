学习url http://www.cnblogs.com/alex3714/p/6351797.html

celery -A tasks worker --loglevel=info

celery -A proj worker -l info

(examples) [root@rhel7-ops celery_stuff]# celery multi start demoname -A  proj -l info
celery multi v4.1.0 (latentcall)
> Starting nodes...
	> demoname@rhel7-ops: OK
	> worker@rhel7-ops: OK
(examples) [root@rhel7-ops celery_stuff]# celery multi start demoname2 -A  proj -l info
celery multi v4.1.0 (latentcall)
> Starting nodes...
	> demoname2@rhel7-ops: OK
	> worker@rhel7-ops: OK
ERROR: Pidfile (worker.pid) already exists.
Seems we're already running? (pid: 6555)

 celery  multi restart w1 -A proj -l info
  celery  multi stop  w1


  ps -elf |grep celery |awk '{ print $4 }'|xargs kill

celery -A tasks worker --loglevel=info

启动任务调度器 celery beat
 celery -A periodic_task beat