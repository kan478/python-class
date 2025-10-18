# sub = lambda a,b: a-b
# print(sub(17, 5))

# multiplication = lambda a,b: a*b
# print(multiplication(8, 4))

# square = lambda z: z**2
# print (square(9))

# even = lambda x: "Even" if x%2 == 0 else "Odd"
# print(even(13))
# print(even(2))

#map
nums = [ 2, 4, 6, 8]
squares = list(map (lambda z: z**2, nums))
# print(squares)
#filter
nums = [1, 2, 3, 4, 5, 6]
odd = list(filter(lambda x: x % 2 != 0, nums))
# print(odd)
# sorted
words = ['strawberry', 'Jackfruit', 'berries', 'apple','cherry']
sorted_list = sorted(words, key=lambda w:len(w))

print(sorted_list)

nums = [5, 234, 8, 1]
print(sorted(nums))

from functools import reduce
totalsum_value = reduce(lambda x, y: x+y, nums)
print(f"sum: {totalsum_value}")