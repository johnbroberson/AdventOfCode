def day_5_try_1():
    # this was my first attempt. it worked, but took extremely, extremely long.
    with open("inputs/day_05.txt", "r") as fp:
        text = fp.read().splitlines()

    from pandas import DataFrame
    segments = DataFrame(columns=["start_x", "start_y", "end_x", "end_y"])
    for line in text:
        data = list(map(int, line.replace(" -> ",",").split(",")))
        segments.loc[len(segments.index)] = data

    points_covered = DataFrame(columns=["x", "y", "frequency"])

    counter = 1
    for index, segment in segments.iterrows():
        if counter % 50 == 0:
            print("{}...".format(counter), end="")
        if segment.start_x == segment.end_x:
            high_y = max(segment.start_y, segment.end_y)
            low_y = min(segment.start_y, segment.end_y)
            for i in range(low_y, high_y+1):
                if ((points_covered.x == segment.start_x) & (points_covered.y == i)).any():
                    existing_entry = points_covered.index[(points_covered.x == segment.start_x) & (points_covered.y == i)].tolist()[0]
                    points_covered.iloc[existing_entry, 2] = points_covered.iloc[existing_entry, 2] + 1
                else:
                    points_covered.loc[len(points_covered.index)] = [segment.start_x, i, 1]
        elif segment.start_y == segment.end_y:
            high_x = max(segment.start_x, segment.end_x)
            low_x = min(segment.start_x, segment.end_x)
            for i in range(low_x, high_x+1):
                if ((points_covered.x == i) & (points_covered.y == segment.start_y)).any():
                    existing_entry = points_covered.index[(points_covered.x == i) & (points_covered.y == segment.start_y)].tolist()[0]
                    points_covered.iloc[existing_entry, 2] = points_covered.iloc[existing_entry, 2] + 1
                else:
                    points_covered.loc[len(points_covered.index)] = [i, segment.start_y, 1]
        else:
            x_increasing = segment.start_x < segment.end_x
            y_increasing = segment.start_y < segment.end_x
            this_x = segment.start_x
            this_y = segment.start_y
            continuing = True
            while continuing:
                if ((points_covered.x == this_x) & (points_covered.y == this_y)).any():
                    existing_entry = points_covered.index[(points_covered.x == this_x) & (points_covered.y == this_y)].tolist()[0]
                    points_covered.iloc[existing_entry, 2] = points_covered.iloc[existing_entry, 2] + 1
                else:
                    points_covered.loc[len(points_covered.index)] = [this_x, this_y, 1]
                continuing = (this_x != segment.end_x and this_y != segment.end_y)
                if x_increasing:
                    this_x += 1
                else:
                    this_x -= 1
                if y_increasing:
                    this_y += 1
                else:
                    this_y -= 1
        counter += 1

    revisited_points = len(points_covered[points_covered.frequency > 1].index)


class Day5Try2():
    # second try, combining my first try and observations from https://github.com/sotsoguk/AdventOfCode2021/blob/69e007a29958b21b12605ed58ea351ccb0d8f3b5/python/day05/day05.py
    from collections import defaultdict

    with open("../inputs/day_05.txt", "r") as fp:
        text = fp.read().splitlines()
    data = [list(map(int, line.replace(" -> ",",").split(","))) for line in text]

    visited_points = defaultdict(int)
    diagonals = []

    for segment in data:
        x1, y1, x2, y2 = segment
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2)+1):
                # defaultdict allows us to bypassing having to check if the key exists/creating it if it doesn't
                visited_points[(x1, i)] += 1
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2)+1):
                visited_points[(i, y1)] += 1
        else:
            diagonals.append(segment)

    part1 = sum([1 if frequency > 1 else 0 for frequency in visited_points.values()])

    # yeah ok this is way faster. I think using pandas was bogging it down 100000%
    # and this is a totally logical way to add things, I forget that list comprehension can just totally substitute in values rather than always do some operation on the existing one

    for segment in diagonals:
        x1, y1, x2, y2 = segment
        dx = 1 if x2 > x1 else -1
        dy = 1 if y2 > y1 else -1
        # ^ this is so much smarter than my boolean solution. simple multiplier!!
        for i in range(abs(x2-x1)+1):
            # and sh*t, using absolute value here ^ to get a range, rather than manually iterating like i was. way better.
            visited_points[(x1+i*dx, y1+i*dy)] += 1
            # and here, getting those multipliers is paying off.

    part2 = sum([1 if frequency > 1 else 0 for frequency in visited_points.values()])

    # YIKES that was fast.
    # alright. I don't feel that bad. I had the framework completely down for how to go about this, and needed refinement + to learn about the defaultdict tool