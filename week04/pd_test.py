import pandas as pd
import numpy as np

df1 = pd.DataFrame({'ID':[222,505,880,1010,6666]*4,
                    'Order_ID':['A','A','B','C','D']*4,
                    'Age':np.random.randint(25,60,20)})

df2 = pd.DataFrame({'ID':[222,350,880,1010,1111]*4,
                    'Order_ID':['A','D','D','B','B']*4,
                    'Age':np.random.randint(25,60,20),})
# print(df1)
# with pd.ExcelWriter(r'week4.xlsx') as xlsx:
#     df1.to_excel(xlsx, sheet_name = 'table1',index=False)
#     df2.to_excel(xlsx, sheet_name = 'table2',index=False)

# 1.获取全部数据
df = pd.read_excel('week4.xlsx',sheet_name='table1')
t2 = pd.read_excel('week4.xlsx',sheet_name='table2')
# 2.获取前10条
limit = df1.loc[0:10]
# 3. SELECT id FROM data;  //id 是 data 表的特定一列
id_cols = df['ID']
# 4. SELECT COUNT(id) FROM data;
id_count = df['ID'].count()
# 5. SELECT * FROM data WHERE id<1000 AND age>30;
data = df[(df['ID']<1000) & (df['Age']>30)]
# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
data_group = df.groupby('ID').aggregate({'Order_ID':'nunique'}).to_dict()
# nunique() 方法用于获取列中所有唯一值的数量,unique() 统计list中的不同值时,返回的是array
# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
data_merge = pd.merge(df,t2, on ='ID',how = 'inner')
# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
data_concat = pd.concat([df,t2],join='inner')
# 9. DELETE FROM table1 WHERE id=10;
data_drop = df.drop(df[df['ID'] == 222].index)
# 10. ALTER TABLE table1 DROP COLUMN column_name;
data_drop1 = df.drop(columns='Age')
# print(data_drop1)

