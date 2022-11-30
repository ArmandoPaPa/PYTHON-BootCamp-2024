import math

print("Hi! Let us calculate how many cans of paint you need to paint a wall(-s)")
wall_height = int(input("Enter the HEIGHT of the wall: "))
wall_width = int(input("Enter the WIDTH of the wall: "))
can_coverage = int(input("Enter COVERAGE (how large area one paint can can paint): "))


def paint_calc(height, width, coverage):
    area = height * width
    cans_needed = math.ceil(area/coverage)
    # cans_needed = area // coverage
    # if cans_needed * coverage < area:
    #     cans_needed += 1
    print(f"Height: {height}, Width: {width} = Area: {area}; Coverage {coverage} "
          f"=> CANS needed: {cans_needed} cans!")


paint_calc(wall_height, wall_width, can_coverage)
