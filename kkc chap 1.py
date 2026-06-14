# # sum of number from 1 to 100

# a=0
# while a!=100:
#     a=a+1
#     print(a)

#Count how many times a number is divisible by 2 before reaching 0.
# a = int(input("enter the number which can be divisible by 2:-"))
# tries = 0
# temp = a

# while True:
#     if a % 2 == 0 and a > 0:
#         tries += 1
#         a = a // 2
#     else:
#          break   

# print(f"the number of time is {tries}")  


#  ATM Machine:

# Ask user for PIN
# They get 3 attempts
# Wrong PIN → "incorrect, X attempts remaining"
# 3 wrong attempts → "card locked"
# Correct PIN → "welcome, access granted"

# correct_pin="1234"
# attempts=3
# while attempts>0:
#     user_pin=input("enter your pin :-")
#     if user_pin==correct_pin:
#         print("welcome! access granted ")
#         break
#     else:
#          attempts -=1
#          if attempts>0:
#              print(f"incorrect,{attempts} attempts remaining")
#          else:
#             print("card locked")

# n = int(input("Enter number of terms: "))
# n1, n2 = 0, 1

# if n <= 0:
#     print("Please enter a number greater than 0")

# while n > 0:
#     n1, n2 = n2, n1 + n2
#     n = n - 1

# # This prints instantly because it only outputs one number at the very end
# print(f"The final Fibonacci number is {n1}")


# total=0
# while True:
#     num=int(input("enter 0 to stop and have a sum of previous"))
#     if num==0:
#         break

#     total+=num

# print(f"the sum is {total}")


