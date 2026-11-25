import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


os.makedirs("output", exist_ok=True)
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (8, 5)

print("="*50)
print("TITANIC SURVIVAL ANALYSIS")
print("="*50)


try:
    df = sns.load_dataset("titanic")
    print("Dataset loaded from Seaborn.")
except Exception as e:
    print("Could not load from Seaborn. Please download titanic.csv from Kaggle.")
    print(e)
    df = pd.read_csv("titanic.csv")

print(f"\nShape of dataset: {df.shape} (rows, columns)")
print("\nFirst 5 rows:")
print(df.head())
print("\nColumns:")
print(df.columns.tolist())
print("\nData Types & Missing Values:")
print(df.isnull().sum())
print("\nBasic Statistics:")
print(df.describe(include='all'))


print("\n--- DATA CLEANING ---")

df['age'] = df['age'].fillna(df['age'].median())

df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])

if 'deck' in df.columns:
    df = df.drop(columns=['deck'])
print(f"Missing values after cleaning:\n{df.isnull().sum()}")
print(f"Overall Survival Rate: {df['survived'].mean()*100:.2f}%")


plt.figure()
sns.countplot(x='survived', data=df, palette='pastel')
plt.title('Overall Survival Count (0 = Died, 1 = Survived)')
plt.xlabel('Survived'); plt.ylabel('Number of Passengers')
plt.savefig('output/1_overall_survival.png'); plt.show()
plt.close()


plt.figure()
sns.barplot(x='sex', y='survived', data=df, palette='Set2')
plt.title('Survival Rate by Gender')
plt.ylabel('Survival Rate'); plt.ylim(0, 1)
plt.savefig('output/2_survival_by_gender.png'); plt.show()
plt.close()
print("\nSurvival Rate by Gender:")
print(df.groupby('sex')['survived'].mean())


plt.figure()
sns.barplot(x='class', y='survived', data=df, palette='Blues', order=['First','Second','Third'])
plt.title('Survival Rate by Passenger Class')
plt.ylabel('Survival Rate'); plt.ylim(0, 1)
plt.savefig('output/3_survival_by_class.png'); plt.show()
plt.close()
print("\nSurvival Rate by Class:")
print(df.groupby('class')['survived'].mean())


df['age_group'] = pd.cut(df['age'], bins=[0,12,18,35,60,100], labels=['Child (0-12)','Teen (13-18)','Adult (19-35)','Middle Age (36-60)','Senior (60+)'])
plt.figure()
sns.barplot(x='age_group', y='survived', data=df, palette='viridis')
plt.title('Survival Rate by Age Group')
plt.ylabel('Survival Rate'); plt.ylim(0, 1); plt.xticks(rotation=15)
plt.savefig('output/4_survival_by_age.png'); plt.show()
plt.close()
print("\nSurvival Rate by Age Group:")
print(df.groupby('age_group', observed=True)['survived'].mean())

plt.figure()
sns.barplot(x='class', y='survived', hue='sex', data=df, palette='coolwarm', order=['First','Second','Third'])
plt.title('Survival Rate by Class and Gender')
plt.ylabel('Survival Rate'); plt.ylim(0, 1)
plt.savefig('output/5_survival_class_gender.png'); plt.show()
plt.close()


plt.figure()
sns.histplot(data=df, x='fare', hue='survived', kde=True, bins=30, palette='Set1')
plt.title('Fare Distribution: Survived vs Died')
plt.xlabel('Fare Paid'); plt.ylabel('Count')
plt.savefig('output/6_fare_distribution.png'); plt.show()
plt.close()


plt.figure(figsize=(8,6))
numeric_df = df.select_dtypes(include='number')
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.savefig('output/7_correlation_heatmap.png'); plt.show()
plt.close()


print("\n" + "="*50)
print("KEY FINDINGS / CONCLUSION")
print("="*50)
print("1. Women had a much higher survival rate than men.")
print("2. First Class passengers survived more than Third Class.")
print("3. Children had a higher survival chance than adults.")
print("4. Passengers who paid higher fare had better survival chance.")
print("5. Gender and Class together were the strongest factors.")
print("\nAll charts saved in 'output' folder.")
print("Project Completed Successfully!")
