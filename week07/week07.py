from flask import Flask
from flask import request
import json
from flask import render_template
from flask import redirect
from flask import session
week04=Flask(
    __name__,
    static_folder="static",
    static_url_path="/static"
)
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path=".env",override=True)
week04.secret_key = os.getenv("secret_key")
import mysql.connector
mydb = mysql.connector.connect(
  host=os.getenv("host"),
  user=os.getenv("user"),
  password=os.getenv("password")
)
print(mydb)
cursor=mydb.cursor()
cursor.execute("USE mydb")
#cursor.execute("CREATE TABLE member (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, username VARCHAR(255) NOT NULL UNIQUE, password VARCHAR(255) NOT NULL)")
#使用GET方法，處理路徑/對應函式
#首頁
@week04.route("/")
def index():
    return render_template("index.html")
    
#失敗頁面
@week04.route("/error/")
def wrong():
    reply=request.args.get("message","")
    return render_template("error.html",message=reply)       
#註冊驗證
@week04.route("/signup",methods=["POST"])
def register():
    enter1=request.form["title"]
    enter2=request.form["username"]
    enter3=request.form["password"]
    sql=("SELECT*FROM member WHERE username=%s")
    adr = (enter2, )
    cursor.execute(sql, adr)
    result = cursor.fetchone()
    if result is None:
        sql = "INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
        val = (enter1, enter2, enter3)
        cursor.execute(sql, val)
        mydb.commit()
        return redirect("/")
    else:
        return redirect("/error/?message=帳號重複無法使用")
    cursor.close()
 
    
#登入驗證
@week04.route("/signin",methods=["POST"])
def handle():
    input1=request.form["username"]
    input2=request.form["password"]
    sql=("SELECT*FROM member WHERE username=%s AND password=%s ")
    adr = (input1, input2, )
    cursor.execute(sql, adr)
    result1 = cursor.fetchone()
    showname=result1[1]
    if result1 is not None:
        session["account"]=input1
        session["showname"]=showname
        return redirect("/member/")
    elif (input1=="") or (input2==""):
        return redirect("/error/?message=登入前!請輸入你專屬的通關密語")
    else:
        return redirect("/error/?message=Oops!帳號密碼輸入錯誤囉~")
    cursor.close()   

#會員頁面
@week04.route("/member/")
def username():
    if "account" in session:
        showname=session["showname"]
        return render_template("member.html",name=showname)
    else:
        return redirect("/")


#建立查詢
@week04.route("/api/members")
def search():
    data=request.args.get("username")
    sql=("SELECT id, name, username FROM member WHERE username=%s")
    adr = (data, )
    cursor.execute(sql, adr)
    info = cursor.fetchone()
    if info is not None:
        idinfo=info[0]
        nameinfo=info[1]
        usernameinfo=info[2]
        return json.dumps({
            "data":{
                "id":idinfo,
                "name":nameinfo,
                "username":usernameinfo
            }
        },ensure_ascii=False)
    else:
        return json.dumps({
            "data":None
        })
    cursor.close()
#登出
@week04.route("/signout")
def signout():
    session.pop("account", None)
    return redirect("/")

#指定埠號
week04.run(port=3000)

mydb.close()







