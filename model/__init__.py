from model.attraction_model import attraction
print("hhhhhhh這是來自init的聲音")
from model.attraction_model import name
kkk="1234999"







# ##try more by apple
# import mysql.connector.pooling
# dbconfig={
# 	"user":"root",
# 	"password":"Bb0970662139",
# 	"host":"localhost",
# 	"database":"taipei_day_trip",
# }
# connection_pool = mysql.connector.pooling.MySQLConnectionPool(
# 	pool_name="wehelp_pool",
# 	pool_size=5,
# 	pool_reset_session=True,
# 	**dbconfig
# )
# connection_object = connection_pool.get_connection()
# mycursor =  connection_object.cursor()

# mycursor.close()
# connection_object.close()

from model.attraction_model import connect
from model.DealDatabase import DealDatabase
from model.DealDatabase import DealBooking
from model.DealDatabase import GetDataForBookingPage
from model.DealDatabase import DeleteDataForBookingPage