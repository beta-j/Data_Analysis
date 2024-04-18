# -*- coding: utf-8 -*-
"""LAS3021 - PANDAS - Titanic Tutorial

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14r07G2GO8IZdbOZ2rUhPtY3WU0jP8l-J
"""

import pandas as pd
import numpy as np

titanic_df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vRUS-gYW6aKJRuAr1E1YzPXEaxUH1f-awlAf-STu6-d0Gr02I_9c_I7NAf4mz1kVDGGBrYbCytSHaUk/pub?output=csv')
titanic_df.head(5)

titanic_df.info()

titanic_df.isnull().sum()

titanic_df.dtypes

titanic_df.describe()

titanic_df.Age.mean()

titanic_df['Age'].hist(bins=10)

titanic_df['Age'].dropna().hist(bins=10)

titanic_df[100:110]

titanic_df[100:110][['Name', 'Sex', 'Age']]

titanic_df.Name.sort_values(ascending=True).head(5)

titanic_df.sort_values(by='Name')[:5]

titanic_df[titanic_df.Fare >15].sort_values(by='Fare', ascending=False)

def title(fullname):
  lower_case = fullname.lower()
  if 'dr.' in lower_case:
    return 'Doctor'
  elif 'mr.' in lower_case:
    return 'Mister'
  elif 'ms.' in lower_case:
    return 'Mistress'
  elif 'mrs.' in lower_case:
    return 'Missus'
  else: return 'Unknown'




titanic_df[titanic_df.Name.apply(title) == 'Doctor'].head(5)

titanic_df.drop(columns = 'Siblings/Spouses Aboard').head(5)

titanic_df['Survived'].unique()

titanic_df.groupby(by='Pclass').mean('Age')
#OR you can use: titanic_df.groupby('Pclass').Age.mean()



titanic_df.Name[titanic_df.Name.apply(title) == 'Doctor']

titanic_df['Salutation'] = titanic_df.Name.apply(title)
titanic_df.drop(columns='Siblings/Spouses Aboard').head(5)

titanic_df.groupby('Salutation').Age.mean()

p = {'person_id' : pd.Series([1,2,3,4]),
     'name': pd.Series(['Andrew', 'Neville', 'Maria', 'Marc'])}
person = pd.DataFrame(p)
person

c={'course_id':pd.Series(['MTH113', 'PHY103', 'BGY1829', 'SC1029']),
   'course_name': pd.Series(['Maths', 'Physics', 'Biology', 'Scoial Science']),
   'person_id': pd.Series([1,2,3])}
course = pd.DataFrame(c)
course

pd.merge(person, course, left_on='person_id', right_on='person_id', how='inner')

pd.merge(person, course, left_on='person_id', right_on='person_id', how='outer')

pd.merge(person, course, left_on='person_id', right_on='person_id', how='right')

pd.merge(person, course, left_on='person_id', right_on='person_id', how='left')

titanic_df.corr()

