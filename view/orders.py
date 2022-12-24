from flask import *
from flask import jsonify

#相應app.py
orders_blueprint=Blueprint("orders_blueprint",__name__)
orders_auth_blueprint=Blueprint("orders_auth_blueprint",__name__)


from model import jwt_decode
from model import order_data_is_empty
from model import check_email_format
from model import order_reservation_exist

@orders_blueprint.route("/api/orders",methods=["POST"])
def api_orders():
    try:
        get_token=request.cookies.get("token")
        decode=jwt_decode(get_token)
        person_id=decode["data"]["id"]
        order_data_from_frontEnd = request.get_json()
        if order_data_is_empty(order_data_from_frontEnd):
            return jsonify({"error": True,"message": "order資料皆不可為空"})
        # contact_email=order_data_from_frontEnd["order"]["contact"]["email"]
        # if not check_email_format(contact_email):
        #     return jsonify({"error":True,"message":"信箱型態有誤"})
        if not order_reservation_exist(person_id,order_data_from_frontEnd):
            return jsonify({"error":True,"message":"此筆預約訂單並不存在"})
        
        
        
        
        print("hello orders")
        print(order_data_from_frontEnd)


        return jsonify({"ok":True})
    except Exception as e:
        print("orders伺服器內部錯誤: ",e)
        return jsonify({"error": True,"message": "orders伺服器內部錯誤"})