student = {'alice' : 85,'jack' : 90,'jill' : 100,'hill' : 45}
name = input("Enter the student's name:") 
if name not in student:
    print(f"No student found with name {name}.")
else:
    print(f"{name}'s marks: {student[name]}")