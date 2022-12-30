from flask import *
from flask import jsonify

#相應app.py
booking_blueprint=Blueprint("booking_blueprint",__name__)


from model import jwt_decode
from model import booking_data_is_empty
from model import booking_people_exist
from model import update_booking_data
from model import insert_booking_data
from model import get_data_for_booking_page
from model import delete_data_for_bookin_page
@booking_blueprint.route("/api/booking",methods=["POST","GET","DELETE"])
def api_booking():
	if request.method=="POST":
		try:
			get_token=request.cookies.get("token")
			decode=jwt_decode(get_token)
			person_id=decode["data"]["id"]
			# 驗證booking流程
			booking_information = request.get_json()
			booking_attraction_id = booking_information["attractionId"]
			booking_date=booking_information["date"]
			booking_price=booking_information["price"]
			booking_time=booking_information["time"]
			if booking_data_is_empty(booking_attraction_id,booking_date,booking_price,booking_time):
				return jsonify({"error": True,"message": "booking資料皆不可為空"})
			if booking_people_exist(person_id):
				update_booking_data(booking_attraction_id,booking_date,booking_price,booking_time,person_id)
			else:
				insert_booking_data(booking_attraction_id,booking_date,booking_price,booking_time,person_id)
			return jsonify({"ok":True})
		except:
			return jsonify({"error": True,"message": "booking伺服器內部錯誤"})


	if request.method=="GET":
		try:
			# 驗證token  待辦 新增驗證存放在資料庫的token
			get_token=request.cookies.get("token")
			decode=jwt_decode(get_token)
			print(decode)
			username=decode["data"]["name"]
			person_id=decode["data"]["id"]
			response=get_data_for_booking_page(username,person_id)
			print(response)
			return jsonify(response)
		except:
			return jsonify({"error": True,"message": "booking伺服器內部錯誤"})


	if request.method=="DELETE":
		try:
			get_token=request.cookies.get("token")
			decode=jwt_decode(get_token)
			person_id=decode["data"]["id"]
			attractio_id= request.get_json()["attractionId"]
			delete_data_for_bookin_page(attractio_id,person_id)
			return jsonify({"ok":True})
		except:
			return jsonify({"error": True,"message": "booking伺服器內部錯誤"})













	# if request.method=="POST":
	# 	try:
	# 		getToken=request.cookies.get("token")
	# 		decoded=jwt.decode(getToken,secret_key,algorithms='HS256')     #decode-algorithms
	# 		personId=decoded["data"]["id"]
	# 		bookingDataFromFrontEnd = request.get_json() 
	# 		response=deal_Booking(bookingDataFromFrontEnd,personId)
	# 		return (response)
	# 	except:
	# 		return jsonify({"error": True,"message":"未登入系統，拒絕存取"})

	# if request.method=="GET":
	# 	try:
	# 		getToken=request.cookies.get("token")
	# 		decoded=jwt.decode(getToken,secret_key,algorithms='HS256')     #decode-algorithms
	# 		username=decoded["data"]["name"]
	# 		personId=decoded["data"]["id"]
	# 		print("7777777777777",username)
	# 		response=GetDataForBookingPage(username,personId)
	# 		print("88888")
	# 		return response
	# 	except:
	# 		print("except")
	# 		return jsonify({"error":True})
	
	# if request.method=="DELETE":
	# 	try:
	# 		getToken=request.cookies.get("token")
	# 		decoded=jwt.decode(getToken,secret_key,algorithms='HS256')     #decode-algorithms
	# 		personId=decoded["data"]["id"]
	# 		# print("DDDDDDDD")
	# 		attractionId= request.get_json()["attractionId"]
	# 		print("77777777777",attractionId)
	# 		DeleteDataForBookingPage(attractionId,personId)
	# 		return jsonify({"ok":True})
	# 	except:
	# 		return jsonify({"error": True,"message":"未登入系統，拒絕存取"})

