# ========================	read.env	========================
import os
from dotenv import load_dotenv
load_dotenv()
jwt_secret_key=os.getenv("jwt_secret_key")
jwt_algorithm=os.getenv("jwt_algorithm")



import jwt
import datetime
def jwt_encode(person_information):
    idPersion = person_information["id_people"]
    name = person_information["name"]
    email = person_information["email"]
    secret_key = jwt_secret_key
    payload={"data":{"id":idPersion,"email":email,"name":name},'iat': datetime.datetime.utcnow(),'exp':(datetime.datetime.utcnow() + datetime.timedelta(days=7))}
    token=jwt.encode(payload,secret_key,algorithm=jwt_algorithm)      #encode-algorithm
    return token

def jwt_decode(get_token):
    secret_key = jwt_secret_key
    decoded_token=jwt.decode(get_token,secret_key,algorithms=jwt_algorithm)     #decode-algorithms
    return decoded_token