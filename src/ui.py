from colorama import init, Fore, Style
init(autoreset=True)

def print_welcome():
    print(Fore.CYAN + "\n🤖 CodexSanus is awake. What would you like to ask?")
    print(Fore.YELLOW + "(Type 'exit' to close the session)\n")

def print_response(text):
    print(Fore.GREEN + "\n🤖 Agent Response:\n" + Style.RESET_ALL + text)

def print_error(error):
    print(Fore.RED + f"\n⚠️ Error: {error}")