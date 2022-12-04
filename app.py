from flask import *
from flask import jsonify

#blueprint引入--------------------------------------------
from view.attractions import attractions_blueprint
from view.attraction_id import attraction_id_blueprint
from view.categories import categories_blueprint


app=Flask(__name__)
app.config["JSON_AS_ASCII"]=False
app.config["TEMPLATES_AUTO_RELOAD"]=True

# import mysql.connector
# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Bb0970662139"
# )
# mycursor=mydb.cursor()
# sql="USE taipei_day_trip"
# mycursor.execute(sql)


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



app.register_blueprint(attractions_blueprint)
# @app.route("/api/attractions",methods=["GET"])
# def api_attractions():
# 	# try:
	
# 	page_num=int(request.args.get("page",""))
# 	keyword=request.args.get("keyword","")
# 	page_maxnum=12
# 	##單純頁數
# 	if keyword == "":
# 		mycursor=mydb.cursor()
# 		sql_fetchall="SELECT *from datas3 LIMIT %s,%s"
# 		first_num=page_num*0
# 		last_num=(page_num+1)*page_maxnum-1
# 		adr_fetchall=(page_num*page_maxnum,page_maxnum)
# 		mycursor.execute(sql_fetchall,adr_fetchall)
# 		myresult_fetchall=mycursor.fetchall()
# 		total_amount=len(myresult_fetchall)
# 		# print(myresult_fetchall[0])
# 		# print(myresult_fetchall)       

# 		for i in range(len(myresult_fetchall)):
# 			myresult_fetchall[i]=list(myresult_fetchall[i])
# 			# print()
# 			# print(myresult_fetchall[i][9])
# 			myresult_fetchall[i][9]=myresult_fetchall[i][9].split(" ")

# 		if total_amount !=0:
# 			mytitle = mycursor.description
# 			column_name =[col[0] for col in mytitle]
# 			data=[]
# 			for i in range(total_amount):
# 				data.append(dict(zip(column_name,myresult_fetchall[i])))
# 			if len(data)==page_maxnum:
# 				next_page=page_num+1
# 			else:
# 				next_page=None
# 		else:
# 			return jsonify({                              
# 					"error": True,
# 					"message": "沒有資料了"	
# 				})

# 		return jsonify({                              
# 					"nextPage": next_page,
# 					"data": data	
# 				})




# 	#模糊&完全
# 	else:
# 		mycursor=mydb.cursor()
# 		sql_keyword="SELECT *FROM datas3 WHERE category=%s or name like concat('%',%s,'%') LIMIT %s,%s"
# 		first_num=page_num*0
# 		last_num=(page_num+1)*page_maxnum-1
# 		adr_keyword=(keyword,keyword,page_num*page_maxnum,page_maxnum)
# 		mycursor.execute(sql_keyword,adr_keyword)
# 		myresult_keyword=mycursor.fetchall()
# 		total_amount=len(myresult_keyword)

# 		for i in range(len(myresult_keyword)):
# 			myresult_keyword[i]=list(myresult_keyword[i])
# 			myresult_keyword[i][9]=myresult_keyword[i][9].split(" ")

# 		if total_amount !=0:
# 			mytitle = mycursor.description
# 			column_name =[col[0] for col in mytitle]
# 		# 	print()
# 		# 	print(column_name)
# 		# 	print(myresult_keyword)
# 			data=[]
# 			for i in range(total_amount):
# 				data.append(dict(zip(column_name,myresult_keyword[i])))
# 			if len(data)==page_maxnum:
# 				next_page=page_num+1
# 			else:
# 				next_page=None
# 		else:
# 			return jsonify({                              
# 					"error": True,
# 					"message": "沒有資料了"	
# 				})

# 		return jsonify({                              
# 					"nextPage": next_page,
# 					"data": data	
# 				})
# 	# except:
# 	# 	return jsonify({
# 	# 		"error":True,
# 	# 		"message":"奇奇妙妙錯誤"
# 	# 	})

# 	# finally:
# 	# 	mydb.close()


app.register_blueprint(attraction_id_blueprint)
# @app.route("/api/attraction/<attractionId>",methods=["GET"])
# def api_attractionId(attractionId):
# 	get_attractionId=attractionId
# 	# print(content)
# 	mycursor=mydb.cursor()
# 	sql="SELECT *FROM datas3 WHERE id=%s"
# 	adr=(get_attractionId,)
# 	mycursor.execute(sql,adr)
# 	myresult=mycursor.fetchall()
# 	# print(myresult)
# 	if myresult != []:
# 		mytitle = mycursor.description
# 		column_name =[col[0] for col in mytitle]
# 		# print(column_name)
# 		# print(myresult[0])
# 		data=[]
# 		for i in range(0,1):
# 			data.append(dict(zip(column_name,list(myresult[i]))))
# 		data=data[0]
# 		data["images"]=data["images"].split(" ")
# 		imgs_notnull=[]
# 		for e in data["images"]:
# 			if e!="" and ".MP3" not in e and ".FLV" not in e:
# 				imgs_notnull.append(e)
# 		data["images"]=imgs_notnull
# 		print(data)

# 		return jsonify({
# 				"data": data
# 			})

# 	else:
# 		return jsonify({
# 				"error": True,
# 				"message":"景點編號不正確"
# 			})
#-------------------------------------------------#-------------------------------------------------
app.register_blueprint(categories_blueprint)
# @app.route("/api/categories",methods=["GET"])
# def api_cotegories():
# 	try:	
# 		category_data=[]
# 		mycursor2=mydb.cursor()
# 		sql2="SELECT DISTINCT category FROM datas3"
# 		mycursor2.execute(sql2)
# 		myresult_category=mycursor2.fetchall()
# 		# for e in myresult_category:
# 		# 	category_data.append(str(e).replace("(","").replace(")","").replace(",","").replace("'",""))
# 		category_data = [cat[0] for cat in myresult_category]
		
# 		# print(myresult_category)
# 		print(category_data)
# 		return jsonify({
# 					"data": category_data
					
# 				})

# 	except TypeError:
# 		return jsonify({
# 					"error": True,
# 					"message":"型別發生錯誤"
# 				})

# 	except NameError:
# 		return jsonify({
# 					"error": True,
# 					"message":"使用沒有被定義的對象"
# 				})
				
# 	except Exception:
# 		return jsonify({
# 					"error": True,
# 					"message":"不知道怎麼了，反正發生錯誤惹"
# 				})




app.run(host='0.0.0.0',port=3000)








	# else:
    #     #模糊&完全
	# 	mycursor=mydb.cursor()
	# 	sql_keyword="SELECT *FROM datas3 WHERE category=%s or name like concat('%',%s,'%')"
	# 	adr_keyword=(keyword,keyword)
	# 	mycursor.execute(sql_keyword,adr_keyword)
	# 	myresult_keyword=mycursor.fetchall()
	# 	total_amount=len(myresult_keyword)
	# 	# print(myresult_keyword)
	# 	# return myresult_keyword
	# 	if total_amount !=0:
    #         return "error1"

	# 	# 	mytitle = mycursor.description
	# 	# 	column_name =[col[0] for col in mytitle]
	# 	# 	# print()
	# 	# 	# print(column_name)
	# 	# 	# print(myresult_fetchall)
            
	# 	# 	data=[]
    #     #     for i in range(total_amount):
    #     #         data.append(dict(zip(column_name,list(myresult_keyword[i]))))

    #     #     if total_amount < page_maxnum:
    #     #         page_num=None
    #     #         return jsonify({                              
    #     #             "nextPage": page_num,
    #     #             "data": data	
    #     #         })
    #     #     else:
    #     #         page_num=page_num+1
    #     #         return jsonify({                              
    #     #             "nextPage": page_num,
    #     #             "data": data	
    #     #         })



	# 	else:
	# 		return "error"
	# 	# # if total_amount < page_maxnum:
	# 	# # 	page_num=None
	# 	# # 	return jsonify({                              
	# 	# # 		"nextPage": page_num,
	# 	# # 		"data": data	
	# 	# # 	})
	# 	# # else:
	# 	# # 	page_num=page_num+1
	# 	# # 	return jsonify({                              
	# 	# # 		"nextPage": page_num,
	# 	# # 		"data": data	
	# 	# # 	})



				
	# finally:
	# 	mycousor.close()

			# return jsonify({                              
			# 	"nextPage": page_num,
			# 	"data": data	
			# })

	# except:
	# 	return jsonify({                              
	# 			"error": True,
	# 			"message": "ERROR_500"	
	# 		}),500




		# print(myresult_fetchall[0])
		# return str(myresult_fetchall[0])
	# else:
	# 	return "7777"

	# for i in range(total_amount):
	# 	myresult_fetchall[i]=list(myresult_fetchall[i])
	# 	myresult_fetchall[i][9]=myresult_fetchall[i][9].split(" ")

	# return myresult_fetchall

	# sql_fetchall="SELECT *from datas3 LIMIT %s,%s"
		# adr_fetchall=(0,12)
		# mycursor.execute(sql_fetchall,adr_fetchall)


	# print()
	# print(myresult_fetchall[0])
	# return str(myresult_fetchall[0])



	# 	# print(myresult[i][9])
	# 	myresult_real=[]
	# 	for e in myresult[i][9]:
	# 		if e!="" and ".MP3" not in e and ".FLV" not in e:
	# 			myresult_real.append(e)
	# 	myresult[i][9]=myresult_real


	# # # #取category
	# category_data=[]
	# mycursor2=mydb.cursor()
	# sql2="SELECT DISTINCT category FROM datas2"
	# mycursor2.execute(sql2)
	# myresult_category=mycursor2.fetchall()
	# for e in myresult_category:
	# 	category_data.append(str(e).replace("(","").replace(")","").replace(",","").replace("'","").replace("\\u3000",""))
	# print("keyword= ",keyword==None)
	# ##判斷比對方式
	# if keyword != "" and keyword in category_data:
	# 	print("category完全比對")
	# 	if keyword=="其他":
	# 		keyword="其  他"

	# 	mycursor=mydb.cursor()
	# 	sql_keyword="SELECT *FROM datas2 WHERE category=%s"
##--####sql_keyword="SELECT *FROM datas2 WHERE category=%s or name like concat('%',%s,'%')"
##--####adr_keyword=(keyword,keyword)
	# 	adr_keyword=(keyword,)
	# 	mycursor.execute(sql_keyword,adr_keyword)
	# 	myresult_keyword=mycursor.fetchall()
	# 	keyword_search_amount=len(myresult_keyword)
	# 	total_amount=keyword_search_amount
	# 	myresult=myresult_keyword

	# elif keyword == "":
	# 	print("不比了")

	# else:
	# 	#完全沒用到&keyword時的判定
	# 	if keyword == None:
	# 		pass
	# 	else:
	# 		print("name模糊比對")
	# 		mycursor=mydb.cursor()
	# 		print(keyword)
	# 		sql_vague="SELECT *FROM datas2 WHERE name like concat('%',%s,'%')"
	# 		adr_vague=(keyword,)
	# 		mycursor.execute(sql_vague,adr_vague)
	# 		myresult_vague=mycursor.fetchall()
	# 		vague_search_amount=len(myresult_vague)
	# 		total_amount=vague_search_amount
	# 		myresult=myresult_vague
	# 		print(myresult)

	
	# if (page_num)*12 > total_amount or page_num<0:
	# 	return jsonify({
	# 		"error": True,
	# 		"message": "錯誤!!! 超出可查詢範圍"
	# 	})

	# #正常+有下一頁
	# elif (page_num+1)*12<=total_amount:
	# 	mytitle = mycursor.description
	# 	column_name =[col[0] for col in mytitle]
	# 	data=[]
	# 	for i in range((page_num)*12,(page_num+1)*12):
	# 		data.append(dict(zip(column_name,list(myresult_fetchall[i]))))
	# 	return jsonify({                              
	# 		"nextPage": page_num+1,
	# 		"data": data		
	# 	})

	# #正常+無下一頁
	# else:
	# 	mytitle = mycursor.description
	# 	column_name =[col[0] for col in mytitle]
	# 	data=[]
	# 	# for i in range(0,12):
	# 	for i in range((page_num)*12,total_amount):
	# 		data.append(dict(zip(column_name,list(myresult_fetchall[i]))))
	# 	return jsonify({
	# 		"nextPage": None,
	# 		"data": data
	# 	})




# @app.route("/api/attraction/<attractionId>",methods=["GET"])
# def api_attractionId(attractionId):
# 	get_attractionId=attractionId
# 	# print(content)
# 	mycursor=mydb.cursor()
# 	sql="SELECT *FROM datas2 WHERE id=%s"
# 	adr=(get_attractionId,)
# 	mycursor.execute(sql,adr)
# 	myresult=mycursor.fetchall()
# 	# print(myresult)
# 	if myresult != []:
# 		mytitle = mycursor.description
# 		column_name =[col[0] for col in mytitle]
# 		# print(column_name)
# 		# print(myresult[0])
# 		data=[]
# 		for i in range(0,1):
# 			data.append(dict(zip(column_name,list(myresult[i]))))
# 		data=data[0]
# 		data["images"]=data["images"].split(" ")
# 		imgs_notnull=[]
# 		for e in data["images"]:
# 			if e!="" and ".MP3" not in e and ".FLV" not in e:
# 				imgs_notnull.append(e)
# 		data["images"]=imgs_notnull

# 		return jsonify({
# 				"data": data
# 			})

# 	else:
# 		return jsonify({
# 				"error": True,
# 				"message":"景點編號不正確"
# 			})


# @app.route("/api/categories",methods=["GET"])
# def api_cotegories():
# 	try:	
# 		category_data=[]
# 		mycursor2=mydb.cursor()
# 		sql2="SELECT DISTINCT category FROM datas2"
# 		mycursor2.execute(sql2)
# 		myresult_category=mycursor2.fetchall()
# 		# print(myresult_category[0])
# 		# print(myresult_category)
# 		for e in myresult_category:
# 			category_data.append(str(e).replace("(","").replace(")","").replace(",","").replace("'","").replace("\\u3000",""))
# 		print(category_data)
# 		return jsonify({
# 					"data": category_data
					
# 				})

# 	except TypeError:
# 		return jsonify({
# 					"error": True,
# 					"message":"型別發生錯誤"
# 				})

# 	except NameError:
# 		return jsonify({
# 					"error": True,
# 					"message":"使用沒有被定義的對象"
# 				})
				
# 	except Exception:
# 		return jsonify({
# 					"error": True,
# 					"message":"不知道怎麼了，反正發生錯誤惹"
# 				})

# app.run(host='0.0.0.0',port=3000)

















###==============================================























# from flask import *
# from flask import jsonify

# app=Flask(__name__)
# app.config["JSON_AS_ASCII"]=False
# app.config["TEMPLATES_AUTO_RELOAD"]=True

# import mysql.connector
# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Bb0970662139"
# )
# mycursor=mydb.cursor()
# sql="USE taipei_day_trip"
# mycursor.execute(sql)


# # Pages
# @app.route("/")
# def index():
# 	return render_template("index.html")
# @app.route("/attraction/<id>")
# def attraction(id):
# 	return render_template("attraction.html")
# @app.route("/booking")
# def booking():
# 	return render_template("booking.html")
# @app.route("/thankyou")
# def thankyou():
# 	return render_template("thankyou.html")




# @app.route("/api/attractions",methods=["GET"])
# def api_attraction():
# 	page_num=request.args.get("page",None)
# 	page_num=int(page_num)
# 	keyword=request.args.get("keyword",None)
	
# 	mycursor=mydb.cursor()
# 	sql="SELECT *FROM datas2"
# 	mycursor.execute(sql)
# 	myresult=mycursor.fetchall()
# 	total_amount=len(myresult)

# 	for i in range(total_amount):
# 		myresult[i]=list(myresult[i])
# 		myresult[i][9]=myresult[i][9].split(" ")
# 		# print(myresult[i][9])
# 		myresult_real=[]
# 		for e in myresult[i][9]:
# 			if e!="" and ".MP3" not in e and ".FLV" not in e:
# 				myresult_real.append(e)
# 		myresult[i][9]=myresult_real


# 	# # #取category
# 	category_data=[]
# 	mycursor2=mydb.cursor()
# 	sql2="SELECT DISTINCT category FROM datas2"
# 	mycursor2.execute(sql2)
# 	myresult_category=mycursor2.fetchall()
# 	for e in myresult_category:
# 		category_data.append(str(e).replace("(","").replace(")","").replace(",","").replace("'","").replace("\\u3000",""))
# 	print("keyword= ",keyword==None)
# 	##判斷比對方式
# 	if keyword != "" and keyword in category_data:
# 		print("category完全比對")
# 		if keyword=="其他":
# 			keyword="其  他"

# 		mycursor=mydb.cursor()
# 		sql_keyword="SELECT *FROM datas2 WHERE category=%s"
# 		adr_keyword=(keyword,)
# 		mycursor.execute(sql_keyword,adr_keyword)
# 		myresult_keyword=mycursor.fetchall()
# 		keyword_search_amount=len(myresult_keyword)
# 		total_amount=keyword_search_amount
# 		myresult=myresult_keyword

# 	elif keyword == "":
# 		print("不比了")

# 	else:
# 		#完全沒用到&keyword時的判定
# 		if keyword == None:
# 			pass
# 		else:
# 			print("name模糊比對")
# 			mycursor=mydb.cursor()
# 			print(keyword)
# 			sql_vague="SELECT *FROM datas2 WHERE name like concat('%',%s,'%')"
# 			adr_vague=(keyword,)
# 			mycursor.execute(sql_vague,adr_vague)
# 			myresult_vague=mycursor.fetchall()
# 			vague_search_amount=len(myresult_vague)
# 			total_amount=vague_search_amount
# 			myresult=myresult_vague
# 			print(myresult)

	
# 	if (page_num)*12 > total_amount or page_num<0:
# 		return jsonify({
# 			"error": True,
# 			"message": "錯誤!!! 超出可查詢範圍"
# 		})

# 	#正常+有下一頁
# 	elif (page_num+1)*12<=total_amount:
# 		mytitle = mycursor.description
# 		column_name =[col[0] for col in mytitle]
# 		data=[]
# 		for i in range((page_num)*12,(page_num+1)*12):
# 			data.append(dict(zip(column_name,list(myresult[i]))))
# 		return jsonify({                              
# 			"nextPage": page_num+1,
# 			"data": data		
# 		})

# 	#正常+無下一頁
# 	else:
# 		mytitle = mycursor.description
# 		column_name =[col[0] for col in mytitle]
# 		data=[]
# 		# for i in range(0,12):
# 		for i in range((page_num)*12,total_amount):
# 			data.append(dict(zip(column_name,list(myresult[i]))))
# 		return jsonify({
# 			"nextPage": None,
# 			"data": data
# 		})


# @app.route("/api/attraction/<attractionId>",methods=["GET"])
# def api_attractionId(attractionId):
# 	get_attractionId=attractionId
# 	# print(content)
# 	mycursor=mydb.cursor()
# 	sql="SELECT *FROM datas2 WHERE id=%s"
# 	adr=(get_attractionId,)
# 	mycursor.execute(sql,adr)
# 	myresult=mycursor.fetchall()
# 	# print(myresult)
# 	if myresult != []:
# 		mytitle = mycursor.description
# 		column_name =[col[0] for col in mytitle]
# 		# print(column_name)
# 		# print(myresult[0])
# 		data=[]
# 		for i in range(0,1):
# 			data.append(dict(zip(column_name,list(myresult[i]))))
# 		data=data[0]
# 		data["images"]=data["images"].split(" ")
# 		imgs_notnull=[]
# 		for e in data["images"]:
# 			if e!="" and ".MP3" not in e and ".FLV" not in e:
# 				imgs_notnull.append(e)
# 		data["images"]=imgs_notnull

# 		return jsonify({
# 				"data": data
# 			})

# 	else:
# 		return jsonify({
# 				"error": True,
# 				"message":"景點編號不正確"
# 			})


# @app.route("/api/categories",methods=["GET"])
# def api_cotegories():
# 	try:	
# 		category_data=[]
# 		mycursor2=mydb.cursor()
# 		sql2="SELECT DISTINCT category FROM datas2"
# 		mycursor2.execute(sql2)
# 		myresult_category=mycursor2.fetchall()
# 		# print(myresult_category[0])
# 		# print(myresult_category)
# 		for e in myresult_category:
# 			category_data.append(str(e).replace("(","").replace(")","").replace(",","").replace("'","").replace("\\u3000",""))
# 		print(category_data)
# 		return jsonify({
# 					"data": category_data
					
# 				})

# 	except TypeError:
# 		return jsonify({
# 					"error": True,
# 					"message":"型別發生錯誤"
# 				})

# 	except NameError:
# 		return jsonify({
# 					"error": True,
# 					"message":"使用沒有被定義的對象"
# 				})
				
# 	except Exception:
# 		return jsonify({
# 					"error": True,
# 					"message":"不知道怎麼了，反正發生錯誤惹"
# 				})

# app.run(host='0.0.0.0',port=3000)







# # 參考


# # 	#推薦
# # 	# sql="SELECT *from datas limit 0,12"
# # 	sql="SELECT *from datas limit %s,%s"
# # 	# mycursor.execute(sql)
# # 	adr=(0,12)
# # 	mycursor.execute(sql,adr)
# # 	myresult=mycursor.fetchall()
# # 	myresult=jsonify(myresult)
# # 	return myresult


# # 	#換方法
# # 	sql="SELECT *FROM datas"
# # 	cursor.execute(sql)
# # 	result=cursor.fetchmany(5)
# # 	print(result)
# # 	return result



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




