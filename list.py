list1=[]
while True:
    animal=input("Enter animal name: ")
    if animal != "":
        list1.append(animal)
    else:
        break

for i in list1:
    if i=="bird":
        print("The",i,"can fly in the sky")

    else:
        print(i,"is an animal")
