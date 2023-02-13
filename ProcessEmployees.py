"""
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
"""

import csv

# open the file

employees = open("employee_data.csv", "r")
reader = csv.reader(employees)
next(reader)


# create an empty dictionary

employee_dict = {}

# use a loop to iterate through the csv file
department = "Marketing"
full_name = "First Name" + "Last Name"

for row in reader:
    department_num = row[3]
    salary = row[5]
if department_num == department:
    print("Manager Name:", full_name)
    print("New Salary:", salary)


for dict in employees:
    print(dict)

    # check if the employee fits the search criteria
    # department: marketing

if department in employee_dict:
    print(employee_dict[department])


print()
print("=========================================")
print()

# iternate through the dictionary and print out the key and value as per printout

infile = open("employee_data.csv", "r")

reader = csv.reader(infile, delimiter=",")
fieldrow = next(reader)

department = "Marketing"
Promotion = []
total = 0

for column in reader:
    First_name = row[1]
    Last_name = row[2]
    dep_name = row[3]
    salary = row[5]

if dep_name == department:
    Promotion.append([Promotion, round(total, 2)])
    department = "department"
    Promotion = salary * 0.1


with open("employee_data.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Full Name", "New Salary"])
for employee in department:
    writer.rwiterow(employee[0], employee[1])
