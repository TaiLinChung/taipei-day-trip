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

# ========================	build table for accounts	========================
sql="""CREATE TABLE IF NOT EXISTS 
		accounts(id_people INT PRIMARY KEY AUTO_INCREMENT,
		name VARCHAR(200),email VARCHAR(200),password VARCHAR(200))"""
mycursor2.execute(sql)

# ========================	build table for reservationflash	========================
sql="""CREATE TABLE IF NOT EXISTS 
		reservationflash(id INT PRIMARY KEY AUTO_INCREMENT,
		attractionId INT,date VARCHAR(20),time VARCHAR(20),
		price INT,personId INT)"""
mycursor2.execute(sql)

# ========================	build table for historical_order	========================
sql="""CREATE TABLE IF NOT EXISTS 
		historical_order(
			order_number INT PRIMARY KEY AUTO_INCREMENT,
			order_account_id INT,
			order_contact_name VARCHAR(200),
			order_contact_email VARCHAR(200),
			order_contact_phone VARCHAR(200),
			order_date VARCHAR(200),
			order_time VARCHAR(200),
			order_attraction_id INT,
			order_price INT,
			transaction_time VARCHAR(20),
			order_status INT NOT NULL DEFAULT 1)"""
mycursor2.execute(sql)

# # ========================	build table for transaction_record	========================
# sql="""CREATE TABLE IF NOT EXISTS 
# 		transaction_record(order_number INT PRIMARY KEY,
# 		order_status VARCHAR(1500),transaction_time VARCHAR(30))"""
# mycursor2.execute(sql)



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
		print(myresult_categories)
		for item in myresult_categories:
			category_items.append(item["category"])
		print(category_items)
		return (category_items)
	except Exception as e:
		print("DealDatabase categories_search_bar_item_data()發生問題",e)
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



def write_historical_order(person_id,order_data_from_frontEnd):
	try:
		connection_object = connection_pool.get_connection()
		mycursor = connection_object.cursor(dictionary=True) # 把fetchone跟fetchall的搜尋結果回傳都為字典形式
		order_contact_name=order_data_from_frontEnd["order"]["contact"]["name"]
		order_contact_email=order_data_from_frontEnd["order"]["contact"]["email"]
		order_contact_phone=order_data_from_frontEnd["order"]["contact"]["phone"]
		order_date=order_data_from_frontEnd["order"]["trip"]["date"]
		order_time=order_data_from_frontEnd["order"]["trip"]["time"]
		order_attraction_id=order_data_from_frontEnd["order"]["trip"]["attraction"]["id"]
		order_price=order_data_from_frontEnd["order"]["price"]
		sql="INSERT INTO historical_order(order_account_id,order_contact_name,order_contact_email,order_contact_phone,order_date,order_time,order_attraction_id,order_price) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
		val = (person_id,order_contact_name,order_contact_email,order_contact_phone,order_date,order_time,order_attraction_id,order_price)
		mycursor.execute(sql,val)
		connection_object.commit()
		sql="SELECT order_number FROM historical_order ORDER BY order_number DESC LIMIT 1;"
		mycursor.execute(sql)
		last_order_number=mycursor.fetchone()
		# print(last_order_number)
		return last_order_number["order_number"]
	except Exception as e:
		print("DealDatabase write_historical_order()發生問題: ",e)
	finally:
		mycursor.close()
		connection_object.close()


from datetime import datetime
def write_transaction_record_in_historical_order(the_last_order_number,tappay_api_response):
	try:
		connection_object = connection_pool.get_connection()
		mycursor = connection_object.cursor(dictionary=True) # 把fetchone跟fetchall的搜尋結果回傳都為字典形式
		now = datetime.now()
		date_time = now.strftime("%Y%m%d%H%M%S")
		sql="UPDATE historical_order SET transaction_time=%s,order_status=%s WHERE order_number=%s"
		val = (date_time,tappay_api_response["status"],the_last_order_number)	
		mycursor.execute(sql,val)
		connection_object.commit()
		return True

	except Exception as e:
		print("DealDatabase write_transaction_record()發生問題: ",e)
	finally:
		mycursor.close()
		connection_object.close()


def delete_reservation_flash_by_person_id(person_id):
	try:
		connection_object = connection_pool.get_connection()
		mycursor = connection_object.cursor(dictionary=True) # 把fetchone跟fetchall的搜尋結果回傳都為字典形式		
		sql="DELETE FROM reservationflash WHERE personId=%s"
		val =(person_id,)	
		mycursor.execute(sql,val)
		connection_object.commit()
	except Exception as e:
		print("DealDatabase delete_reservation_flash_by_person_id()發生問題: ",e)
	finally:
		mycursor.close()
		connection_object.close()




def get_transaction_record_in_historical_order(the_last_order_number):
	try:
		connection_object = connection_pool.get_connection()
		mycursor = connection_object.cursor(dictionary=True) # 把fetchone跟fetchall的搜尋結果回傳都為字典形式
		sql="SELECT transaction_time,order_status FROM historical_order WHERE order_number=%s;"
		val = (the_last_order_number,)	
		mycursor.execute(sql,val)
		# mycursor.execute(sql)
		transaction_record=mycursor.fetchone()
		# print(transaction_record)
		if transaction_record["order_status"]==0:
			return({
				"data": {
					"number": str(transaction_record["transaction_time"]+str(the_last_order_number)),
					"payment": {
					"status": transaction_record["order_status"],
					"message": "付款成功"
					}
				}
			})
		else:
			return({
				"error": True,
  				"message": transaction_record["order_status"],
				# 新增
				"number": str(transaction_record["transaction_time"]+str(the_last_order_number))
			})

	except Exception as e:
		print("get_transaction_record_in_historical_order()發生問題: ",e)
	finally:
		mycursor.close()
		connection_object.close()




def get_transaction_record_by_order_number(order_number):
	try:
		connection_object = connection_pool.get_connection()
		mycursor = connection_object.cursor(dictionary=True) # 把fetchone跟fetchall的搜尋結果回傳都為字典形式
		sql="SELECT order_attraction_id FROM historical_order WHERE order_number=%s"
		val = (order_number,)
		mycursor.execute(sql,val)
		order_attraction_id=mycursor.fetchone()["order_attraction_id"]
		# print("order_number: ",order_number)
		# print("order_attraction_id: ",order_attraction_id)
		sql="SELECT *FROM historical_order INNER JOIN datas3 WHERE historical_order.order_number=%s and datas3.id=%s;"
		val = (order_number,order_attraction_id)	
		mycursor.execute(sql,val)
		# print("------")
		total_record=mycursor.fetchone()
		# print(total_record)
		if total_record==None:
			return ({"error": True,"message": "歷史訂單中不存在此筆資料"})
		
		return(
			{
  				"data": {
    				"number": str(total_record["transaction_time"])+str(total_record["order_number"]),
    				"price": total_record["order_price"],
    				"trip": {
      					"attraction": {
        					"id": total_record["order_attraction_id"],
        					"name": total_record["name"],
        					"address": total_record["address"],
        					"image": total_record["images"].split(" ")[0]
      					},
      					"date": total_record["order_date"],
      					"time": total_record["order_time"]
    				},
					"contact": {
						"name": total_record["order_contact_name"],
						"email": total_record["order_contact_email"],
						"phone": total_record["order_contact_phone"]
					},
					"status": total_record["order_status"]
  				}
			}

		)

	except Exception as e:
		print("DealDatabase get_transaction_record_by_order_number()發生問題: ",e)
	finally:
		mycursor.close()
		connection_object.close()




def get_transaction_record_by_transaction_number(transaction_number,person_id):
	try:
		connection_object = connection_pool.get_connection()
		mycursor = connection_object.cursor(dictionary=True) # 把fetchone跟fetchall的搜尋結果回傳都為字典形式
		transaction_time=str(transaction_number)[:14]
		order_number=str(transaction_number)[14:]

		sql="SELECT * FROM historical_order WHERE order_number=%s and transaction_time=%s and order_account_id=%s"
		val = (order_number,transaction_time,person_id)
		mycursor.execute(sql,val)
		total_record=mycursor.fetchone()
		sql="SELECT *FROM datas3 WHERE id=%s"
		val = (total_record["order_attraction_id"],)
		mycursor.execute(sql,val)
		attractions_information=mycursor.fetchone()
		if total_record!=None:
			return(
				{
					"data": {
						"number": str(total_record["transaction_time"])+str(total_record["order_number"]),
						"price": total_record["order_price"],
						"trip": {
							"attraction": {
								"id": total_record["order_attraction_id"],
								"name": attractions_information["name"],
								"address": attractions_information["address"],
								"image": attractions_information["images"].split(" ")[0]
							},
							"date": total_record["order_date"],
							"time": total_record["order_time"]
						},
						"contact": {
							"name": total_record["order_contact_name"],
							"email": total_record["order_contact_email"],
							"phone": total_record["order_contact_phone"]
						},
						"status": total_record["order_status"]
					}
				}

			)

	except Exception as e:
		print("DealDatabase get_transaction_record_by_transaction_number()發生問題: ",e)
	finally:
		mycursor.close()
		connection_object.close()

