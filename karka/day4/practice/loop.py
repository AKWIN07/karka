# for i in range(5):
#     print(i)

# for i in range(5,20):
#     print(i)

# a=10
# for i in range(a+1):
#     if(i%2==0):
#         print(i,"its a even number")
#     else:
#         print(i,"its an odd number")


# a=[6,8,7,6,8,9,10]
# for i in a:
#     if(i%2==0):
#         print(i,"its a even number")
#     else:
#         print(i,"its an odd number")



# a=[6,-8,7,6,-8,9,-10]
# for i in a:
#     if(i>=0):
#         print(i,"its a positive number")
#     else:
#         print(i,"its a negative number")

n=5
for i in range(1,n+1):
    for j in range(i):
        print('*',end=' ')
    print()