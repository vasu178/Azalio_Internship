
import os
import venv

# 1. Create project folder
project = "day5"

if not os.path.exists(project):
    os.mkdir(project)
    print("Project folder created!")
else:
    print("Project folder already exists!")

# 2. Create virtual environment
venv_path = os.path.join(project, "venv")

if not os.path.exists(venv_path):
    venv.create(venv_path, with_pip=True)
    print("Virtual environment created!")
else:
    print("Virtual environment already exists!")

# 3. Create main.py
file_path = os.path.join(project, "main.py")

if not os.path.exists(file_path):
    with open(file_path, "w") as file:
        file.write("print('Hello Python!')")
    print("main.py created!")

# 4. Display project contents
print("\nProject contents:")

for item in os.listdir(project):
    print(item)
