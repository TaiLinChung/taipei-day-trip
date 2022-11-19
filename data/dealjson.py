import json
 
with open('taipei-attractions.json',"r", encoding="utf-8") as fp:
    data = json.load(fp)
# print(data["result"]["results"][0]["CAT"])
# sss=""
# for item in data["result"]["results"]:
#     if item["_id"]==1:
#         print(item["file"])
#         sss=item["file"]
#     # print(item["_id"])
#     # print()
#     # print()
# print()
# sss=sss.upper()
# print(sss)
# print()
# sss=sss.replace(" ","").replace(".JPG",".JPG ")
# sss=sss.split(" ")
# print(sss)
# # https://www.runoob.com/python/att-string-replace.html
# # print(type(sss))
# # print(sss.replace(".JPG",".JPG "))



##前置作業與資料庫連線創建資料庫跟表
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Bb0970662139",
    # auth_plugin='mysql_native_password'
    # port="3306"
)
mycursor=mydb.cursor()
sql="CREATE DATABASE IF NOT EXISTS taipei_day_trip"
mycursor.execute(sql)
sql="USE taipei_day_trip"
mycursor.execute(sql)
# sql="CREATE TABLE IF NOT EXISTS datas(id INT,name VARCHAR(20),category VARCHAR(20),description VARCHAR(1000) ,address VARCHAR(1000),transport VARCHAR(1000),mrt VARCHAR(200),longitude FLOAT,latitude FLOAT,images VARCHAR(2000))"
# mycursor.execute(sql)
sql="CREATE TABLE IF NOT EXISTS datas2(id INT,name VARCHAR(20),category VARCHAR(20),description TEXT ,address VARCHAR(1000),transport VARCHAR(1000),mrt VARCHAR(200),longitude FLOAT,latitude FLOAT,images TEXT)"
mycursor.execute(sql)





##整理開始
for item in data["result"]["results"]:
    print("1_id: ",item["_id"])
    print("2_name: ",item["name"])
    print("3_category: ",item["CAT"])
    print("4_description: ",item["description"])
    print("5_address: ",item["address"])
    print("6_transport: ",item["direction"])
    print("7_mrt: ",item["MRT"])
    print("8_lat: ",item["latitude"])
    print("9_lng: ",item["longitude"])
    # item["file"]=item["file"].replace(" ","").upper().replace(".JPG",".JPG ").split(" ")
    item["file"]=item["file"].replace(" ","").upper().replace(".JPG",".JPG ")
    print("10_images: ",item["file"])
    # print(item["file"])
    # len_file=len(item["file"])
    # new_itemfile=[]
    # for i in range(len_file):
    #     if item["file"][i] != "" and ".MP3" not in item["file"][i] and ".FLV" not in item["file"][i]:
    #         new_itemfile.append(item["file"][i])
    # # print("new_itemfile",new_itemfile)
    # #回填處理過的
    # item["file"]=new_itemfile
    # print("10_images: ",item["file"])
    # print()
    # print()
    
    mycursor=mydb.cursor()
    sql="INSERT INTO datas2(id,name,category,description,address,transport,mrt,latitude,longitude,images) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(item["_id"],item["name"],item["CAT"],item["description"],item["address"],item["direction"],item["MRT"],item["latitude"],item["longitude"],item["file"])
    mycursor.execute(sql,val)
    mydb.commit()


    # sql="INSERT INTO datas(name,category) VALUES(%s,%s)
    # val=(item["_id"],item["name"])
    # mycursor.execute(sql,val)