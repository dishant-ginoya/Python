# #  You have two lists of dictionaries representing two datasets. Each dictionary contains details
# #  about employees and their projects. You need to filter and join these datasets based on
# #  specific criteria using lambda functions and Python's filter() and map() functions.
# #
# # Output: [
# #   {"name": "Alice", "department": "Engineering", "projects": ["AI Research", "Cloud Computing"]},
# #   {"name": "Charlie", "department": "Engineering", "projects": ["Backend Development"]}
# #  ]
# # ---------------------------


employees = [
    {"id": 1, "name": "Alice", "department": "Engineering"},
    {"id": 2, "name": "Bob", "department": "Marketing"},
    {"id": 3, "name": "Charlie", "department": "Engineering"},
    {"id": 4, "name": "David", "department": "Sales"}
]
projects = [
    {"project_id": 101, "employee_id": 1, "project_name": "AI Research"},
    {"project_id": 102, "employee_id": 2, "project_name": "Market Analysis"},
    {"project_id": 103, "employee_id": 3, "project_name": "Backend Development"},
    {"project_id": 104, "employee_id": 4, "project_name": "Sales Strategy"},
    {"project_id": 105, "employee_id": 1, "project_name": "Cloud Computing"}
]

engineering_emp = list(filter(lambda emp: emp['department'] == 'Engineering', employees))

# projects_by_emp = {
#     project['employee_id']: [x['project_name'] for x in projects if x['employee_id'] == project['employee_id']] for
#     project in projects}


projects_by_emp = {}
[projects_by_emp.update({project['employee_id']: [project['project_name']]}) if project[
                                                                                    'employee_id'] not in projects_by_emp else
 projects_by_emp[project['employee_id']].append(project['project_name']) for project in projects]

# output = [{'name': i['name'], 'department': i['department'], 'projects': projects_by_emp[i['id']]} for i in
#           engineering_emp]

output = list(map(lambda x: {"name": x['name'], "department": x['department'], "projects": projects_by_emp[x['id']]},
                  engineering_emp))

# print(projects_by_emp)

print(output)

# # -------------------
# # Output: [
#     {"name": "Alice", "department": "Engineering", "projects": ["AI Research", "Cloud Computing"]},
#     {"name": "Charlie", "department": "Engineering", "projects": ["Backend Development"]}
# ]
