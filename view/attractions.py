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
attractions_blueprint=Blueprint("attractions_blueprint",__name__)


@attractions_blueprint.route("/api/attractions",methods=["GET"])
def api_attractions():
	try:
		connection_object = connection_pool.get_connection()
		

		page_num=int(request.args.get("page",""))
		keyword=request.args.get("keyword","")
		page_maxnum=12
		##單純頁數
		if keyword == "":
			# mycursor=mydb.cursor()
			mycursor =  connection_object.cursor()
			sql_fetchall="SELECT *from datas3 LIMIT %s,%s"
			adr_fetchall=(page_num*page_maxnum,page_maxnum)
			mycursor.execute(sql_fetchall,adr_fetchall)
			myresult_fetchall=mycursor.fetchall()
			total_amount=len(myresult_fetchall)
			# print(myresult_fetchall[0])
			# print(myresult_fetchall)   
			sql_fetchmore="SELECT *from datas3 LIMIT %s,%s"
			adr_fetchmore=(page_num*page_maxnum,page_maxnum+1)
			mycursor.execute(sql_fetchmore,adr_fetchmore)
			myresult_fetchmore=mycursor.fetchall()
			more_amount=len(myresult_fetchmore)

			for i in range(len(myresult_fetchall)):
				myresult_fetchall[i]=list(myresult_fetchall[i])
				# print()
				# print(myresult_fetchall[i][9])
				myresult_fetchall[i][9]=myresult_fetchall[i][9].split(" ")

			if total_amount !=0:
				mytitle = mycursor.description
				column_name =[col[0] for col in mytitle]
				data=[]
				for i in range(total_amount):
					data.append(dict(zip(column_name,myresult_fetchall[i])))
				if more_amount==page_maxnum+1:
					next_page=page_num+1
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




		#模糊&完全
		else:
			# mycursor=mydb.cursor()
			mycursor =  connection_object.cursor()
			sql_keyword="SELECT *FROM datas3 WHERE category=%s or name like concat('%',%s,'%') LIMIT %s,%s"
			first_num=page_num*0
			last_num=(page_num+1)*page_maxnum-1
			adr_keyword=(keyword,keyword,page_num*page_maxnum,page_maxnum)
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
					next_page=page_num+1
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
		return {"error":True},500
	finally:
		mycursor.close()
		connection_object.close()
