names = []
phones = []
num = 3

for i in range(num):
    name = input("Name: ")
    phone = int(input("Phone number: "))

    names.append(name)
    phones.append(phone)

print("\tName\tPhone Number")

for i in range(num):
    print(f'\t{names[i]}\t{phones[i]}')

s = input("Enter the Name to search: ")
if s in names:
    index = names.index(s)
    name = names[index]
    phone = phones[index]

    print("Name: {}, Phone Number: {}".format(name,phone))
else:
    print("Name not found")