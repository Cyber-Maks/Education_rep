_tasks = []

def add_task(name):
    _tasks.append(name)

def list_tasks():
    for t in _tasks:
        print(t)

def remove_task(name):
    if name in _tasks:
        _tasks.remove(name)
