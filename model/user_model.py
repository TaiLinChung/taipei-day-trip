# ========================	read.env	========================

import os
from dotenv import load_dotenv
load_dotenv()
sql_password=os.getenv("sql_password")

import mysql.connector.pooling

dbconfig={
	"user":"root",
	"password":sql_password,
	"host":"localhost",
	"database":"taipei_day_trip",
}
#	create connection pool
connection_pool = mysql.connector.pooling.MySQLConnectionPool(
	pool_name="wehelp_pool",
	pool_size=5,
	pool_reset_session=True,
	**dbconfig
)


# ========================	check user_id_in_token_exist	========================
def check_user_id_in_token_exist(decode):
    try:
        user_id=decode["data"]["id"]
        connection_object = connection_pool.get_connection()
        mycursor = connection_object.cursor(dictionary=True) # 設定fetchone跟fetchall有搜尋結果時的回傳都為字典形式
        sql_check="SELECT *FROM accounts WHERE id_people=%s"
        adr_check=(user_id,)
        mycursor.execute(sql_check,adr_check)
        myresult=mycursor.fetchone()
        if myresult != None:
            return True
    except:
        print("user_model check_user_id_in_token_exist()發生問題")
    finally:
        mycursor.close()
        connection_object.close()