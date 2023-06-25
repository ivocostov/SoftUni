wall_dimension_height_x = float(input())
wall_dimension_longitude_y = float(input())
roof_side_triangle_h = float(input())
door_in_m2 = 1.2 * 2
sidewall_windows_in_m2 = 1.5 * 1.5
green_paint_coverage_sqm_per_liter = 3.4
red_paint_coverage_sqm_per_liter = 4.3

total_sqm_front_and_back_wall = 2 * (wall_dimension_height_x * wall_dimension_height_x) - door_in_m2
total_sqm_sidewall = 2 * (wall_dimension_height_x * wall_dimension_longitude_y) - 2 * sidewall_windows_in_m2
total_sqm_roof_side_triangle_area = 2 * (wall_dimension_height_x * roof_side_triangle_h / 2)
total_sqm_roof_top_side = 2 * (wall_dimension_height_x * wall_dimension_longitude_y)

total_green_paint_for_walls = (total_sqm_front_and_back_wall + total_sqm_sidewall) / green_paint_coverage_sqm_per_liter
total_red_paint_for_roof = (total_sqm_roof_side_triangle_area + total_sqm_roof_top_side) \
                           / red_paint_coverage_sqm_per_liter
print("{:.2f}".format(total_green_paint_for_walls))
print("{:.2f}".format(total_red_paint_for_roof))
