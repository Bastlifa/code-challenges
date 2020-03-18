import math

ab = int(input())
bc = int(input())

m = (ab**2 + bc**2)**0.5

theta = math.asin(bc/m)

angle = round(90 - theta*180/math.pi)

print(f'{angle}°')