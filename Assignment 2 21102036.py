#Question 1
string="Python is a case sensitive language"
     #a To find length of string
length=len(string)
print("The length of string is:",length)
     #b Reverse order of string
reverse=string[::-1]
print("The reverse order of the string in one line code is:",reverse)
     #c Slice Function
sliced_string=string[10:26]
print("The new sliced string is:",sliced_string)
     #d Replace Function
replaced_string=string.replace("a case sensitive","object oriented")
print("The new replaced string is:",replaced_string)
      #e Index of substring
indexed=string.index("a")
print("The index of substring a is:",indexed)
      #f Remove white spaces
removed=string.replace(" ","")
print("New string is given by:",removed)
print("\n")

#Question 2
Name="Anshula Sharma"
SID=21102036
Department_Name="Civil"
CGPA=9.9
Line1="Hey,{} Here!".format(Name)
line2="My SID is {}".format(SID)
line3="I am from {} department and my CGPA is {}".format(Department_Name,CGPA)

print(Line1)
print(line2)
print(line3)
print("\n")

#Question 3
a=56
b=10
A=a&b
B=a|b
C=a^b
D=a<<2 , b<<2
E=a>>2 , b>>4
print("Output of a&b is:",A)
print("Output of a|b is:",B)
print("Output of a^b is:",C)
print("Left shift both a and b with 2 bits is:",D)
print("Right shift a with 2 bits and b with 4 bits is:",E)
print("\n")

#Question 4
String=input("Enter the string:")
if 'name' in String:
       print("Yes")
else:
       print("No")

print("\n")

#Question 5
s1=int(input("Enter the first side of triangle:"))
s2=int(input("Enter the second side of triangle:"))
s3=int(input("Enter the third side of triangle:"))
while(s1+s2>s3) and (s1+s3>s2) and (s2+s3>s1):
    print("Triangle is valid")
    break
print("\n")


#Question 6
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
num=a^b
Count_flipped_bit = 0
while (num !=0):
    num= num & (num - 1)
    Count_flipped_bit += 1
print("Number of bits needed to be flipped to convert a to b is:",Count_flipped_bit)
print("\n")

