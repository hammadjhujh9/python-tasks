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
        print("The number is odd")
    
