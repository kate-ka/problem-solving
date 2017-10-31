def ribbon_dimensions(w, h, l):
    sides = sorted([w, h, l])
    side1 = sides[0]
    side2 = sides[1]
    ribbon = side1 + side1 + side2 + side2
    bow = w * h * l
    total = ribbon + bow
    return total



with open('day2.txt', 'r') as f:
    total_paper = 0
    ribbon = 0
    for item in f.readlines():
        dimensions = [int(item) for item in item.split('x')]
        w, h, l = int(dimensions[0]), int(dimensions[1]), int(dimensions[2])
        ribbon += ribbon_dimensions(w, h,l)
        paper = 2 * l * w + 2 * w * h + 2 * h * l
        dimensions.remove(max(dimensions))
        smallest_size = dimensions[0] * dimensions[1]
        total_paper = total_paper + smallest_size + paper
print(total_paper) # 1588178
print(ribbon) # 3783758

