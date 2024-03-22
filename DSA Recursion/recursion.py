# def print_nums(n):

#     if n == 0:
#         return

#     print_nums(n-1)
#     print(n)

# print_nums(5)
# -------------------------------------------------
# lst = [1,2, [3,[4]],5]

# def flatten_list(lst):
#     output = []
#     for item in lst:
#         if isinstance(item, list):
#            output+=flatten_list(item)

#         else:
#             output.append(item)

#     return output

# print(flatten_list(lst, ))


lst = [[1, 0, 0, 0, 0],
       [1, 1, 1, 0, 0],
       [0, 0, 1, 0, 0],
       [0, 1, 1, 0, 0],
       ]


def is_in(r,c, lst):
    return 0 <= r < len(lst) and 0<=c < len(lst[0])

def find_path(r, c, lst):
    
    if r==3 and c==4:
        a=3
    lst[r][c] = -1
    print(r, c)

    if is_in(r+1,c, lst) and lst[r+1][c] == 1:
        find_path(r+1, c)

    if is_in(r, c+1, lst) and lst[r][c+1] == 1:
        find_path(r, c+1,lst)
        
    if is_in(r, c-1, lst) and lst[r][c-1]==1:
        find_path(r, c-1, lst)
    
    if is_in(r-1, c, lst) and lst[r-1][c]==1:
        find_path(r-1, c, lst)
        

find_path(0, 0, lst)

# from sys import getrecursionlimit
# print(getrecursionlimit())

# (0,0), (1,0), (1,1), (1,2), (2,2), (3,2), (3,1)
