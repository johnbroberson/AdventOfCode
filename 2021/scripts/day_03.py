def day_3_part_1():
    with open("inputs/day_03.txt", "r") as fp:
        text = fp.read().splitlines()
    #
    col_sums = []
    for i in range(0, len(text[0])):
        col_sums.append([int(x[i]) for x in text])
    #
    digits = []
    for i in range(0, len(col_sums)):
        digits.append(str(round(sum(col_sums[i])/len(col_sums[i]))))
    #
    gamma_rate = "".join(digits)
    epsilon_rate = gamma_rate.replace("0", "F").replace("1", "0").replace("F", "1")
    #
    product = int(gamma_rate, 2) * int(epsilon_rate, 2)
    #
    print(product)

class day_3_part_2:
    with open("inputs/day_03.txt", "r") as fp:
        text = fp.read().splitlines()
    #
    col_sums = []
    for i in range(0, len(text[0])):
        col_sums.append([int(x[i]) for x in text])
    #
    digits = []
    for i in range(0, len(col_sums)):
        digits.append(str(round(sum(col_sums[i])/len(col_sums[i]))))
    #
    from pandas import DataFrame
    text_list = [list(i) for i in text]
    text_df = DataFrame(data=text_list)
    #
    ogr_subset = text_df
    for i in range(0, len(digits)):
        digit_col_mode = ogr_subset[i].mode()
        if len(digit_col_mode.index) == 1:
            most_common_digit_in_this_col = digit_col_mode.values[0]
        else:
            most_common_digit_in_this_col = "1"
        ogr_subset = ogr_subset[ogr_subset[i] == most_common_digit_in_this_col]
        if len(ogr_subset.index) == 1:
            break
    #
    csr_subset = text_df
    for i in range(0, len(digits)):
        digit_col_mode = csr_subset[i].mode()
        if len(digit_col_mode.index) == 1:
            most_common_digit_in_this_col = digit_col_mode.values[0]
        else:
            most_common_digit_in_this_col = "1"
        csr_subset = csr_subset[csr_subset[i] != most_common_digit_in_this_col]
        if len(csr_subset.index) == 1:
            break
    #
    ogr_list = ogr_subset.head().values.tolist()[0]
    csr_list = csr_subset.head().values.tolist()[0]
    #
    ogr_binary = "".join(ogr_list)
    csr_binary = "".join(csr_list)
    #
    ogr_decimal = int(ogr_binary, 2)
    csr_decimal = int(csr_binary, 2)
    #
    life_support_rating = ogr_decimal * csr_decimal