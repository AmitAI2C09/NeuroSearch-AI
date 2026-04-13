# 🔍 NeuroSearch — Multimodal AI Search Engine

NeuroSearch is an AI-powered multimodal image retrieval system that allows users to search images using text, image, or a combination of both. It leverages the CLIP (Contrastive Language–Image Pretraining) model to map text and images into a shared embedding space, enabling semantic search across different modalities.

Unlike traditional keyword-based systems, NeuroSearch understands the meaning behind queries and retrieves visually and semantically relevant results using similarity-based ranking.

---

## 🚀 Features

- Text to Image Search using natural language queries  
- Image to Image Search for visual similarity  
- Combined Search using both text and image inputs  
- Cosine similarity-based ranking  
- Modern and responsive UI built with Streamlit  

---

## 🧠 How It Works

The system follows a simple pipeline:

Input (Text or Image) → CLIP Embedding → Similarity Calculation → Ranking → Output

Both text and images are converted into vector embeddings using CLIP, and cosine similarity is used to find the most relevant matches.

---

## 🛠️ Tech Stack

Python  
PyTorch  
OpenAI CLIP  
Streamlit  
NumPy  

---

## 📸 Screenshots

### Text Search
![Text Search](screenshots/text_search.png)

### Image Search
![Image Search](screenshots/image_search.png)

### Combined Search
![Combined Search](screenshots/combined_search.png)

---

## 📂 Project Structure

```
NeuroSearch/
│── app.py
│── model.py
│── utils.py
│── requirements.txt
│── screenshots/
│── images/
```

---

## ▶️ Run Locally

```
git clone https://github.com/AmitAI2C09/NeuroSearch-AI.git
cd NeuroSearch-AI
pip install -r requirements.txt
streamlit run app.py
```

---

## 📌 Future Improvements

- Improve retrieval accuracy  
- Add FAISS for faster search  
- Deploy as a web application  
- Expand dataset  

---

## 👨‍💻 Author

Amit Prakash Singh  
B.Tech CSE (AI)

---

## ⭐ Acknowledgements

OpenAI CLIP  
Streamlit
