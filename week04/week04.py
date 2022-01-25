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
#使用GET方法，處理路徑/對應函式
#首頁
@week04.route("/")
def index():
    return render_template("index.html")
#會員頁面
@week04.route("/member/")
def success():
    if "account" in session:
        return render_template("member.html")
    else:
        return redirect("/")
    
#失敗頁面
@week04.route("/error/")
def wrong():
    reply=request.args.get("message","")
    return render_template("error.html",message=reply)       

#登入驗證
@week04.route("/signin",methods=["POST"])
def handle():
    input1=request.form["data"]
    input2=request.form["p"]
    if (input1=="test") and (input2=="test"):
        session["account"]=input1
        return redirect("/member/")
    elif (input1=="") or (input2==""):
        return redirect("/error/?message=登入前!請輸入你專屬的通關密語")
    else:
        return redirect("/error/?message=Oops!帳號密碼輸入錯誤囉~")

@week04.route("/signout")
def signout():
     session.pop("account", None)
     return redirect("/")

#指定埠號
week04.run(port=3000)
https://a225521.github.io/wehelp-assignments/week04/

