import os
import torch
from model import get_image_embedding, get_text_embedding
from utils import cosine_similarity
import streamlit as st
from PIL import Image

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="NeuroSearch", layout="wide")

# -----------------------------
# 🔥 UI STYLE
# -----------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}
.title {
    text-align: center;
    font-size: 60px;
    font-weight: 800;
    background: linear-gradient(90deg, #00dbde, #fc00ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.subtitle {
    text-align: center;
    color: #cccccc;
    margin-bottom: 30px;
}
.glass {
    background: rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    padding: 15px;
    backdrop-filter: blur(10px);
}
.stButton>button {
    width: 100%;
    border-radius: 12px;
    height: 50px;
    font-weight: bold;
    background: linear-gradient(90deg, #00dbde, #fc00ff);
    color: white;
    border: none;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.markdown('<div class="title">NeuroSearch</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Multimodal AI Search Engine</div>', unsafe_allow_html=True)

# -----------------------------
# CONFIG
# -----------------------------
IMAGE_FOLDER = "images"
valid_extensions = (".jpg", ".jpeg", ".png")

image_files = [
    f for f in os.listdir(IMAGE_FOLDER)
    if f.lower().endswith(valid_extensions)
]

# -----------------------------
# LOAD EMBEDDINGS
# -----------------------------
@st.cache_resource
def load_embeddings():
    embeddings = {}
    for img in image_files:
        path = os.path.join(IMAGE_FOLDER, img)
        embeddings[img] = get_image_embedding(path)
    return embeddings

image_embeddings = load_embeddings()

# -----------------------------
# 🔥 TOP-K FUNCTION (CORE)
# -----------------------------
def get_top_k(query_embedding, image_embeddings, k=6):
    similarities = []
    image_names = []

    for img, emb in image_embeddings.items():
        sim = cosine_similarity(query_embedding, emb)
        similarities.append(sim)
        image_names.append(img)

    similarities = torch.tensor(similarities)

    topk_values, topk_indices = torch.topk(similarities, k)

    results = []
    for i in range(k):
        img_name = image_names[topk_indices[i]]
        score = topk_values[i].item()
        results.append((img_name, score))

    return results

# -----------------------------
# INPUT UI
# -----------------------------
col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.markdown('<div class="glass">', unsafe_allow_html=True)

    query = st.text_input("🔍 Describe what you want...", key="query")
    uploaded_file = st.file_uploader("📤 Upload image", type=["jpg","jpeg","png"])

    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# MODE
# -----------------------------
col1, col2, col3 = st.columns(3)

if "mode" not in st.session_state:
    st.session_state.mode = "Text"

if col1.button("🔤 Text"):
    st.session_state.mode = "Text"
if col2.button("🖼️ Image"):
    st.session_state.mode = "Image"
if col3.button("🔥 Combined"):
    st.session_state.mode = "Combined"

mode = st.session_state.mode
st.markdown(f"### 🔎 Mode: {mode}")

# -----------------------------
# TOP-K SLIDER
# -----------------------------
k = st.slider("Number of results (Top-K)", 3, 12, 6)

# -----------------------------
# DISPLAY RESULTS
# -----------------------------
def display_results(scores):
    cols = st.columns(3)

    for i, (img, score) in enumerate(scores):
        with cols[i % 3]:
            st.markdown('<div class="glass">', unsafe_allow_html=True)

            st.image(
                os.path.join(IMAGE_FOLDER, img),
                width=240
            )

            st.markdown(f"**Score:** {score:.2f}")

            st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# TEXT SEARCH
# -----------------------------
if mode == "Text" and query:

    with st.spinner("🔍 AI is searching..."):
        query_embedding = get_text_embedding(f"a photo of a {query}")
        scores = get_top_k(query_embedding, image_embeddings, k)

    display_results(scores)

# -----------------------------
# IMAGE SEARCH
# -----------------------------
elif mode == "Image" and uploaded_file is not None:

    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", width=300)

    with st.spinner("🔍 AI is searching..."):
        temp_path = "temp.jpg"
        image.save(temp_path)

        query_embedding = get_image_embedding(temp_path)
        scores = get_top_k(query_embedding, image_embeddings, k)

    display_results(scores)

# -----------------------------
# COMBINED SEARCH
# -----------------------------
elif mode == "Combined" and uploaded_file is not None and query:

    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", width=300)

    with st.spinner("🔍 AI is searching..."):
        temp_path = "temp.jpg"
        image.save(temp_path)

        image_embedding = get_image_embedding(temp_path)
        text_embedding = get_text_embedding(f"a photo of {query}")

        combined_embedding = torch.mean(
            torch.stack([image_embedding, text_embedding]),
            dim=0
        )

        scores = get_top_k(combined_embedding, image_embeddings, k)


    display_results(scores)

