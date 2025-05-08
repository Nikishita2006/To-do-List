#To-do
task=[]
def menu():
    print("\n To-do List")
    print("1.To add a task")
    print("2.To view all your tasks")
    print("3.To edit the given task")
    print("4.To delete the given task")
    print("5.To mark a successfully completed task")
    print("6.To Exit")
    r=input("Enter your preferred choice from(1-5):")
    if(r=="1"):
        add()
    elif(r=="2"):
        view()
    elif(r=="3"):
        edit()
    elif(r=="4"):
        delete()
    elif(r=="5"):
        mark()
    else:
        exit_app()

def add():
    while True:
        r=input("Enter your task(one at a time):")
        print("Your task is successfully recorded")
        c={"Task":r,"Status":"Pending"}
        task.append(c)
        z=input("Do you want to enter your next task:(yes/no)").lower()
        if(z!="yes"):
            break
        
def view():
    if not task:
        print("No tasks added yet")
    else:
        print("\n Tasks and their Status")
        for t in task:
            print(t["Task"],"-",t["Status"])
def edit():
    while True:
        view()
        found=False
        x=input("Enter the task you want to edit:")
        for t in task:
            if(t["Task"]==x):
                w=input("Enter the new task:")
                t["Task"]=w
                found=True
                print("Task successfully edited")
                break
        if not found:
            print("Task not found,Try again!")
            continue
        l=input("Do you want to edit any other task?(yes/no):").lower()
        if(l!="yes"):
            break
def delete():
    while True:
        view()
        found=False
        p=input("Enter the task you want to delete:")
        for t in task:
            if(t["Task"]==p):
                task.remove(t)
                print("Task is successfully deleted")
                found=True
        if not found:
            print("Task not found,Try again")
            continue
        g=input("Do you want to delete any other task?(yes/no):").lower()
        if(g!="yes"):
            break
def mark():
    while True:
        view()
        found=False
        s=input("Enter your completed task:")
        for t in task:
            if(t["Task"]==s):
                t["Status"]="Done"
                print("Task- {} is marked as done".format(s))
                found=True
                break
        if not found:
            print("Task not found,Try again!")
            continue
        b=input("Do you want to mark any other task?(yes/no):").lower()
        if(b!="yes"):
            break
def exit_app():
    print("All your tasks are successfully saved")
    exit()
while True:
    menu()
            
        
           
    
    
        
