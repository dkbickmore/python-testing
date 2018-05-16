##for i in range(1,30,-1):
##    print(i)
##    


string = "corey james balb <dkbickmore@gmail.com>"

start = string[::-1].find("<")
end = len(string) - 1

email = string[-start:end]

name = string[:-start-1]

print(email)
print(name)

print("this is a testr")

print("another test")
