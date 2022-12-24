
import jwt
import datetime
def jwt_encode(person_information):
    idPersion = person_information["id_people"]
    name = person_information["name"]
    email = person_information["email"]
    secret_key = "wehelpJwtKEY@999"
    payload={"data":{"id":idPersion,"email":email,"name":name},'iat': datetime.datetime.utcnow(),'exp':(datetime.datetime.utcnow() + datetime.timedelta(days=7))}
    token=jwt.encode(payload,secret_key,algorithm='HS256')      #encode-algorithm
    return token

def jwt_decode(get_token):
    secret_key = "wehelpJwtKEY@999"
    decoded_token=jwt.decode(get_token,secret_key,algorithms='HS256')     #decode-algorithms
    return decoded_token