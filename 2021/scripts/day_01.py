def day_1_part_1():
    with open("inputs/day_1.txt", "r") as fp:
        text = list(map(int, fp.read().splitlines()))
    #
    increases_counter = 0
    for i in range(1, len(text)):
        if text[i] > text[i-1]:
            increases_counter += 1
    #
    print(increases_counter)

def day_1_part_2():
    with open("inputs/day_1.txt", "r") as fp:
        text = list(map(int, fp.read().splitlines()))
    #
    increases_counter = 0
    for i in range(0, len(text)-3):
        window_a = text[i] + text[i+1] + text[i+2]
        window_b = text[i+1] + text[i+2] + text[i+3]
        if window_b > window_a:
            increases_counter += 1
    #
    print(increases_counter)