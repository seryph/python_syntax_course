# Functions

def say_hi():
  print("Hi")


say_hi()


print('\n')



# Args
def say_hi_to_me(name):
    print(f"Hi {name}")


say_hi_to_me('Bill')



print('\n')


def args_function(*nums):
    for num in nums:
        print(num)


args_function(1, 2, 3 ,4 ,5 ,6)



print('\n')



# Keyword Args
def say_hi_full_name(**name):
  print(f"Hi {name['first_name']} {name['last_name']}")

say_hi_full_name(first_name = "John", last_name = "Smith")



print('\n')



# Lambda Functions


lamda_example = lambda num : num + 10

print(lamda_example(6))
