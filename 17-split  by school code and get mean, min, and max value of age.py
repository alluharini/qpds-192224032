import pandas as pd

data = {
    'student_name': ['Alice', 'Bob', 'Charlie', 'David', 'Ella', 'Frank'],
    'school_code': ['A', 'B', 'A', 'C', 'B', 'C'],
    'age': [15, 16, 14, 15, 16, 17]
}

df = pd.DataFrame(data)
age_stats = df.groupby('school_code')['age'].agg(['mean', 'min', 'max'])
print(age_stats)
