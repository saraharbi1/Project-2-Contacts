from person import Person
from contacts import Contacts

# اختبار فئة Person
p1 = Person("Ahmad", {'primary': 123456789, 'mobile': 223344556}, "ahmad@institution.edu")
p2 = Person("Ahmad", {'primary': 123456789, 'mobile': 223344556}, "ahmad@institution.edu")
p3 = Person("Ali", {'home': 998877665}, "ali@example.com")

print("__str__ test:")
print(p1)
print()

print("__eq__ test:")
print("p1 == p2:", p1 == p2)  
print("p1 == p3:", p1 == p3)  
print()

print("Test comparisons (by sorting):")
people = [p3, p1]
people.sort()  
for p in people:
    print(p.name)
print()


contacts = Contacts()
contacts.append(p1)
contacts.append(p2) 
contacts.append(p3)

print("Contact List:")
for person in contacts:
    print(person)
print()

print("Number of duplicates in contacts:", contacts.count_duplicates())
