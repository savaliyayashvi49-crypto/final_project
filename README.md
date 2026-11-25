# final_project

Titanic Survival Analysis
Project Overview
This project analyzes the Titanic passenger dataset to understand which factors influenced survival.
It is an Exploratory Data Analysis (EDA) project using Python, Pandas, Matplotlib, and Seaborn.

Objectives
Clean and explore the Titanic dataset
Analyze survival rates by gender, class, age, and fare
Visualize patterns using charts
Draw conclusions from the data
Dataset
Source: Titanic Dataset from Kaggle / Seaborn
Rows: 891 passengers
Key Columns: survived, pclass, sex, age, fare, embarked, class, sibsp, parch
No manual download is required. The dataset is loaded directly using Seaborn:

df = sns.load_dataset("titanic")
Tools and Libraries
Python 3.x
Pandas - Data cleaning and analysis
Matplotlib - Plotting
Seaborn - Statistical visualization
Folder Structure
titanic_project/
├── main.py
├── requirements.txt
├── README.md
└── output/
    ├── survival_count.png
    ├── survival_by_gender.png
    ├── survival_by_class.png
    └── correlation.png
How to Run
Install dependencies:
pip install -r requirements.txt
Run the project:
python main.py
View charts in the output folder.
Data Cleaning
Missing Age values filled with median age
Missing Embarked values filled with most common port
Deck column dropped due to too many missing values
Analysis Performed
Overall Survival Rate
Survival Rate by Gender
Survival Rate by Passenger Class
Survival Rate by Age Group
Survival Rate by Class and Gender
Fare Distribution - Survived vs Died
Correlation Heatmap
Key Findings
Overall survival rate was around 38%.
Women had a much higher survival rate than men.
First Class passengers survived more than Third Class passengers.
Children had a higher chance of survival than adults.
Passengers who paid higher fare had better survival chances.
Gender and passenger class were the strongest factors affecting survival.
Conclusion
Survival on the Titanic was not random. It mainly depended on gender, passenger class, and age.
The "women and children first" policy and better access for First Class passengers clearly affected the results.




