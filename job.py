from crontab import CronTab

user = "swardhan"
host = "localhost"
port = 27017
comment = "mongobackup"
default_time = {
	"minute": "*",
	"hour": "*",
	"dom": "*",
	"mon": "*",
	"dow": "*"
}

command = "mongodump"

#Checks if the Job already doesn't exist and then starts it
def start(user=user, time=default_time):
	my_cron = CronTab(user=user)
	command = "mongodump"
	flag = False
	for job in my_cron:
		if job.comment == "mongobackup":
			flag = True
			break
	if not flag: 
		job = my_cron.new(command=command, comment="mongobackup")
		job.setall(time["minute"], time["hour"], time["dom"], time["mon"], time["dow"])
	my_cron.write()
	return flag

def stop(user=user, comment=comment):
	my_cron = CronTab(user=user)
	flag = False
	for job in my_cron:
		if job.comment == comment:
			flag = True
			my_cron.remove(job)
	my_cron.write()
	return flag

def change_time(user=user, time):
	my_cron = CronTab(user=user)
	job = my_cron.new(command=command, comment="user_mongobackup")
	job.setall(time["minute"], time["hour"], time["dom"], time["mon"], time["dow"])
	my_cron.write()


