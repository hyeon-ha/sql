import pandas as pd
# pd.set_options('display_max_columns', 20)
import pymysql
import numpy as np
import pickle





# def insert(self, sql):
#     try:
#         with conn.cursor() as cursor:
#             cursor.execute(sql)
#         conn.commit()
#     except:
#         print('conn error')
#     finally:
#         conn.close()

df = pd.read_csv('../datasets/netflix_titles.csv')
print(df.head())
# print(df.tail())
df.info()
df.fillna('', inplace=True)
for i in range(len(df)):
    for j in range(12):
        if j !=7:
            df.iloc[i, j] = df.iloc[i, j].replace('"', '\\\"')  ##sql에 \" 라 보내기 위해
            df.iloc[i, j] = df.iloc[i, j].replace("'", "\\\'")



# df.fillna('', inplace=True)
# df= df.replace('"','%\\"')
# df= df.replace("'","\\'")

conn = pymysql.connect(user='root',
                       passwd='789632',  # 자신의 비번 입력
                       host='127.0.0.1',
                       port=3306,
                       db='netflix',
                       charset='utf8')

errors = []
# with open('./errors.pickle','rb') as f:
#     error_list = pickle.load(f)
# for i in error_list:

# with open("./errors_description.pickle", 'rb') as f:
#     error_list = pickle.load(f)


errors = []

for i in range(len(df)):
    try:

        sql = '''insert into contents value(
                        {}, {}, {} ,{} ,{} ,{} ,{} ,{} ,{} ,{} ,{} ,{});'''.format(
            '"{}"'.format(df.iloc[i, 0]),
            '"{}"'.format(df.iloc[i, 1]),
            '"{}"'.format(df.iloc[i, 2]),
            'null' if df.iloc[i,3] == '' else '"{}"'.format(df.iloc[i, 3]),
            'null' if df.iloc[i,3] == '' else '"{}"'.format(df.iloc[i, 4]),
            'null' if df.iloc[i,3] == '' else '"{}"'.format(df.iloc[i, 5]),
            'null' if df.iloc[i,3] == '' else '"{}"'.format(df.iloc[i, 6]),
            df.iloc[i,7],
            'null' if df.iloc[i,3] == '' else '"{}"'.format(df.iloc[i, 8]),
            'null' if df.iloc[i,3] == '' else '"{}"'.format(df.iloc[i, 9]),
            '"{}"'.format(df.iloc[i, 10]),
            '"{}"'.format(df.iloc[i, 11]))
        print(sql)
        with conn.cursor() as cursor:
            cursor.execute(sql)
            conn.commit()
    except:
        errors.append(i)
        print(i)

conn.close()
with open('./errors.pickle', 'wb') as f:
    pickle.dump(errors,f)



# print(len(data_a))
# print(len(data_b))
# print(df.listed_in.head())
# print(df.type.unique())
# max_length = 0
# df_duration = df_duration.dropna(inplace=False)
# df_duration.reset_index(drop=True, inplace= True)
# # for i,con in enumerate(df_date_added):
# #    if max_length < len(con):
# #
# # #         max_length = len(con)
# # #         print(len(df_date_added[i]))
# # #         print(df_date_added[i])
# # #         print(i)
# # max_value = 0
# for i, year in enumerate(df_duration):
#     if max_value < year:
#         max_value = year

# print(max_length)








#




