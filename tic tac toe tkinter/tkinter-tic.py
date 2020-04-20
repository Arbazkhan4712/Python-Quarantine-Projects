from turtle import *
import tkinter.messagebox
import tkinter
import random
import math
import datetime
import time
import sys

screenMin = 0
screenMax = 300
Human = -1
Computer = 1

class Board:
    
    def __init__(self, board=None, screen=None):
        self.screen = screen
        if screen == None:
            if board!=None:
                self.screen = board.screen

        self.items = []
        for i in range(3):
            rowlst = []
            for j in range(3):
                if board==None:
                    rowlst.append(Dummy())
                else:
                    rowlst.append(board[i][j])

            self.items.append(rowlst)

    # Accessor method for the screen
    def getscreen(self):
        return self.screen

   
    def __getitem__(self,index):
        return self.items[index]

    
    def __eq__(self,other):
        for i in range(len(self.items)):
            for j in range(len(self[i])):
                if self[i][j].eval() != other[i][j].eval():
                    return False
        return True 

   
    def reset(self):

        self.screen.tracer(1)
        for i in range(3):
            for j in range(3):
                self.items[i][j].goto(-100,-100)
                self.items[i][j] = Dummy()

        self.screen.tracer(0)

    
    def eval(self):
        win = []
        i = 0
        if ((self.items[0][0].eval() == self.items[1][1].eval() == self.items[2][2].eval() or
             self.items[0][2].eval() == self.items[1][1].eval() == self.items[2][0].eval()) and
             self.items[1][1].eval() != 0):
            win.append(self.items[1][1].eval())
        while not (1 in win and -1 in win) and i < 3:
            if (self.items[i][0].eval() == self.items[i][1].eval() == self.items[i][2].eval() and
                self.items[i][0].eval() != 0):
                win.append(self.items[i][0].eval())
            elif (self.items[0][i].eval() == self.items[1][i].eval() == self.items[2][i].eval() and
                  self.items[0][i].eval() != 0):
                win.append(self.items[0][i].eval())
            i += 1
        if 1 in win and -1 in win:
            return None
        try:
            return win[0]
        except:
            return 0

   
    def full(self):
        for i in range(len(self.items)):
            for j in range(len(self.items[i])):
                if self[i][j].eval() == 0:
                    return False
        return True

    
    def drawXOs(self):

        for row in range(3):
            for col in range(3):
                if self[row][col].eval() != 0:
                    self[row][col].st()
                    self[row][col].goto(col*100+50,row*100+50)

        self.screen.update()


class Dummy:
    def __init__(self):
        pass

    def eval(self):
        return 0

    def goto(self,x,y):
        pass

class X(RawTurtle):
    def __init__(self, canvas = None):
        if canvas != None:
            super().__init__(canvas)
            self.ht()
            self.getscreen().register_shape("X",((-40,-36),(-40,-44),(0,-4),(40,-44),(40,-36),(4,0), \
                                       (40,36),(40,44),(0,4),(-40,44),(-40,36),(-4,0),(-40,-36)))
            self.shape("X")
            self.penup()
            self.speed(5)
            self.goto(-100,-100)

    def eval(self):
        return Computer

class O(RawTurtle):
    def __init__(self, canvas = None):
        if canvas != None:
            super().__init__(canvas)
            self.ht()
            self.shape("circle")
            self.penup()
            self.speed(5)
            self.goto(-100,-100)

    def eval(self):
        return Human

def minimax(player,board):
    moves = []
    if board.eval() != 0:
        return board.eval()
    elif board.full():
        return 0
    for i in range(3):
        for j in range(3):
            if board[i][j].eval() == 0:
                if player == Computer:
                    board[i][j] = X()
                elif player == Human:
                    board[i][j] = O()
                moves.append(minimax(player * -1, board))
                board[i][j] = Dummy()
    if player == Computer:
        return max(moves)
    elif player == Human:
        return min(moves)




class TicTacToe(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.buildWindow()
        self.paused = False
        self.stop = False
        self.running = False
        self.turn = Human
        self.locked = False

    def buildWindow(self):

        cv = ScrolledCanvas(self,600,600,600,600)
        cv.pack(side = tkinter.LEFT)
        t = RawTurtle(cv)
        screen = t.getscreen()
        screen.tracer(100000)

        screen.setworldcoordinates(screenMin,screenMin,screenMax,screenMax)
        screen.bgcolor("white")
        t.ht()

        frame = tkinter.Frame(self)
        frame.pack(side = tkinter.RIGHT,fill=tkinter.BOTH)
        board = Board(None, screen)

        def drawGrid():
            screen.clear()
            screen.tracer(1000000)
            screen.setworldcoordinates(screenMin,screenMin,screenMax,screenMax)
            screen.bgcolor("white")
            screen.tracer(0)
            t = RawTurtle(cv)
            t.ht()
            t.pu()
            t.width(10)
            t.color("blue")
            for i in range(2):
                t.penup()
                t.goto(i*100+100,10)
                t.pendown()
                t.goto(i*100+100,290)
                t.penup()
                t.goto(10,i*100+100)
                t.pendown()
                t.goto(290,i*100+100)

            screen.update()


        def newGame():
            #drawGrid()
            self.turn = Human
            board.reset()
            self.locked =False
            screen.update()


        def startHandler():
            newGame()

        drawGrid()

        startButton = tkinter.Button(frame, text = "New Game", command=startHandler)
        startButton.pack()

        def quitHandler():
            self.master.quit()

        quitButton = tkinter.Button(frame, text = "Quit", command=quitHandler)
        quitButton.pack()

        def computerTurn():
            self.locked = True

           

            b = Board()
            for row in range(3):
                for col in range(3):
                    b[row][col] = board[row][col]
            moves = []

            for i in range(3):
                for j in range(3):
                    if b[i][j].eval() == 0:
                        b[i][j] = X()
                        moves.append([(i, j), minimax(Human,b)])
                        b[i][j] = Dummy()

            maxMove = moves[0][0]
            bestValue = moves[0][1]
            for val in moves:
                if val[1] > bestValue:
                    bestValue = val[1]
                    maxMove = val[0]

          
            row, col = maxMove
            board[row][col] = X(cv)
            self.locked = False


        def mouseClick(x,y):
            if not self.locked:
                row = int(y // 100)
                col = int(x // 100)

                if board[row][col].eval() == 0:
                    board[row][col] = O(cv)

                    self.turn = Computer

                    board.drawXOs()

                    if not board.full() and not abs(board.eval())==1:
                        computerTurn()

                        self.turn = Human

                        board.drawXOs()
                    else:
                        self.locked = True

                    if board.eval() == 1:
                        tkinter.messagebox.showwarning("Game Over","X wins!!!")

                    if board.eval() == -1:
                        tkinter.messagebox.showwarning("Game Over","O wins !")

                    if board.full():
                        tkinter.messagebox.showwarning("Game Over","It was a tie.")

        screen.onclick(mouseClick)

        screen.listen()

def main():
    root = tkinter.Tk()
    root.title("Tic Tac Toe")
    application = TicTacToe(root)
    application.mainloop()

if __name__ == "__main__":
    main()