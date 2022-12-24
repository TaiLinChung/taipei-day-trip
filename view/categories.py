from flask import *
from flask import jsonify


from model import get_categories_search_bar_item_data
#相應app.py
categories_blueprint=Blueprint("categories_blueprint",__name__)

@categories_blueprint.route("/api/categories",methods=["GET"])
def api_categories():
	try:
		response=get_categories_search_bar_item_data()
		return jsonify({"data": response})
	except Exception as e:
		print("categories伺服器內部錯誤: ",e)
		return jsonify({"error": True,"message": "categories伺服器內部錯誤"})
	
