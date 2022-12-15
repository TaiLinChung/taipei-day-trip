from flask import *
from flask import jsonify
import mysql.connector.pooling

dbconfig={
	"user":"root",
	"password":"Bb0970662139",
	"host":"localhost",
	"database":"taipei_day_trip",
}
#	create connection pool
connection_pool = mysql.connector.pooling.MySQLConnectionPool(
	pool_name="wehelp_pool",
	pool_size=5,
	pool_reset_session=True,
	**dbconfig
)


#相應app.py
booking_blueprint=Blueprint("booking_blueprint",__name__)
bookingResponse=None
from model import DealBooking
from model import GetDataForBookingPage
from model import DeleteDataForBookingPage
secret_key = "wehelpJwtKEY@999"
import jwt
@booking_blueprint.route("/api/booking",methods=["POST","GET","DELETE"])
def api_booking():
	if request.method=="POST":
		try:
			getToken=request.cookies.get("token")
			decoded=jwt.decode(getToken,secret_key,algorithms='HS256')     #decode-algorithms
			personId=decoded["data"]["id"]
			bookingDataFromFrontEnd = request.get_json() 
			response=DealBooking(bookingDataFromFrontEnd,personId)
			return (response)
		except:
			return jsonify({"error": True,"message":"未登入系統，拒絕存取"})

	if request.method=="GET":
		try:
			getToken=request.cookies.get("token")
			decoded=jwt.decode(getToken,secret_key,algorithms='HS256')     #decode-algorithms
			username=decoded["data"]["name"]
			personId=decoded["data"]["id"]
			print("7777777777777",username)
			response=GetDataForBookingPage(username,personId)
			print("88888")
			return response
		except:
			print("except")
			return jsonify({"error":True})
	
	if request.method=="DELETE":
		try:
			getToken=request.cookies.get("token")
			decoded=jwt.decode(getToken,secret_key,algorithms='HS256')     #decode-algorithms
			personId=decoded["data"]["id"]
			# print("DDDDDDDD")
			attractionId= request.get_json()["attractionId"]
			print("77777777777",attractionId)
			DeleteDataForBookingPage(attractionId,personId)
			return jsonify({"ok":True})
		except:
			return jsonify({"error": True,"message":"未登入系統，拒絕存取"})

