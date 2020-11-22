import io
import requests
import pandas as pd
url = 'https://raw.githubusercontent.com/AdiPersonalWorks/Random/master/student_scores%20-%20student_scores.csv'
s = requests.get(url).content
df = pd.read_csv(io.StringIO(s.decode('utf-8')))
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(df.loc[:,['Hours']],df.loc[:,['Scores']])
print(lr.predict([[9.25]]))
