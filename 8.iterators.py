
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

def basic_gen():
    n = 1
    print(f'first num is {n}')
    yield n

    for i in range(4):
      n += 1
      i += 1
      print(f'next num is {n}')
      yield n



for num in basic_gen():
    print(num)


print('\n')


# List Comprehension

comprehension = [4 * n for n in range(3)]
print(comprehension)