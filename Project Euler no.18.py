


import time

def row_sum(row_data, row_num):

    for i in range(len(row_data[row_num])):

        row_data[row_num][i] += max([row_data[row_num+1][i], row_data[row_num+1][i+1]])

    if len(row_data[row_num])==1: return row_data[row_num][0]

    else: return row_sum(row_data, row_num-1)


rows = []

with open('no18.txt') as f:

    for line in f:
        rows.append([int(i) for i in line.rstrip('\n').split(" ")])


start = time.time()
result = row_sum(rows, len(rows)-2)
elapsed = time.time() - start

print("%s found %s seconds" % (result , elapsed))
