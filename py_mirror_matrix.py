# def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
#     clean = []
#     for new_list in matrix:
#         clean.append(new_list[::-1])
#     return clean

def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    new_list = []
    for row in matrix:
        new_list.append(row[::-1])
    return new_list