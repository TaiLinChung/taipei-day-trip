from flask import *
from flask import jsonify
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Bb0970662139")


mycursor2=mydb.cursor()
sql="CREATE DATABASE IF NOT EXISTS taipei_day_trip"
mycursor2.execute(sql)
sql="USE taipei_day_trip"
mycursor2.execute(sql)

# ========================	build index for data3	========================
# sql="ALTER TABLE datas3 DROP INDEX ON data3 IF EXISTS"
# mycursor2.execute(sql)
try:
	sql="ALTER TABLE datas3 DROP INDEX attractionId_index"
	mycursor2.execute(sql)
except:
	sql="ALTER TABLE datas3 ADD INDEX attractionId_index(id)"
	mycursor2.execute(sql)
sql="CREATE TABLE IF NOT EXISTS reservationflash(id INT PRIMARY KEY AUTO_INCREMENT,attractionId INT,date VARCHAR(20),time VARCHAR(20),price INT,personId INT)"
mycursor2.execute(sql)

# ========================	table for accounts	========================
mycursor2.execute(sql)
sql="CREATE TABLE IF NOT EXISTS accounts(id_people INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(200),email VARCHAR(200),password VARCHAR(200))"

mycursor2.close()
mydb.close()



import mysql.connector.pooling
import mysql.connector.pooling
dbconfig={
	"user":"root",
	"password":"Bb0970662139",
	"host":"localhost",
	"database":"taipei_day_trip",
}
connection_pool = mysql.connector.pooling.MySQLConnectionPool(
	pool_name="wehelp_pool",
	pool_size=5,
	pool_reset_session=True,
	**dbconfig
)




# ========================	register	========================

def register_email_exist(email):
	try:
		connection_object = connection_pool.get_connection()
		mycursor = connection_object.cursor(dictionary=True) # 設定fetchone跟fetchall有搜尋結果時的回傳都為字典形式
		sql_check="SELECT *FROM accounts WHERE email=%s"
		adr_check=(email,)
		mycursor.execute(sql_check,adr_check)
		myresult_checkEmail=mycursor.fetchone()
		if myresult_checkEmail != None:
			return True
	except:
		print("DealDatabase register_email_exist()發生問題")
	finally:
		mycursor.close()
		connection_object.close()



def register(name,email,password):
	try:
		connection_object = connection_pool.get_connection()
		mycursor = connection_object.cursor(dictionary=True)
		sql_register="INSERT INTO accounts(name,email,password) VALUES(%s,%s,%s)"
		val_register=(name,email,password)
		mycursor.execute(sql_register,val_register)
		connection_object.commit()
		return True
	except:
		print("DealDatabase register()發生問題")
	finally:
		mycursor.close()
		connection_object.close()


# ========================	signin	========================



def signin_account_exist(email,password):
	try:
		connection_object = connection_pool.get_connection()
		mycursor = connection_object.cursor(dictionary=True)
		sql_check="SELECT *FROM accounts WHERE email=%s and password=%s"
		adr_check=(email,password)
		mycursor.execute(sql_check,adr_check)
		myresult_check=mycursor.fetchone()
		if myresult_check!=None:
			return myresult_check
	except:
		print("DealDatabase signin_account_exist()發生問題")
	finally:
		mycursor.close()
		connection_object.close()



# ========================	booking	========================

def booking_people_exist(person_id):
	try:
		connection_object = connection_pool.get_connection()
		mycursor = connection_object.cursor(dictionary=True)
		sql_check="SELECT *FROM reservationflash where personId=%s"
		adr_check=(person_id,)
		mycursor.execute(sql_check,adr_check)
		myresult_check=mycursor.fetchone()
		if myresult_check!=None:
			return myresult_check
	except:
		print("DealDatabase booking_people_exist()發生問題")
	finally:
		mycursor.close()
		connection_object.close()


def update_booking_data(booking_attraction_id,booking_date,booking_price,booking_time,person_id):
	try:
		connection_object = connection_pool.get_connection()
		mycursor = connection_object.cursor(dictionary=True)
		sql_update="UPDATE reservationflash SET attractionId=%s,date=%s,price=%s,time=%s WHERE personId=%s"
		val_update=(booking_attraction_id,booking_date,booking_price,booking_time,person_id)
		mycursor.execute(sql_update,val_update)
		connection_object.commit()
	except:
		print("DealDatabase update_booking_data()發生問題")
	finally:
		mycursor.close()
		connection_object.close()


def insert_booking_data(booking_attraction_id,booking_date,booking_price,booking_time,person_id):
	try:
		connection_object = connection_pool.get_connection()
		mycursor = connection_object.cursor(dictionary=True)
		sql_deposit="INSERT INTO reservationflash(attractionId,date,price,time,personId) VALUES(%s,%s,%s,%s,%s)"
		val_deposit=(booking_attraction_id,booking_date,booking_price,booking_time,person_id)
		mycursor.execute(sql_deposit,val_deposit)
		connection_object.commit()
	except:
		print("DealDatabase insert_booking_data()發生問題")
	finally:
		mycursor.close()
		connection_object.close()


def get_data_for_booking_page(username,person_id):
	try:
		connection_object = connection_pool.get_connection()
		mycursor = connection_object.cursor(dictionary=True) # 把fetchone跟fetchall的搜尋結果回傳都為字典形式
		sql="SELECT datas3.id,datas3.name,datas3.address,datas3.images,reservationflash.date,reservationflash.time,reservationflash.price FROM datas3 INNER JOIN reservationflash ON reservationflash.personId=%s and datas3.id = reservationflash.attractionId"
		val=(person_id,)
		mycursor.execute(sql,val)
		myresult=mycursor.fetchone()

		if myresult==None:
			return ({"username":username,"data":None})
		img=myresult["images"].split(" ")
		data_for_booking_page=(
			{
				"data":{
					"attraction":{
						"id":myresult["id"],
						"name":myresult["name"],
						"address":myresult["address"],
						"image":img[0],
						},
						"date":myresult["date"],
						"time":myresult["time"],
						"price":myresult["price"],
						
				},"username":username
			})
		return (data_for_booking_page)
	except:
		print("get_data_for_booking_page()發生問題")
		return ({"error": True,"message": "伺服器內部錯誤"})
	finally:
		mycursor.close()
		connection_object.close()



def delete_data_for_bookin_page(attractio_id,person_id):
	try:
		# print("目標attractionId",attractionId,"目標personId",personId)
		connection_object = connection_pool.get_connection()
		mycursor =  connection_object.cursor()
		sql = "DELETE FROM reservationflash WHERE attractionId = %s and personId = %s"
		val = (attractio_id,person_id)
		mycursor.execute(sql,val)
		connection_object.commit()
	except:
		print("DealDatabase delete_data_for_bookin_page()發生問題")
	finally:
		mycursor.close()
		connection_object.close()




# ========================	categories_search_bar_item	========================

def get_categories_search_bar_item_data():
	try:
		connection_object = connection_pool.get_connection()
		mycursor = connection_object.cursor(dictionary=True) # 把fetchone跟fetchall的搜尋結果回傳都為字典形式
		category_items=[]
		sql="SELECT DISTINCT category FROM datas3"
		mycursor.execute(sql)
		myresult_categories=mycursor.fetchall()
		for item in myresult_categories:
			category_items.append(item[0])
		return (category_items)
	except:
		print("DealDatabase categories_search_bar_item_data()發生問題")
	finally:
		mycursor.close()
		connection_object.close()




# ========================	categories_picture_item	========================


def loading_all_picture_by_attractions(page_maxnum,page_num_now):
	try:
		connection_object = connection_pool.get_connection()
		mycursor = connection_object.cursor(dictionary=True) # 把fetchone跟fetchall的搜尋結果回傳都為字典形式
		sql_fetchall="SELECT *from datas3 LIMIT %s,%s"
		adr_fetchall=(page_num_now*page_maxnum,page_maxnum)
		mycursor.execute(sql_fetchall,adr_fetchall)
		myresult_fetchall=mycursor.fetchall()
		total_amount=len(myresult_fetchall)

		sql_fetchmore="SELECT *from datas3 LIMIT %s,%s"
		adr_fetchmore=(page_num_now*page_maxnum,page_maxnum+1)
		mycursor.execute(sql_fetchmore,adr_fetchmore)
		myresult_fetchmore=mycursor.fetchall()
		more_amount=len(myresult_fetchmore)

		for i in range(len(myresult_fetchall)):
			myresult_fetchall[i]=list(myresult_fetchall[i])
			myresult_fetchall[i][9]=myresult_fetchall[i][9].split(" ")

		if total_amount !=0:
			mytitle = mycursor.description
			column_name =[col[0] for col in mytitle]
			data=[]
			for i in range(total_amount):
				data.append(dict(zip(column_name,myresult_fetchall[i])))
			if more_amount==page_maxnum+1:
				next_page=page_num_now+1
			else:
				next_page=None
		else:
			return jsonify({                              
					"error": True,
					"message": "沒有資料了"	
				})

		return jsonify({                              
					"nextPage": next_page,
					"data": data	
				})

	except:
		print("DealDatabase loading_picture_by_attractions()發生問題")
	finally:
		mycursor.close()
		connection_object.close()


def loading_select_picture_by_attractions(page_maxnum,page_num_now,keyword):
	try:
		connection_object = connection_pool.get_connection()
		mycursor = connection_object.cursor(dictionary=True) # 把fetchone跟fetchall的搜尋結果回傳都為字典形式		
		sql_keyword="SELECT *FROM datas3 WHERE category=%s or name like concat('%',%s,'%') LIMIT %s,%s"
		adr_keyword=(keyword,keyword,page_num_now*page_maxnum,page_maxnum)
		mycursor.execute(sql_keyword,adr_keyword)
		myresult_keyword=mycursor.fetchall()
		total_amount=len(myresult_keyword)

		for i in range(len(myresult_keyword)):
			myresult_keyword[i]=list(myresult_keyword[i])
			myresult_keyword[i][9]=myresult_keyword[i][9].split(" ")

		if total_amount !=0:
			mytitle = mycursor.description
			column_name =[col[0] for col in mytitle]
		# 	print()
		# 	print(column_name)
		# 	print(myresult_keyword)
			data=[]
			for i in range(total_amount):
				data.append(dict(zip(column_name,myresult_keyword[i])))
			if len(data)==page_maxnum:
				next_page=page_num_now+1
			else:
				next_page=None
		else:
			return jsonify({                              
					"error": True,
					"message": "沒有資料了"	
				})

		return jsonify({                              
					"nextPage": next_page,
					"data": data	
				})
	except:
		print("DealDatabase loading_select_picture_by_attractions()發生問題")
	finally:
		mycursor.close()
		connection_object.close()







# ========================	deal_orders	========================

def order_reservation_exist(person_id,order_data_from_frontEnd):
	try:
		connection_object = connection_pool.get_connection()
		mycursor = connection_object.cursor(dictionary=True) # 把fetchone跟fetchall的搜尋結果回傳都為字典形式
		attraction_id=order_data_from_frontEnd["order"]["trip"]["attraction"]["id"]
		sql="SELECT *FROM reservationflash WHERE personId=%s and attractionId=%s"
		adr=(person_id,attraction_id)
		mycursor.execute(sql,adr)
		myresult=mycursor.fetchone()
		if myresult != None:
			return True
	except Exception as e:
		print("DealDatabase order_reservation_exist()發生問題: ",e)
	finally:
		mycursor.close()
		connection_object.close()




























# # 寫入reservationflash
# # bookingAttractionId=None
# # bookingDate=None
# # bookingPrice=None
# # bookingTime=None
# def deal_Booking(bookingData,personId):
# 	bookingAttractionId=bookingData["attractionId"]
# 	bookingDate=bookingData["date"]
# 	bookingPrice=bookingData["price"]
# 	bookingTime=bookingData["time"]
# 	if bookingAttractionId != "" and bookingDate != "" and bookingPrice != "" and bookingTime != "":
# 		try:
# 			connection_object = connection_pool.get_connection()
# 			mycursor =  connection_object.cursor()
# 			sql_check="SELECT *FROM reservationflash where personId=%s"
# 			val_check=(personId,)
# 			mycursor.execute(sql_check,val_check)
# 			myresult_check=mycursor.fetchone()
# 			if myresult_check!=None:
# 				# sql_update="UPDATE reservationflash SET attractionId=%s,date=%s,price=%s,time=%s WHERE id=1"
# 				sql_update="UPDATE reservationflash SET attractionId=%s,date=%s,price=%s,time=%s WHERE personId=%s"
# 				val_update=(bookingAttractionId,bookingDate,bookingPrice,bookingTime,personId)
# 				mycursor.execute(sql_update,val_update)
# 				connection_object.commit()
# 				# print("更新資料")
# 			else:
# 				sql_deposit="INSERT INTO reservationflash(attractionId,date,price,time,personId) VALUES(%s,%s,%s,%s,%s)"
# 				val_deposit=(bookingAttractionId,bookingDate,bookingPrice,bookingTime,personId)
# 				mycursor.execute(sql_deposit,val_deposit)
# 				connection_object.commit()
# 				# print("註冊資料")
# 			return jsonify({"ok":True})
# 		except:
# 			return jsonify({"error": True,"message": "註冊伺服器內部錯誤"})
# 		finally:
# 			mycursor.close()
# 			connection_object.close()

# 	else:
# 		return jsonify({"error": True,"message": "訂購資料皆不可為空"})




# def GetDataForBookingPage(username,personId):
# 	try:
# 		connection_object = connection_pool.get_connection()
# 		# mycursor =  connection_object.cursor()
# 		mycursor = connection_object.cursor(dictionary=True) # 把fetchone跟fetchall的搜尋結果回傳都為字典形式
# 		# sql="SELECT datas3.id,datas3.name,datas3.address,datas3.images,reservationflash.date,reservationflash.time,reservationflash.price FROM datas3 INNER JOIN reservationflash ON datas3.id = reservationflash.attractionId"
# 		sql="SELECT datas3.id,datas3.name,datas3.address,datas3.images,reservationflash.date,reservationflash.time,reservationflash.price FROM datas3 INNER JOIN reservationflash ON reservationflash.personId=%s and datas3.id = reservationflash.attractionId"
# 		val=(personId,)
# 		mycursor.execute(sql,val)
# 		# mycursor.execute(sql)
# 		myresult=mycursor.fetchone()

# 		print("---------------666myresult1-----------")
# 		print(myresult)
		
# 		# for result in myresult2:
# 		# 	columns = [col[0] for col in mycursor.description]
# 		# 	data=dict(zip(columns,result))
# 		# 	print(result)
# 		# 	# print(data)
# 		# print("---------------666myresult2-----------")
# 		# myresult2=mycursor.fetchall()
# 		# print(myresult2)
		


# 		print("--------------------------")
# 		# CREATE TABLE IF NOT EXISTS reservationflash(id INT PRIMARY KEY AUTO_INCREMENT,attractionId INT,date VARCHAR(20),time VARCHAR(20),price INT,personId INT
# 		if myresult!=None:
# 		# if myresult!=[]:	
# 			# print(myresult["id"])


# 			# print("---------------666-----------")
# 			# for result in myresult:
# 			# 	# columns = [col[0] for col in mycursor.description]
# 			# 	# data=dict(zip(columns,result))
# 			# 	print(result)
# 			# # print(data)



# 			# print("--------------")

# 			img=myresult["images"].split(" ")
# 			response=(
# 			{
# 				"data":{
# 					"attraction":{
# 						"id":myresult["id"],
# 						"name":myresult["name"],
# 						"address":myresult["address"],
# 						"image":img[0],
# 						},
# 						"date":myresult["date"],
# 						"time":myresult["time"],
# 						"price":myresult["price"],
						
# 				},"username":username
# 			})
# 			print("進入")
# 			print(response)
# 			return jsonify(response)

# 		else:
# 			response=({"username":username,"data":None})
# 			return jsonify(response)
		

# 	except:
# 		return jsonify({"error": True,"message": "伺服器內部錯誤"})
# 	finally:
# 		mycursor.close()
# 		connection_object.close()
# 	# return ("hello")



# def DeleteDataForBookingPage(attractionId,personId):
# 	try:
# 		# print("目標attractionId",attractionId,"目標personId",personId)
# 		connection_object = connection_pool.get_connection()
# 		mycursor =  connection_object.cursor()
# 		sql = "DELETE FROM reservationflash WHERE attractionId = %s and personId = %s"
# 		# sql = "DELETE FROM reservationflash"
# 		val = (attractionId,personId)
# 		mycursor.execute(sql,val)
# 		connection_object.commit()
# 		print("is done")
# 	except:
# 		return jsonify({"error": True,"message": "伺服器內部錯誤"})
# 	finally:
# 		mycursor.close()
# 		connection_object.close()





# # from model import registe
# checkDataResponse=None
# def DealDatabase(name,email,password):
# 	# print("got it inside??")
# 	# print(kkk)
# 	print(name,email,password)

# 	connection_object = connection_pool.get_connection()
# 	mycursor =  connection_object.cursor()
# 	global checkDataResponse
# 	# name=name
# 	# email=email
# 	# password=password
# 	try:
# 		sql_check="SELECT *FROM accounts WHERE email=%s"
# 		adr_check=(email,)
# 		mycursor.execute(sql_check,adr_check)
# 		myresult_checkEmail=mycursor.fetchone()
# 		print("註冊前檢查",myresult_checkEmail)
# 		if myresult_checkEmail==None:
# 			print("可以執行註冊")
# 			registe(name,email,password) #---------------------是不是不能這樣做 當然可以
# 			checkDataResponse=({"ok":True})
# 		else:
# 			print("DeakDatabase未執行註冊")
# 			checkDataResponse=({"error":True,"message":"Email重複，點此重新註冊"})
# 	except:
# 		print("有問題")
# 		checkDataResponse=({"error":True,"message":"500 伺服器內部錯誤"})
# 	finally:
# 		mycursor.close()
# 		connection_object.close()

# def registe(name,email,password):
# 	try:
# 		connection_object=connection_pool.get_connection()
# 		mycursor=connection_object.cursor()
# 		print("xxx")
# 		print(name,email,password)
# 		sql_register="INSERT INTO accounts(name,email,password) VALUES(%s,%s,%s)"
# 		val_register=(name,email,password)
# 		mycursor.execute(sql_register,val_register)
# 		connection_object.commit()
# 	except:
# 		print("註冊資料庫時發生問題")
# 	finally:
# 		mycursor.close()
# 		connection_object.close()


