import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
matplotlib.use('TkAgg')
from matplotlib.backends.backend_pdf import PdfPages

data = {
    "Question": [
        "Have you ever used any of these mobile apps in the past to help with your well-being",
        "Have you ever used any of these mobile apps in the past to help with your well-being",
        "Have you ever used any of these mobile apps in the past to help with your well-being",
        "Have you ever used any of these mobile apps in the past to help with your well-being",
        "Did the mobile app/apps help you?",
        "Did the mobile app/apps help you?",
        "Did the mobile app/apps help you?",
        "Did the mobile app/apps help you?",
        "Count of Ethnic Background",
        "Count of Ethnic Background",
        "Count of Ethnic Background",
        "Count of Ethnic Background",
        "How often do you talk to others about your health and well-being",
        "How often do you talk to others about your health and well-being",
        "How often do you talk to others about your health and well-being",
        "How often do you talk to others about your health and well-being",
        "What type of content would you find the most useful on a mobile app?",
        "What type of content would you find the most useful on a mobile app?",
        "What type of content would you find the most useful on a mobile app?",
        "What type of content would you find the most useful on a mobile app?",
        "What type of content would you find the most useful on a mobile app?",
    ],
    "Response": [
        "Calm", "Buddha Sounds", "MyFitnessPal", "Apple Fitness",
        "No", "Maybe", "N/A", "Yes",
        "Prefer not to answer", "Asian", "White", "Hispanic or Latino",
        "Daily", "Weekly", "Rarely", "Monthly",
        "Music", "External Resources", "Interactive Activities", "Community", "Videos and Articles"
    ],
    "Percentage_or_Count": [
        "10%", "10%", "10%", "10%",
        "6.3%", "12.5%", "50%", "31.3%",
        "10%", "10%", "10%", "70%",
        5, 4, 4, 1,
        "1.6%", "11.3%", "25.8%", "25.8%", "33.9%"
    ]
}

df = pd.DataFrame(data)

df['is_percent'] = df['Percentage_or_Count'].astype(str).str.contains('%')
percentage_data = df[df['is_percent']].copy()
percentage_data['Percentage'] = percentage_data['Percentage_or_Count'].str.replace('%', '').astype(float)

count_data = df[~df['is_percent']].copy()
count_data['Count'] = count_data['Percentage_or_Count'].astype(int)

sns.set(style="whitegrid", color_codes=True)

for question, group in percentage_data.groupby('Question'):
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.pie(group['Percentage'], labels=group['Response'], autopct='%1.1f%%', startangle=140)
    ax.set_title(question, wrap=True)
    plt.tight_layout()
    plt.pause(0.001)
    plt.show(block=False)

for question, group in count_data.groupby("Question"):
    plt.figure(figsize=(10, 7))
    sns.barplot(data=group, x='Response', y='Count', palette="Blues_d")
    plt.title(question, wrap=True)
    plt.xlabel("Response")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.pause(0.001)
    plt.show(block=False)

print(df)
plt.show()