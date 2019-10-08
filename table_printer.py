def table_printer(tableData):
    column = len(tableData)
    row = len(tableData[0])
    col_length = 0
    longest = ''

    for i in tableData:
        for j in i:
            if len(j) > len(longest):
                longest = j

    col_length = len(longest)

    for i in range(row):
        for j in range(column):
            print(tableData[j][i].rjust(col_length), end=' ')
        print()


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

print('Fruits'.rjust(8) + 'People'.rjust(9) + 'Animals'.rjust(9))
print('------'.rjust(8) + '------'.rjust(9) + '------'.rjust(9))
table_printer(tableData)
