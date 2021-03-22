import pandas as pd 
import csv

df = pd.read_csv('/Users/SarthakPratik/Desktop/ds_comp_pro/Data_Cleaning/glassdoor_jobs.csv')



#salary parsing
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)


df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
min_kd = salary.apply(lambda x: x.replace('K','').replace('$',''))

min_hr = min_kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

df['Min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['Max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))

df['Avg_salary'] = (df.Min_salary + df.Max_salary)/2

#company name

df['Comp_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating']<0 else x['Company Name'][:-3],axis =1)

#size

df['Size'] = df['Size'].apply(lambda x: x.lower().replace('employees',''))

#age

df['Age'] = df['Founded'].apply(lambda x: x if x < 0 else 2020 - x)

#state field 
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])
df.job_state.value_counts()

#python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)

df.columns

df_out = df.drop(['Unnamed: 0'], axis =1)

df_out.to_csv('salary_data_cleaned.csv',index = False)
