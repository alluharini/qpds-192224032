import pandas as pd
data = {
    'DEPARTMENT_ID': [10,10, 20, 30, 40, 50, 60, 70, 80, 90,10,20,30]
}
df = pd.DataFrame(data)
# Select and print distinct DEPARTMENT_ID
distinct_dept_ids = df['DEPARTMENT_ID'].unique()
print(distinct_dept_ids)