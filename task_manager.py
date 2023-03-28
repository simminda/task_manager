''' 
A Task Manager program to keep track of all duties per assigned individual within an organisation.
Features provided:
- user authentication/Login
- task management
- viewing of tasks and filtering by user
- user/task reports and statistics
'''

from datetime import datetime
import os
from getpass import getpass

# Defining constants
TOP_LINE = "\n----------------------------------------------------"
BOTTOM_LINE = "----------------------------------------------------"


def reg_user():        
        username = "admin"
        new_user = False
        admin_pass_check = False
        new_user_pass_check = False

        # Confirm admin password to prevent accidental access by lower user
        while admin_pass_check is False:        
            password = input("\nPlease confirm admin password: ")
            with open("user.txt", "r") as f:                
                for line in f:
                    if  username in line and password in line:
                        admin_pass_check = True 
        
        # Capture new user avoiding repeat user name
        while new_user is False:                
            with open("user.txt", "r+") as f:
                username = input("\nPlease enter username for new user: ").lower()
                for line in f:
                    column = line.split(",")
                    if username in column[0]:
                        print(TOP_LINE)
                        print("✘ Username already exists. Please try again")
                        print(BOTTOM_LINE)
                    else:
                        new_user = True
                        print(TOP_LINE)
                        print(f"New username is: {username}")
                        print(BOTTOM_LINE)
                        f.write("\n"+username+", ")
        
        # Capture password for new user and ensure confirmation via double entry
        while new_user_pass_check is False:     
            with open("user.txt", "a") as f:
                pass1 = ""
                pass2 = " "
                while pass1 != pass2:
                    pass1 = input("\nPlease create a password: ")
                    pass2 = input("Please re-enter password: ") 
                    if pass1 == pass2:
                        new_user_pass_check = True
                        f.write(pass1)
                        print(TOP_LINE)
                        print("✦ Successfully registered!")
                        print(BOTTOM_LINE)
                    else:
                        print(TOP_LINE)
                        print("✘ Passwords do not match")  
                        print(BOTTOM_LINE)


def add_task():        
    print("\n\n* Add Task *")
    username = input("\nEnter user to assign to task: ").lower()
    task = input("Enter title of task: ").lower()
    task_desc = input("Enter task description: ")
    start_date = input("Enter start date for task e.g. '1 Jan 2000': ")
    due_date = input("Enter due date for task e.g. '1 Jan 2000': ")
    completion = input("Is the task completed yet? ").lower()
        
    with open("tasks.txt", "a") as f:
            f.write("\n" + username + ", " + task + ", " + task_desc + ", " 
                    + start_date + ", " + due_date + ", " + completion)
    
    print(TOP_LINE)
    print("✦ Thank You. Task has been added")   
    print(BOTTOM_LINE) 


def view_all():
        print("\033[1;32m",TOP_LINE)        
        print(" ALL TASKS ")
        print(BOTTOM_LINE) 
        with open("tasks.txt", "r") as f:
            for line in f:
                column = line.split(", ")
                print(f"\nUser\t\t\t: {column[0]}")
                print(f"Task\t\t\t: {column[1]}")
                print(f"Task Description\t: {column[2]}")
                print(f"Start Date\t\t: {column[3]}")
                print(f"Due Date\t\t: {column[4]}")
                print(f"Completed?\t\t: {column[5]}")
        print("\033[0m")


def main_menu():             
    '''
    Present appropriate Home Screen based on the user and take user selection
    '''
    if username == 'admin':
        print("       \033[1;32m  ╔═══════════════════════════╗ ")
        print("═════════   WELCOME TO TASK MANAGER   ═════════")
        print("         ╚═══════════════════════════╝ ")
        print("\nPlease select one of the following options:")
        print("r - register user")
        print("a - add task")
        print("va - view all tasks")
        print("vm - view my tasks")
        print("gr - generate reports")
        print("s - display statistics")
        print("e - exit\n\033[0m")
    else:
        print("       \033[1;32m  ╔═══════════════════════════╗ ")
        print("═════════   WELCOME TO TASK MANAGER   ═════════")
        print("         ╚═══════════════════════════╝ ")
        print("\nPlease select one of the following options:")
        print("a - add task")
        print("va - view all tasks")
        print("vm - view my tasks")
        print("e - exit\n\033[0m")
    
    # Request user input and call on appropriate function
    selection_validation = False

    while selection_validation is False:
        selection = input("Enter selection here: ").lower()
        if selection == "r":   
            selection_validation = True
            reg_user()
        elif selection == "a":      
            selection_validation = True
            add_task()
        elif selection == "va":     
            selection_validation = True
            view_all()
        elif selection == "vm":     
            selection_validation = True
            view_mine()
        elif selection == "s":      
            selection_validation = True
            view_statistics()
        elif selection == "gr":      
            selection_validation = True
            generate_reports()
        elif selection == "e":      
            selection_validation = True
            exit()
        else:                       
            print("\nInvalid Selection. Please try again.\n")


def view_mine():             
    '''
    views user specific tasks
    '''
    while True:     # looping through function so program doesn't close after every task edit
        print("\033[1;32m",TOP_LINE)
        print(f"* Tasks for {username} * ")
        print(BOTTOM_LINE) 
        with open ("tasks.txt", "r") as f:
            index = 0
            for line in f:
                line = line.strip("\n")
                column = line.split(", ")
                if username == column[0]:
                    index+= 1
                    print(f"Task Number\t\t: {column[6]}")
                    print(f"Task Description\t: {column[2]}")
                    print(f"Start Date\t\t: {column[3]}")
                    print(f"Due Date\t\t: {column[4]}")
                    print(f"Completed?\t\t: {column[5]}")
                    print("") 
            print("\033[0m")
            if index == 0:
                print("\u001b[31m✘ No active tasks found\n\033[0m")
                exit()
            elif index != 0:
                task_to_edit = int(input("Enter a task number to edit or '-1' to return to main menu: "))

                if task_to_edit == -1:
                    print(TOP_LINE)
                    print("Thank You")
                    print(BOTTOM_LINE)
                    main_menu() 
                    break;                   

        # read lines in file. edit the line with the task number entered
        f = open("tasks.txt","r")
        list_of_lines = f.readlines()
        print("\033[1;32m\nWhat would you like to do? ")
        print("a - mark as complete")
        print("b - mark as incomplete")
        print("c - edit task details\n\033[0m")
        
        selection_validation = False

        while selection_validation is False:
            selection = input("\nEnter Selection: ").lower()
            if selection == 'a':
                selection_validation = True
                line_to_edit = list_of_lines[task_to_edit-1]                # Isolate line to edit
                list_line_to_edit = line_to_edit.strip("\n").split(", ")    # Isolate words in line to edit
                list_line_to_edit[5] = "yes"                                # Isolate and edit the 6th word in line to edit
                line_to_edit = str(list_line_to_edit)                       # Go back to line to edit 
                line_to_edit = line_to_edit.replace("'", "").strip("[").strip("]")     # Remove excess characters to match read to write format
                list_of_lines[task_to_edit-1] = line_to_edit + "\n"         # Update the list of lines with edited line
                f = open("tasks.txt","w")                                   # Write lines back to file (with updated line)
                f.writelines(list_of_lines)
                f.close()
                print(TOP_LINE)
                print("✦ Thank you. Task has been marked as complete.")
                print(BOTTOM_LINE)
            elif selection == 'b':
                selection_validation = True
                line_to_edit = list_of_lines[task_to_edit-1]                
                list_line_to_edit = line_to_edit.strip("\n").split(", ")    
                list_line_to_edit[5] = "no"                                 
                line_to_edit = str(list_line_to_edit)                       
                line_to_edit = line_to_edit.replace("'", "").strip("[").strip("]")     
                list_of_lines[task_to_edit-1] = line_to_edit + "\n"         
                f = open("tasks.txt","w")                                   
                f.writelines(list_of_lines)
                f.close()
                print(TOP_LINE)
                print("✦ Thank you. Task has been marked as incomplete.")
                print(BOTTOM_LINE)
            elif selection == 'c':
                selection_validation = True
                line_to_edit = list_of_lines[task_to_edit-1]                
                list_line_to_edit = line_to_edit.strip("\n").split(", ")    
                if list_line_to_edit[5] == "yes":
                    print(TOP_LINE)
                    print("✘ Sorry, this task has been marked as complete and cannot be edited")
                    print(BOTTOM_LINE)
                    main_menu()
                    break
                elif list_line_to_edit[5] == "no":
                    print("\nEdit task\n")
                    list_line_to_edit[0] = input("Confirm user to assign to task: ").lower()
                    list_line_to_edit[4] = input("Confirm Due Date: ")
                    line_to_edit = str(list_line_to_edit)                       
                    line_to_edit = line_to_edit.replace("'", "").strip("[").strip("]")     
                    list_of_lines[task_to_edit-1] = line_to_edit + "\n"         
                    f = open("tasks.txt","w")                                  
                    f.writelines(list_of_lines)
                    f.close()
                    print(TOP_LINE)
                    print("✦ Thank you. Task has been updated. ")
                    print(BOTTOM_LINE)            


def view_statistics():
    # Request password to prevent accidental access by lower user who knows "s" shortcut
    pass_check = False                      
    while pass_check is False:
        password = input("\nPlease confirm admin password: ")
        with open("user.txt", "r") as f:                
            for line in f:
                if username in line and password in line:
                    pass_check = True  

    # Check if files exist. If not, call method to generate them.
    isTask = os.path.isfile("task_overview.txt")    
    isUser = os.path.isfile("user_overview.txt")
    if isTask == False or isUser == False:
        generate_reports()

    print("\033[1;32m",TOP_LINE)    
    print(" STATISTICS ")
    print(BOTTOM_LINE)
    print("\033[0mTasks Overview\n\033[1;32m")
    with open("task_overview.txt", "r") as f:
        contents = ""
        for line in f:
            contents =contents + line
        print(contents)

    print("\033[0m\nUser Overview\n\033[1;32m")
    with open("user_overview.txt", "r") as f:
        contents = ""
        for line in f:
            contents =contents + line
        print(contents)
    
    print("\033[0m")    


def generate_reports():
    pass_check = False                     
    while pass_check is False:
        password = input("\nPlease confirm admin password: ")
        with open("user.txt", "r") as f:                
            for line in f:
                if username in line and password in line:
                    pass_check = True 

    # This part of the code handles task overview
    with open ("tasks.txt", "r") as f:
        line_count = 0
        yes_count = 0
        no_count = 0
        overdue_count = 0
        for line in f:
            if line != "\n":        
                line_count +=1                                  # Determine number of lines/tasks
            line_list = line.split(", ")
            d1 = datetime.strptime(line_list[4], '%d %B %Y')    # Determine dates
            d2 = datetime.today()
            if d2 > d1 and line_list[5] == "no":
                overdue_count +=1
            if line_list[5] == "yes":                           # Determine number of completed
                yes_count += 1
            if line_list[5] == "no":                            # Determine number of incomplete
                no_count +=1

            with open ("task_overview.txt","w") as f:
                f.write(f"Task Count\t\t= {line_count}")
                f.write(f"\nCompleted Tasks\t\t= {yes_count}")
                f.write(f"\nIncomplete Tasks\t= {no_count}")
                f.write(f"\nOverdue Tasks\t\t= {overdue_count}")
                f.write(f"\nIncomplete Ratio\t= {(no_count/line_count)*100}%")
                f.write(f"\nOverdue Ratio\t\t= {(overdue_count/line_count)*100}%")

    # This part of the code handles user overview
    with open("tasks.txt", "r") as f:   
        # Identify each unique user        
        list_users = []
        for line in f:
            line_list = line.strip("\n").split(", ")        # task list
            list_users.append(line_list[0])                 # add users to a new list
            list_unique_users = set(list_users)             # trim list of duplicate users
            list_unique_users = list(list_unique_users)     # convert to iterable list    

    # Count the score(total recurrance) of each task(line) per user    
    with open("tasks.txt", "r") as f:           
        scores = {}
        for line in f:
            words = line.strip("\n").split(", ")
            for usr in list_unique_users: 
                if usr in line:
                    scores[usr] = scores.get(usr,0) + 1
                    sum = 0
                    for i in scores:
                        sum = sum + scores[i]
        scores_string = scores                  # temp variable to print out data neatly
        scores_string = str(scores).replace(",","\n").strip('{}').replace("'","").replace(" ","")
        with open("user_overview.txt","w") as f:
            f.write("Task Count\n" + scores_string)
            f.write("\nAll Users: " + str(sum))
            f.write("\n\nTask Distribution")
            for key in scores:    
                f.write(f"\n{key}\t: {(scores[key]/sum)*100} %")

    # Count the score of incomplete tasks per user         
    with open("tasks.txt", "r") as f:           
        scores = {}
        for line in f:
            words = line.strip("\n").split(", ")
            for usr in list_unique_users: 
                if "no" in line and usr in line:
                    scores[usr] = scores.get(usr,0) + 1
                    sum = 0
                    for i in scores:
                        sum = sum + scores[i]
        with open("user_overview.txt","a") as f:
            f.write("\n\nIncomplete Tasks")
            f.write("\nCount\t= " + str(sum))
            for key in scores:    
                f.write(f"\n{key}\t: {round((scores[key]/sum)*100, 2)} %")

    # Count the score of complete tasks per user
    with open("tasks.txt", "r") as f:           
        scores = {}
        for line in f:
            words = line.strip("\n").split(", ")
            for usr in list_unique_users: 
                if "yes" in line and usr in line:
                    scores[usr] = scores.get(usr,0) + 1
                    sum = 0
                    for i in scores:
                        sum = sum + scores[i]
        with open("user_overview.txt","a") as f:
            f.write("\n\nComplete Tasks")
            f.write("\nCount\t= "+ str(sum))
            for key in scores:    
                f.write(f"\n{key}\t: {(scores[key]/sum)*100} %")

    # Count the score of incomplete + overdue tasks per user
    with open("tasks.txt", "r") as f:           
        scores = {}
        for line in f:
            words = line.strip("\n").split(", ")
            d1 = datetime.strptime(words[4], '%d %B %Y')    # Determine dates
            d2 = datetime.today()
            for usr in list_unique_users: 
                if "no" in line and usr in line and d2>d1:
                    scores[usr] = scores.get(usr,0) + 1
                    sum = 0
                    for i in scores:
                        sum = sum + scores[i]
        with open("user_overview.txt","a") as f:
            f.write("\n\nOverdue Tasks")
            f.write("\nCount\t= " + str(sum))
            for key in scores:    
                f.write(f"\n{key}\t: {(scores[key]/sum)*100} %")
    
    print(TOP_LINE)
    print("✦ Reports saved to default location")
    print("Thank you")
    print(BOTTOM_LINE)

# Login to program
user = False
pass_check = False
users_list = []

# Get existing users_list from file + Get saved password list from file
with open("user.txt", "r") as f:    
    for line in f:
       column = line.split(",")
       users_list.append(column[0])

# Ask user for username and check against list appended from file                  
while user is False:                
    username = input("\nPlease Enter Username: ").lower()
    if username in users_list: 
        user = True
        print(TOP_LINE)
        print(f"✦ Welcome {username}")
        print(BOTTOM_LINE)
    else:
        print("\n ✘ User does not exist.")
        break; # System should not proceed to ask for password if user does not exist

    # Ask user for password and check against file
    while pass_check is False: 
        password = getpass("\nPlease Enter Password: \n")     
        with open("user.txt", "r") as f:
            for line in f:
                # Check if password entered is in same line as username entered and validated above
                if username in line and password in line: 
                    pass_check = True
    
    main_menu()






