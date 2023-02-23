# Task-Manager-Functions
This code consists of functions to manage user registration, task creation, and task viewing for a task management system. Additionally, it includes functionality to display statistics and generate reports.

User Registration
The reg_user() function handles user registration. Only the admin can register new users, and if a non-admin user attempts to register, they will receive an error message. If the user does not exist already, the function prompts the user for their desired username and password. The function then writes the new user's credentials to a text file named user.txt.

Task Creation
The add_task() function allows a user to add a new task to the system. The user is prompted for the task's details, including the person's username, task title, task description, task due date, and current date. The function then writes the task information to a text file named tasks.txt.

Task Viewing
There are two functions to view tasks: view_all() and view_mine(). view_all() displays all the tasks in the tasks.txt file. view_mine() only displays tasks assigned to the currently logged-in user. Users can select a specific task to view or return to the main menu.

Statistics Display
The display_stats() function displays statistics about the task management system. Specifically, it displays the total number of tasks and users in the system.

Report Generation
The generate_reports() function generates a report containing details of all tasks. The report includes the total number of tasks, the number of tasks completed, the number of tasks incomplete, and the number of tasks overdue. The function writes the report to a text file named task_overview.txt.
