# nums = [10, 20, 30,654,6554,454]

# sum = 0
# for item in nums:
#     sum += item

# print(sum)

#len

name = "Kangaroo"
print(len(name))

#type

print(type(4))
print(type(4.5))
print(type("what are you doing?"))
print(type([1,2,3]))

#sum
nums = [10, 20, 20]
print(sum(nums))
print(sum(nums, 200))

sum = 0
total = 0
while sum < len(nums):
    total += nums[sum]
    sum += 1
print(total)

# max,min
print(max(10, 20, 25))
print(min(10, 20, 5))


#abs
print(abs(-10))
print(abs(3.45678))

#sorted
nums = [5, 2, 8, 1]
print(sorted(nums))        
print(sorted(nums, reverse=True))

#id()
x=100
print(id(x))

#help()
help(len)

#input
Question = input("what are you doing?")
print("YEAH ",Question)
