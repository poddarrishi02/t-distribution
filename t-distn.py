x = input("Enter data \n")

arr = x.split(" ")
arr = list(map(float, arr))

length=len(arr)

average = 0
for y in arr:
    average += y
average = average/length

var = 0
for y in arr:
    var += (y - average)**2
var = var/length

s2 = 0
for y in arr:
    s2 += (y - average)**2
s2 = s2/(length-1)
s=s2**0.5
print("Enter t(alpha/2,n-1) or z(alpha/2) value:")
t = float(input())
error=t*s/(length**0.5)
t_lower=average-error
t_upper=average+error

print("number of objects: ", length)
print("average: ", average)
print("var: ", var)
print("sd: ", var**0.5)
print("S square: ", s2)
print("S: ", s)
print("error of z/t distribution: ", error)
print("lower range of z/t distribution: ", t_lower)
print("upper range of z/t distribution: ", t_upper)
