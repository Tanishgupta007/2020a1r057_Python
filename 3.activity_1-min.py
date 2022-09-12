# the smallest item in a list

number = [3,4,5,2,65,32,22]

min_number = min(number)

print("The Smallest Number in the list ",number," is " ,min_number)

# the smallest string in a list
string = ['Tanish' , 'gupta', 'pythonLab']
min_str = min(string , key=len)
print("The Smallest string in the list ",string," is " ,min_str)