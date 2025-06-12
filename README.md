# 🚗 Car Info Chatbot

An AI-powered chatbot that provides detailed information about classic cars. It combines semantic search, local embeddings, and a lightweight language model (TinyLLaMA) to answer natural language questions about car specifications like MPG, horsepower, displacement, and more.

---

## 💡 Features

- 🧠 **Semantic Search** using SentenceTransformers
- ⚡ **Fast Retrieval** with FAISS vector indexing
- 🤖 **LLM Response Generation** using locally run TinyLLaMA
- 📊 **Classic Car Dataset** extracted from `Automobile.csv`
- 🧾 **Field-specific Filtering** of car attributes
- 🌐 **Streamlit Interface** for easy interaction

---

## 🛠️ Tech Stack

- Python 3.9+
- Pandas
- FAISS
- SentenceTransformers (`paraphrase-MiniLM-L6-v2`)
- ctransformers (`TinyLLaMA`)
- Streamlit

---

## 📂 Project Structure
```bash
.
├── main.py # Main logic and question handler
├── car_rag.py # Data loading, embedding, and FAISS logic
├── app.py # Streamlit frontend
├── Automobile.csv # Classic car dataset
└── models/
└── tinyllama-1.1b-chat-v1.0.Q8_0.gguf # Local LLM model file
```


---

## 🚀 How It Works

1. **Data Loading**: Car info is loaded from `Automobile.csv`.
2. **Text Embedding**: Each row is transformed into a text blob and embedded via SentenceTransformer.
3. **FAISS Indexing**: All embeddings are indexed for quick similarity search.
4. **User Query**: The chatbot takes a question and finds the most relevant car entry.
5. **Field Extraction**: `main.py` parses user intent and extracts the requested car fields.
6. **Streamlit App**: A web UI allows users to ask questions interactively.

---

## 🖥️ How to Run Locally

1. **Install dependencies**:

```bash
pip install -r requirements.txt
```
2. **Place the TinyLLaMA model in the models/ directory**:

Ensure it's named:
```bash
tinyllama-1.1b-chat-v1.0.Q8_0.gguf
```
3. **Run the Streamlit App**:

```bash
streamlit run app.py
```

## ✅ Example Questions

Here are a few example queries you can try:

- **"Ford Mustang horsepower and acceleration"**  
- **"AMC Gremlin MPG"**  
- **"Toyota Corona Mark II displacement and weight"**

These questions will return specific stats from the top-matching car record in the dataset.

---

## 📌 Notes

- The chatbot uses **semantic search** and responds based on the **most similar entry** in the dataset.
- Ensure your `Automobile.csv` file is **properly formatted** and contains clean, consistent values.
- If no relevant data is found or the requested field is missing, the bot replies with:  
  ❌ _"Sorry, I couldn’t find the requested info."_

---

## 📷 Architecture Diagram

Refer to the image below for a visual representation of how the system works:

![image](https://github.com/user-attachments/assets/bbed1333-340a-4958-a5db-cee0307726f0)



