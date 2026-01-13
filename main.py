import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#definitions
df = pd.read_csv('healthcare-dataset-stroke-data.csv')
id = df['id']
gender = df['gender']
age = df['age']
hypertension = df['hypertension']
heart_disease = df['heart_disease']
ever_married = df['ever_married']
work_type = df['work_type']
residence_type = df['Residence_type']
avg_glucose_level = df['avg_glucose_level']
bmi = df['bmi']
smoking_status = df['smoking_status']
stroke = df['stroke']

# plotting
# Correlation between BMI and stroke chance
sns.boxplot(x=stroke, y=bmi)
plt.xticks([0, 1], ['No Stroke', 'Stroke'])
plt.xlabel('Had Stroke')
plt.ylabel("BMI")
plt.title("Correlation between BMI and Strokes")
plt.savefig('bmi_stroke.png')
plt.close()

# Correlation between being married and having a stroke
sns.barplot(x=ever_married, y=stroke)
plt.ylabel('Stroke Rate')
plt.xlabel('Ever Married')
plt.title('Correlation Between Being Married and Having a Stroke')
plt.savefig('married_stroke.png')
plt.close()

# Correlation between type of work and having a stroke
sns.barplot(x=work_type, y=stroke)
plt.ylabel('Stroke Rate')
plt.xlabel('Type of Work')
plt.savefig('work_type_stroke.png')
plt.close()

# Correlation between pre-existing health conditions and having a stroke
sns.barplot(data=df, x=hypertension | heart_disease, y=stroke)
plt.ylabel('Stroke Rate')
plt.xticks([0, 1], ['No Health Conditions', 'Pre-existing Health Conditions'])
plt.xlabel('Health Conditions')
plt.savefig('health_conditions_stroke.png')
plt.close()

# Correlation between gender and strokes
sns.barplot(x=gender, y=stroke)
plt.ylabel('Stroke Rate')
plt.xlabel('Gender')
plt.savefig('gender_stroke.png')
plt.close()

# Correlation between glucose levels and stroke rate
sns.boxplot(x=stroke, y=avg_glucose_level)
plt.savefig('glucose_stroke.png')
plt.close()