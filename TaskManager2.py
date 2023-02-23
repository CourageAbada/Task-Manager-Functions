import datetime
from datetime import date, datetime


#Only allowing the admin to register new users if the user is not admin then error message will be desplayed
#only allows user to view statistics
def reg_user():
    global username_list
    if username == 'admin':
        with open('user.txt', 'a+') as file:
            print('Please enter the following details to create a new account:')
            
            while True:
                new_username = input('Username: ')
                new_password = input('Password: ')
                if new_username in username_list:
                    print("username exists")

                else:
                    print(f"welcome {new_username}! Please enter your password below")
                    password_confirmation = input('Please confirm your Password: ')

                    if new_password == password_confirmation:
                        print('Well done you have registered sucessfully')
                        file.write(f"\n{new_username}, {new_password}")
                        break
                    else:
                        print('Please enter the correct password:')
                        password_confirmation = input('Please confirm your Password: ')
    else:
        print('Only admin is allowed to register new users ')


#A function If the user inputs a then it will allow them to add a task
def add_task():
        with open('tasks.txt', 'a+') as file:
            print('Please enter the following information about the tasks:')
            task_username = input('The person\'s username: ')
            task_title = input('The task title: ')
            task_description = input('Description of the task: ')
            task_duedate = input('Task Due Date: ')
            current_date = input('Current date: ')
            task_complition = 'No'
            file.write(f"\n{task_username}, {task_title}, {task_description}, {task_duedate}, {current_date}, {task_complition} ")


# A function that If user inputs va then it allows them to view all tasks
def view_all():    
        with open('tasks.txt', 'r+') as file:
            for line in file:
                split_data = line.split(', ')
                peoples_names = f"""Name: {split_data[0]}\nTask: {split_data[1]}\nTask Description: {split_data[2]}\nTask Due Date: {split_data[3]}
                \nCurrent date: {split_data[4]}\nIs the task complete: {split_data[5]}"""
                print(peoples_names)


# A function that If user inputs vm it allows them to only view their tasks
def view_mine():
    tn = 1
    dic_tasks = {}
    with open('tasks.txt', 'r+') as file:
        for line in file:
            dic_tasks[tn] = line.split(", ")
            task_username, task_title, task_description, task_duedate, current_date, task_complition = line.split(", ")
            if username ==  task_username:
                print(f'''tn: {tn}\nName: {task_username}\nTask: {task_title}\nTask Description: {task_description}
                \nTask Due Date: {task_duedate}\nCurrent date: {current_date}\nIs the task complete: {task_complition}''')
            tn += 1
        task_choice = int(input("select either a specific task by entering a number or input ‘-1’ to return to the main menu: "))
        
        if task_choice == -1:
            print("going home")
        else:

            chosen_task = dic_tasks[task_choice]
            task_complition_answer = chosen_task[-1]

            if task_complition_answer == 'Yes\n':
                chosen_task[-1] = chosen_task[-1].replace('No','Yes')
                print(chosen_task)
                print(dic_tasks.values())

    with open("tasks.txt", "w") as file:
        for line in dic_tasks.values():
            file.write(", ".join(line))

#Putting all the code for 'ds' under a function
def display_stats():
    task_num = 0
    user_num = 0
    with open('tasks.txt', 'r') as task_title:
        for line in task_title:
            task_num += 1
    print(f'\nTotal number of task: {task_num}')

    with open('user.txt', 'r') as username:
        for line in username:
            user_num +=1
    print(f'Total number of users: {user_num}\n')

#Function that if user puts in 'gr' it will generate the reports of all the users and tasks linked to them
def generate_reports():
    with open('task_overview.txt',"w") as task_track:
        task_num = 0
        task_complete = 0
        task_incomplete = 0
        overdue_task = 0
        current_date = datetime.today()
        with open('tasks.txt', 'r') as task_title:
            for line in task_title:
                task_num += 1
                line = line.split(', ')
                if line[-1] == 'Yes\n':
                    task_complete +=1
                elif line[-1] == 'No\n':
                    task_incomplete += 1
                    overdue_task += 1
                today = date.today()
                new_given_date = today.strftime('%d %b %Y')
                percentage_incomplete =  (task_incomplete/(task_complete + task_incomplete))*100
        print(f'''Total number of task: {task_num}\n
The total of complete task: {task_complete}\n
The total of uncomplete tasks are: {task_incomplete}\n
The total of overdue tasks are: {overdue_task}\n
The Percentage of tasks incomplete: {percentage_incomplete}%''')

        task_track.write(f'''Total number of task: {task_num}
The total of complete task: {task_complete}
The total of uncomplete tasks are: {task_incomplete}
The total of overdue tasks are: {overdue_task}
The Percentage of tasks incomplete: {percentage_incomplete}%''')

    with open('user_overview.txt',"w") as user_track:
        with open('user.txt', 'r') as usernames:
            username_content = usernames.readlines()
            output = f"The total number of users is {len(username_content)}\n"
            with open("tasks.txt", "r") as tasks_file:
                tasks_list = tasks_file.readlines()
                
                for line in username_content: #r = admin
                    
                    line = line.replace("/n", "").split(", ")
                    user = line[0]
                    current_date = datetime.today
                    user_task_count = 0
                    percetange_task_complete = 0
                    percentage_task_incomplete = 0
                    task_complete = 0
                    task_incomplete = 0
                    percentage_overdue = 0
                    for task in tasks_list:
                        task = task.split(", ")
                        task_user = task[0]

                        if user == task_user:
                            user_task_count += 1


                            if task [-1].strip('\n').lower() == 'yes':
                                task_complete +=1 
                            else:
                                task_incomplete +=1
                            #count the task that are overdue
                    
                    task_assigned_percentage = user_task_count/ len(tasks_list) * 100
                    percetange_task_complete = (task_complete / user_task_count) * 100
                    percentage_task_incomplete = (task_incomplete/ user_task_count) * 100
                    percentage_overdue = (task_incomplete/ user_task_count) * 100
                    output += f'''{user}\ntotal task is: {user_task_count}
The total percentage assigned to user: {round(task_assigned_percentage, 2)}%
The total number of completed task is: {task_complete}.
The percentage of task that are completed: {percetange_task_complete}%
The percentage of task that are incompleted: {percentage_task_incomplete}%
The percentage of task that are overdue: {percentage_overdue}%
'''
            print(output)
            user_track.write(output)
    return output

#Login section asking the user to login and checking to see if the username and password match the stored username and passwords that are in user.txt
#If Password does not match then user should try again
with open('user.txt', 'r') as file:
    username_password = file.readlines()
    username_list = []
    while True:
        logged_in = False
        print('Please enter the following details:')
        username = input('Username:')
        password = input('Password:')
        for i in username_password:
            split_data = i.strip().split(", ")
            cor_user = split_data[0].strip("\n")
            username_list.append(cor_user)
            cor_pass = split_data[1].strip("\n")
            if password == cor_pass and username == cor_user:
                logged_in = True
                break
            elif password != cor_pass and cor_user != username:
                continue
            else:
                print('User does not exist please enter the correct username and Password')
        if logged_in:
            print("Logged in")
            break


while True:

    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - generate reports
d - display statistics
e - Exit
: ''').lower()
# Calling all the funcions
    if menu == 'r':
        reg_user()

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine()

    elif menu == 'd' and username == 'admin':
        display_stats()

    elif menu == 'gr':
        generate_reports()

#Allows user to leave once done
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    
# Asks user to reenter their choice if they have selected the wrong option
    else:
        print("You have made a wrong choice, Please Try again")
