import json
import sys
import os
from datetime import datetime

filename = 'todo.json'
def load_task(): #checks if a file with such name exists
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return[]
    return []

def save_task(n): # saves to the same file
    with open(filename, 'w') as f:
        json.dump(n, f, indent=4)

def format_task():
    print('The format is: ')
    print('[add] <description> <status>')
    print('[done|delete|in-progress] <task_id>')
    print('[list]')
    print('[search] <description>')
    print('[update] <task_id> <description>')
    sys.exit(1)
    
def return_format(i):
    if i.get('UpdatedAt') == None:
        print(f"{i['id']}: {i['description']} (Status: {i['status']}) [Created at: {i['CreatedAt']}]")
    else:
        print(f"{i['id']}: {i['description']} (Status: {i['status']}) [Created at: {i['CreatedAt']}] [Updated at: {i['UpdatedAt']}]")




def command_add(lst):
    if len(lst) < 3:
        print('a description is needed')
        format_task()
    else:
        if lst[-1].lower() == 'todo' or lst[-1].lower() == 'done'or lst[-1].lower() == 'in-progress':# brute force checks if the last word is correct for the code to run
            desc = ' '.join(lst[2:-1])
            task_status = lst[-1]
        else:
            desc = ' '.join(lst[2:])
            task_status = 'todo'
        task = load_task()
        task_id = len(task) + 1
        task_date = datetime.now().strftime('%d-%m-%Y %H-%M-%S') 
        task.append({'id': task_id, 'description': desc, 'status': task_status, 'CreatedAt': task_date}) #appends to the list
        save_task(task)
        print(f'task added: {desc} (Status: {task_status}) [Created at: {task_date}]')


            
def status_update(lst):
    if len(lst) < 3:
        print("Error: task_id missing")
        format_task()

    try:
        target_id = int(lst[-1])
    except ValueError:
        print('task_id should be a number. Run `python todo.py` for help.')
        sys.exit(1)

                
    task = load_task()    
    if len(task) == 0:
        print('no task found')
                
    elif int(lst[-1]) > len(task):
        print(f'no task found with id {lst[-1]}')

    update_date = datetime.now().strftime('%d-%m-%Y %H-%M-%S')
    for i in task:
        if i['id'] == int(lst[-1]):
            i['status'] = lst[1]
            i.update({'UpdatedAt': update_date})
            return_format(i)

    save_task(task)
    
        

        



        

def delete_status(lst):
    if len(lst) < 3:
        print("Error: task_id missing")
        format_task()

    try:
        target_id = int(lst[-1])
    except ValueError:
        print('task_id should be a number. Run `python todo.py` for help.')
        sys.exit(1)

            
    task = load_task()
    if len(task) == 0:
        print('no task found')
            
    elif int(lst[-1]) > len(task):
        print(f'no task found with id {lst[-1]}')

        
    for i, t in enumerate(task):
        if t['id'] == int(lst[-1]):
            task.pop(i)
            print(f'task {target_id} deleted')
            for i, t in enumerate(task, start=1):
                t['id'] = i       
    save_task(task)




def list_task(lst):
    task = load_task()
    if not task:
        print('the todo list is empty. Run `python todo.py` for help.')
        sys.exit(1)

    if len(lst) > 2:
        status_search = lst[-1].lower()
        for i in task:
            if i['status'].lower() == status_search:
                return_format(i)
            else:
                continue
    else:
        for i in task:
            return_format(i)

                

def search_task(lst):
    if len(lst) < 3:
        print("Error: search description missing")
        format_task()
    task = load_task()
    desc = ' '.join(lst[2:])
    for i in task:
        if desc in i['description']:
            return_format(i)
        else:
            continue

                

def update_task(lst):
    if len(lst) < 3:
        print("Error: task_id missing")
        format_task()
    if len(lst) < 4:
        print('Error: a description is missing')
        format_task()

    try:
        target_id = int(lst[2])
    except ValueError:
        print('task_id should be a number. Run `python todo.py` for help.')
        sys.exit(1)
            
    task = load_task()
    if len(task) == 0:
        print('no task found')
            
    elif int(lst[2]) > len(task):
        print(f'no task found with id {lst[2]}')
            
        
    update_date = datetime.now().strftime('%d-%m-%Y %H-%M-%S')
    desc = ' '.join(lst[3:])
    for i in task:
        if i['id'] == int(lst[2]):
            i['description'] = desc
            i.update({'UpdatedAt': update_date})
            return_format(i)
    save_task(task)
    
        
    


def main():
    lst = sys.argv

    if len(lst) < 2: # checks if the arguements match what is required for the code to run
        format_task()
    if lst[1].lower() == 'add':
        command_add(lst)
    elif lst[1].lower() == 'done' or lst[1] == 'in-progress':
        status_update(lst)
    elif lst[1].lower() == 'delete':
        delete_status(lst)
    elif lst[1].lower() == 'list':
        list_task(lst)
    elif lst[1].lower() == 'search':
        search_task(lst)
    elif lst[1].lower() == 'update':
        update_task(lst)
    else:
        format_task()



if __name__ == '__main__':
    main()

