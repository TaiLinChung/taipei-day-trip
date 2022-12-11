
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


#create connection pool
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
    # checkCookie()
    checkDataRegister()
    return jsonify(checkDataResponse)
    # return jsonify({"error":True,"message":"check the information and maybe doubleEmail"})


#   check databasesEmail
def checkDataRegister():
    global checkDataResponse
    try:
        connection_object = connection_pool.get_connection()
        mycursor =  connection_object.cursor()
        sql_check="SELECT *FROM accounts WHERE email=%s"
        adr_check=(email,)
        mycursor.execute(sql_check,adr_check)
        myresult_check=mycursor.fetchone()
        # email未註冊過
        if myresult_check==None and name!="" and password!="":
            print("有執行註冊")
            # 執行註冊動作
            register()
            checkDataResponse={"ok":True}
        else:
            print("未執行註冊")
            checkDataResponse={"error":True,"message":"400 註冊失敗 重複的 Email 或其他原因"}
    except:
        print("有問題")
        checkDataResponse=({"error":True,"message":"500 伺服器內部錯誤"})
    finally:
        mycursor.close()
        connection_object.close()


def register():
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

    global checkDataResponse
    if request.method=="PUT":
        SigninDataFromFrontEnd = request.get_json()
        if SigninDataFromFrontEnd != {}:
            global email
            email=SigninDataFromFrontEnd["email"]
            global password
            password=SigninDataFromFrontEnd["password"]
            checkDataSignin()
            print("我在登入頁面")
            return checkDataResponse
        # # 前往非登入狀態 把cookie解掉換成空，待改成PUT方法
        # else:
        #     checkDataResponse=jsonify({"error":True,"message":"非登入狀態"})
        #     checkDataResponse.set_cookie("token",'', expires=0)
        #     return checkDataResponse
    
    if request.method=="GET":
        # checkCookie()
        getToken=request.cookies.get("token")
        print("查看當前頁面cookies中的Token",getToken)
        # decoded
        if getToken!=None:
            decoded=jwt.decode(getToken,secret_key,algorithms='HS256')     #decode-algorithms
            print("解密完看data中的登錄者姓名",decoded["data"]["name"])
            return decoded
        else:
            print("沒有token")
            return jsonify({"data":None})
    ##signout
    if request.method=="DELETE":
        logOutDataFromFrontEnd = request.get_json()
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
from datetime import datetime
def jwtEncode():
    global payload
    global token
    payload={"data":{"id":idPersion,"email":email,"name":name,"admin":True}}
    print(payload)
    token=jwt.encode(payload,secret_key,algorithm='HS256')      #encode-algorithm
    print(token)
    # decoded=jwt.decode(token,secret_key,algorithms='HS256')     #decode-algorithms
    # print(decoded)

