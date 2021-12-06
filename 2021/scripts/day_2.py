def day_2_part_1():
    with open("inputs/day_2.txt", "r") as fp:
        text = fp.read().splitlines()
    #
    forwards = [int(i[-1]) for i in text if "forward" in i]
    ups = [int(i[-1]) for i in text if "up" in i]
    downs = [int(i[-1]) for i in text if "down" in i]
    #
    delta_x = sum(forwards)
    delta_y = sum(downs) - sum(ups)
    #
    product = delta_x * delta_y
    #
    print(product)

def day_2_part_2():
    with open("inputs/day_2.txt", "r") as fp:
        text = fp.read().splitlines()
    #
    aim = 0
    delta_x = 0
    delta_y = 0
    #
    for i in text:
        if "down" in i:
            aim += int(i[-1])
        elif "up" in i:
            aim -= int(i[-1])
        else:
            delta_x += int(i[-1])
            delta_y += (int(i[-1]) * aim)
    #
    product = delta_x * delta_y
    #
    print(product)