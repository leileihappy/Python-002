import pandas as pd
import MySQLdb, pymysql
from emanalysis import EmAnalysis

dbInfo = {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'root',
    'password' : 'anlei6666',
    'db' : 'test'
}
def insertComment(dbInfo,listdata):
    conn = pymysql.connect(host = dbInfo['host'],
    port = dbInfo['port'],
    user = dbInfo['user'],
    password = dbInfo['password'],
    db = dbInfo['db'])
    cur = conn.cursor()

    try:
        for i in range(len(listdata)):
            data=listdata[i]
            sql = 'insert into zdm_comment_score(title,comment,comment_date,score) values (%s,%s,%s,%s)'
            cur.execute(sql,(data[0],data[1],data[2],data[3]))
        cur.close()
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()

mysql_cn = MySQLdb.connect(host = dbInfo['host'],
    port = dbInfo['port'],
    user = dbInfo['user'],
    password = dbInfo['password'],
    db = dbInfo['db'])

df = pd.read_sql('select * from zdm_comment;', con=mysql_cn)    
mysql_cn.close()

rowdata = df.dropna()
scores = []
for data in rowdata['comment']:
    score = EmAnalysis().analysis(data)
    scores.append(score)
rowdata['score'] = scores
rowdata1 = rowdata.drop('id',axis=1)
insertComment(dbInfo,rowdata1.values)
