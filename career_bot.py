
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

career_keywords = {
    "Software Engineer": ["code", "python", "java", "developer", "programming"],
    "Graphic Designer": ["design", "photoshop", "drawing", "illustration", "creativity"],
    "Doctor": ["medical", "health", "hospital", "doctor"],
    "Teacher": ["teach", "education", "school", "students"],
    "Accountant": ["finance", "money", "account", "tax", "numbers"],
    "Entrepreneur": ["business", "startup", "management", "sales"]
}

def recommend_career(user_input):
    tokens = word_tokenize(user_input.lower())
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    recommended = []

    for career, keywords in career_keywords.items():
        if any(keyword in tokens for keyword in keywords):
            recommended.append(career)

    return recommended if recommended else ["Sorry, no match found. Try mentioning more interests."]
