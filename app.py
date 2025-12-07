#  FILE 4 — `app.py`
```python
from src.workflows.main_graph import run_workflow

def main():
    print("\n=== AutoAI Personal Assistant ===")
    print("Choose a task:")
    print("1. Summarize Email")
    print("2. Review Resume")
    print("3. Interpret Video Transcript")
    print("4. Generate Dataset")
    print("5. Run Multi-Agent Workflow")

    choice = input("\nEnter choice: ").strip()

    run_workflow(choice)

if __name__ == "__main__":
    main()
