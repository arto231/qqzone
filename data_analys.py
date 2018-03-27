import json
import os
import pymysql
import time
#存入数据库
def dataToMySql():
    con=pymysql.connect(
        host='localhost',
        user='root',
        password="root",
        database='py',
        port=3306,
    )
    con.set_charset('utf8')
    cur=con.cursor()
    cur.execute("SELECT VERSION()")
    print(cur.fetchone())
    cur.execute('SET NAMES utf8;')
    cur.execute('SET CHARACTER SET utf8;')
    cur.execute('SET character_set_connection=utf8;')
    sql="insert into mooods (message,content,type,createTime,name,qq_number,cmtnum,commentlist) values ({},{},{},{},{},{},{},{});"
    #sql_inst=sql.format("sds","sds",int(45),'2016-03-01',"sds","asd",int(45),"sada")
    # sql = "insert into info (qq_number,created_time,content,commentlist,source_name,cmtnum,name) values ({},{},{},{},{},{},{});"
      # sql = "insert into mooods (message,content,type,createTime,name,qq_number,cmtnum,commentlist) values ('sds','sds',45,'2016-03-01','ds','asd',45,'sada');"
    # querry="select * from mooods"
    print(sql)


    dir_names=[i for i in os.listdir('mood_detail') if not i.endswith('.xls')]
    # 获取所有好友目录列表
    for ii in dir_names:
        moodsList=[i for i in os.listdir('mood_detail/'+ii) if i.endswith('.json')]
        print('当前文件是：[mood_detail/'+ii+"]")
        moods_count=1
        # 获取所有mood json
        for i in moodsList:

            with open('mood_detail/'+ii+"/"+i,'r',encoding='utf-8') as w:
                s=w.read()[17:-2]
                js=json.loads(s)
                print('当前位置是：[mood_detail/' + ii +"/"+i+"]")
                #获取json中msg中的对象
                for msg in js['msglist']:
                    m=-1
                    if not msg['commentlist']:
                        msg['commentlist']=list()
                    message = "\""+'msg'+"\""
                    content="\""+str(msg['content'])+"\""
                    type="\""+str((msg['conlist']))+"\""
                    name="\""+str(msg['name'])+"\""
                    qq_number="\""+str(msg['uin'])+"\""
                    cmtnum=int(msg['cmtnum'])
                    commentlist="\""+str([(x['content'],x['createTime2'],x['name'],x['uin']) for x in list(msg['commentlist'])])+"\""
                    createDate_or=msg['created_time']
                    t = time.localtime(createDate_or)
                    createTime="\""+time.strftime("%Y-%m-%d %X",t)+"\""
                    sql_=sql.format(message,content,type,createTime,name,qq_number,cmtnum,commentlist)
                    try :
                        cur.execute(sql_)
                    except :
                        print("execute error")
                        print(sql_)
                        moods_count+=1

        try:

            con.commit()
        except :
            print("commit error")
    con.close()
def mydataToMySql():
    con=pymysql.connect(
        host='localhost',
        user='root',
        password="root",
        database='py',
        port=3306,
    )
    con.set_charset('utf8')
    cur=con.cursor()
    cur.execute("SELECT VERSION()")
    print(cur.fetchone())
    cur.execute('SET NAMES utf8;')
    cur.execute('SET CHARACTER SET utf8;')
    cur.execute('SET character_set_connection=utf8;')
    sql="insert into mooods (message,content,type,createTime,name,qq_number,cmtnum,commentlist) values ({},{},{},{},{},{},{},{});"
    #sql_inst=sql.format("sds","sds",int(45),'2016-03-01',"sds","asd",int(45),"sada")
    # sql = "insert into info (qq_number,created_time,content,commentlist,source_name,cmtnum,name) values ({},{},{},{},{},{},{});"
      # sql = "insert into mooods (message,content,type,createTime,name,qq_number,cmtnum,commentlist) values ('sds','sds',45,'2016-03-01','ds','asd',45,'sada');"
    # querry="select * from mooods"
    print(sql)
    path_my="my"


    dir_names=[i for i in os.listdir(path_my) if not i.endswith('.xls')]
    # 获取所有好友目录列表
    for ii in dir_names:
        moodsList=[i for i in os.listdir(path_my+'/'+ii) if i.endswith('.json')]
        print('当前文件是：['+path_my+'/'+ii+"]")
        moods_count=1
        # 获取所有mood json
        for i in moodsList:

            with open(path_my+'/'+ii+"/"+i,'r',encoding='utf-8') as w:
                s=w.read()[17:-2]
                js=json.loads(s)
                print('当前位置是：['+path_my+'/' + ii +"/"+i+"]")
                #获取json中msg中的对象
                for msg in js['msglist']:
                    m=-1
                    if not msg['commentlist']:
                        msg['commentlist']=list()
                    message = "\""+'msg'+"\""
                    content="\""+str(msg['content'])+"\""
                    type="\""+str((msg['conlist']))+"\""
                    name="\""+str(msg['name'])+"\""
                    qq_number="\""+str(msg['uin'])+"\""
                    cmtnum=int(msg['cmtnum'])
                    commentlist="\""+str([(x['content'],x['createTime2'],x['name'],x['uin']) for x in list(msg['commentlist'])])+"\""
                    createDate_or=msg['created_time']
                    t = time.localtime(createDate_or)
                    createTime="\""+time.strftime("%Y-%m-%d %X",t)+"\""
                    sql_=sql.format(message,content,type,createTime,name,qq_number,cmtnum,commentlist)
                    try :
                        cur.execute(sql_)
                    except :
                        print("execute error")
                        print(sql_)
                        moods_count+=1

        try:

            con.commit()
        except :
            print("commit error")
    con.close()
def showAllMood():

    con = pymysql.connect(
        host='localhost',
        user='root',
        password="root",
        database='py',
        port=3306,
    )
    con.set_charset('utf8')
    cur = con.cursor()
    cur.execute("SELECT VERSION()")
    print(cur.fetchone())
    cur.execute('SET NAMES utf8;')
    cur.execute('SET CHARACTER SET utf8;')
    cur.execute('SET character_set_connection=utf8;')
    qq_number_input="563364899"
    sql="select content from mooods where qq_number={} and createTime between '2014-01-01' and '2018-01-01'".format(qq_number_input)
    cur.execute(sql)
    results =cur.fetchall()
    k=1
    mood_sum=['qq号']
    for x in results:
        k += 1
        mood_sum.append(x)

    print("总数：" + str(k) + "条")
    if not os.path.exists("./all_moods"+""):
        os.makedirs("./all_moods/"+"")
    with open('./all_moods/'  + qq_number_input +  '.txt', 'w',encoding='utf-8') as w:
       w.write(str(mood_sum))





#dataToMySql()

showAllMood()
#mydataToMySql()






#存入Excel
# def dataToExcel():
#     d=[i for i in os.listdir('mood_detail') if not i.endswith('.xls')]
#     for ii in d:
#         wb=xlwt.Workbook()
#         sheet=wb.add_sheet('sheet1',cell_overwrite_ok=True)
#         sheet.write(0,0,'content')
#         sheet.write(0,1,'createTime')
#         sheet.write(0,2,'commentlist')
#         sheet.write(0,3,'source_name')
#         sheet.write(0,4,'cmtnum')
#         fl=[i for i in os.listdir('mood_detail/'+ii) if i.endswith('.json')]
#         print('mood_detail/'+ii)
#         k=1
#         for i in fl:
#             with open('mood_detail/'+ii+"/"+i,'r',encoding='latin-1') as w:
#                 s=w.read()[17:-2]
#                 js=json.loads(s)
#                 print(i)
#                 for s in js['msglist']:
#                     m=-1
#                     sheet.write(k,m+1,str(s['content']))
#                     sheet.write(k,m+2,str(s['createTime']))
#                     if not s['commentlist']:
#                         s['commentlist']=list()
#                     sheet.write(k,m+3,str([(x['content'],x['createTime2'],x['name'],x['uin']) for x in list(s['commentlist'])]))
#                     sheet.write(k,m+4,str(s['source_name']))
#                     sheet.write(k,m+5,str(s['cmtnum']))
#                     k+=1
#         if not os.path.exists('mood_detail/Excel/'):
#             os.mkdir('mood_detail/Excel/')
#         try:
#             wb.save('mood_detail/Excel/'+ii+'.xls')
#         except Exception:
#             print("error")
#

""""
def dataToExcel():
    ll=0
    d=[i for i in os.listdir('mood_detail') if not i.endswith('.xls')]
    for ii in d:
        # wb=xlwt.Workbook()
        # sheet=wb.add_sheet('sheet1',cell_overwrite_ok=True)
        # sheet.write(0,0,'content')
        # sheet.write(0,1,'createTime')
        # sheet.write(0,2,'commentlist')
        # sheet.write(0,3,'source_name')
        # sheet.write(0,4,'cmtnum')
        fl=[i for i in os.listdir('mood_detail/'+ii) if i.endswith('.json')]
        print('mood_detail/'+ii)
        k=1
        for i in fl:
            with open('mood_detail/'+ii+"/"+i,'r',encoding='latin-1') as w:
                s=w.read()[17:-2]
                js=json.loads(s)
                print(i)
                for s in js['msglist']:
                    ll+=1
                    m=-1
                    # sheet.write(k,m+1,str(s['content']))
                    # sheet.write(k,m+2,str(s['createTime']))
                    if not s['commentlist']:
                        s['commentlist']=list()
                    # sheet.write(k,m+3,str([(x['content'],x['createTime2'],x['name'],x['uin']) for x in list(s['commentlist'])]))
                    # sheet.write(k,m+4,str(s['source_name']))
                    # sheet.write(k,m+5,str(s['cmtnum']))
                    k+=1
        if not os.path.exists('mood_detail/Excel/'):
            os.mkdir('mood_detail/Excel/')
    print(ll)
        # try:
        #     wb.save('mood_detail/Excel/'+ii+'.xls')
        # except Exception:
        #     print("error")

dataToExcel()
"""





