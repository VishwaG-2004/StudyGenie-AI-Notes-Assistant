import streamlit as st

from modules.pdf_reader import extract_text_from_pdf
from modules.summarizer import generate_summary
from modules.qa import ask_question
from modules.ocr import extract_text_from_image

st.title("StudyGenie AI Notes Assistant")

st.write("Upload PDF or Image and generate summary")

text_data=""

file=st.file_uploader(
    "Upload file",
    type=["pdf","png","jpg","jpeg"]
)

if file:

    if file.type=="application/pdf":

        with open("temp.pdf","wb") as f:
            f.write(file.read())

        text_data=extract_text_from_pdf("temp.pdf")

    else:

        with open("temp.png","wb") as f:
            f.write(file.read())

        text_data=extract_text_from_image("temp.png")

    st.success("Text extracted")

    if st.button("Generate Summary"):

        summary=generate_summary(text_data)

        st.subheader("Summary")

        st.write(summary)

    question=st.text_input("Ask question from document")

    if question:

        answer=ask_question(question,text_data)

        st.subheader("Answer")

        st.write(answer)