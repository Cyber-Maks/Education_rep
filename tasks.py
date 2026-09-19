_tasks = []

def add_task(name):
    _tasks.append(name)

def list_tasks():
    for t in _tasks:
        print(t)
