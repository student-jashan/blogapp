import streamlit as st
import requests
import os

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

st.title("📝 Blog App")

menu = st.sidebar.selectbox(
    "Menu",
    ["Create Post", "Get Post", "Update Post", "Delete Post"]
)

# ---------------- CREATE ----------------
if menu == "Create Post":
    st.header("Create Post")

    title = st.text_input("Title")
    content = st.text_area("Content")

    if st.button("Create"):
        data = {"title": title, "content": content}

        res = requests.post(f"{API_URL}/posts/", json=data)

        if res.status_code == 201:
            st.success("Post created")
            st.json(res.json())
        else:
            st.error(res.text)

# ---------------- GET ----------------
elif menu == "Get Post":
    st.header("Get Post")

    post_id = st.number_input("Post ID", min_value=1)

    if st.button("Fetch"):
        res = requests.get(f"{API_URL}/posts/{post_id}")

        if res.status_code == 200:
            st.json(res.json())
        else:
            st.error("Not found")

# ---------------- UPDATE ----------------
elif menu == "Update Post":
    st.header("Update Post")

    post_id = st.number_input("Post ID", min_value=1)
    title = st.text_input("New Title")
    content = st.text_area("New Content")

    if st.button("Update"):
        data = {"title": title, "content": content}

        res = requests.put(f"{API_URL}/posts/{post_id}", json=data)

        if res.status_code == 200:
            st.success("Updated")
            st.json(res.json())
        else:
            st.error(res.text)

# ---------------- DELETE ----------------
elif menu == "Delete Post":
    st.header("Delete Post")

    post_id = st.number_input("Post ID", min_value=1)

    if st.button("Delete"):
        res = requests.delete(f"{API_URL}/posts/{post_id}")

        if res.status_code == 200:
            st.success("Deleted")
        else:
            st.error(res.text)