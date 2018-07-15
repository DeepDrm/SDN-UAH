from subprocess import call

fichero = input("Fichero a sumar al: ")
call(["git", "add","/home/ser/Desktop/TFG/TFG-GIT/SDN-UAH/"+fichero])

mensaje = input("Mensaje del commit: ")
call(["git", "commit","-m",mensaje])

branch = input("Branch del commit: ")
call(["git", "push","origin",branch])