from flask import *
from flask import jsonify

#相應app.py
orders_blueprint=Blueprint("orders_blueprint",__name__)
order_num_blueprint=Blueprint("order_num_blueprint",__name__)


from model import jwt_decode
from model import order_data_is_empty
from model import check_email_format
from model import order_reservation_exist
from model import write_historical_order
from model import pay_by_prime_API
from model import write_transaction_record_in_historical_order
from model import get_transaction_record_in_historical_order
from model import delete_reservation_flash_by_person_id


@orders_blueprint.route("/api/orders",methods=["POST"])
def api_orders():
    try:
        get_token=request.cookies.get("token")
        decode=jwt_decode(get_token)
        person_id=decode["data"]["id"]
        order_data_from_frontEnd = request.get_json()
        if order_data_is_empty(order_data_from_frontEnd):
            return jsonify({"error": True,"message": "order資料皆不可為空"})
        contact_email=order_data_from_frontEnd["order"]["contact"]["email"]
        if not check_email_format(contact_email):
            return jsonify({"error":True,"message":"信箱型態有誤"})
        if not order_reservation_exist(person_id,order_data_from_frontEnd):
            return jsonify({"error":True,"message":"此筆訂單並不存在屬於您的預訂清單中"})
        the_last_order_number=write_historical_order(person_id,order_data_from_frontEnd)
        tappay_api_response=pay_by_prime_API(order_data_from_frontEnd)
        write_transaction_record_in_historical_order(the_last_order_number,tappay_api_response)
        delete_reservation_flash_by_person_id(person_id)
        transaction_record=get_transaction_record_in_historical_order(the_last_order_number)
        return jsonify(transaction_record)

    except Exception as e:
        print("orders伺服器內部錯誤: ",e)
        return jsonify({"error": True,"message": "orders伺服器內部錯誤"})



# 利用獲取訂單歷史資訊
# from model import get_transaction_record_by_order_number
from model import get_transaction_record_by_transaction_number
@order_num_blueprint.route("/api/order/<orderNumber>",methods=["GET"])
def api_order_num(orderNumber):
    # print(orderNumber)
    try:
        print(orderNumber)
        get_token=request.cookies.get("token")
        decode=jwt_decode(get_token)
        person_id=decode["data"]["id"]
        transaction_number=orderNumber
        transaction_record=get_transaction_record_by_transaction_number(transaction_number,person_id)
        # print(transaction_record)
        if transaction_record:
            return jsonify(transaction_record)
        return jsonify({"error":True,"message":"此筆訂單並不存在屬於您的預訂清單中"})

    except Exception as e:
        print("order/<orderNumber>伺服器內部錯誤: ",e)
        return jsonify({"error": True,"message": "order/<orderNumber>伺服器內部錯誤"})