
from flask import *
from flask import jsonify

##前置作業與資料庫連線創建資料庫跟表

import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Bb0970662139"
)
mycursor=mydb.cursor()
sql="CREATE DATABASE IF NOT EXISTS taipei_day_trip"
mycursor.execute(sql)
sql="USE taipei_day_trip"
mycursor.execute(sql)
sql="CREATE TABLE IF NOT EXISTS accounts(id_people INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(200),email VARCHAR(200),password VARCHAR(200))"
mycursor.execute(sql)



#相應app.py
user_blueprint=Blueprint("user_blueprint",__name__)
user_auth_blueprint=Blueprint("user_auth_blueprint",__name__)


#   Set Gobal
name=""
email=""
password=""

#   use POST get front
@user_blueprint.route("/api/user",methods=["POST"])
def api_user():
    global name
    name=request.form["registerName"]
    global email
    email=request.form["registerEmail"]
    global password
    password=request.form["registerPassword"]
    # print("1:",name)
    # checkEmail()
    return checkEmail()

#   check databases
def checkEmail():
    try:
        mycursor=mydb.cursor()
        sql_check="SELECT *FROM accounts WHERE email=%s"
        adr_check=(email,)
        mycursor.execute(sql_check,adr_check)
        myresult_check=mycursor.fetchone()

        # email未註冊過
        if myresult_check==None and name!="" and password!="":
            # 執行註冊動作
            register()
            return jsonify({"ok":True}),200
        else:
            return jsonify({"error":True,"message":"check the information and maybe doubleEmail"}),400 #人為問題
    except:
        return jsonify({"error":"checkEmail()"}),500 #伺服器網路運作問題
    

#   use POST get front
@user_auth_blueprint.route("/api/user/auth",methods=["GET","PUT","DELETE"])
def api_user_auth():
    return "7777"




def register():
    sql_register="INSERT INTO accounts(name,email,password) VALUES(%s,%s,%s)"
    val_register=(name,email,password)
    mycursor.execute(sql_register,val_register)
    mydb.commit()

#         sql="INSERT INTO accounts(name,account,password) VALUES(%s,%s,%s)"
#         val=(name,account,password)
#         mycursor.execute(sql,val)
#         mydb.commit()









# from flask import jsonify
# @app.route("/api/member/",methods=["GET","PATCH"])
# def apimember():
#     if request.method=="GET":
#         account=request.args.get("username",None)
#         mycursor=mydb.cursor()
#         sql="SELECT id_people,name,account FROM accounts WHERE account=%s"
#         adr=(account,)
#         mycursor.execute(sql,adr)
#         myresult=mycursor.fetchone()




# ##前置作業與資料庫連線創建資料庫跟表

# import mysql.connector
# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Bb0970662139"
# )
# mycursor=mydb.cursor()
# sql="CREATE DATABASE IF NOT EXISTS signin"
# mycursor.execute(sql)
# sql="USE signin"
# mycursor.execute(sql)
# sql="CREATE TABLE IF NOT EXISTS accounts(id_people INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(20),account VARCHAR(20),password VARCHAR(20))"
# mycursor.execute(sql)
# sql="CREATE TABLE IF NOT EXISTS messageTable(id_message INT PRIMARY KEY AUTO_INCREMENT,id_people INT,message VARCHAR(200))"
# mycursor.execute(sql)



# #1.導引至前端主頁面
# #使用GET方法，處理路徑/的對應函式
# @app.route("/")
# def index():
#     return render_template("indexW06.html")



# #2.接收前端回傳的註冊資訊
# #使用POST方法，處理路徑/signup 的對應函式
# @app.route("/signup", methods=["POST"])
# def signup():
#     #接收 POST 方法的 Query String
#     account=request.form["account"]
#     password=request.form["password"]
#     name=request.form["name"]
#     print("註冊姓名",name)
#     print("註冊帳號",account)
#     print("註冊密碼",password)

#     #3.連線資料庫判定是否註冊過
#     mycursor=mydb.cursor()
#     sql_all="SELECT *FROM accounts WHERE (account=%s and password=%s) or name=%s"
#     adr_all=(account,password,name)
#     mycursor.execute(sql_all,adr_all)
#     myresult_all=mycursor.fetchone()

#     sql_name="SELECT *FROM accounts WHERE name=%s"
#     adr_name=(name,)
#     mycursor.execute(sql_name,adr_name)
#     myresult_name=mycursor.fetchone()

#     #3.1帳號密碼在資料庫中找不到，註冊成功，導向登入頁面member
#     if myresult_all == None and (name!="" and account!="" and password!=""):
#         sql="INSERT INTO accounts(name,account,password) VALUES(%s,%s,%s)"
#         val=(name,account,password)
#         mycursor.execute(sql,val)
#         mydb.commit()
#         return redirect("http://127.0.0.1:3000/")

#     elif myresult_all == None and (name=="" or account=="" or password==""):
#         return redirect("http://127.0.0.1:3000/error?message=資料不全請重新填寫")
    
#     elif myresult_all == None and myresult_name != None:
#         print("註冊姓名重複，導向錯誤頁面")
#         return redirect("http://127.0.0.1:3000/error?message=暱稱重複已經被註冊過")

#     else:
#         print("已註冊過，導向錯誤頁面")
#         return redirect("http://127.0.0.1:3000/error?message=同組帳號"+'、'+"密碼已經被註冊")
        
