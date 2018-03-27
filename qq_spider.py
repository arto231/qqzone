#coding:utf-8
from  selenium import webdriver
import requests
import time
import os
from urllib import parse
import configparser

class Spider(object):
    def __init__(self):
        print("初始化，访问空间")
        self.web=webdriver.Chrome()
        self.web.get('https://user.qzone.qq.com')#打开qqZone
        config = configparser.ConfigParser(allow_no_value=False)
        config.read('userinfo.ini')
        self.__username =config.get('qq_info','qq_number')
        self.__password=config.get('qq_info','qq_password')
        print("username=,"+self.__username+"  password="+ self.__password)
        self.headers={
                'host': 'h5.qzone.qq.com',
                'accept-encoding':'gzip, deflate, br',
                'accept-language':'zh-CN,zh;q=0.8',
                'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
                'connection': 'keep-alive'
        }
        self.req=requests.Session()
        self.cookies={}

    

    def login(self):
        print("正在登陆")
        self.web.switch_to_frame('login_frame')
        log=self.web.find_element_by_id("switcher_plogin")
        log.click()
        time.sleep(1)
        username=self.web.find_element_by_id('u')
        username.send_keys(self.__username)
        ps=self.web.find_element_by_id('p')
        ps.send_keys(self.__password)
        btn=self.web.find_element_by_id('login_button')
        time.sleep(1)
        btn.click()
        time.sleep(2)
        self.web.get('https://user.qzone.qq.com/{}'.format(self.__username))
        cookie=''
        print('https://user.qzone.qq.com/{}'.format(self.__username))
        print(cookie)
        for elem in self.web.get_cookies():
            cookie+=elem["name"]+"="+ elem["value"]+";"
        self.cookies=cookie
        print(self.cookies)
        self.get_g_tk()
        self.headers['Cookie']=self.cookies
        time.sleep(10)
       # self.web.quit()
    def del_moods(self):
        print("del")

        
    
    def get_frends_url(self):
        print("get_frends_url")
        url='https://user.qzone.qq.com/proxy/domain/r.qzone.qq.com/cgi-bin/tfriend/friend_ship_manager.cgi?'
        params = {
            "uin": self.__username,
            "do": '1',
            "rd": '0.8401873752868374',
            "fupdate": '1',
            "clean": '1',
            "g_tk": self.g_tk,
            "qzonetoken": 'd155a6b94433331f1c7f2015fd775b15022392bf643440c95daf2d72cf9db6a0edf43b35c211ac3d',
            "g_tk": self.g_tk
        }
        url = url + parse.urlencode(params)
        print("获取到好友列表的Url:"+url)
        return url

    def get_frends_num(self):
        url=self.get_frends_url()
        url_=url
        page=self.req.get(url=url_,headers=self.headers)
        if not os.path.exists("./frends/"):
            os.mkdir("frends/")
        with open('./frends/'+"friendsList"+'.json','w',encoding='utf-8') as w:
                    w.write(page.text)


    def get_mood_url(self):
        print("get_mood_url,")
        url='https://h5.qzone.qq.com/proxy/domain/taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6?'
        params = {
              "sort":0,
                  "start":0,
              "num":20,
            "cgi_host": "http://taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6",
              "replynum":100,
              "callback":"_preloadCallback",
              "code_version":1,
            "inCharset": "utf-8",
            "outCharset": "utf-8",
            "notice": 0,
              "format":"jsonp",
              "need_private_comment":1,
              "g_tk": self.g_tk
              }
        url = url + parse.urlencode(params)
        print("get_mood_url__________url,")
        return url

    def get_qq_number_mood_detail(self):
        url = self.get_mood_url()
        t = True
        QQ_number = "563364899"
        url_ = url + '&uin=' + str(QQ_number)
        pos = 0
       # print("现在是qq=[" + str(u['uin']) + "]name=[" + u['name'] + "]的动态 URL：" + url_)

        while (t):
            url__ = url_ + '&pos=' + str(pos)
            mood_detail = self.req.get(url=url__, headers=self.headers)
            print(QQ_number, QQ_number, pos)
            if "\"msglist\":null" in mood_detail.text or "\"message\":\"对不起,主人设置了保密,您没有权限查看\"" in mood_detail.text:
                t = False
            else:
                if not os.path.exists("./my/"):
                    os.mkdir("my/")
                try:
                    if not os.path.exists("./my/" + QQ_number):
                        os.mkdir("my/" +QQ_number)
                    with open('./my/' + QQ_number + "/" + str(QQ_number) + "_" + str(pos) + '.json', 'w',
                              encoding='utf-8') as w:
                        w.write(mood_detail.text)
                    pos += 20
                except:
                    print("特殊字符")
                    if not os.path.exists("./my/" + "特殊字符" + str(QQ_number)):
                        os.mkdir("my/" + "特殊字符" + str(QQ_number))
                    with open('./my/' + "特殊字符" + str(QQ_number) + "/" + str(QQ_number) + "_" + str(
                            pos) + '.json', 'w',
                              encoding='utf-8') as w:
                        w.write(mood_detail.text)
                    pos += 20

    def get_mood_detail(self):
        print("get_mood_url__________url,")
        from getFrends import frends_list
        url = self.get_mood_url()
        print("获取好友mood列表："+url)
        for u in frends_list:
            t = True
            QQ_number=u['uin']
            url_ = url + '&uin=' + str(QQ_number)
            pos = 0
            print ("现在是qq=[" + str(u['uin']) + "]name=[" + u['name'] + "]的动态 URL：" + url_)

            while (t):
                url__ = url_ + '&pos=' + str(pos)
                mood_detail = self.req.get(url=url__, headers=self.headers)
                print(QQ_number,u['name'],pos)
                if "\"msglist\":null" in mood_detail.text or "\"message\":\"对不起,主人设置了保密,您没有权限查看\"" in mood_detail.text:
                    t = False
                else:
                    if not os.path.exists("./mood_detail/"):
                        os.mkdir("mood_detail/")
                    try:
                        if not os.path.exists("./mood_detail/"+u['name']):
                            os.mkdir("mood_detail/"+u['name'])
                        with open('./mood_detail/'+u['name']+"/" +str(QQ_number)+"_"+ str(pos) + '.json', 'w',encoding='utf-8') as w:
                            w.write(mood_detail.text)
                        pos += 20
                    except:
                        print("特殊字符")
                        if not os.path.exists("./mood_detail/" + "特殊字符"+str(QQ_number)):
                            os.mkdir("mood_detail/" + "特殊字符"+str(QQ_number))
                        with open('./mood_detail/' + "特殊字符"+str(QQ_number) + "/" + str(QQ_number) + "_" + str(pos) + '.json', 'w',
                                  encoding='utf-8') as w:
                            w.write(mood_detail.text)
                        pos += 20

            time.sleep(2)



    def get_g_tk(self):
        print("get_mood_url__________url,")
        p_skey = self.cookies[self.cookies.find('p_skey=')+7: self.cookies.find(';', self.cookies.find('p_skey='))]
        print (p_skey)
        h=5381
        for i in p_skey:
            h+=(h<<5)+ord(i)
        print('g_tk',h&2147483647)
        print (self.cookies)
        self.g_tk=h&2147483647

        

if __name__=='__main__':
    sp=Spider()
    sp.login()
    sp.get_qq_number_mood_detail()
   # sp.get_frends_num()
   # sp.get_mood_detail()
    #from data_analys import dataToExcel
