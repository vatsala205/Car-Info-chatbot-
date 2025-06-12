from car_rag import load_car_csv, embed_texts, build_faiss_index, get_top_car_data

# Load and prepare once to reuse
file_path = "Automobile.csv"
texts = load_car_csv(file_path)
embeddings, embed_model = embed_texts(texts)
index = build_faiss_index(embeddings)

def extract_requested_fields(question: str, car_data: str) -> str:
    question = question.lower()
    response = ""
    fields_map = {
        "mpg": "MPG",
        "horsepower": "Horsepower",
        "model year": "Model Year",
        "cylinders": "Cylinders",
        "weight": "Weight",
        "acceleration": "Acceleration",
        "origin": "Origin",
        "displacement": "Displacement",
    }

    emojis = {
        "mpg": "⛽",
        "horsepower": "⚡",
        "model year": "🕰️",
        "cylinders": "🔧",
        "weight": "⚖️",
        "acceleration": "🚀",
        "origin": "🌍",
        "displacement": "📏"
    }

    for key, label in fields_map.items():
        if key in question:
            for line in car_data.split('|'):
                if label.lower() in line.lower():
                    response += f"{emojis.get(key, '🔹')} {line.strip()}\n"

    return response.strip() or "❌ Sorry, I couldn’t find the requested info."

def ask_question(user_question: str, debug=False) -> str:
    top_car_data = get_top_car_data(user_question, texts, index, embed_model, top_k=1)
    return extract_requested_fields(user_question, top_car_data)

# Optional alias
get_answer = ask_question
