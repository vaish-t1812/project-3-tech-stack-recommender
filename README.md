<<<<<<< HEAD

=======
# Tech Stack Career Recommendation System

A content-based recommendation system that suggests career paths based on a user's skills and interests.

## Project Overview

This project is an Artificial Intelligence recommendation system developed as part of Industrial Training Project 3.

The system asks the user to enter their skills and recommends the top three career roles based on the similarity between the user's skills and the skills associated with different careers.

## Objective

The objective of this project is to build a simple recommendation system that:

- Accepts user skills as input
- Matches user skills with career skill descriptions
- Uses TF-IDF for text vectorization
- Uses cosine similarity to measure similarity
- Ranks careers according to similarity
- Displays the top three recommendations

## How the System Works

The recommendation process follows these steps:

1. Load the career skills dataset.
2. Ask the user to enter their skills.
3. Validate the user input.
4. Convert career skills and user skills into TF-IDF vectors.
5. Calculate cosine similarity between the user and each career.
6. Sort careers according to their similarity scores.
7. Display the top three career recommendations.

## Technologies Used

- Python
- Pandas
- Scikit-learn
- TF-IDF
- Cosine Similarity
- CSV

## Project Structure

- `README.md` - Project documentation
- `raw_skills.csv` - Career roles and associated skills
- `recommendation_system.py` - Main recommendation system
- `requirements.txt` - Python dependencies
- `test_results.md` - Testing results
- `.gitignore` - Files and folders excluded from Git

## Dataset

The project uses a manually curated CSV dataset containing career roles and their associated skills.

The dataset currently contains career roles such as:

- Data Scientist
- Machine Learning Engineer
- Data Analyst
- Backend Developer
- Frontend Developer
- DevOps Engineer
- Cloud Architect
- Data Engineer
- Cybersecurity Engineer
- Mobile App Developer

## Example

### Example Input

`Python, SQL, Statistics`

### Example Output

1. **Data Scientist**  
   Similarity Score: `0.5052`  
   Skills: Python, SQL, Statistics, Machine Learning, Pandas, NumPy

2. **Data Analyst**  
   Similarity Score: `0.4783`  
   Skills: Python, SQL, Excel, Statistics, Power BI, Tableau

3. **Backend Developer**  
   Similarity Score: `0.2646`  
   Skills: Python, Java, SQL, APIs, REST, Databases, Git

The exact recommendations and similarity scores depend on the user's input and the dataset.

## How to Run

### 1. Clone the Repository

`git clone https://github.com/vaish-t1812/project-3-tech-stack-recommender.git`

### 2. Open the Project Folder

`cd project-3-tech-stack-recommender`

### 3. Create a Virtual Environment

`python -m venv venv`

### 4. Activate the Virtual Environment

On Windows PowerShell:

`.\venv\Scripts\Activate.ps1`

### 5. Install Dependencies

`pip install -r requirements.txt`

### 6. Run the Recommendation System

`python recommendation_system.py`

## AI Concepts Used

### TF-IDF

TF-IDF stands for Term Frequency-Inverse Document Frequency.

It converts text into numerical vectors based on the importance of terms within the collection of documents.

In this project, TF-IDF is used to represent:

- Career skill descriptions
- User-entered skills

### Cosine Similarity

Cosine similarity measures the similarity between the user's TF-IDF vector and each career's TF-IDF vector.

Higher similarity scores indicate a closer match between the user's entered skills and the career skill description.

## Recommendation Process

User enters skills

↓

Input validation

↓

Career dataset loaded

↓

TF-IDF vectorization

↓

Cosine similarity calculation

↓

Similarity scores

↓

Career ranking

↓

Top 3 career recommendations

## Testing

The recommendation system was tested with different skill combinations, including:

- Data and SQL skills
- Machine Learning skills
- Frontend development skills
- Cloud and DevOps skills
- Empty input

Testing results are documented in `test_results.md`.

## Limitations

This is a simple educational recommendation system.

The recommendations depend on the skills available in the manually curated dataset.

The system does not use:

- Real-time job-market information
- Salary information
- Employment statistics
- User history
- External job-market APIs

## Future Improvements

Possible future improvements include:

- Expanding the career dataset
- Adding more skills and career roles
- Creating a graphical user interface
- Adding skill suggestions or autocomplete
- Allowing users to rate recommendations
- Improving the dataset using real-world career information
- Deploying the application as a web application

## Conclusion

This project demonstrates how text processing and similarity techniques can be used to create a simple content-based recommendation system.

The system converts user skills and career skill descriptions into numerical representations using TF-IDF, compares them using cosine similarity, ranks the results, and recommends the three careers with the highest similarity scores.
