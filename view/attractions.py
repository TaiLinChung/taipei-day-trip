from flask import *
from flask import jsonify

#相應app.py
attractions_blueprint=Blueprint("attractions_blueprint",__name__)

from model import loading_all_picture_by_attractions
from model import loading_matched_picture
@attractions_blueprint.route("/api/attractions",methods=["GET"])
def api_attractions():

	try:
		page_num_now=int(request.args.get("page",""))
		keyword=request.args.get("keyword","")
		page_maxnum=12
		##單純頁數
		if keyword == "":
			response=loading_all_picture_by_attractions(page_maxnum,page_num_now)
			return jsonify(response)
		#模糊&完全
		else:
			
			response=loading_matched_picture(keyword,page_num_now,page_maxnum)
			return jsonify(response)
	except Exception as e:
		print("attractions伺服器內部錯誤: ",e)
		return jsonify({"error":True,"message":"500 伺服器內部錯誤"})

