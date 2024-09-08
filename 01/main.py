import os

arquivo1 = open("dados1.txt", "w", encoding="utf-8")
print(os.path.abspath(arquivo1.name))

arquivo1.write("Antonio Jânderson Machado da Silva!")

print(os.path.relpath(arquivo1.name))
print(arquivo1)
