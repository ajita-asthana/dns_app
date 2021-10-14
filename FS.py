from flask import Flask, request, redirect url_for 
app = Flask(__name__)

@app.route('/register' , methods = ["PUT"])
def register():
	content = request.get_json()
	hostname = content.get('hostname')
	ip = content.get('ip')
	as_ip = content.get('as_ip')
	as_port = content.get('as_port')
	print(hostname)
	return f"{hostname} {ip} {as_ip} {as_port}"


@app.route('/fibonacci' , methods = ["GET"])
def fibonacci():
	number = int(request.args.get('number', None))
	if type(number) != int:
		return "Bad Format!", 400
	num_list = [0,1]
	if number > 2:
		for i in range (2, number):
			num_list.append(num_list[i-1] + num_list[i-2])
	return f"{num_list[number-1]}"


app.run(host='0.0.0.0',
	port = 9090,
	debug=True)