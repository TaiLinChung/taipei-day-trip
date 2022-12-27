from flask import *
from flask import jsonify


#相應app.py
attraction_id_blueprint=Blueprint("attraction_blueprint",__name__)

from model import get_attraction_data_by_id
@attraction_id_blueprint.route("/api/attraction/<attractionId>",methods=["GET"])
def api_attractionId(attractionId):
	try:
		response=get_attraction_data_by_id(attractionId)
		return jsonify(response)
	except:
		return {"error":True},500
