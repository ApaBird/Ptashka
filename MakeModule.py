from sys import argv
import os

try:
    nameModule = argv[1]
except:
    print("Передайте имя модуля")
    quit()

if __name__ == "__main__":
    if not os.path.isdir("Module"):
        os.mkdir("Module")

    path = f"Module\\{nameModule}"
    if not os.path.isdir(path):
        os.mkdir(path)
        f = open(f"{path}\\Command.py", 'a')
        f.write("import option")
        f.close()
        open(f"{path}\\Option.py", 'a').close()
        open(f"{path}\\LoadModule.py", 'a').close()
