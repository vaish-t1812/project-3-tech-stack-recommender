# Test Results

This document records the tests performed on the Tech Stack Career Recommendation System.

The system was tested using different combinations of user skills to check whether the recommendation results change according to the entered skills.

## Test 1: Data and SQL Skills

### Input

Python, SQL, Statistics

### Expected Behavior

The system should recommend careers related to Python, SQL, and Statistics.

### Result

1. Data Scientist
   - Similarity Score: 0.5052

2. Data Analyst
   - Similarity Score: 0.4783

3. Backend Developer
   - Similarity Score: 0.2646

### Status

Passed

---

## Test 2: Machine Learning Skills

### Input

Python, Machine Learning, TensorFlow

### Expected Behavior

The system should recommend careers related to Python and Machine Learning.

### Result

1. Machine Learning Engineer
   - Similarity Score: 0.6606

2. Data Scientist
   - Similarity Score: 0.4453

3. Cybersecurity Engineer
   - Similarity Score: 0.0827

### Status

Passed

---

## Test 3: Frontend Development Skills

### Input

HTML, CSS, JavaScript, React

### Expected Behavior

The system should recommend a frontend development career.

### Result

1. Frontend Developer
   - Similarity Score: 0.8324

### Status

Passed

---

## Test 4: Cloud and DevOps Skills

### Input

AWS, Docker, Kubernetes

### Expected Behavior

The system should recommend careers related to cloud computing, DevOps, and container technologies.

### Result

1. DevOps Engineer
   - Similarity Score: 0.5769

2. Machine Learning Engineer
   - Similarity Score: 0.1794

3. Cloud Architect
   - Similarity Score: 0.1768

### Status

Passed

---

## Test 5: Empty Input Validation

### Input

No skills entered.

### Expected Behavior

The system should not accept empty input and should ask the user to enter at least one skill.

### Result

The system displayed an input validation message and requested valid input.

### Status

Passed

---

## Overall Testing Summary

The recommendation system was tested using multiple skill combinations.

The results show that different user inputs produce different career recommendations and similarity scores.

The system also correctly validates empty input.

### Testing Status

All documented tests passed successfully.

## Conclusion

The testing demonstrates that the recommendation system can:

- Accept user skill preferences
- Validate user input
- Convert skill descriptions into TF-IDF vectors
- Calculate cosine similarity
- Rank career roles based on similarity
- Display the top career recommendations