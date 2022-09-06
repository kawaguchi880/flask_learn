from random import sample
from flask import Blueprint, render_template,redirect
from apps.sampleSite.forms import KweetForm,jankennForm,taipinnguForm,ReserveForm,KakeiboForm,kakeiboDelectionForm
from apps.sampleSite.models import Kweet,Reserve,Kakeibo
from apps.app import db
import random

sampleSite = Blueprint(
    "sampleSite",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="static/sampleSite"
)

@sampleSite.route('/',methods = ["GET","POST"])
def index():
    form = KweetForm()
    # 変数formにform.pyに定義しておいたKweetFormというclassを作る
    # FlaskFormクラスを継承したKweetFormクラス内にあったis_submittedメソッドを実行
    if form.is_submitted():
        print("submit!")
        message = form.message.data or ''
        if message != '':
            kweet = Kweet(message=message)
            db.session.add(kweet)
            db.session.commit()
        # メッセージが空白出ないのならmessageListに追加


    dbData = {
        "id":123,
        "name":"name",
        "form": form,
        "kweetList":Kweet.query.all()

    }

    return render_template("index.html", data=dbData)

@sampleSite.route('/page2')
def page2():
    return render_template("page2.html")

@sampleSite.route('/reserve',methods=["GET","POST"])
def reserve():
    reserveForm = ReserveForm()
    reserved = False

    if reserveForm.is_submitted():
        name = reserveForm.name.data
        startAt = reserveForm.startAt.data
        endAt = reserveForm.endAt.data
        count = reserveForm.count.data

        reserve = Reserve(
            name=name,
            start_at=startAt,
            end_at = endAt,
            count=count
        )

        db.session.add(reserve)
        db.session.commit()
    return render_template("reserve.html",form=reserveForm,reserved=reserved)



@sampleSite.route('/reserveList',methods=["GET"])
def reserveList():
    reserveList = Reserve.query.all()
    print(reserveList)
    return render_template("reserveList.html",reserveList=reserveList)


@sampleSite.route('/kakeibo',methods=["GET","POST"])
def kakeibo():
    kakeiboForm = KakeiboForm()
    kakeiboed=False
    totalcost=False
    kakeiboList={}
    print("aaaa")

    # if kakeiboForm.is_submitted():
    date = kakeiboForm.date.data
    budget = kakeiboForm.budget.data
    item = kakeiboForm.item.data
    cost = kakeiboForm.cost.data
    if (budget=="on"):
        budget="支出"
    elif(budget is None):
        budget="入力なし"
    print("aaa")
    print(date)
    print(budget)
    print(item)
    print(cost)

    kakeibo = Kakeibo(
        date=date,
        budget=budget,
        item = item,
        cost=cost
    )

    db.session.add(kakeibo)
    db.session.commit()
    kakeiboList = kakeibo.query.all()
    totalcost=0
    for kakeibo in kakeiboList:
        if kakeibo.cost is None:
            print(kakeibo.cost)
        else:
            totalcost +=kakeibo.cost
    return render_template("kakeibo.html",form=kakeiboForm,kakeiboed=kakeiboed,kakeiboList=kakeiboList,totalcost=totalcost)

@sampleSite.route('/kakeiboDelection',methods=["POST"])
def kakeiboDelection():
    kakeiboDelection = kakeiboDelectionForm()
    item_id = kakeiboDelection.item_id.data
    print("item_id")
    print(item_id)
    item = db.session.query(Kakeibo).filter(Kakeibo.id == item_id).one()
    db.session.delete(item)
    db.session.commit()
    return redirect("/kakeibo")

@sampleSite.route('/application1')
def app1():
    return render_template("application1.html")

@sampleSite.route('/application2',methods = ["GET","POST"])
def app2():
    result="引き分け"
    form = jankennForm()
    # 変数formにform.pyに定義しておいたKweetFormというclassを作る
    # FlaskFormクラスを継承したKweetFormクラス内にあったis_submittedメソッドを実行
    if form.is_submitted():
        print("submit!")
        choice = form.choice.data
        m = random.randint(0,2)

        if(choice == "グー"):
            p=0
        elif(choice == "ちょき"):
            p=1
        elif(choice == "ぱー"):
            p=2

        i = (p-m) % 3
        if i == 0:
        #drawの場合
            result = "引き分け"
        elif i == 1:
        #loseの場合
            result = "勝ち"
        else:
        #winの場合
            result = "負け"

    dbData = {
        "form": form,
        "result":result
    }

    return render_template("application2.html",data=dbData)

@sampleSite.route('/application3',methods = ["GET","POST"])
def app3():
    score = 0

    questionData=[
        "開発","レンダー","Webサービス","はじめまして","こんにちは","linux","nginx","flask"
    ]
    form = taipinnguForm()

    if form.is_submitted():
        prequestion = form.prequestion.data
        answer = form.taipunngu.data
        score = form.score.data
        if(answer==prequestion):
            score +=1

    m = random.randint(0,len(questionData))
    question = questionData[m]

    dbData={
        "form": form,
        "question":question,
        "score":score
    }
    return render_template("application3.html",data=dbData)



@sampleSite.route('/map')
def map():
    return render_template("map.html")


@sampleSite.route('/study')
def study():
    # 標準出力で表示
    print("ああああああああ")
    # 文字列
    str1 = "あいうえお" + "かきくけこ"
    print(str1)
    print(str1[0])  #1文字だけ取り出す
    print(str1[0:4])
    print(str1 * 3)


    str2 = "さしすせそ"

    print('%sの次は%s'%(str1,str2))

    print('{0}の次は{1}'.format(str1,str2))


    print(str1.replace('あいうえお','たちつてと'))

    str3 = "ctouD study!"
    print(str3.upper())
    print(str3.lower())
    print(str3.count('u'))


    # my_class = MyClass('ABC')
    # print(my_class.p_1)

    # my_class1 = MyClass(p_1='ABC')
    # print(my_class1.p_1)

    # my_class2 = MyClass(p_1=0.5)
    # print(my_class2.p_1)

    # my_class3 = MyClass(p_1=0xFF)
    # print(my_class3.p_1)

    # my_class4 = MyClass(p_1=[1,2,3])
    # print(my_class4.p_1,my_class4.p_1[0])

    # print(my_class.func_sample(arg1=10,arg2=20))

    # print(my_class.func_sample(arg2=50,arg1=30))


    user1_data = {
            'user_id':'A00001',
            'name':'user1',
            'Science':50,
            'Mathematics':30 ,
            'Physics':20 ,
            'Design':90
        }

    user2_data = {
            'user_id':'A00002',
            'name':'user2',
            'Science':50,
            'Mathematics':90 ,
            'Physics':25 ,
            'Design':90
        }

    user3_data = {
            'user_id':'A00003',
            'name':'user3',
            'Science':80,
            'Mathematics':30 ,
            'Physics':50 ,
            'Design':20
        }

    my_class = MyClass()

    my_class.add_user_data(user=user1_data)
    my_class.add_user_data(user=user2_data)
    my_class.add_user_data(user=user3_data)

    print(my_class.get_user_summary(user_id=user1_data['user_id']))
    print(my_class.get_user_average(user_id=user1_data['user_id']))
    # print(my_class.is_passed(user_id=user1_data['user_id']))
    Mathsum=user1_data['Mathematics']+user2_data['Mathematics']+user3_data['Mathematics']

    data={
        "sum":my_class.get_user_summary(user_id='A00001'),
        "average":my_class.get_user_average(user_id='A00001'),
        "pass":my_class.is_passed(user_id='A00001',subject='Physics'),
        "subject_average":my_class.get_subject_average(sum = Mathsum)
    }







    return render_template("study.html",data = data)


class MyClass:
    # def __init__(self,p_1):
    #     print("コンストラクタ！(なくてもいい)")
    #     self.p_1=p_1

    # def __del__(self):
    #         print("デストラクタ!(なくてもいい)")


    def __init__(self):
        self.users=[]

    def get_user_summary(self,user_id):
        for user in self.users:
            if user['user_id'] == user_id:
                return user['Science']\
                + user['Mathematics']\
                + user['Physics']\
                + user['Design']
        return 0


    def add_user_data(self,user):
        self.users.append(user)
        #  userの追加
        print(self.users)


    def get_user_average(self,user_id):
        for user in self.users:
            if user['user_id'] == user_id:
                return (user['Science']\
                + user['Mathematics']\
                + user['Physics']\
                + user['Design'])/4
        return 0

    def is_passed(self,user_id,subject):
        for user in self.users:
            if user['user_id'] == user_id:
                if user[subject] >=50:
                    return True
                else:
                    return False

    def get_subject_average(self,sum):
        average = sum/3
        return average
