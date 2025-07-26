# Technical Explanation

## 1. Agent Workflow

Our agent processes user input in the following steps:

1. **Receive user input:** The CLI prompts the user to enter a question or command.
2. **Retrieve relevant memory (optional):** Previously stored conversations or responses are loaded from a local JSON file to maintain context.
3. **Plan sub-tasks:** The Planner module breaks the user input into simpler subtasks. Currently, this is a simple wrapper that prefixes the input with "Explain briefly:" to guide the model.
4. **Call tools or APIs:** The Executor module sends each planned subtask prompt to the Google Gemini API (via the `google.generativeai` SDK) to generate a text response.
5. **Summarize and return final output:** The responses for all subtasks are concatenated and displayed to the user. The conversation is then appended to memory for future context.

## 2. Key Modules

- **Planner (`planner.py`):**  
  Converts complex user input into simplified subtasks by prepending a prompt. This is a straightforward placeholder for future advanced planning (e.g., ReAct, BabyAGI).

- **Executor (`executor.py`):**  
  Handles API calls to Google Gemini, selecting the preferred model dynamically and sending prompt(s) for text generation. Returns clean text output.

- **Memory Store (`memory.py`):**  
  Implements persistent memory by saving conversation logs in a JSON file (`memory.json`). Supports loading existing memory at startup and appending new entries after each interaction.

- **UI (`ui.py`):**  
  Manages user interaction in the command line, printing welcome messages, responses, and errors with simple formatting.

- **Logger (`logger.py`):**  
  Captures runtime information and errors, saving logs to file for observability.

## 3. Tool Integration

- **Google Gemini API:**  
  Integrated via the `google.generativeai` Python SDK.  
  The Executor module chooses the best available Gemini model with content generation capability and sends prompts for response generation.

## 4. Observability & Testing

- **Logging:**  
  All key events (user input, agent response, errors) are logged with timestamps in a dedicated `logs/` directory via the Logger module.

- **Testing:**  
  While no formal automated tests are included, manual testing covers the full main loop (user input → planning → execution → output → memory persistence).

## 5. Known Limitations

- **Basic planning logic:**  
  The Planner currently just prefixes the input and does not truly decompose tasks or reason multi-step.

- **Latency on API calls:**  
  Each prompt waits synchronously for Google Gemini responses, which can cause delay if the API is slow or rate-limited.

- **Limited memory capabilities:**  
  Memory is simply appended and loaded from a JSON file without vector similarity or advanced retrieval, so context relevance can degrade with longer sessions.

- **Error handling:**  
  Basic try-except in main loop, but no retry logic or fallback mechanisms for failed API calls.

---