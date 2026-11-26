#Reverse a string using Python
Inputtext=input("Enter the string to reverse it:")
print("The Entered string to reverse is: ",Inputtext)

def reverse_string(Inputtext):
    reversed_text = ""
    for char in Inputtext:
        reversed_text = char + reversed_text
    return reversed_text
print(reverse_string(Inputtext))