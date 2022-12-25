from flask import *
from flask import jsonify

#相應app.py
thankyou_blueprint=Blueprint("thankyou_blueprint",__name__)



from model import jwt_decode
from model import get_transaction_record_by_transaction_number
@thankyou_blueprint.route("/thankyou",methods=["GET"])
def api_thankyou():
    get_token=request.cookies.get("token")
    decode=jwt_decode(get_token)
    person_id=decode["data"]["id"]
    transaction_number=int(request.args.get("number",""))
    print(transaction_number)
    if not get_transaction_record_by_transaction_number(transaction_number,person_id):
        # print("您試圖輸入的單編號不屬於您")
        return ({"error":True,"message":"您試圖輸入的單編號不屬於您，請確認"})
    return render_template("thankyou.html")