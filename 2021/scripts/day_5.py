def day_5_part_1():
with open("inputs/day_5.txt", "r") as fp:
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