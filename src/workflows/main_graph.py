"""
This file simulates a LangGraph-style state workflow.
Each task is delegated to an agent in sequence.
"""

from src.agents.email_agent import summarize_email
from src.agents.resume_agent import review_resume
from src.agents.video_agent import interpret_video_transcript
from src.agents.dataset_agent import generate_dataset

def run_workflow(choice):
    if choice == "1":
        email = input("\nEnter email text:\n")
        print("\n--- Summary ---")
        print(summarize_email(email))

    elif choice == "2":
        resume = input("\nPaste resume text:\n")
        print("\n--- Resume Review ---")
        print(review_resume(resume))

    elif choice == "3":
        transcript = input("\nPaste video transcript:\n")
        print("\n--- Video Interpretation ---")
        print(interpret_video_transcript(transcript))

    elif choice == "4":
        topic = input("\nTopic for dataset: ")
        rows = int(input("Number of rows: "))
        print("\n--- Generated Dataset ---")
        print(generate_dataset(topic, rows))

    elif choice == "5":
        print("\nRunning Multi-Agent Workflow:")
        print("\nStep 1: Email Summary")
        print(summarize_email("Meeting tomorrow regarding Q4 financial strategy."))

        print("\nStep 2: Resume Review")
        print(review_resume("Experienced software engineer with Python and AI experience."))

        print("\nStep 3: Video Understanding")
        print(interpret_video_transcript("Today we explore AI safety and LLM alignment."))

        print("\nStep 4: Dataset Generation")
        print(generate_dataset("AI startups", 5))

    else:
        print("Invalid choice.")
