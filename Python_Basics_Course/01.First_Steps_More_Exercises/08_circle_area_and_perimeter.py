from math import pi
circle_radius = float(input())

calculated_area = circle_radius * circle_radius * pi
calculated_parameter = 2 * pi * circle_radius

print("{:.2f}".format(calculated_area))
print("{:.2f}".format(calculated_parameter))