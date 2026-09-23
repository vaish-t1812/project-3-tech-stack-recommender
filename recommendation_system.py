import pandas as pd

print("========================================")
print("    TECH STACK RECOMMENDATION SYSTEM")
print("========================================")

print("\nLoading career dataset...")

data = pd.read_csv("raw_skills.csv")

print("\nDataset loaded successfully!")
print("\nCareer roles available:")

print(data["role"])