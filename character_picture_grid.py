def picture(gridParameter):
    for i in range(6):
        for j in range(len(gridParameter)):
            print(gridParameter[j][i], end='')
        print()


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '#', '#', '.', '.', '.'],
        ['#', '#', '#', '#', '.', '.'],
        ['#', '#', '#', '#', '#', '.'],
        ['.', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '#', '.'],
        ['#', '#', '#', '#', '.', '.'],
        ['.', '#', '#', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

picture(grid)
