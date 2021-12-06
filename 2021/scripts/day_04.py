class Day4Part1:
    with open("inputs/day_04.txt", "r") as fp:
        text = fp.read().splitlines()
    #
    #
    #
    numbers_to_draw = list(map(int, text[0].split(",")))
    #
    boards_data = text[1:]
    boards_data = list(filter(None, boards_data))
    boards_data = [list(filter(None, x.split(" "))) for x in boards_data]
    #
    boards = {}
    boards_data_row_num = 0
    board_num = 0
    for row in boards_data:
        row = [int(x) for x in row]
        if board_num not in boards.keys():
            boards[board_num] = {"rows": []}
        boards[board_num]["rows"].append(row)
        if "columns" not in boards[board_num].keys():
            boards[board_num]["columns"] = [[m] for m in row]
        else:
            for i in range(0, 5):
                boards[board_num]["columns"][i].append(row[i])
        boards_data_row_num += 1
        if boards_data_row_num % 5 == 0:
            board_num += 1
    #
    #
    #
    number_drawn = numbers_to_draw[0]
    winning_board_id = None
    #
    #
    #
    for number_drawn in numbers_to_draw:
        for board_id in boards.keys():
            boards[board_id]["rows"] = [
                [i for i in x if i != number_drawn]
                for x
                in boards[board_id]["rows"]
            ]
            boards[board_id]["columns"] = [
                [i for i in x if i != number_drawn]
                for x
                in boards[board_id]["columns"]
            ]
            for row in boards[board_id]["rows"]:
                if len(row) == 0:
                    winning_board_id = board_id
                    break
            for column in boards[board_id]["columns"]:
                if len(column) == 0:
                    winning_board_id = board_id
                    break
            if winning_board_id is not None:
                break
        if winning_board_id is not None:
            break
    #
    #
    #
    sum_unmarked_numbers = 0
    for row in boards[winning_board_id]["rows"]:
        sum_unmarked_numbers += sum(row)
    #
    #
    #
    product = number_drawn * sum_unmarked_numbers

class Day4Part2:
    with open("inputs/day_04.txt", "r") as fp:
        text = fp.read().splitlines()
    #
    #
    #
    numbers_to_draw = list(map(int, text[0].split(",")))
    #
    boards_data = text[1:]
    boards_data = list(filter(None, boards_data))
    boards_data = [list(filter(None, x.split(" "))) for x in boards_data]
    #
    boards = {}
    boards_data_row_num = 0
    board_num = 0
    for row in boards_data:
        row = [int(x) for x in row]
        if board_num not in boards.keys():
            boards[board_num] = {"rows": []}
        boards[board_num]["rows"].append(row)
        if "columns" not in boards[board_num].keys():
            boards[board_num]["columns"] = [[m] for m in row]
        else:
            for i in range(0, 5):
                boards[board_num]["columns"][i].append(row[i])
        boards_data_row_num += 1
        if boards_data_row_num % 5 == 0:
            board_num += 1
    #
    #
    #
    number_drawn = numbers_to_draw[0]
    winning_board_id = None
    excluded_boards = set()
    original_num_boards = len(boards.keys())
    #
    for number_drawn in numbers_to_draw:
        for board_id in boards.keys():
            if board_id in excluded_boards:
                pass
            boards[board_id]["rows"] = [
                [i for i in x if i != number_drawn]
                for x
                in boards[board_id]["rows"]
            ]
            boards[board_id]["columns"] = [
                [i for i in x if i != number_drawn]
                for x
                in boards[board_id]["columns"]
            ]
            for row in boards[board_id]["rows"]:
                if len(row) == 0:
                    excluded_boards.add(board_id)
                    if len(excluded_boards) == original_num_boards:
                        winning_board_id = board_id
                    break
            for column in boards[board_id]["columns"]:
                if len(column) == 0:
                    excluded_boards.add(board_id)
                    if len(excluded_boards) == original_num_boards:
                        winning_board_id = board_id
                    break
            if winning_board_id is not None:
                break
        if winning_board_id is not None:
            break
    #
    #
    #
    sum_unmarked_numbers = 0
    for row in boards[winning_board_id]["rows"]:
        sum_unmarked_numbers += sum(row)
    #
    #
    #
    product = number_drawn * sum_unmarked_numbers

















