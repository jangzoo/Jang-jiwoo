## ISBN
x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())
x5 = int(input())
x6 = int(input())
x7 = int(input())
x8 = int(input())
x9 = int(input())

x10 = (x1 + x2*2 + x3*3 + x4*4 + x5*5 + x6*6 + x7*7 + x8*8 + x9*9) % 11
print(int(x10))

#the crickets as a thermometer
N_60 = int(input())
T_F = 50 + (N_60-40)/4
T_C = 10 + (N_60-40)/7
result = "temperature (Fahrenheit): %s\ntemperature (Celsius): %s" %(T_F,T_C)
print(result)

#where is the father
a = int(input())
b = int(input())
c = int(input())

son_age = float( (a+b-b*c)/(c-1) )
mother_age = float(a + son_age) 

m = float(mother_age*12)
s = float(son_age*12)

result = 'The mother is %d months old and her son %d months.' %(m, s)
print(result)



###great circle navigation
import math
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
r = 6371
d = round(r*math.acos(math.sin(math.radians(x1))*math.sin(math.radians(x2)) + math.cos(math.radians(x1))*math.cos(math.radians(x2))*math.cos(math.radians(y1) - math.radians(y2))))

print( 'The great-circle distance is %d km.' %d )
print( f'The great-circle distance is {d} km.' )

###iec units
g = int(input())
m = int(input())
k = int(input())
b = int(input())

SI = g*10**9 + m*10**6 +k*10**3 + b

gib = round(SI / 2**30)
mib = round((SI - gib*(2**30))/2**20)
if mib < 0 : 
    mib = int(1024+mib)
    gib -= 1
kib = round((SI - gib*(2**30) - mib*(2**20))/2**10)
if kib < 0 : 
    kib = int(1024+kib)
    mib -= 1
b = round((SI - gib*(2**30) - mib*(2**20) - kib*(2**10)))
if b < 0 : 
    b = int(1024+b)
    kib -= 1

print( f'{SI}b\n{gib}Gib, {mib}Mib, {kib}Kib, {b}b' )