
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
mycursor.close()


# from view.sample import my_func
# my_func()
# my_func()
# from model.aaa import my_func
# my_func()
# from model.attraction_model import attraction
from model import attraction #模組
from model import name
from model import connect
print(name)
# print(attraction())
attraction()
connect(4,5)
connect(7,10)

# from model.user_model import user
# attraction()
# user()



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



#相應app.py
user_blueprint=Blueprint("user_blueprint",__name__)
user_auth_blueprint=Blueprint("user_auth_blueprint",__name__)


#Set Gobal
name=None
email=None
password=None
idPersion=None
checkDataResponse=None


from model import DealDatabase
#POST
@user_blueprint.route("/api/user",methods=["POST"])
def api_user():
    registerDataFromFrontEnd = request.get_json()  
    global name
    name=registerDataFromFrontEnd["name"]
    global email
    email=registerDataFromFrontEnd["email"]
    global password
    password=registerDataFromFrontEnd["password"]
    print("我在註冊頁面")
    ##try apple--------------------------------------------------------------------
    # print("-----英雄------",DealDatabase(name,email,password))
    # DealDatabase(name,email,password)

    checkRegisteEmail()
    return jsonify(checkDataResponse)



# first checkEmail
import re
def checkRegisteEmail():
    if re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
        dataRegiste()
    else:
        checkDataResponse={"error":True,"message":"信箱有誤，點此重新註冊"}
        return jsonify(checkDataResponse)



#   DataRegiste
def dataRegiste():
    global checkDataResponse
    try:
        connection_object = connection_pool.get_connection()
        mycursor =  connection_object.cursor()
        sql_check="SELECT *FROM accounts WHERE email=%s"
        adr_check=(email,)
        mycursor.execute(sql_check,adr_check)
        myresult_check=mycursor.fetchone()
        if myresult_check==None and name!="" and password!="":
            print("有執行註冊")
            registe()
            checkDataResponse={"ok":True}
        else:
            print("未執行註冊")
            checkDataResponse={"error":True,"message":"Email重複，點此重新註冊"}
    except:
        print("原本的有問題")
        checkDataResponse=({"error":True,"message":"500 伺服器內部錯誤"})
    finally:
        mycursor.close()
        connection_object.close()


def registe():
    try:
        connection_object = connection_pool.get_connection()
        mycursor =  connection_object.cursor()
        sql_register="INSERT INTO accounts(name,email,password) VALUES(%s,%s,%s)"
        val_register=(name,email,password)
        mycursor.execute(sql_register,val_register)
        connection_object.commit()
    except:
        print("有問題")
    finally:
        mycursor.close()
        connection_object.close()


#"GET","PUT","DELETE"
@user_auth_blueprint.route("/api/user/auth",methods=["GET","PUT","DELETE"])
def api_user_auth():
    print("user/auth每次被呼叫收到的訊息",request.data)
    global checkDataResponse
    if request.method=="PUT":
        SigninDataFromFrontEnd = request.get_json()
        global email
        email=SigninDataFromFrontEnd["email"]
        global password
        password=SigninDataFromFrontEnd["password"]
        checkDataSignin()
        print("我在登入頁面")
        return checkDataResponse
    
    if request.method=="GET":
        # checkCookie
        getToken=request.cookies.get("token")
        # print("查看當前頁面cookies中的Token",getToken)
        # decoded
        if getToken!=None:
            try:
                # print("執行解密")
                decoded=jwt.decode(getToken,secret_key,algorithms='HS256')     #decode-algorithms
                # print("解密完看data中的登錄者姓名",decoded["data"]["name"])
                return decoded
            except:
                # 10S測試用
                # print("token失效還想進入!!!送你出去")
                return jsonify({"data":None})
        else:
            print("沒有token")
            return jsonify({"data":None})
    ##signout
    if request.method=="DELETE":
        print("登出刪除token")
        # logOutDataFromFrontEnd = request.get_json()
        checkDataResponse=jsonify({"ok":True})
        checkDataResponse.set_cookie("token",'', expires=0)
        return checkDataResponse



def checkDataSignin():
    global checkDataResponse
    global idPersion
    global name
    global email
    global password
    try:
        connection_object = connection_pool.get_connection()
        mycursor =  connection_object.cursor()
        sql_check="SELECT *FROM accounts WHERE email=%s and password=%s"
        adr_check=(email,password)
        mycursor.execute(sql_check,adr_check)
        myresult_check=mycursor.fetchone()
        
        if myresult_check!=None and name!="" and password!="":
            print("登入成功")
            idPersion = myresult_check[0]
            name = myresult_check[1]
            email = myresult_check[2]
            password = myresult_check[3]
            jwtEncode()
            checkDataResponse = jsonify({"ok":True})
            checkDataResponse.set_cookie("token",token,max_age = 7 * 24 * 60 * 60)

        else:
            print("登入失敗")
            checkDataResponse=jsonify({"error":True,"message":"400 登入資料錯誤 或其他原因"}) #人為問題
    except:
        print("伺服器內部有問題")
        checkDataResponse=({"error":True,"message":"500 伺服器內部錯誤"})
    finally:
        mycursor.close()
        connection_object.close()



# jwtEncode
# header={"typ":"JWT","alg":"HS256"}
payload={}
secret_key = "wehelpJwtKEY@999"
token=None
import jwt
import datetime
def jwtEncode():
    global payload
    global token
    
    # payload={"data":{"id":idPersion,"email":email,"name":name},'iat': datetime.datetime.utcnow(),'exp':(datetime.datetime.utcnow() + datetime.timedelta(seconds=10))}
    payload={"data":{"id":idPersion,"email":email,"name":name},'iat': datetime.datetime.utcnow(),'exp':(datetime.datetime.utcnow() + datetime.timedelta(days=7))}
    # print(payload)
    token=jwt.encode(payload,secret_key,algorithm='HS256')      #encode-algorithm
    # print(token)
    # decoded=jwt.decode(token,secret_key,algorithms='HS256')     #decode-algorithms
    # print(decoded)

    # # 設置 JWT 有效期限為 10 秒
    # expiration_time = datetime.timedelta(seconds=10)
    # header = {"alg": "HS256"}
    # payload = {"id":idPersion,"email":email,"name":name}
    # token = pyjwt.PyJWT.encode(header, payload, secret_key, expiration_time)

