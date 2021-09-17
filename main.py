from tkinter import *
from game import Game
from time import sleep


root = Tk()
root.title('Tic Tac Toe')
game = Game('red')

redpoints = 0
bluepoints = 0

squareGrid = {
    'square00': [0, 1],
    'square01': [1, 1],
    'square02': [2, 1],
    'square10': [0, 2],
    'square11': [1, 2],
    'square12': [2, 2],
    'square20': [0, 3],
    'square21': [1, 3],
    'square22': [2, 3]
}

label = Label(
    root, text=f'Red: {redpoints} | Blue: {bluepoints}', bg=game.first_color, pady=10)
label.grid(columnspan=3, row=0, sticky='ew')


def whenSquareClicked(square):
    game.move(square)
    if game.winner or game.draw:
        if game.winner:
            changeCounter()
            highlightWinnerSquares(game.winner_squares)
        game.restart()
        root.after('5000', lambda: restartGrid())
    updateLabelColor()


def changeCounter():
    global redpoints, bluepoints
    if game.winner == 'red':
        redpoints += 1
    else:
        bluepoints += 1
    label.configure(text=f'Red: {redpoints} | Blue: {bluepoints}')


def highlightWinnerSquares(squaresToHighlight):
    for k in squareGrid:
        id = str(squareGrid[k]['textvariable'])[-2:]
        if not id in squaresToHighlight:
            squareGrid[k]['bg'] = '#ffffff'
            squareGrid[k]['state'] = DISABLED


def updateLabelColor():
    if game.first_color == 'red':
        color = 'red' if game.amount_of_moves % 2 == 0 else 'blue'
    else:
        color = 'blue' if game.amount_of_moves % 2 == 0 else 'red'
    label.configure(
        bg=color)


def restartGrid():
    global squareGrid
    for k in squareGrid:
        squareGrid[k].configure(
            command=lambda i=squareGrid[k]: whenSquareClicked(i), state=ACTIVE, bg='#d9d9d9')


for k, v in squareGrid.items():
    column, row = v
    squareGrid[k] = Button(root, padx=97, pady=80,
                           state=None, textvariable=k)
    squareGrid[k].configure(
        command=lambda i=squareGrid[k]: whenSquareClicked(i))
    squareGrid[k].grid(column=column, row=row)


root.minsize(600, 600)
root.maxsize(600, 600)
root.mainloop()
