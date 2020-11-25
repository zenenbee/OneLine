print("                     .__  .__               \n  ____   ____   ____ |  | |__| ____   ____  \n /  _ \\ /    \\_/ __ \\|  | |  |/    \\_/ __ \\ \n(  <_> )   |  \\  ___/|  |_|  |   |  \\  ___/ \n \\____/|___|  /\\___  >____/__|___|  /\\___  >\n            \\/     \\/             \\/     \\/ ")
print("\nOneLine : The 'good' programming language")
a = input("Line 1:\n")

c = len(a)
b = 0
count = 0
prints = ""
printing = False
error = ""
looppoint = -1
while b < c:

    if error == "":
        char = a[b]
        b += 1


        if printing:
            if char != "$":
                prints += char

        if char == "$":
            if printing:
                printing = False
                print(prints)
            else:
                printing = True
                prints = ""

        if char == "^":
            count += 1
        if char == "_":
            count += -1
        if char == "~":
            print(count)

        if char == "!":
            if looppoint == -1:
                looppoint = b
            else:
                if count == 0:
                    looppoint = -1
                else:
                    b = looppoint





input()
