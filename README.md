🔍 NeuroSearch — CLIP-based Multimodal AI Search Engine

NeuroSearch is an AI-powered multimodal retrieval system that enables semantic search across text and images. It leverages a pretrained CLIP model to map both modalities into a shared embedding space, allowing efficient cross-modal similarity search.

Unlike traditional keyword-based systems, NeuroSearch retrieves results based on semantic understanding using embedding similarity.

---

🚀 Features

- 🔎 Text-to-Image Search using natural language queries
- 🖼️ Image-to-Image Search for visual similarity
- 🔗 Combined Search (Text + Image)
- 📊 Top-K Retrieval System (ranked results)
- 🎯 Cosine similarity-based matching
- 🌐 Interactive UI built with Streamlit

---

🧠 Core Idea

NeuroSearch uses representation learning to embed both text and images into a shared vector space:

Text → Embedding
Image → Embedding
Similarity → Cosine Similarity

The system retrieves the Top-K most relevant results based on similarity scores.

---

⚙️ How It Works

1. User inputs text or uploads an image
2. CLIP encodes inputs into embeddings
3. Dataset images are encoded into the same space
4. Cosine similarity is computed
5. Top-K most similar images are retrieved and displayed

---

🛠️ Tech Stack

- Python
- PyTorch
- OpenAI CLIP
- Streamlit
- NumPy

---

📊 Dataset

The dataset used in this project consists of manually collected images from publicly available sources.

- Images are stored locally in the "/images" directory
- The dataset contains diverse categories such as animals, objects, and scenes
- No labels are required, as CLIP performs zero-shot semantic matching

This setup demonstrates how multimodal retrieval systems can work even without explicitly labeled datasets.

- Dataset size: ~200 images

  

📸 Screenshots

### Text Search
![Text Search](screenshots/text_search.png)

### Image Search
![Image Search](screenshots/image_search.png)

### Combined Search
![Combined Search](screenshots/combined_search.png)

📂 Project Structure

NeuroSearch/

│── app.py                      # Streamlit UI

│── model.py                    # CLIP embedding functions

│── utils.py                    # Similarity + ranking logic

│── images/                     # Dataset

│── screenshots/.               # Demo images


---

▶️ Run Locally

git clone https://github.com/AmitAI2C09/NeuroSearch-AI.git
cd NeuroSearch-AI
pip install -r requirements.txt
streamlit run app.py

---

📌 Future Improvements

- Faster retrieval using FAISS
- Larger and more diverse dataset
- Fine-tuning CLIP for domain-specific tasks
- Deploy as a scalable web application

---

💡 Key Learnings

- Multimodal representation learning
- Embedding-based retrieval systems
- Practical use of pretrained deep learning models

---

👨‍💻 Author

Amit Prakash Singh
B.Tech CSE (AI)

---

⭐ Acknowledgements

- OpenAI CLIP
- Streamlit
