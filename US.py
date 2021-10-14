from flask import Flask, request, redirect, url_for
app = Flask(__name__)

@app.route('/fibonacci', methods = ["GET"])
def user():
	hostname = request.args.get('hostname' , None)
	fs_post = request.args.get('fs_port' , None)
	number = request.args.get('number' , None)
	as_ip = request.argsget('as_ip' , None)
	as_port = request.args.get('as_port', None)
	if hostname == None or fs_port == None or number == None or as_ip == None or as_port == None:
		return "Parameter Missing" , 400
	return f"{hostname} {fs_port} {number} {as_ip} {as_port}"

app.run(host = '0.0.0.0',
	port = 8080
	debug=True
	)