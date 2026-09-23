import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("========================================")
print("    TECH STACK RECOMMENDATION SYSTEM")
print("========================================")

print("\nLoading career dataset...")

data = pd.read_csv("raw_skills.csv")

print("\nDataset loaded successfully!")

print("\nPlease enter your skills.")
print("Example: Python, SQL, Machine Learning")

while True:
    user_input = input("\nEnter your skills: ").strip()

    if user_input:
        break

    print("Input cannot be empty. Please enter at least one skill.")

print("\nYou entered:")
print(user_input)

# Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Combine career skills and user input
documents = data["skills"].tolist() + [user_input]

# Convert the text into TF-IDF vectors
tfidf_matrix = vectorizer.fit_transform(documents)

print("\nTF-IDF conversion completed!")

# Calculate cosine similarity
similarity_scores = cosine_similarity(
    tfidf_matrix[-1],
    tfidf_matrix[:-1]
)

# Add similarity scores to the dataset
data["similarity"] = similarity_scores[0]

# Sort careers by similarity score
recommendations = data.sort_values(
    by="similarity",
    ascending=False
)

# Select the top 3 careers
top_recommendations = recommendations.head(3)

print("\n========================================")
print("       TOP CAREER RECOMMENDATIONS")
print("========================================")

for index, row in top_recommendations.iterrows():
    print(f"\n{index + 1}. {row['role']}")
    print(f"   Similarity Score: {row['similarity']:.4f}")
    print(f"   Skills: {row['skills']}")