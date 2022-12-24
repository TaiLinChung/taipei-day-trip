def register_data_is_empty(name,email,password):
    if name == "" or email == "" or password == "":
        return True

def signin_data_is_empty(email,password):
    if email == "" or password == "":
        return True


def booking_data_is_empty(booking_attraction_id,booking_date,booking_price,booking_time):
    if booking_attraction_id == "" or booking_date == "" or booking_price == "" or booking_time == "":
        return True


def order_data_is_empty(order_data_from_frontEnd):
    prime=order_data_from_frontEnd["prime"]
    order_price=order_data_from_frontEnd["order"]["price"]
    attraction_id=order_data_from_frontEnd["order"]["trip"]["attraction"]["id"]
    attraction_name=order_data_from_frontEnd["order"]["trip"]["attraction"]["name"]
    attraction_address=order_data_from_frontEnd["order"]["trip"]["attraction"]["address"]
    attraction_image=order_data_from_frontEnd["order"]["trip"]["attraction"]["image"]
    order_date=order_data_from_frontEnd["order"]["trip"]["date"]
    order_time=order_data_from_frontEnd["order"]["trip"]["time"]
    contact_name=order_data_from_frontEnd["order"]["contact"]["name"]
    contact_email=order_data_from_frontEnd["order"]["contact"]["email"]
    contact_phone=order_data_from_frontEnd["order"]["contact"]["phone"]
    if prime == "" or order_price == "" or attraction_id == "" or attraction_name == "" or attraction_address == "" or attraction_image == "" or order_date == "" or order_time == "" or contact_name == "" or contact_email == "" or contact_phone == "":
        return True




import re
# from flask import jsonify
def check_email_format(email):
    if re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
        return True
