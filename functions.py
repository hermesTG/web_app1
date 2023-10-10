FILEPATH='todos.txt'

def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local=file_local.readlines()
    return todos_local


def write_to_file(local_todos):
    with open('todos.txt', 'w') as file:
        file.writelines(local_todos)


if __name__=="__main__":
    print(get_todos())