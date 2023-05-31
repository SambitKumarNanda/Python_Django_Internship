a = "Sambit Kumar Nanda"
print(a[::-1])

# String methods
a = "Sambit Kumar Nanda"
b = "   Sambit   "

# String Methods

# print(a.capitalize())
# print(a.casefold())
# print(a.count('a'))
# print(a.isupper())
# print(b.islower())
# print(a.isdigit())
# print(a.split(" "))
# print(b.strip())
# print(a.replace('S', 'n'))

# Number of occurances of an element
# input_list = [1, 11, 2, 3, 4, 2, 2, 5, 5, 6, 6, 6, 7]
string_input = "SambitKumarNanda"
target_element = input("Enter the element whose number of occurances will be found out: ")

def count_ele(string_input, target_element):
    count = 0
    for i in range(len(string_input)):
        if target_element == string_input[i]:
            count += 1
    return count


print(f"Number of occurrences of {target_element} is {count_ele(string_input, target_element)}")



# filter out duplicates -> return new list
# old_list = [1, 1, 2, 2, 3, 4, 5]
# new_list = []
# for i in range(len(old_list)):
#     if old_list[i] not in new_list:
#         new_list.append(old_list[i])
# print(new_list)