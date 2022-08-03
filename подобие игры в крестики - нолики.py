

print('Enter cells: ')  #вводим значения для решетки (всего 9 значений), где каждая ячейка может принимать X либо O либо _
cells = input()
print('---------')
print('|',' '.join(cells[0:3]), '|')
print('|',' '.join(cells[3:6]), '|')
print('|',' '.join(cells[6:9]), '|')
print("---------")
winning_arrays = [cells[0: 3], cells[3: 6], cells[6: 9], cells[0] + cells[3] + cells[6], cells[1] + cells[4] + cells[7], cells[2] + cells[5] + cells[8], cells[0] + cells[4] + cells[8], cells[2] + cells[4] + cells[6]]
if abs(cells.count('X') - cells.count('O')) > 1 or ('XXX' in winning_arrays and 'OOO' in winning_arrays):
    print('Impossible')  #условия для невозможного расположения значений в решетке
elif 'XXX' in winning_arrays:
    print('X wins')  #условия для аобеды X
elif 'OOO' in winning_arrays:
    print('O wins')  #условия для победы O
elif '_' not in cells and 'XXX' and 'OOO' not in winning_arrays:
    print('Draw')  #условие ничьи
elif '_' in cells and 'XXX' and 'OOO' not in winning_arrays:
    print('Game not finished')  #условие когда игра не закончена


