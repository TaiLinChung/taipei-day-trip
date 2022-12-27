
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


# ========================	categories_picture_item	========================

##單純頁數
def loading_all_picture_by_attractions(page_maxnum,page_num_now):
    try:
        connection_object = connection_pool.get_connection()
        mycursor = connection_object.cursor()#(dictionary=True) 把fetchone跟fetchall的搜尋結果回傳都為字典形式
        sql_fetchall="SELECT *from datas3 LIMIT %s,%s"
        adr_fetchall=(page_num_now*page_maxnum,page_maxnum)
        mycursor.execute(sql_fetchall,adr_fetchall)
        myresult_fetchall=mycursor.fetchall()
        total_amount=len(myresult_fetchall)

        sql_fetchmore="SELECT *from datas3 LIMIT %s,%s"
        adr_fetchmore=(page_num_now*page_maxnum,page_maxnum+1)
        mycursor.execute(sql_fetchmore,adr_fetchmore)
        myresult_fetchmore=mycursor.fetchall()
        more_amount=len(myresult_fetchmore)

        for i in range(len(myresult_fetchall)):
            myresult_fetchall[i]=list(myresult_fetchall[i])
            myresult_fetchall[i][9]=myresult_fetchall[i][9].split(" ")

        if total_amount !=0:
            mytitle = mycursor.description
            column_name =[col[0] for col in mytitle]
            data=[]
            for i in range(total_amount):
                data.append(dict(zip(column_name,myresult_fetchall[i])))
            if more_amount==page_maxnum+1:
                next_page=page_num_now+1
            else:
                next_page=None
        else:
            return ({                              
                    "error": True,
                    "message": "沒有資料了"	
                    })
        return ({                              
                "nextPage": next_page,
                "data": data	
                })

    except Exception as e:
        print("attractions_model loading_picture_by_attractions()發生問題",e)
        return {"error":True},500
    finally:
        mycursor.close()
        connection_object.close()


#模糊&完全
def loading_matched_picture(keyword,page_num_now,page_maxnum):
    try:
        connection_object = connection_pool.get_connection()
        mycursor = connection_object.cursor()#(dictionary=True) 把fetchone跟fetchall的搜尋結果回傳都為字典形式
        sql_keyword="SELECT *FROM datas3 WHERE category=%s or name like concat('%',%s,'%') LIMIT %s,%s"

        adr_keyword=(keyword,keyword,page_num_now*page_maxnum,page_maxnum)
        mycursor.execute(sql_keyword,adr_keyword)
        myresult_keyword=mycursor.fetchall()
        total_amount=len(myresult_keyword)

        for i in range(len(myresult_keyword)):
            myresult_keyword[i]=list(myresult_keyword[i])
            myresult_keyword[i][9]=myresult_keyword[i][9].split(" ")

        if total_amount !=0:
            mytitle = mycursor.description
            column_name =[col[0] for col in mytitle]
        # 	print()
        # 	print(column_name)
        # 	print(myresult_keyword)
            data=[]
            for i in range(total_amount):
                data.append(dict(zip(column_name,myresult_keyword[i])))
            if len(data)==page_maxnum:
                next_page=page_num_now+1
            else:
                next_page=None
        else:
            return ({                              
                    "error": True,
                    "message": "沒有資料了"	
                    })

        return ({                              
                "nextPage": next_page,
                "data": data	
                })

    except Exception as e:
        print("attractions_model load_matched_picture()發生問題",e)
        return {"error":True},500
    finally:
        mycursor.close()
        connection_object.close()