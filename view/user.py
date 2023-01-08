from flask import *
from flask import jsonify


#相應app.py
user_blueprint=Blueprint("user_blueprint",__name__)
user_auth_blueprint=Blueprint("user_auth_blueprint",__name__)


from model import register_data_is_empty
from model import check_email_format
from model import register_email_exist
from model import register
from model import signin_data_is_empty
from model import signin_account_exist




@user_blueprint.route("/api/user",methods=["POST"])
def api_user():
    try:
        registerDataFromFrontEnd = request.get_json()  
        name=registerDataFromFrontEnd["name"]
        email=registerDataFromFrontEnd["email"]
        password=registerDataFromFrontEnd["password"]
        if register_data_is_empty(name,email,password):
            return jsonify({"error":True,"message":"註冊資料不可為空"})
        if not check_email_format(email):
            return jsonify({"error":True,"message":"信箱型態有誤，點此重新註冊"})
        if register_email_exist(email):
            return jsonify({"error":True,"message":"信箱已被註冊，點此重新註冊"})
        if register(name,email,password):
            return jsonify({"ok":True})
    except Exception as e:
        print("api_user伺服器內部錯誤: ",e)
        return jsonify({"error":True,"message":"500 伺服器內部錯誤"})




from model import jwt_encode
from model import jwt_decode
from model import check_user_id_in_token_exist
@user_auth_blueprint.route("/api/user/auth",methods=["GET","PUT","DELETE"])
def api_user_auth():

    if request.method=="PUT":
        try:
            SigninDataFromFrontEnd = request.get_json()
            email=SigninDataFromFrontEnd["email"]
            password=SigninDataFromFrontEnd["password"]
            if signin_data_is_empty(email,password):
                return jsonify({"error":True,"message":"登入資料不可為空"})
            if not check_email_format(email):
                return jsonify({"error":True,"message":"信箱型態有誤，請確認"})
            if not signin_account_exist(email,password):
                return jsonify({"error":True,"message":"400 登入失敗"}) #人為問題
            person_information=signin_account_exist(email,password)
            token=jwt_encode(person_information)
            response=jsonify({"ok":True})
            response.set_cookie("token",token,max_age = 7 * 24 * 60 * 60)
            return response
        except Exception as e:
            print("api_user_auth伺服器內部錯誤: ",e)
            return jsonify({"error":True,"message":"500 伺服器內部錯誤"})

    if request.method=="GET":
        get_token=request.cookies.get("token")
        if get_token==None:
            return jsonify({"data":None})
        try:
            decode=jwt_decode(get_token)
            if not check_user_id_in_token_exist(decode):
                return jsonify({"data":None})
            return jsonify(decode)
        except Exception as e:
            print("api_user_auth伺服器內部錯誤: ",e)
            return jsonify({"error":True,"message":"500 伺服器內部錯誤"})

    if request.method=="DELETE":
        try:
            response=jsonify({"ok":True})
            response.set_cookie("token",'', expires=0)
            return response
        except Exception as e:
            print("api_user_auth伺服器內部錯誤: ",e)
            return jsonify({"error":True,"message":"500 伺服器內部錯誤"})
