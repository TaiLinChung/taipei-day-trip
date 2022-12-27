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

def get_attraction_data_by_id(attractionId):
    try:

        get_attractionId=attractionId
        connection_object = connection_pool.get_connection()
        mycursor =  connection_object.cursor()
        sql="SELECT *FROM datas3 WHERE id=%s"
        adr=(get_attractionId,)
        mycursor.execute(sql,adr)
        myresult=mycursor.fetchall()
        # print(myresult)
        if myresult != []:
            mytitle = mycursor.description
            column_name =[col[0] for col in mytitle]
            # print(column_name)
            
            data=[]
            for i in range(0,1):
                data.append(dict(zip(column_name,list(myresult[i]))))
            data=data[0]
            data["images"]=data["images"].split(" ")
            imgs_notnull=[]
            for e in data["images"]:
                if e!="" and ".MP3" not in e and ".FLV" not in e:
                    imgs_notnull.append(e)
            data["images"]=imgs_notnull
            # print(data)

            return ({
                        "data": data
                    })

        else:
            return ({
                        "error": True,
                        "message":"景點編號不正確"
                    })
    except Exception as e:
        print("attraction_id_model get_attraction_data_by_id()發生問題",e)
        return {"error":True},500

    finally:
        mycursor.close()
        connection_object.close()