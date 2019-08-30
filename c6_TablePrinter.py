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
    print(col_length)

    for i in range(row):
        for j in range(column):
            print(tableData[j][i].rjust(col_length), end=' ')
        print()


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

table_printer(tableData)
