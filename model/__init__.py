# 使用init原理解析演示
# from model.attraction_model import attraction
# print("hhhhhhh這是來自init的聲音")
# from model.attraction_model import name
# kkk="1234999"
# from model.attraction_model import connect


from model.CheckData import signin_data_is_empty
from model.DealDatabase import signin_account_exist

from model.CheckData import register_data_is_empty
from model.CheckData import check_email_format
from model.DealDatabase import register_email_exist
from model.DealDatabase import register

from model.CheckData import booking_data_is_empty
from model.DealDatabase import booking_people_exist
from model.DealDatabase import update_booking_data
from model.DealDatabase import insert_booking_data
from model.DealDatabase import get_data_for_booking_page
from model.DealDatabase import delete_data_for_bookin_page

from model.jwt import jwt_encode
from model.jwt import jwt_decode


from model.DealDatabase import get_categories_search_bar_item_data
from model.DealDatabase import loading_all_picture_by_attractions
from model.DealDatabase import loading_select_picture_by_attractions



from model.CheckData import order_data_is_empty
from model.DealDatabase import order_reservation_exist
from model.DealDatabase import write_historical_order
from model.tappay import pay_by_prime_API
from model.DealDatabase import write_transaction_record_in_historical_order
# from model.DealDatabase import change_history_order_status
from model.DealDatabase import get_transaction_record_in_historical_order
from model.DealDatabase import delete_reservation_flash_by_person_id

from model.DealDatabase import get_transaction_record_by_order_number

from model.DealDatabase import get_transaction_record_by_transaction_number





# # from model.DealDatabase import DealDatabase
# from model.DealDatabase import deal_Booking
# from model.DealDatabase import GetDataForBookingPage
# from model.DealDatabase import DeleteDataForBookingPage

