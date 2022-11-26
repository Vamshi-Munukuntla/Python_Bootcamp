import os
# from main import up_one_directory_level


print(os.getcwd())
# up_one_directory_level()
# up_one_directory_level()
print(os.getcwd())
entries = os.scandir(".")
count = 0
for entry in entries:
    if os.path.isfile(entry):
        print(entry.name)
        count += 1
print(f'Total number of files in this directory: {count}')

