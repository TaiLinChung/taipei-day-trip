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

# import mysql.connector
# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Bb0970662139"
# )
# mycursor=mydb.cursor()
# sql="USE taipei_day_trip"
# mycursor.execute(sql)

#相應app.py
categories_blueprint=Blueprint("categories_blueprint",__name__)

@categories_blueprint.route("/api/categories",methods=["GET"])
def api_categories():
	try:	
		connection_object = connection_pool.get_connection()
		category_data=[]
		# mycursor2=mydb.cursor()
		mycursor2 =  connection_object.cursor()
		sql2="SELECT DISTINCT category FROM datas3"
		mycursor2.execute(sql2)
		myresult_category=mycursor2.fetchall()
		# for e in myresult_category:
		# 	category_data.append(str(e).replace("(","").replace(")","").replace(",","").replace("'",""))
		category_data = [cat[0] for cat in myresult_category]
		
		# print(myresult_category)
		print(category_data)
		return jsonify({
					"data": category_data
					
				})

	except TypeError:
		return jsonify({
					"error": True,
					"message":"型別發生錯誤"
				})

	except NameError:
		return jsonify({
					"error": True,
					"message":"使用沒有被定義的對象"
				})
				
	except Exception:
		return jsonify({
					"error": True,
					"message":"不知道怎麼了，反正發生錯誤惹"
				})
	finally:
		mycursor2.close()
		connection_object.close()