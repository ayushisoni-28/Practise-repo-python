# lets create a list first taking the input from user

user_len_list=int(input('Enter the lenght of list you want to create: '))
user_list=[]
for i in range(user_len_list):
    print('Enter element material:')
    element=int(input())
    user_list.append(element)

print('Original list now is:')
print(user_list)

#now sorting
for i in range(user_len_list):
    for j in range(i+1,user_len_list):
        if user_list[i]>user_list[j]:
            temp=user_list[i]
            user_list[i]=user_list[j]
            user_list[j]=temp


print(user_list)