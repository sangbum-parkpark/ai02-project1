from flask import Flask, render_template, request, redirect, url_for
import sys
import pandas as pd
app = Flask(__name__)
import database
import mylist
import random

# database.py, mylist.py를 불러온다.

# Home 화면
@app.route("/")
def home():
    return render_template("home.html")


# 향수 데이터 등록
@app.route("/apply")
def apply():
    return render_template("apply.html")

# 사진 등록하기
@app.route("/applyphoto")
def photo_apply():
    name = request.args.get("name")
    brand = request.args.get("brand")
    description = request.args.get("description")
    notes = request.args.get("notes")

    database.save(name, brand, description, notes)
    return render_template("apply_photo.html")

# 사진 업로드 완료. 후 다시 apply 화면으로
@app.route("/upload_done", methods=["POST"])
def upload_done():
    uploaded_files = request.files["file"]
    uploaded_files.save("static/img/{}.jpeg".format(database.now_index()))
    return redirect(url_for("apply")) 


################################################### Search 미완성#####################################################################3
@app.route("/search", methods=['GET','POST'])
def search():
    search_list = []
    search = request.args.get("search")
    # search = request.form("text")
    df = pd.read_csv("database.csv")

    for i in range (len(df)):
        if df.iloc[i][1] == search or df.iloc[i][2] == search:
            search_list.append(df.iloc[i].tolist())

    return render_template("search.html", html_search_list=search_list)

# My list
@app.route("/mylist")
def my_list():
    html_my_list = mylist.load_list()
    return render_template("mylist.html", html_my_list= html_my_list)


@app.route("/mylistview", methods=["GET", "POST"])
def mylist_view():
    search = request.args.get("name")
    df = pd.read_csv("database.csv")

    if 'Unnamed: 0' in df.columns:
        df = df.drop('Unnamed: 0', axis=1)

    if '' in df.columns:
        df = df.drop('', axis=1)

    # my_list = mylist.load_list()

    for i in range (len(df)):
        if df.iloc[i][1] == search or df.iloc[i][2] == search:
            name = df.iloc[i][1]
            brand = df.iloc[i][2]
            description = df.iloc[i][3]
            notes = df.iloc[i][4]
            image_URL = df.iloc[i][5]
            mylist.save(name, brand, description, notes, image_URL)
        
        # elif search in my_list[i][1] or search in my_list[i][2]:
        #     return render_template("already_exist.html")
    
    html_my_list = mylist.load_list()
    html_range = range(len(html_my_list))
    return render_template("mylist_view.html", html_my_list = html_my_list, html_range=html_range)

# Perfume info
@app.route("/item")
def item():
    html_my_list = mylist.load_list()
    html_range = range(len(html_my_list))
    return render_template("item.html", html_my_list = html_my_list, html_range=html_range)

# Delete
@app.route("/delete", methods=["GET", "POST", "DELETE"])
def delete():
    thing = request.args.get("name")
    df = pd.read_csv("mylist.csv")

    index_list = []

    for i in range(len(df)):
        if df.iloc[i][1] == thing:
            index_list.append(i)

    df = df.drop(index=index_list)
    df = df.reset_index()
    df = df.drop('index', axis=1)
    mylist.delete_all()
    for i in range (len(df)):
        name = df.iloc[i][1]
        brand = df.iloc[i][2]
        description = df.iloc[i][3]
        notes = df.iloc[i][4]
        image_URL = df.iloc[i][5]
        mylist.save(name, brand, description, notes, image_URL)

    html_my_list = mylist.load_list()
    html_range = range(len(html_my_list))
    return render_template("mylist_view.html", html_my_list = html_my_list, html_range=html_range)


# Recommend
@app.route("/recommend")
def recommend():
    my_list = mylist.load_list()
    database_list = database.load_list()

    mylist_note = []
    for i in range(len(my_list)):
        # mylist에 저장한 모든 향수들의 노트를 합친 리스트
        mylist_note = mylist_note + my_list[i][4].split(',')

    # 노트 네임 수 
    mylist_count = {}
    for i in mylist_note:
        try: mylist_count[i] += 1
        except: mylist_count[i]=1

    # 노트 Name을 count에 따라 내림차순으로 정렬
    mylist_rank = sorted(mylist_count.items(), key=(lambda x: x[1]), reverse = True)

    myfavorite = mylist_rank[0][0]
    html_recommend_list = []
    for i in range(len(database_list)):
        if myfavorite in database_list[i][4].split(','):
            html_recommend_list.append(database_list[i])
    html_recommend_list = random.sample(html_recommend_list, 5)
    return render_template("recommend.html", html_recommend_list=html_recommend_list)

if __name__ == "__main__":
    app.run(debug=True)