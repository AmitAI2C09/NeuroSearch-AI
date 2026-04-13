# 🔍 NeuroSearch: Multimodal AI Search Engine

NeuroSearch is an AI-powered multimodal image retrieval system that enables users to search images using text, image, or a combination of both. The system leverages the CLIP (Contrastive Language–Image Pretraining) model to map images and text into a shared embedding space, allowing cross-modal search and semantic understanding.

Unlike traditional keyword-based search systems, NeuroSearch understands the meaning behind queries and retrieves the most relevant images using similarity-based ranking.

This project supports three types of search:
- Text to Image Search: Users can enter natural language queries to retrieve relevant images.
- Image to Image Search: Users can upload an image to find visually similar images.
- Combined Search: Users can refine search results using both text and image inputs together.

The system works by converting both queries and dataset images into embeddings using CLIP. These embeddings are then compared using cosine similarity, and the most similar results are ranked and displayed.

The overall pipeline follows:
Input (Text/Image) → CLIP Embedding → Similarity Calculation → Ranking → Output Results

Tech stack used in this project includes Python, PyTorch, OpenAI CLIP, Streamlit, and NumPy. The UI is built using Streamlit with custom styling to provide a modern and visually appealing interface.

Project structure:
- app.py: Main application with UI and search logic
- model.py: Handles CLIP model loading and embedding generation
- utils.py: Contains similarity calculation functions
- requirements.txt: Project dependencies
- images/: Dataset used for retrieval

To run the project locally:
1. Clone the repository:
   git clone https://github.com/AmitAI2C09/NeuroSearch-AI.git
2. Navigate to the folder:
   cd NeuroSearch-AI
3. Install dependencies:
   pip install -r requirements.txt
4. Run the application:
   streamlit run app.py

Future improvements include improving retrieval accuracy, integrating FAISS for faster similarity search, deploying the application online, and expanding the dataset for better performance.

Author:
Amit Prakash Singh  
B.Tech Computer Science (AI)

Acknowledgements:
This project uses the CLIP model developed by OpenAI and the Streamlit framework for building the user interface.
