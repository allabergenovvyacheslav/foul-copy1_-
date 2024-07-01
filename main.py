data_structure = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]




def calculate_structure_sum(data_structure):
    total = 0
    for i in data_structure:
        if isinstance(i, list):
            total = total + calculate_structure_sum(i)
        else:
            total = total + i

    return total


result = calculate_structure_sum(data_structure)
print(result)



