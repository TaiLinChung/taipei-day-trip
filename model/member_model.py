
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
connection_pool = mysql.connector.pooling.MySQLConnectionPool(
	pool_name="wehelp_pool",
	pool_size=5,
	pool_reset_session=True,
	**dbconfig
)

def get_account_information_by_person_id(person_id):
    try:
        connection_object = connection_pool.get_connection()
        mycursor = connection_object.cursor(dictionary=True) # 設定fetchone跟fetchall有搜尋結果時的回傳都為字典形式
        sql_check="SELECT *FROM accounts WHERE id_people=%s"
        adr_check=(person_id,)
        mycursor.execute(sql_check,adr_check)
        myresult=mycursor.fetchone()
        return myresult   
        # print(person_id)

    except Exception as e:
        print("member_model get_account_information_by_person_id()發生問題",e)
    finally:
        mycursor.close()
        connection_object.close()


def change_email_is_allowed(email):
    try:
        connection_object = connection_pool.get_connection()
        mycursor = connection_object.cursor(dictionary=True) # 設定fetchone跟fetchall有搜尋結果時的回傳都為字典形式
        sql_check="SELECT *FROM accounts WHERE email=%s"
        adr_check=(email,)
        mycursor.execute(sql_check,adr_check)
        myresult=mycursor.fetchone()
        if myresult==None:
            return True  

    except Exception as e:
        print("member_model change_email_is_allowed()發生問題",e)
    finally:
        mycursor.close()
        connection_object.close()



def update_account_information(name,email,password,id_people):
    try:
        connection_object = connection_pool.get_connection()
        mycursor = connection_object.cursor(dictionary=True) # 把fetchone跟fetchall的搜尋結果回傳都為字典形式
        sql="UPDATE accounts SET name=%s,email=%s,password=%s WHERE id_people=%s"
        val = (name,email,password,id_people)	
        mycursor.execute(sql,val)
        connection_object.commit()
        person_information={
            "id_people":id_people,
            "name":name,
            "email":email
        }
        return person_information 

    except Exception as e:
        print("member_model update_account_information()發生問題",e)
    finally:
        mycursor.close()
        connection_object.close()






# ========================	register	========================

# def register_email_exist(email):
# 	try:
# 		connection_object = connection_pool.get_connection()
# 		mycursor = connection_object.cursor(dictionary=True) # 設定fetchone跟fetchall有搜尋結果時的回傳都為字典形式
# 		sql_check="SELECT *FROM accounts WHERE email=%s"
# 		adr_check=(email,)
# 		mycursor.execute(sql_check,adr_check)
# 		myresult_checkEmail=mycursor.fetchone()
# 		if myresult_checkEmail != None:
# 			return True
# 	except:
# 		print("DealDatabase register_email_exist()發生問題")
# 	finally:
# 		mycursor.close()
# 		connection_object.close()