import matplotlib.pyplot as plt
import os

path = input("Enter directory: ")
path.replace("'\'", "\\")

os.chdir(path)
files = os.listdir(path)

extensions = [os.path.splitext(i)[1] if "." in i else "dirs" for i in files]
values = []

for type_of_extension in set(extensions):
    values.append(list(extensions).count(type_of_extension))

labels = set(extensions)

plt.title(f"Types of files in {os.path.split(path)[1]}")
plt.axis("equal")
plt.pie(values, labels=list(labels), autopct='%.2f')
plt.show()
