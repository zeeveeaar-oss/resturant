import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')
df = df.dropna()
print(df.head())
print(df.info())

sns.barplot(x='day', y='total_bill', hue='sex', data=df)
plt.title('Average Total Bill per Day by Gender')
plt.xlabel('Day')
plt.ylabel('Average Bill')
plt.show()

sns.countplot(x='day', hue='sex', data=df)
plt.title('Number of Diners per day by Gender')
plt.xlabel('Day')
plt.ylabel('Count')
plt.show()

sns.boxplot(x='day', y='total_bill', hue='sex', data=df)
plt.title('Spread of Total Bill per day')
plt.xlabel('Day')
plt.ylabel('total bill')
plt.show()

sns.stripplot(x='day', y='total_bill', hue='sex', data=df)
plt.title('Every Bill Amount per day (strip plot)')
plt.xlabel('Day')
plt.ylabel('total bill')
plt.show()

sns.swarmplot(x='day', y='total_bill', hue='sex', data=df)
plt.title('Spread of Total Bill per day')
plt.xlabel('Day')
plt.ylabel('total bill')
plt.show()

sns.jointplot(x='total_bill', y='tip', data=df)
plt.suptitle('Total Bill vs Tip', y=1.02)
plt.show()

sns.jointplot(x='total_bill', y='tip', data=df, kind='Kde')
plt.suptitle('Total Bill vs Tip - KDE joint plot', y=1.02)
plt.show()

sns.pairplot(df[['total_bill', 'tip', 'size']])
plt.suptitle('Pair plot - Bill, Tip and party Size', y=1.02)
plt.show()

sns.pointplot(x='day', y='total_bill', hue='sex', data=df)
plt.title('Average Bill per day')
plt.xlabel('Day')
plt.ylabel('Average Bill')
plt.show()

sns.Implot(x='total_bill', y='tip', data=df)
plt.title('Total Bill vs Tip - Trend Line')
plt.show()