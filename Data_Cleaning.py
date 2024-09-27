import numpy as np
import pandas as pd
import matplotlib.pyplot as plt # visualizing data
import seaborn as sns

df = pd.read_csv(r"C:\Users\Junaid Javed\Downloads\Sales_data.csv", encoding= 'unicode_escape')
print(df.head())
print(df.shape)
#drop unrelated/blank columns
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)

pd.isnull(df).sum()
df.dropna(inplace=True)

# change data type
df['Amount'] = df['Amount'].astype('int')

print(df['Amount'].dtypes)
print(df.columns)
print(df.describe())
print(df[['Age', 'Orders', 'Amount']].describe())

# plotting a bar chart for Gender and it's count

ax = sns.countplot(x = 'Gender',data = df)

for bars in ax.containers:
    ax.bar_label(bars)

#plt.show()

# plotting a bar chart for gender vs total amount

sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)

plt.show()