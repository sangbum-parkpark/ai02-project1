import pandas as pd
import database
import mylist
# my_list = database.load_list()


# 제품 이름으로 검색
# my_list = []
df = pd.read_csv("database.csv")

# df.iloc[i] 행 데이터, df.iloc[i][1] -> Name, df.iloc[i][2] -> Brand
# Brand = 'A Lab on Fire'
# for i in range (len(df)):
#     if df.iloc[i][2] == Brand:
#         my_list.append(df.iloc[i].tolist())

# Name = 'Nocturnal Poetry Parfum'
# for i in range (len(df)):
#     if df.iloc[i][1] == Name:
#         my_list.append(df.iloc[i].tolist())

# print(my_list)


# search = "PRIN"
# my_list = []
# for i in range (len(df)):
#     if df.iloc[i][1] == search or df.iloc[i][2] == search:
#         # my_list.append(df.iloc[i].tolist())
#         name = df.iloc[i][1]
#         brand = df.iloc[i][2]
#         description = df.iloc[i][3]
#         notes = df.iloc[i][4]
#         mylist.save(name, brand, description, notes)
    
# my_list = mylist.load_list()
# database_list = database.load_list()

# mylist_note = []
# for i in range(len(my_list)):
#     # mylist에 저장한 모든 향수들의 노트를 합친 리스트
#     mylist_note = mylist_note + my_list[i][4].split(',')

# # 노트 네임 수 
# mylist_count = {}
# for i in mylist_note:
#     try: mylist_count[i] += 1
#     except: mylist_count[i]=1

# # 노트 Name을 count에 따라 내림차순으로 정렬
# mylist_rank = sorted(mylist_count.items(), key=(lambda x: x[1]), reverse = True)

# myfavorite = mylist_rank[0][0]

# for i in range(len(database_list)):

#     if myfavorite in database_list[i][4].split(','):
#         print(database_list[i][1])


# thing = "Eshu Extrait"
# index_list = []
# for i in range(len(df)):
#     if df.iloc[i][1] == thing:
#         index_list.append(i)
# df = df.drop(index=index_list)
# df.to_csv("mylist.csv", mode = "a", header=False)

# res[0] -> mylist내 가장 많이 중복된 노트 Name과 count
# res[0][0] -> mylist내 가장 많이 중복된 노트
mylist.delete_all()
breakpoint()