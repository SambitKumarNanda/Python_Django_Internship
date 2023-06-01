class ds_class:
    
    def iterate_dict_using_key(self,dict_var):
        for i in dict_var.keys():
            print(f"{i} : {dict_var[i]}")
            
    def iterate_dict_using_item(self,dict_var):
        for i, j in dict_var.items():
            print(f"{i} : {j}")
    
    def iterate_list(self,list_var):
        for i in range(len(list_var)):
            print(list_var[i],end=" ")
            
    def append_at_beginning_of_list(self,list_var):
        b =[]
        if len(list_var) == 0:
            list_var.append(element)
        else:
            b.append(element)
            for index in range(1, len(list_var)+1):
                b.append(0)
            for index in range(0, len(list_var)):
                b[index+1] = list_var[index]
        print(b)
    
    def sum_of_items_in_2dlist(self,list_var):
        for i in range(len(a)):
            for j in range(len(a[i])):
                print(a[j][i],end=" ")
            print()
            
    def sum_of_diagonals_in_2dlist(self,list_var):
        sum = 0
        for row in range(len(a)):
            for col in range(len(a[row])):
                if row == col or row == row + col - 1:
                    sum += a[row][col]
        print(sum)
        
    def matrix_sum(self,list_var1,list_var2):
        c = []
        for i in range(len(list_var1)):
            for j in range(len(list_var2)):
                c.append(list_var1[i][j] + list_var2[i][j])
        
    def matrix_mul(self,list_var1,list_var2):
        for i in range(len(list_var1)):
            for j in range(len(list_var1[i])):
                sum = 0
                for k in range(len(list_var2[i])):
                    sum += list_var1[i][k]*list_var2[k][j]
                print(sum,end=" ")
            print()
            
    def num_of_occurences_in_string(self,input_string,target_value):
        count = 0
        for i in range(len(input_string)):
            if target_value == input_string[i]:
                count+=1
        return count
    
    def filter_dup(self,list_input):
        new_list = []
        for i in range(len(list_input)):
            if list_input[i] not in new_list:
                new_list.append(list_input[i])
        print(new_list)