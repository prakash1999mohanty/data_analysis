# make to do list for user
# 1. add task
# 2.delete task
# 3.display task
# 4.update task
task=[]
def add_task():
    n=int(input('Enter the no. of task:'))
    for i in range (n):
        a=input('enter the task:')
        task.append(a)
    print ("task added successfully")
    print(task)

def del_task():
    #print("tryry")
    prev_task=input('enter the task which want to delete: ')
    if prev_task in task:
        task.remove(prev_task)
        print('task deleted ')
        print(task)
    else:
        print(prev_task)

def dis_task():
    if task==[]:
        print('at first add task')
    else:
        print(task)
    
def update_task():
    old_task=input('the task you want to update:')
    index_old=task.index(old_task)
    new_task=input("enter new task:")
    task[index_old]=new_task
    print('task update successfully')


print('press 1 for add \n press 2 for delete \n press 3 for display \n press 4 for update \n')
while True:
    user_inpt=int(input('enter your choice:'))


    if user_inpt==1:
        add_task()
    elif user_inpt==2:
        del_task()
    elif user_inpt==3:
        dis_task()
    elif user_inpt==4:
        update_task()
    else:
        print('exit')
        break

