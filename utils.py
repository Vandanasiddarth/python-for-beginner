def find_max(list):
    greatest_no = list[0]
    for i in list:
        if i > greatest_no:
            greatest_no = i
    return greatest_no