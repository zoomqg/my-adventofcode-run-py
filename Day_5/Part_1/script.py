import numpy as np

# opening the file in read mode
file = open("sample.txt", "r")
  
# reading the file
data = file.read()

# moving data lines to list
data_list = data.split("\n")

# closing the file
file.close()

# removing all unnecessary chars and creating a numpy array
data_list = [x.replace(' -> ', ',') for x in data_list]
data_list = [x.split(',') for x in data_list]
data_list = np.array(data_list, int)
data_list = data_list.reshape(len(data_list), 2, 2)

print(data_list)

# making blank diagram with zeros
find_max = np.amax(data_list, axis=0)
max_x = max(find_max[0][0], find_max[1][0]) + 1
max_y = max(find_max[0][1], find_max[1][1]) + 1
diagram = np.zeros((max_y, max_x))

for i in range(0, len(data_list)):
    # cover y axis (checking if x axis is same in both lines)
    if data_list[i][0][0] == data_list[i][1][0]:
        column = data_list[i][0][0]
        start_point = data_list[i][0][1]
        finish_point = data_list[i][1][1]
        # necessary for 'for' loop
        if start_point > finish_point:
            start_point, finish_point = finish_point, start_point
        finish_point += 1
        for row in range(start_point, finish_point):
            diagram[row][column] += 1
    # cover x axis
    elif data_list[i][0][1] == data_list[i][1][1]:
        row = data_list[i][0][1]
        start_point = data_list[i][0][0]
        finish_point = data_list[i][1][0]
        # necessary for 'for' loop
        if start_point > finish_point:
            start_point, finish_point = finish_point, start_point
        finish_point += 1
        for column in range(start_point, finish_point):
            diagram[row][column] += 1


#print(diagram)
print(np.count_nonzero(diagram >= 2))