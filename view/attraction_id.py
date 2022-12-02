from flask import *
from flask import jsonify

import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Bb0970662139"
)
mycursor=mydb.cursor()
sql="USE taipei_day_trip"
mycursor.execute(sql)

#相應app.py
attraction_id_blueprint=Blueprint("attraction_blueprint",__name__)


@attraction_id_blueprint.route("/api/attraction/<attractionId>",methods=["GET"])
def api_attractionId(attractionId):
	get_attractionId=attractionId
	# print(content)
	mycursor=mydb.cursor()
	sql="SELECT *FROM datas3 WHERE id=%s"
	adr=(get_attractionId,)
	mycursor.execute(sql,adr)
	myresult=mycursor.fetchall()
	# print(myresult)
	if myresult != []:
		mytitle = mycursor.description
		column_name =[col[0] for col in mytitle]
		# print(column_name)
		# print(myresult[0])
		data=[]
		for i in range(0,1):
			data.append(dict(zip(column_name,list(myresult[i]))))
		data=data[0]
		data["images"]=data["images"].split(" ")
		imgs_notnull=[]
		for e in data["images"]:
			if e!="" and ".MP3" not in e and ".FLV" not in e:
				imgs_notnull.append(e)
		data["images"]=imgs_notnull
		print(data)

		return jsonify({
				"data": data
			})

	else:
		return jsonify({
				"error": True,
				"message":"景點編號不正確"
			})