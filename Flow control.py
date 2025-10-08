#This program asks for name and 2 simple quetion loop
print('Please enter your name') #ask for their name
myName = input()
print('Hello', myName)
print('What state are you from?')
state = input()
print(state,'Thats pretty sick!!')
while True:
    print('Do you like Dinosaurs? (yes/no) :')
    answer = input()
    if answer !='yes':
        continue
    print('Is this how you make dinosaurs? (yes/no):')
    question = input()
    if question == 'no':
        break
print('No, This how you play god.')

