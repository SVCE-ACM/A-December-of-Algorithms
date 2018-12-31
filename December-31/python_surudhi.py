def ClosestEnemyII(array):
    enemies = []
    for i, row in enumerate(array):
        for j, col in enumerate(list(row)):
            if col == '1': px, py = (i, j)
            	if col == '2': enemies.append((i,j))
    moves = []
    for x, y in enemies:
        no_wrap = abs(px - x) + abs(py - y)
        col_wrap, row_wrap = abs(px - x) + abs(py - (len(array) - y)), abs((px + len(array)) - x) + abs(py-y)
        moves.append(min(no_wrap, col_wrap, row_wrap))
    return min(moves) if moves else 0	
print ClosestEnemyII(raw_input())
