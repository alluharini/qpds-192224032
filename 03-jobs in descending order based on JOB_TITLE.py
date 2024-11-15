import pandas as pd
data={
    'emp_id':[1,2,3,4],
    'emp_job':['CR','IT','ACC','IT']
}
df=pd.DataFrame(data)
sorted_list=df.sort_values(by='emp_job',ascending=True)
print(sorted_list)
