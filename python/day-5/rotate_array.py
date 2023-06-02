a = [1,2,3,4,5]
r = input("Enter the order: ")
times = int(input("Enter the times: "))

# def array_rotation(a,r,times):
#     if r == 'r':
#         if times < len(a):
#             return a[times:] + a[:times]
#         elif times == len(a):
#             return a
#         else:
#             return a[times%len(a):] + a[:times%len(a)]
        
#     elif r == 'l':
#         if times < len(a):
#             return a[-times:] + a[:len(a)-times]
#         elif times == len(a):
#             return a
#         else:
#             return {a[-(times%len(a)):] + a[:len(a)-(times%len(a))]}  

def array_rotation(a,r,times):
    times%=len(a)
    if r == 'r':
        return a[times:] + a[:times] if times != len(a) else  a 
        
    elif r == 'l':
        return  a[-times:] + a[:len(a)-times] if times != len(a) else  a

print(array_rotation(a, r, times))


def rotate_left(a):
    temp = a[len(a) - 1]
    for i in range(len(a) - 1,0,-1):
        a[i] = a[i-1]
    a[0] = temp
    return a

def rotate_right(a):
    temp = a[0]
    for i in range(len(a) - 1):
        a[i] = a[i + 1]
    a[len(a) - 1] = temp
    return a 

def rotate(order,times,a):
    while times > 0:
        if order == 'r':
            rotate_right(a)
        elif order == 'l':
            rotate_left(a)