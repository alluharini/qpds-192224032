import pandas as pd
data = {
    'student_name': ['Alice', 'Bob', 'Charlie', 'David', 'Ella', 'Frank'],
    'school_code': ['A', 'B', 'A', 'C', 'B', 'C'],
    'class': ['X', 'Y', 'X', 'Z', 'Y', 'Z'],
    'score': [85, 90, 78, 88, 76, 95]
}
df = pd.DataFrame(data)
grouped_df = df.groupby(['school_code', 'class'])
print("Grouped DataFrame:")
for (school, class_name), group in grouped_df:
    print(f"\nGroup: School Code = {school}, Class = {class_name}")
    print(group)
