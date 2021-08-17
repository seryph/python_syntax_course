
# Iterators

iter1 = ("first", "second", "third")

for val in iter1:
  print(val)



print('\n')


iter2 = ("first", "second", "third")
iterate = iter(iter2)

print(next(iterate))
print(next(iterate))
print(next(iterate))




print('\n')




# Generators

def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(firstn(10))


print('\n')


# List Comprehension

operation = [1 + n for n in range(15)]
print(operation)