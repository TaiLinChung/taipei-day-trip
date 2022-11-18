from flask import *
from flask import jsonify

app=Flask(__name__)
app.config["JSON_AS_ASCII"]=False
app.config["TEMPLATES_AUTO_RELOAD"]=True

import mysql.connector
mydb=mysql.connector.connect(
# mydb=MySQLConnection(
    host="localhost",
    user="root",
    password="Bb0970662139"
)
mycursor=mydb.cursor()
sql="USE taipei_day_trip"
mycursor.execute(sql)


# Pages
@app.route("/")
def index():
	return render_template("index.html")
@app.route("/attraction/<id>")
def attraction(id):
	return render_template("attraction.html")
@app.route("/booking")
def booking():
	return render_template("booking.html")
@app.route("/thankyou")
def thankyou():
	return render_template("thankyou.html")




@app.route("/api/attractions",methods=["GET"])
def api_attractions():
	page_num=request.args.get("page",None)
	page_num=int(page_num)
	keyword=request.args.get("keyword",None)
	# print("page_num",page_num)
	# print(keyword)
	
	mycursor=mydb.cursor()
	sql="SELECT *FROM datas2"
	mycursor.execute(sql)
	myresult=mycursor.fetchall()
	total_amount=len(myresult)
	# print("total_amount= ",total_amount)
	# print(myresult)
	# ct=0
	
# sss=img.jpg img.jpg 
# sss=sss[0:-1]
	for i in range(total_amount):
		# print(ct)
		# ct+=1
		# print("777",(myresult[i]))
		# print(list(myresult[i])[9].split(" "))
		
		myresult[i]=list(myresult[i])
		myresult[i][9]=myresult[i][9].split(" ")
		print(myresult[i][9])
		myresult_real=[]
		for e in myresult[i][9]:
			if e!="" and ".MP3" not in e and ".FLV" not in e:
				myresult_real.append(e)
		myresult[i][9]=myresult_real


	# # #取category
	category_data=[]
	mycursor2=mydb.cursor()
	sql2="SELECT DISTINCT category FROM datas2"
	mycursor2.execute(sql2)
	myresult_category=mycursor2.fetchall()
	# print(myresult_category[0])
	# print(myresult_category)
	for e in myresult_category:
		category_data.append(str(e).replace("(","").replace(")","").replace(",","").replace("'","").replace("\\u3000",""))
		# list2.append(list(e))
	# print(category_data)
	# print(list2)
	print("keyword= ",keyword==None)
	##判斷比對方式
	if keyword != "" and keyword in category_data:
		# return "YES"
		print("category完全比對")
		if keyword=="其他":
			keyword="其  他"

		mycursor=mydb.cursor()
		sql_keyword="SELECT *FROM datas2 WHERE category=%s"
		adr_keyword=(keyword,)
		mycursor.execute(sql_keyword,adr_keyword)
		myresult_keyword=mycursor.fetchall()
		keyword_search_amount=len(myresult_keyword)
		total_amount=keyword_search_amount
		myresult=myresult_keyword
		#----------------

	elif keyword == "":
		print("不比了")

	else:
		#完全沒用到&keyword時的判定
		if keyword == None:
			pass
		else:
			print("name模糊比對")
			mycursor=mydb.cursor()
			# sql_vague="SELECT *FROM datas WHERE name like '% %s %'"
			print(keyword)
			sql_vague="SELECT *FROM datas2 WHERE name like concat('%',%s,'%')"
			adr_vague=(keyword,)
			mycursor.execute(sql_vague,adr_vague)
			myresult_vague=mycursor.fetchall()
			vague_search_amount=len(myresult_vague)
			total_amount=vague_search_amount
			myresult=myresult_vague

	
	if (page_num)*12 > total_amount or page_num<0:
		return jsonify({
			"error": True,
			"message": "錯誤!!! 超出可查詢範圍"
		})

	#正常+有下一頁
	elif (page_num+1)*12<=total_amount:
		# if key_word != None:

		# 	return "woooooo"


		mytitle = mycursor.description
		column_name =[col[0] for col in mytitle]
		# column_name=[]
		# for col in mytitle:
		# 	column_name.append(col[0])

		# data = [dict(zip(column_name, list(row)))for row in myresult]
		# print(myresult)
		data=[]
		for i in range((page_num)*12,(page_num+1)*12):
			data.append(dict(zip(column_name,list(myresult[i]))))
		# for row in myresult:
			# data.append(dict(zip(column_name,list(row))))

			# print(list(zip(column_name,list(row))))
			# print()
			# print()
		# print(data)
		# print(mytitle)
		# print("----------------------")
		# print(column_name)
		# print("----------------------")

		#觀念嘗試
		# aaa=[(1, 4), (2, 5), (3, 6)]
		# bbb=dict(aaa)
		# print(bbb)

		


		return jsonify({                              
			"nextPage": page_num+1,
			"data": data		
		})

	#正常+無下一頁
	else:
		#取剩餘所有
		# overage=total_amount%12
		# last_start=total_amount-overage+1
		# sql="SELECT *from datas limit %s,%s"
		# adr=(last_start,total_amount)
		# mycursor.execute(sql,adr)
		# myresult=mycursor.fetchall()
		mytitle = mycursor.description
		column_name =[col[0] for col in mytitle]
		data=[]
		# for i in range(0,12):
		for i in range((page_num)*12,total_amount):
			data.append(dict(zip(column_name,list(myresult[i]))))
		return jsonify({
			"nextPage": None,
			"data": data
		})


@app.route("/api/attractions/<attractionId>",methods=["GET"])
def api_attractionId(attractionId):
	get_attractionId=attractionId
	# print(content)
	mycursor=mydb.cursor()
	sql="SELECT *FROM datas2 WHERE id=%s"
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

		return jsonify({
				"data": data
			})

	else:
		return jsonify({
				"error": True,
				"message":"景點編號不正確"
			})


@app.route("/api/cotegories",methods=["GET"])
def api_cotegories():
	try:	
		category_data=[]
		mycursor2=mydb.cursor()
		sql2="SELECT DISTINCT category FROM datas2"
		mycursor2.execute(sql2)
		myresult_category=mycursor2.fetchall()
		# print(myresult_category[0])
		# print(myresult_category)
		for e in myresult_category:
			category_data.append(str(e).replace("(","").replace(")","").replace(",","").replace("'","").replace("\\u3000",""))
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



#參考


	# #冠妤推薦
	# # sql="SELECT *from datas limit 0,12"
	# sql="SELECT *from datas limit %s,%s"
	# # mycursor.execute(sql)
	# adr=(0,12)
	# mycursor.execute(sql,adr)
	# myresult=mycursor.fetchall()
	# myresult=jsonify(myresult)
	# return myresult


	# #換方法
	# sql="SELECT *FROM datas"
	# cursor.execute(sql)
	# result=cursor.fetchmany(5)
	# print(result)
	# return result



# @app.route("/api/member/",methods=["GET","PATCH"])
# def apimember():
#     if request.method=="GET":
#         account=request.args.get("username",None)
#         mycursor=mydb.cursor()
#         sql="SELECT id_people,name,account FROM accounts WHERE account=%s"
#         adr=(account,)
#         mycursor.execute(sql,adr)
#         myresult=mycursor.fetchone()

#         # print(myresult)
#         if myresult !=None and session["keyFlag"]=="open":
#             search={
#                 "data":{
#                     "id":myresult[0],
#                     "name":myresult[1],
#                     "username":myresult[2]
#                 }
#             }
#             # return ({
#             #     "data":{
#             #         "id":myresult[0],
#             #         "name":myresult[1],
#             #         "username":myresult[2]
#             #     }
#             # })
            
            
#         else:
#             search={
#                 "data":None
#             }
#             # return ({
#             #     "data":None
#             # })

#         return jsonify(search)
#         # return search
# #-------USE PATCH
#     else:        
#         new_name=request.get_json() #透過JS抓到在HTML輸入的新的名字
#         new_name=new_name["name"]
#         print("new_name",new_name)
#         # print("NULL=",new_name)
#         if new_name=="" or session["keyFlag"] != "open":
#             print({"error":True})
#             return {"error":True}

#         #判定有登入
#         else:
#             print("待改的id_people: ",session["id_people"])

#             mycursor=mydb.cursor()
#             sql="UPDATE accounts SET name =%s  WHERE id_people=%s"
#             adr=(str(new_name),str(session["id_people"]))
#             mycursor.execute(sql,adr)
#             mydb.commit()
#             session["name"]=new_name
#             print({"ok":True})
#             return {"ok":True}




app.run(host='0.0.0.0',port=3000)