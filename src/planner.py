def plan(user_input):
    """
    Divide la tarea en subtareas simples para mejorar la generación.
    Por ejemplo, si la pregunta es compleja, la divide en partes:
    1. Explicación breve
    2. Ejemplo práctico
    3. Posibles aplicaciones
    """
    tasks = []
    tasks.append(f"Explain briefly: {user_input}")
    tasks.append(f"Give a practical example related to: {user_input}")
    tasks.append(f"Describe possible applications or use cases of: {user_input}")
    return tasks
