from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

questions = [
    "What is your name?",
    "What are your working hours?",
    "What courses are available?",
    "How can I contact support?",
    "What is artificial intelligence?"
]

answers = [
    "Our chatbot name is AI Assistant.",
    "We are available 24 hours.",
    "We provide AI, Data Science and Web Development courses.",
    "You can contact support through email.",
    "Artificial Intelligence is the field of making machines learn and think like humans."
]

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(questions)

def chatbot_response(user_input):
    user_vector = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vector, vectors)
    index = similarity.argmax()

    if similarity[0][index] < 0.3:
        return "Sorry, I don't understand."

    return answers[index]
