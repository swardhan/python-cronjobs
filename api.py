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
	"minute": "0",
	"hour": "0",
	"dom": "0",
	"mon": "0",
	"dow": "0"
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
		return jsonify({"result": "Backup Already Running"})
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
		return jsonify({"result": "Error occured"})


@app.route('/db/change_time', methods=['POST'])
def change():
	change_time(user_time=user_time)
	return "Change Time"

if __name__ == '__main__':
	app.run(port=5000, debug=True)