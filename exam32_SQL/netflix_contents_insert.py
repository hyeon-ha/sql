import pandas as pd
import pymysql
import numpy as np
print(np.nan)



#
def insert(self, sql):
    conn = pymysql.connect(user='root',
                           passwd='789632',  # 자신의 비번 입력
                           host='127.0.0.1',
                           port=3306,
                           db='netflix',
                           charset='utf8')

    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
        conn.commit()
    except:
        print('conn error')
    finally:
        conn.close()

df = pd.read_csv('../datasets/netflix_titles.csv')
print(df.head())
# print(df.tail())
df.info()
df.fillna('', inplace=True)
for i in range(len(df)):
    if i < 10 :
        # print(df.iloc[i, :])

        sql = '''insert into netflix_contents value(
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

#
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










