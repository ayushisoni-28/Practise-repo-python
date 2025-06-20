# lets take input first
s_user=input("Enter a string:")
reverse_str=(s_user[::-1])
if s_user==reverse_str:
    print('Its a palindrome')
else:
    print('No its not')