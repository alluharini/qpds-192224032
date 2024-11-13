import pandas as pd

data = {
    'student_name': ['Alice', 'Bob', 'Charlie', 'David', 'Ella', 'Frank'],
    'school_code': ['A', 'B', 'A', 'C', 'B', 'C'],
    'age': [15, 16, 14, 15, 16, 17]
}

df = pd.DataFrame(data)
grouped = df.groupby('school_code')

print(type(grouped))

for group, group_data in grouped:
    print(f"\nGroup: {group}")
    print(group_data)
