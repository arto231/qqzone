#coding:utf-8
import json
import os
def get_Frends_list():
    k = 0
    file_list=[i for i in os.listdir('./frends/') if i.endswith('json')]
    frends_list=[]
    for f in file_list:
        try:
          with  open('./frends/{}'.format(f),'r',encoding='utf-8') as w:
            data=w.read()[75:-4]
            js=json.loads(data)
            print(js)
            for i in js["items_list"]:
                k+=1
                frends_list.append(i)
        except :
            print ("???")
    print ("好友数："+str(k))


    return frends_list


frends_list=get_Frends_list()
print(frends_list)
for x in frends_list:
    print(x)
print(len(frends_list))
