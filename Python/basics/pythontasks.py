# Write a program that prompts the user to enter three integers and displays them in
# increasing order.
def increseorder():
    n1 = int(input("Enter 1 Number : "))
    n2 = int(input("Enter 2 Number : "))
    n3 = int(input("Enter 3 Number : "))

    if n1 < n2:
        temp = n1
        n1 = n2
        n2 = temp

    if n2 < n3:
        temp = n2
        n2 = n3
        n3 = temp

    if n1 < n2:
        temp = n1
        n1 = n2
        n2 = temp

    print(f'The increasing order is :', n1, n2, n3)


# Write a program that prompts the user to enter a three-digit integer and determines
# whether it is a palindrome number. A number is a palindrome if it reads the same from
# right to left and from left to right.

def palindrome():
    n1 = int(input("Enter Number to check whether it palindrome or not : "))
    original_number = n1
    reversed_number = 0
    while n1 != 0:
        remainder = n1 % 10
        reversed_number = reversed_number * 10 + remainder
        n1 = n1 // 10

    print(f'The reversed number is : {reversed_number}')

    if original_number == reversed_number:
        print('The number is palindrome')
    else:
        print('The number is not palindrome')


# Write a Python program which accepts a 4 digit binary numbers as its input and check
# if the number is even or not.
def checkBinaryEven():
    binary_number=int(input("Enter binary to check wheather it's even or odd :"))
    original_number=binary_number
    decimal_number=0
    i=0
    while binary_number!=0:
        remainder=0
        remainder=binary_number%10
        decimal_number=(remainder*pow(2,i))+decimal_number
        binary_number=binary_number//10
        i=i+1
    
    print("The decimal number is", decimal_number, "of binary number", original_number)
    if decimal_number%2==0:
        print("The number is even")
    else:
        print("The number is not even")

# Write a Python program to create and display all combinations of letters, selecting each letter
# from a different key in a dictionary.
# Sample data : {'1':['a','b'], '2':['c','d']}
def combination():
    diction={'1' : ['a','b'], '2': ['c','d']}
    print("The possible combination for the given dictionary are as ")
    i=0
    j=0
    for data in diction['1']:
        for value in diction['2']:
            print(diction['1'][i], diction['2'][j])
            j=j+1
            
        j=0
        i=i+1     

# Write a function called cumsum that takes a list of numbers and returns the cumulative sum;
# that is, a new list where the ith element is the sum of the first i + 1 elements from the original
# list.
def cumsum():
    list1=[20,34,56,21,1]
    print("the cumsum is : ")
    list1[0]=list1[0]
    i=1
    for number in list1[1:]:
        list1[i]=list1[i]+list1[i-1]
        i=i+1

    for number in list1[0:i]:
        print(list1)

# Write a Python program to count the values associated with key in a dictionary.
def countValues():
    diction={'1' : ['a','b','e'], '2': ['c','d']}
    count=0
    for data in diction['1']:
       count=count+1

    print(f'The value associated with specific key = {count}')   

# Given a list of numbers, find and print the elements that appear in the list only once. The
# elements must be printed in the order in which they occur in the original list.
def occurence():
    list1=[1,2,3,3,2,5,3]
    count=0
    for item in list1:
         temp=item
         for thing in list1:
             if thing==temp:
                 count=count+1

         if count==1:
             print(f'{temp} occured once in list')   
         
         count=0

# write a function called is_sorted that takes a list as a parameter and returns True if the list is
# sorted in ascending order and False otherwise.
def SortedListCheck():
    list1=[3,6,1,8,3]
    list2=[6,5,3,2,1]
    size=len(list1)
    i=0 
    for item in list1[0:size]:
        if  list1[item]> item[item+1]:
            bool=False
            break;
        else:
            bool=True    
        i=i+1     

    print(f'The list  ascending order {bool}')

# Write a Python program to check the validity of password input by users. Validation:
# • At least 1 letter between [a-z] and 1 letter between [A-Z].
# • At least 1 number between [0-9].
# • At least 1 character from [$#@].
# • Minimum length 6 characters.
# • Maximum length 16 characters.
def checkPassword():
    password=input("Enter a password :\n• at least 1 letter between [a-z] and 1 letter between [A-Z].• \n• At least 1 number between [0-9].\n• At least 1 character from [$#@].\n• Minimum length 6 characters.\n• Maximum length 16 characters.\n")
     
    lenght=len(password)

    while lenght > 16 or lenght < 8:
        print("Password is invalid input again : ")
        password=input("Enter a password :\n• Minimum length 6 characters.\n• Maximum length 16 characters.\n")
        lenght=len(password)
    
    bool1=False
    bool2=False
    for item in password:
        ascii=ord(item)
        if ascii >=65 and ascii <=90:
            bool1=True
            print("Upper case letter present")
        if ascii >=97 and ascii <=122:
            bool2=True
            print("Lower case letter present")

    while bool1!=True or  bool2!=True:
        print("Password is invalid input again : ")
        print("Upper/Lower case letter not present")
        password=input("Enter a password :\n• at least 1 letter between [a-z] and 1 letter between [A-Z].• \n ")
        bool1=False
        bool2=False
        for item in password:
             ascii=ord(item)
             if ascii >=65 and ascii <=90:
                  bool1=True
                  print("Upper case letter present")
             if ascii >=97 and ascii <=122:
                 bool2=True
                 print("Lower case letter present")
  
    bool1=False
    for item in password:
        ascii=ord(item)
        if ascii >=32 and ascii <=47 or ascii >=58 and ascii <=64 or ascii >=91 and ascii <=96 or ascii >=123 and ascii <=126:
            bool1=True
            print("Special letter present")

    while bool1!=True:
        print("Password is invalid input again : ")
        print("Special case letter not found")
        password=input("Enter a password :\n• At least 1 character from [$#@].\n ")
        bool1=False
        for item in password:
             ascii=ord(item)
             if ascii >=32 and ascii <=47 or ascii >=58 and ascii <=64 or ascii >=91 and ascii <=96 or ascii >=123 and ascii <=126:
              bool1=True
              print("Special letter present")

    bool1=False
    for item in password:
        if item >=0 and item <=9:
            bool1=True
            print("Number present")

    while bool1!=True:
        print("Password is invalid input again : ")
        print("Number not found")
        password=input("Enter a password :\n• At least 1 number between [0-9].\n")
        bool1=False
        for item in password:
             if item >=0 and item <=9:
                 bool1=True
                 print("Number present")

# A Caesar cypher is a weak form of encryption that involves “rotating” each letter by a fixed
# number of places.
def Encryption():
    encryt="zammad"
    key=3
    str1=""
    for item in encryt:
        ascii=ord(item)
        ascii=ascii+key
        if ascii>=97 and ascii >=122 or ascii>=65 and ascii >=90 :
            ascii=ascii-26
        word=chr(ascii)
        str1=str1+word

   
    print(f'Encryption done :  {str1}')



if __name__ == '__main__':
    option = int(input('Select the option to the program :'))
    if option == 1:
        increseorder()
    if option == 2:
        palindrome()
    if option == 3:
        checkBinaryEven()
    if option == 4:
        combination()
    if option == 5:
        cumsum()
    if option == 6:
        countValues()
    if option == 7:
        occurence()
    if option == 8:
        SortedListCheck()
    if option == 9:
        checkPassword()
    if option == 10:
        Encryption()
