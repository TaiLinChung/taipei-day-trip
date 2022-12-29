from flask import *
from flask import jsonify

#blueprint引入--------------------------------------------
from view.attractions import attractions_blueprint
from view.attraction_id import attraction_id_blueprint
from view.categories import categories_blueprint
from view.user import user_blueprint
from view.user import user_auth_blueprint
from view.booking import booking_blueprint
from view.orders import orders_blueprint
from view.orders import order_num_blueprint
from view.thankyou import thankyou_blueprint
from view.member import members_blueprint
from view.member import member_id_blueprint

app=Flask(__name__)
app.config["JSON_AS_ASCII"]=False
app.config["TEMPLATES_AUTO_RELOAD"]=True




# Pages
@app.route("/")
def index():
	return render_template("index.html")
@app.route("/attraction/<id>")
def attraction(id):
	# 參考WEEK04把網址id訊息丟給前端
	return render_template("attraction.html")
@app.route("/booking")
def booking():
	return render_template("booking.html")
@app.route("/thankyou")
def thankyou():
	return render_template("thankyou.html")
@app.route("/member")
def member():
	# 參考WEEK04把網址id訊息丟給前端
	return render_template("member.html")


# api user
app.register_blueprint(user_blueprint)
app.register_blueprint(user_auth_blueprint)
app.register_blueprint(attractions_blueprint)
app.register_blueprint(attraction_id_blueprint)
app.register_blueprint(categories_blueprint)
app.register_blueprint(booking_blueprint)
app.register_blueprint(orders_blueprint)
app.register_blueprint(order_num_blueprint)
app.register_blueprint(thankyou_blueprint)
app.register_blueprint(members_blueprint)
app.register_blueprint(member_id_blueprint)



app.run(host='0.0.0.0',port=3000)






