file = input("Enter your file: ")

idx = file.rfind(".")

ext = file[idx+1:]
filename = file[:idx]

print(f"Your filename is {filename}")
print(f"Your extension is {ext}")