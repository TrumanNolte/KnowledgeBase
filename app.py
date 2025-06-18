import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Life Log", layout="centered")

st.title("🧠 Life Learning Log")

entry = st.text_area("What did you learn or realize today?", height=150)
tag = st.text_input("Optional tag/category")

if st.button("Log this"):
    if entry.strip() != "":
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = f"{timestamp} | {tag if tag else 'untagged'} | {entry.strip()}\n"

        with open("log.txt", "a") as f:
            f.write(log_line)

        st.success("✅ Logged!")
    else:
        st.warning("Please write something before saving.")

if st.checkbox("Show previous logs"):
    try:
        with open("log.txt", "r") as f:
            logs = f.readlines()
            logs = reversed(logs[-10:])
            for log in logs:
                st.markdown(f"> {log}")
    except FileNotFoundError:
        st.info("No logs yet!")