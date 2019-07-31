from flask import Flask, render_template, request, jsonify
from job import start, stop, change_time

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

user_time = {
	"minute": "*",
	"hour": "*",
	"dom": "*",
	"mon": "*",
	"dow": "*"
}

command = "mongodump"

app = Flask(__name__)

@app.route('/')
def index():
	return "Hi!"

@app.route('/db/start', methods=['POST'])
def start_backup():
	ret_val = start()
	if ret_val:		
		return jsonify({"result": "Default Backup Already Running"})
	else:		
		return jsonify({"result": "Started at %s" % default_time})


#For stopping default Cron Job comment should be 'mongobackup'
#For stopping user defined Cron Job comment Should be 'user_mongobackup'
#comments are the only way to differentiate between two jobs
@app.route('/db/stop', methods=['POST'])
def stop_backup():
	data = request.get_json()
	request_comment = data["comment"]
	ret_val = stop(comment=request_comment)
	if ret_val:		
		return jsonify({"result": "Stopped #%s" % request_comment})
	else:
		return jsonify({"result": "Running job for Backup not Found"})


@app.route('/db/change_time', methods=['POST'])
def change():
	data = request.get_json()
	request_time = data["user_time"]
	print(request_time)
	change_time(time=request_time)
	return jsonify({"result": "Started Job for Another Backup at #%s" % request_time})

if __name__ == '__main__':
	app.run(port=5000, debug=True)