def two_numbers(number):
    two_number = ""
    if number == 0:
        return "0"
    else:
        while number > 0:
            remainder = number % 2  
            two_number = str(remainder) + two_number
            number = number // 2  
    return two_number

def eight_numbers(number):
    eight_number = ""
    if number == 0:
        return "0"
    else:
        while number > 0:
            remainder = number % 8  
            eight_number = str(remainder) + eight_number
            number = number // 8  
    return eight_number
    
def sixteen_numbers(number):
    sixteen_number = ""
    if number == 0:
        return "0"
    else:
        while number > 0:
          remainder = number % 16  
          if remainder < 10:
            sixteen_number = str(remainder) + sixteen_number
          else:
            sixteen_number = chr(55 + remainder) + sixteen_number
          number = number // 16
            
    return sixteen_number  
    
number = int(input()) 
two_number = two_numbers(number) 
eight_number = eight_numbers(number) 
sixteen_number = sixteen_numbers(number) 

print(two_number)
print(eight_number)
print(sixteen_number)

