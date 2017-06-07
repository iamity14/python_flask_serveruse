from flask import Flask,request,jsonify


app = Flask(__name__)


@app.route('/game1', methods=['GET','POST'])
def index():
    result = "game play"
    return jsonify([
	{
	"id" : "1",
	"mcname" : "machine1",
	"items" : [
	{
	"item_name" : "frooti",
	"item_cost"	: "10",
	"item_stock" : "5"
	},
	{
	"item_name" : "bisleri",
	"item_cost"	: "20",
	"item_stock" : "4"
	},
	{
	"item_name" : "snacks",
	"item_cost"	: "30",
	"item_stock" : "2"
	}
	]
	},
	{
	"id" : "2",
	"mcname" : "machine2",
	"items" : [
	{
	"item_name" : "frooti Mid2",
	"item_cost"	: "10",
	"item_stock" : "5"
	},
	{
	"item_name" : "bisleri Mid2",
	"item_cost"	: "20",
	"item_stock" : "4"
	},
	{
	"item_name" : "snacks Mid2",
	"item_cost"	: "30",
	"item_stock" : "2"
	}
	]
	},
	{
	"id" : "3",
	"mcname" :"machine3",
	"items" : [
	{
	"item_name" : "frooti Mid3",
	"item_cost"	: "10",
	"item_stock" : "5"
	},
	{
	"item_name" : "bisleri Mid3",
	"item_cost"	: "20",
	"item_stock" : "4"
	},
	{
	"item_name" : "snacks Mid3",
	"item_cost"	: "30",
	"item_stock" : "2"
	}
	]
	}
])

@app.route('/t123', methods=['POST'])
def processjson():
    value = request.form["id22"]
    return value


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)
	#app.run(debug=True)