from math import pi

def compute(radius):
    return pi * radius ** 2



try:
    user_radius = float(raw_input('enter the radius :' ))
    area = compute(user_radius)
    print "radius : {} \narea : {:.3f}".format(user_radius,area)

except ValueError as err:
    print err



