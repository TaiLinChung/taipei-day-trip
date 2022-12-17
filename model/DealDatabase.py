
from model import kkk
print("got it outside??")
print(kkk)


from flask import *
from flask import jsonify

##前置作業與資料庫連線創建資料庫跟表
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Bb0970662139"
)
mycursor2=mydb.cursor()
sql="CREATE DATABASE IF NOT EXISTS taipei_day_trip"
mycursor2.execute(sql)
sql="USE taipei_day_trip"
mycursor2.execute(sql)
# sql="CREATE TABLE IF NOT EXISTS reservationflash(id INT PRIMARY KEY AUTO_INCREMENT,attractionId INT,date VARCHAR(20),time VARCHAR(20),price INT)"
sql="CREATE TABLE IF NOT EXISTS reservationflash(id INT PRIMARY KEY AUTO_INCREMENT,attractionId INT,date VARCHAR(20),time VARCHAR(20),price INT,personId INT)"
mycursor2.execute(sql)
mycursor2.close()
mydb.close()





import mysql.connector.pooling
##try more by apple
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


# from model import registe
checkDataResponse=None
def DealDatabase(name,email,password):
	print("got it inside??")
	print(kkk)
	print(name,email,password)

	connection_object = connection_pool.get_connection()
	mycursor =  connection_object.cursor()
	global checkDataResponse
	# name=name
	# email=email
	# password=password
	try:
		sql_check="SELECT *FROM accounts WHERE email=%s"
		adr_check=(email,)
		mycursor.execute(sql_check,adr_check)
		myresult_checkEmail=mycursor.fetchone()
		print("註冊前檢查",myresult_checkEmail)
		if myresult_checkEmail==None:
			print("可以執行註冊")
			registe(name,email,password) #---------------------是不是不能這樣做 當然可以
			checkDataResponse=({"ok":True})
		else:
			print("DeakDatabase未執行註冊")
			checkDataResponse=({"error":True,"message":"Email重複，點此重新註冊"})
	except:
		print("有問題")
		checkDataResponse=({"error":True,"message":"500 伺服器內部錯誤"})
	finally:
		mycursor.close()
		connection_object.close()

def registe(name,email,password):
	try:
		connection_object=connection_pool.get_connection()
		mycursor=connection_object.cursor()
		print("xxx")
		print(name,email,password)
		sql_register="INSERT INTO accounts(name,email,password) VALUES(%s,%s,%s)"
		val_register=(name,email,password)
		mycursor.execute(sql_register,val_register)
		connection_object.commit()
	except:
		print("註冊資料庫時發生問題")
	finally:
		mycursor.close()
		connection_object.close()





# 寫入reservationflash
# bookingAttractionId=None
# bookingDate=None
# bookingPrice=None
# bookingTime=None
def DealBooking(bookingData,personId):
	bookingAttractionId=bookingData["attractionId"]
	bookingDate=bookingData["date"]
	bookingPrice=bookingData["price"]
	bookingTime=bookingData["time"]
	if bookingAttractionId != "" and bookingDate != "" and bookingPrice != "" and bookingTime != "":
		try:
			connection_object = connection_pool.get_connection()
			mycursor =  connection_object.cursor()
			sql_check="SELECT *FROM reservationflash where personId=%s"
			val_check=(personId,)
			mycursor.execute(sql_check,val_check)
			myresult_check=mycursor.fetchone()
			if myresult_check!=None:
				# sql_update="UPDATE reservationflash SET attractionId=%s,date=%s,price=%s,time=%s WHERE id=1"
				sql_update="UPDATE reservationflash SET attractionId=%s,date=%s,price=%s,time=%s WHERE personId=%s"
				val_update=(bookingAttractionId,bookingDate,bookingPrice,bookingTime,personId)
				mycursor.execute(sql_update,val_update)
				connection_object.commit()
				# print("更新資料")
			else:
				sql_deposit="INSERT INTO reservationflash(attractionId,date,price,time,personId) VALUES(%s,%s,%s,%s,%s)"
				val_deposit=(bookingAttractionId,bookingDate,bookingPrice,bookingTime,personId)
				mycursor.execute(sql_deposit,val_deposit)
				connection_object.commit()
				# print("註冊資料")
			return jsonify({"ok":True})
		except:
			return jsonify({"error": True,"message": "註冊伺服器內部錯誤"})
		finally:
			mycursor.close()
			connection_object.close()

	else:
		return jsonify({"error": True,"message": "註冊上述資料皆不可為空"})




def GetDataForBookingPage(username,personId):
	try:
		connection_object = connection_pool.get_connection()
		# mycursor =  connection_object.cursor()
		mycursor = connection_object.cursor(dictionary=True) # 把fetchone跟fetchall的搜尋結果回傳都為字典形式
		# sql="SELECT datas3.id,datas3.name,datas3.address,datas3.images,reservationflash.date,reservationflash.time,reservationflash.price FROM datas3 INNER JOIN reservationflash ON datas3.id = reservationflash.attractionId"
		sql="SELECT datas3.id,datas3.name,datas3.address,datas3.images,reservationflash.date,reservationflash.time,reservationflash.price FROM datas3 INNER JOIN reservationflash ON reservationflash.personId=%s and datas3.id = reservationflash.attractionId"
		val=(personId,)
		mycursor.execute(sql,val)
		# mycursor.execute(sql)
		myresult=mycursor.fetchone()

		print("---------------666myresult1-----------")
		print(myresult)
		
		# for result in myresult2:
		# 	columns = [col[0] for col in mycursor.description]
		# 	data=dict(zip(columns,result))
		# 	print(result)
		# 	# print(data)
		# print("---------------666myresult2-----------")
		# myresult2=mycursor.fetchall()
		# print(myresult2)
		


		print("--------------------------")
		# CREATE TABLE IF NOT EXISTS reservationflash(id INT PRIMARY KEY AUTO_INCREMENT,attractionId INT,date VARCHAR(20),time VARCHAR(20),price INT,personId INT
		if myresult!=None:
		# if myresult!=[]:	
			# print(myresult["id"])


			# print("---------------666-----------")
			# for result in myresult:
			# 	# columns = [col[0] for col in mycursor.description]
			# 	# data=dict(zip(columns,result))
			# 	print(result)
			# # print(data)



			# print("--------------")

			img=myresult["images"].split(" ")
			response=(
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
			print("進入")
			print(response)
			return jsonify(response)

		else:
			response=({"username":username,"data":None})
			return jsonify(response)
		

	except:
		return jsonify({"error": True,"message": "伺服器內部錯誤"})
	finally:
		mycursor.close()
		connection_object.close()
	# return ("hello")



def DeleteDataForBookingPage(attractionId,personId):
	try:
		print("目標attractionId",attractionId,"目標personId",personId)
		connection_object = connection_pool.get_connection()
		mycursor =  connection_object.cursor()
		sql = "DELETE FROM reservationflash WHERE attractionId = %s and personId = %s"
		# sql = "DELETE FROM reservationflash"
		val = (attractionId,personId)
		mycursor.execute(sql,val)
		connection_object.commit()
		print("is done")
	except:
		return jsonify({"error": True,"message": "伺服器內部錯誤"})
	finally:
		mycursor.close()
		connection_object.close()



