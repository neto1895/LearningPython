planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=' ') # print all on same line

print("")

multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product * mult
print(product)

print("")

s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
# print all the uppercase letters in s, one at a time
for char in s:
    if char.isupper():
        print(char, end='')

print("")

for i in range(5):
    print("Doing important work. i =", i)

print("")

def count_negatives(nums):
    return len([num for num in nums if num < 0])
print(count_negatives([1,-2,-1,-3,0,22]))


#Ejercicio 1

def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    if nums == []: 
        return False
    for num in nums: 
        if (num % 7 == 0 and num !=0 ):
            return True
        else: estado = False
    return estado

# To create a more clean code we can use: 
def oneLineLuckyNomber(nums):
    return any([num % 7 == 0 for num in nums])
        
print(has_lucky_number([3,7]))
print(oneLineLuckyNomber([3,7]))

def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    secc = [x*(t+1) for t in range(n)]
    return secc

print(count_by(2,5))