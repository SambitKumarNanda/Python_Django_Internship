class while_class:
    
    def print_range(self,num):
        i = 1
        while i <= n:
            print(i,end=" ")
            i+=1
            
    def reverse_order(self,num):
        while num > 0:
            print(n,end=" ")
            num = num - 1
            
    def multiplication_table(self,num,target_range):
        i = 1
        while target_range > 0:
            print(f"{num} * {i} = {num * i}")
            i += 1
            times -= 1
            
    def print_factors(self,num):
        while num >= i:
            if num % i == 0:
                print(i)
            i+=1
    
    def prime_number(self,num):
        count = 0
        i = 1
        while num >= i:
            if num % i == 0:
                count += 1
            i += 1
        
        if count == 2:
            print("Prime")
        else:
            print("not prime")
            
    def prime_factors(self,num):
        i = 1
        while num >= i:
            if num % i == 0:
                factor = i
                count = 0
                j = 1
                while factor >= j:
                    if factor % j == 0:
                        count += 1
                    j+=1
                if count == 2:
                    print(factor)
            i+=1
        
    def num_of_digits(self,num):
        count = 0
        while(num > 0):
            count += 1
            num//=10
        print(count)
        
    def armstrong_num(self,num):
        temp = num
        temp2 = num
        digits = 0
        while temp2 != 0:
            temp2 //= 10
            digits += 1

        sum_digits = 0
        while temp != 0:
            sum_digits = sum_digits + (temp % 10) ** digits
            temp //= 10

        if sum_digits == num:
            print(f"{num} is an Armstrong number")
        else:
            print(f"{num} is not an Armstrong number")
            
    
    def palindrome_num(self,num):
        temp = num
        rev = 0
        while temp != 0:
            rev = rev * 10 + (temp % 10)
            temp //= 10

        if num == rev:
            print(f"{num} is a palindrome number")
        else:
            print(f"{num} is not a palindrome number")
            
            
while_obj = while_class()
while_obj.prime_factors(40)