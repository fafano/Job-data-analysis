import pandas as pd
import os

# فعال کردن پشتیبانی از رنگ در ترمینال ویندوز
os.system('')

def highlight_skill(text, skill):
    return text.replace(skill, f"\033[91m{skill}\033[0m") 

try:
    data = pd.read_csv('data.csv')
    print("File loaded successfully!")
except FileNotFoundError:
    print("Error: 'data.csv' not found!")
    exit()

def analyze_jobs_by_skill():
    skill = input("\nEnter the desired skill (for example Python): ").strip()
    skill_lower = skill.lower()
    jobs_with_skill = data[data['skills'].str.lower().str.contains(skill_lower, na=False)]
    count = len(jobs_with_skill)
    
    print(f"\nAnalysis results for '{skill}':")

    if count == 0:
        print("no result!!")
        exit()
    else :
        print(f"Found {count} jobs\n")


    print(f"{'Job Title':<25} | {'City':<10} | {'Skills'}")
    print("-" * 60)
    for _, row in jobs_with_skill.iterrows():
        highlighted_skills = highlight_skill(row['skills'].lower(), skill_lower)
        print(f"{row['job_title']:<25} | {row['city']:<10} | {highlighted_skills}")



analyze_jobs_by_skill()
