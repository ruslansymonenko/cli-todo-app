from pathlib import Path
import json

todos_folder = Path("todos")
todos_folder.mkdir(parents=True, exist_ok=True)
file_path = todos_folder / "todos.json"

def load_file():
    if file_path.exists():
        with file_path.open("r", encoding="utf-8") as f:
            return json.load(f)
    
    return []

def write_file(data):
    with file_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print("Data saved to:", file_path)

def display_todos(data):
    if not data:
        print("Todos list is empty")
        return
    
    print("\n Current todos:")

    for i, todo in enumerate(data, 1):
        status = "✅" if todo["done"] else "❌"
        print(f"{i}. {status} {todo['task']}")
    print()

def toggle_task_status(data, command):
    parts = command.split()
    if len(parts) != 2 or not parts[1].isdigit():
        print("❗ Use format: done 2")
        return

    index = int(parts[1]) - 1

    if not (0 <= index < len(data)):
        print("❗ Uncorrect task number.")
        return

    data[index]["done"] = not data[index]["done"]
    status = "done" if data[index]["done"] else "not done"

    print(f"Task '{data[index]['task']}' отмечена как {status}.")
    display_todos(data)

def delete_task(data, command):
    parts = command.split()
    if len(parts) != 2 or not parts[1].isdigit():
        print("❗ Use format: del 2")
        return

    index = int(parts[1]) - 1

    if not (0 <= index < len(data)):
        print("❗ Incorrect task number.")
        return
    
    removed = data.pop(index)
    print(f"🗑 Task '{removed['task']}' was deleted.")
    display_todos(data)

def main():
    data = load_file()
    display_todos(data)

    print("Enter new todos. For exit write 'exit' and press Enter")

    try:
        while True:
            line = input("> ")
            if line.lower() == "exit":
                break

            if line.startswith("done"):
                toggle_task_status(data, line)
                continue

            if line.startswith("del"):
                delete_task(data, line)
                continue

            todo = {"task": line, "done": False}
            data.append(todo)
            write_file(data=data)
            display_todos(data)

    except KeyboardInterrupt:
        print("\nExit with Ctrl+C")
    

if __name__ == "__main__":
    main()