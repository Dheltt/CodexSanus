CodexSanus — Agentic AI Application
📌 What is this project?


CodexSanus is an AI agent prototype built in Python that:

Receives user input (queries or commands)

Plans and breaks down tasks into subtasks using a modular planner

Executes subtasks via tool calls and internal logic

Maintains memory of past interactions for contextual awareness

Provides final summarized output to the user

This project demonstrates a simple yet extensible architecture for agentic AI workflows with clear separation between planning, execution, memory, and UI layers.

🚀 How to run
Make sure you have Python 3.x installed.

Activate your virtual environment (optional but recommended):


source venv/Scripts/activate  # Windows PowerShell: venv\Scripts\Activate.ps1
Install dependencies (if any):


pip install -r requirements.txt
Run the main app:


python src/main.py
📦 Requirements
Python 3.x

No external libraries beyond those in requirements.txt (currently minimal dependencies)

💡 Example usage
plaintext
🧠 Enter your query: What is AI?

CodexSanus is planning your query...
🧩 Task 1: Define AI
🧩 Task 2: List common applications

✅ AI stands for Artificial Intelligence...
✅ Common applications include natural language processing, computer vision...

📬 Final response:
Artificial Intelligence refers to the simulation of human intelligence by machines...
It is widely used in various fields such as NLP, image recognition, and robotics.
🛠 Project structure
src/ — Source code modules (planner, executor, memory, UI, logger)

🧑‍🔧 Author & credits
Developed by David Fuerte Ramirez

Inspired by agentic AI frameworks and modular design principles, this project is an educational prototype illustrating key AI agent concepts: planning, tool integration, and memory management.