from flask import *
from flask import jsonify

#相應app.py
member_blueprint=Blueprint("member_blueprint",__name__)


from model import jwt_decode
from model import check_user_id_in_token_exist
from model import get_account_information_by_person_id
from model import register_data_is_empty
from model import change_email_is_not_exist
from model import check_email_format
from model import update_account_information
from model import jwt_encode
@member_blueprint.route("/api/member",methods=["GET","POST"])
def api_member():
    if request.method=="GET":
        try:
            get_token=request.cookies.get("token")
            decode=jwt_decode(get_token)
            if not check_user_id_in_token_exist(decode):
                return jsonify({"error":True,"message":"身分異常"})
            person_id=decode["data"]["id"]
            response=get_account_information_by_person_id(person_id)
            return jsonify(response)
        except:
            return jsonify({"error":True,"message":"系統異常，請聯繫客服處理"})


    if request.method=="POST":
        try:
            get_token=request.cookies.get("token")
            newMemberData = request.get_json()
            name=newMemberData["name"]
            email=newMemberData["email"]
            password=newMemberData["password"]
            decode=jwt_decode(get_token)
            id_people=decode["data"]["id"]
            print(newMemberData)
            print("----")
            print(decode)
            origin_token_email=decode["data"]["email"]
            if not check_user_id_in_token_exist(decode):
                return jsonify({"error":True,"message":"身分異常"})
            if register_data_is_empty(name,email,password):
                return jsonify({"error":True,"message":"上方資料請完整填寫"})
            if not check_email_format(email):
                return jsonify({"error":True,"message":"信箱格式不符，請檢查"})
            if not(origin_token_email == email) and not(change_email_is_not_exist(email)):
                return jsonify({"error":True,"message":"信箱重複，請更換"})
            person_information=update_account_information(name,email,password,id_people)
            token=jwt_encode(person_information)
            response=jsonify({"ok":True})
            response.set_cookie("token",token,max_age = 7 * 24 * 60 * 60)
            return response

        except:
            return jsonify({"error":True,"message":"系統異常，請聯繫客服處理"})
