from modules.pdf_reader import extract_text_from_pdf
from modules.summarizer import generate_summary
from modules.qa import ask_question
from modules.ocr import extract_text_from_image

def menu():

    print("\n===== StudyGenie AI =====")

    print("1 Extract PDF text")
    print("2 Extract Image text")
    print("3 Generate Summary")
    print("4 Ask Questions")
    print("5 Exit")

text_data=""

while True:

    menu()

    choice=input("Enter choice:")

    if choice=="1":

        file=input("Enter PDF path:")

        text_data=extract_text_from_pdf(file)

        print("Text extracted")

    elif choice=="2":

        file=input("Enter image path:")

        text_data=extract_text_from_image(file)

        print("Text extracted")

    elif choice=="3":

        if text_data=="":

            print("Load file first")

        else:

            summary=generate_summary(text_data)

            print("\nSummary:\n")

            print(summary)

    elif choice=="4":

        if text_data=="":

            print("Load file first")

        else:

            question=input("Ask question:")

            answer=ask_question(question,text_data)

            print("Answer:",answer)

    elif choice=="5":

        break

    else:

        print("Invalid choice")