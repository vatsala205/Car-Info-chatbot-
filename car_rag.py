import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from ctransformers import AutoModelForCausalLM

# Load csv data
def load_car_csv(file_path):
    df = pd.read_csv(file_path)
    texts = []
    for _, row in df.iterrows():
        text = f"Name: {row['name']} | MPG: {row['mpg']} | Cylinders: {row['cylinders']} | Displacement: {row['displacement']} | Horsepower: {row['horsepower']} | Weight: {row['weight']} | Acceleration: {row['acceleration']} | Model Year: {row['model_year']} | Origin: {row['origin']}"
        texts.append(text)
    return texts

# Embed with SentenceTransformer
def embed_texts(texts):
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    embeddings = model.encode(texts, convert_to_tensor=False)
    return embeddings, model

# Build FAISS Index
def build_faiss_index(embeddings):
    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings).astype('float32'))
    return index

# Load TinyLLaMA locally
llm = AutoModelForCausalLM.from_pretrained(
    "models/tinyllama-1.1b-chat-v1.0.Q8_0.gguf",
    model_type="llama",
    model_file="tinyllama-1.1b-chat-v1.0.Q8_0.gguf",
    local_files_only=True
)

# Generate answer based on question + context
def answer_question(question, texts, index, embed_model, top_k=1, debug=False):
    q_embed = embed_model.encode([question])
    _, I = index.search(np.array(q_embed).astype('float32'), top_k)
    retrieved = [texts[i] for i in I[0]]
    context = "\n".join(retrieved)

    if debug:
        print("\n[DEBUG] Retrieved context:\n", context)

    # Normalize and format
    normalized_context = context.replace("Horsepower:", "Horsepower (hp):") \
                                .replace("Weight:", "Weight (lbs):") \
                                .replace("MPG:", "MPG (miles/gallon):") \
                                .replace("Acceleration:", "Acceleration (0-60 mph in sec):")

    car_name = retrieved[0].split('|')[0].replace("Name:", "").strip().title()

    prompt = f"""You are a helpful assistant that answers questions based only on the car info provided.

### CONTEXT:
{normalized_context}

### QUESTION: {question}
### INSTRUCTIONS: Answer using only the data provided above. Refer to the car as "{car_name}" and ensure units like horsepower (hp) and weight (lbs) are mentioned. If multiple specs are requested, provide all in a clean list.

### ANSWER:"""

    response = llm(prompt)
    return response.strip()

def get_top_car_data(question, texts, index, embed_model, top_k=1):
    q_embed = embed_model.encode([question])
    _, I = index.search(np.array(q_embed).astype('float32'), top_k)
    top_text = texts[I[0][0]]
    return top_text  # return as string for extract_requested_fields to work

