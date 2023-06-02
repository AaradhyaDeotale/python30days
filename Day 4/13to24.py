#30-Days-Of-Python Day 4 Levels 13 to 24


fullname = 'Aaradhya G Deotale'
print(fullname.split())
FAANG = 'Facebook, Amazon, Apple, Netflix, Google'
print(FAANG.split())

string = 'Coding for all'
character = string[0]
print(character)
char2 = string[-1]
print(char2)
char3 = string[10]
print(char3)

name = "Indian Space Research Organisation"
words = name.split()
acronym = ""

for word in words:
    acronym += word[0]
print(acronym)

homecity = 'Mumbai, India '
first_3 = homecity[0:3]
print(first_3)
last_9 = homecity[-9:]
print(last_9)

name = 'aaradhya g deotale '
print(name.find('r'))
print(name.find('w'))

learning = 'I am learning Python today'
print(learning.replace('Python', "Data Science"))

sub_string = 'Py'
ss2 = 'a'
print(learning.index(sub_string))
print(learning.rindex(ss2))

bigstr = 'You cannot end a sentence with because because because is a conjunction'

print(bigstr.find('because'))
print(bigstr.rfind('because'))