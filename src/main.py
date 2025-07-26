from planner import plan
from executor import generate_response
from memory import  load_memory, add_memory_entry
from ui import print_welcome,print_response,print_error

def main():
    print_welcome()
    memory = load_memory()

    while True:
        try:
            user_input = input("\n🧠 Your question: ").strip()

            if user_input.lower() in ['exit', 'q', 'quit']:
                print("👋 CodexSanus is going into standby mode. See you soon.")
                break

            tasks = plan(user_input)
            # Si quieres, genera respuestas para cada tarea y las unes:
            full_response = ""
            for task in tasks:
                response = generate_response(task)
                full_response += response + "\n\n"

            print_response(full_response.strip())
            memory.append({"input": user_input, "response": full_response})
            add_memory_entry(memory, {"input": user_input, "response": full_response})

        except Exception as e:
            print_error(str(e))

if __name__ == "__main__":
    main()