name = input("Enter name: ")
n = int(input("Enter number: "))

if n<=5:
  print ("Good Morning",name,"!")
  for i in range(n):
    print("Welcome!", end=" ")
else: 
  print("Number should be less than 5!")
