import pandas as pd
data = {
    'EMPLOYEE_ID': [102, 101, 101, 201, 114, 122, 200, 176, 176, 200],
    'JOB_ID': ['IT_PROG', 'AC_ACCOUNT', 'AC_MGR', 'MK_REP', 'ST_CLERK', 'ST_CLERK', 'AD_ASST', 'SA_REP', 'SA_MAN', 'AC_ACCOUNT'],
    'DEPARTMENT_ID': [60, 110, 110, 20, 50, 50, 90, 80, 80, 90]
}
df = pd.DataFrame(data)
# Find employees who did two or more jobs
employee_job_counts = df.groupby('EMPLOYEE_ID').size()
employees_with_multiple_jobs = employee_job_counts[employee_job_counts >= 2].index.tolist()
print(employees_with_multiple_jobs)