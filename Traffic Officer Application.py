import sys
import os
import math
import time
import string
import time

start_time = time.time()


data = open("input.txt").read().strip().splitlines()

output = open("/Users/Piyush/Desktop/output.txt", "w+")
# output = open("output.txt", "w+")

filetext = [] # filetext is a list storing each line in input file

for line in data:
    filetext.append(line)  # appending each line in input file to filetext
    # print line

grid_size = filetext[0] # gridsize denoting the city area size
# print grid_size

police = int(filetext[1]) # police denoting the number of police officers
# print police

scooter = filetext[2] # scooter denoting the number of scooters
# print scooter

matrix_coordinates = filetext[3:] # matrix_coordinates is the list containing all the coordinates in input file
# print matrix_coordinates

N = int(grid_size) # Generating a matrix of N*N, initialising all elements value as 0 in the matrix
matrix = [0] * N
for i in range(N):
    matrix[i] = [0] * N

# Generating count for frequency of occurence of each coordinate
for line in matrix_coordinates:
    x_coordinate = int(line.split(",",1)[0])
    y_coordinate = int(line.split(",", 1)[1])

    matrix[x_coordinate][y_coordinate] += 1  # Incrementing count for occurence of each coordinate in matrix_coordinates list

# Printing all elements in the matrix
ele_list = []
colno=0
for element in matrix:
    # print element
    for ele in element:
        ele_list.append([ele,colno])
        colno+=1

ele_list = sorted(ele_list, key=lambda x :x[0], reverse=True)
# print ele_list  # Sorted ele_list

max_activity = 0  # maximum activity points for all solutions
overall_max = 0
# Function checking if it's safe to place a police officer at matrix[x_coordinate][y_coordinate]
def is_safe(row, column):
    if (row in row_list) or (column in column_list) or ((row - column) in diagonal_list) or ((row + column) in antidiagonal_list):
        return False
    return True


def solution(ele_list, police):
    global max_activity
    global overall_max
    if police == 0:
        overall_max = max(overall_max, max_activity)
        return


    for idx, val in enumerate(ele_list):
        # print ele_list
        if overall_max >= max_activity + val[0]*police:
            return
        key_row = val[1] / size
        key_column = val[1] % size

        if is_safe(key_row, key_column):
            row_list.append(key_row)
            column_list.append(key_column)
            diagonal_list.append(key_row - key_column)
            antidiagonal_list.append(key_row + key_column)
            indexes_list.append(val[1])
            max_activity += val[0]

            solution(ele_list[idx:], police-1)

            row_list.pop()
            column_list.pop()
            diagonal_list.pop()
            antidiagonal_list.pop()
            indexes_list.pop()
            max_activity -= val[0]

size = int(grid_size)

row_list = []
column_list = []
diagonal_list = []
antidiagonal_list = []
indexes_list = []

for i in range(size*size): # Iterating over the whole size*size
    r = ele_list[i][1] / size  # Extracting row of the element and denoting it as r
    c = ele_list[i][1] % size  # Extracting column of the element and denoting it as c

    row_list.append(r)  # Appending row to row_list
    column_list.append(c)  #
    diagonal_list.append(r - c)
    antidiagonal_list.append(r + c)
    indexes_list.append(ele_list[i][1])

    max_activity += ele_list[i][0]
    solution(ele_list[i+1:], police-1)

    indexes_list.append(max_activity)
    del row_list[:]
    del column_list[:]
    del diagonal_list[:]
    del antidiagonal_list[:]
    del indexes_list[:]
    max_activity = 0


# print("%s seconds" % (time.time() - start_time)) # Printing execution time in seconds

print overall_max
temporary = str(overall_max)
output.write(temporary)
output.close()