class for_class:
    
    def print_range(self,range_num):
        for i in range(range_num):
            print(i)
            
    def reverse_order(self,range_num):
        for i in range(range_num,0,-1):
            print(i)
            
    def multiplication_table(self,num,range_num):
        for i in range(1,range_num+1):
            print(f"{i} x {num} = {i * num}")
            
    def display_factors(self,num):
        for i in range(num):
            if n % i == 0:
                print(i)
                
    def prime_numbers(self,num):
        count = 0
        for i in range(2, num + 1):
            if num % i == 0:
                count += 1
        if count == 2:
            print("It is a prime number")
        else:
            print("It is not a prime number")
            
    def prime_factors(self,num):
        for i in range(1, num + 1):
            if num % i == 0:
                factor = i
                count = 0
                for j in range(2, factor + 1):
                    if factor % j == 0:
                        count += 1
                if count == 2:
                    print(factor)
                    
        
    def number_of_digits(self,num):
        temp = num
        count = 0
        for i in str(temp):
            temp //= 10
            count += 1
        print(count)
        
        
    def is_armstrong(self,num):
        temp = num
        count = 0
        for i in str(temp):
            temp //= 10
            count+=1
            
        temp1 = num
        sum = 0
        for i in str(temp1):
            sum += int(i) ** count
            temp1/=10
        
        if sum == num:
            print("Armstrong")
        else:
            print("Not Armstrong")
            
            
    def is_palindrome(self,num):
        temp = num
        count = 0
        for i in str(temp):
            temp //= 10
            count+=1
        
        temp1 = num
        rev = 0
        for i in str(temp1)[::-1]:
            rev = rev * 10 + int(i)
            temp1/=10
            
        if num == rev:
            print("Palindrome")
        else:
            print("Not Palindrome")
        
    
for_obj = for_class()
for_obj.is_palindrome(123)