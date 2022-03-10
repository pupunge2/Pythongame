def point_inside_rect(x, y, r1, r2, r3, r4):
    return x > r1 and x < r1 + r3 and y > r2 and y < r2 + r4

def point_inside_rect_list(x, y, rect):
    return x > rect[0] and x < rect[0] + rect[2] and y > rect[1] and y < rect[1] + rect[3]

def two_circle_overlap(x1, y1, x2, y2, r1, r2):
    return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2) < (r1 + r2) * (r1 + r2)
