_tasks = []

def add_task(name):
    _tasks.append(name)
    print(f"[INFO] Задачка добавлена: {name}")

def list_tasks():
    for t in _tasks:
        print(t)

def remove_task(name):
    if name in _tasks:
        _tasks.remove(name)
