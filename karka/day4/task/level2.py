# a=[7,-9,8,-4,2,-10]
# b=[]
# for i in a:
#     if (i<0):
#         b.append(i)
#         print(b)


# a = [3, 4, 5, 6, 7, 8, 9, 10]
# b=[]
# for i in a:
#     if (i%2==1):
#         b.append(0)
#         print(b)
#     else:
#         b.append(i)
#         print(b)

# n=int(input('entr a num'))


# age=int(input('enter ur age:'))
# if (age<16):
#     print("u can't drive")
# elif(age==16 or age==17):
#     print("you can drive but no vote")
# elif(age>=18 and age<=24):
#     print("u can vote but not rent a car")
# else:
#     print("you can do prtty much anything")

# n=10
# sum=0
# for i in range(1,n+1):
#     sum+=i
#     print(sum)

    
# for i in range(10,56):
#     if(i%2==0):
#         print(i,"its a even number")
#     else:
#         print(i,"its an odd number")

# a=int(input('enter a num:'))
# b=int(input('enter a num:'))
# c=a*b
# print(c)
# if (c>500):
#     sum=a+b
#     print(sum)
# else:
#     print("invalid")

# a=[1,2,2,3,4,5,6,6]
# a=list(dict.fromkeys(a))
# print(a)


# sum=0
# while 0<1:
#     n=int(input('num:'))
#     sum+=n
#     print(sum)
#     if (n==0):
#         break


# remove=3
# a=[3,2,2,3]
# b=[]
# count=0
# for i in a:
#     if i!=remove:
#         b.append(i)
#         print(b)
#     else:
#         count+=1
# for j in range(1,count+1):
#     b.append('-')
#     print(b)

# num=int(input('num:'))
# while num>9:
#     num = sum(int(i) for i in str(num))
#     print(num)


# a=[1,0,9,8,0,8,0]
# for i in range(len(a)):
#     if (i==0):
#         a.insert(i+1,0)
#         print(a)
    

# num=[[1,2],[3,4]]
# sum=0
# sum1=0
# for i in num[0]:
#     sum+=i
#     print(sum)
# for j in num[1]:
#     sum1+=j
#     print(sum1)
# s=sum+sum1
# print(s)

# num=[['4270'],['3690']]
# s=num[0]+num[1]
# print(s)

# a=[5,10,20,2,0,33,100,90]
# b=[]
# for i in range(0,len(a),2):
#     c=a[i]
#     d=a[i+1]
#     b.extend([c,d,c+d])
#     print(b)

# a= [0,1,0,3,12]
# b=[]
# c=[]
# for i in a:
#     if(i!=0):
#         b.append(i)
#         print(b)
#     else:
#         c.append(i)
#         print(c)
#     print(b+c)


# def if (x % 2 == 0):
#         print('Even')


#     else:
#         print('Odd')
# checkOddEven(9)checkOddEven(x):
    

# a=int(input('value of a='))
# b=int(input('value of b='))
# a,b=b,a
# print('a=',a,'b=',b)


# a = input("Enter a word: ")
# b = input("Enter another word: ").lower()

# if sorted(a) == sorted(b):
#     print("It's an anagram: True")
# else:
#     print("It's not an anagram: False")


# a=input('enter a string:')
# b=''
# for i in a:
#     if (i!=' '):
#         b+=i
# print('string without space',b)

# input=[5,10,20,2,0,33,100,90]
# output=[]
# for i in range(len(input)):
#     output.append(input[i])
#     if(i+1)%2==0:
#         output.append(input[i]+input[i-1])
# print(output)

# a=[2,2,1,1,2,2,2]
# count=0
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if (a[i]==a[j]):
#             count+=1
#         if (count>4):
#             print(i,'is the most value')
#         else:
#             print(i,'is a least value')        

# def add_digits(num):
#     if num==0:
#         return 0
#     return (num-1)%9+1
# a=int(input('enter a num:'))
# print(add_digits(a))
    
a=[1,2,3,4,5]
largest=max(a)
print(largest)