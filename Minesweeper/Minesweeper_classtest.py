from tkinter import *
import random
from functools import partial
cols = 8
rows = 9
mines = 10

minegrid=[] # 2d lista på rutnätet med minor

class Setup:
    def __init__(self,cols,rows): #sätter ut minor på rutnätet
        self.grid= [[0 for i in range(cols)]for i in range(rows)] #sätter upp ett rut nät med nollor som används som spelplan
        for i in range(len(grid)):
            self.col=[]
            for j in range(len(grid[i])):
                self.x= random.randint(1,5) # Ger en 20% chans att varje cell ska bli en ruta
                if self.x==1:
                    self.col.append(-1)
                else:
                    self.col.append(0)
            self.minegrid.append(col)
        return neighbors_setup(cols,rows)

    def neighbors_setup(self.cols,rows): # sätter upp hur många minor som varje cell har intill sig (om cellen inte själv är en mina)
        for row in range(rows):
                for col in range(cols): # for loop för att gå genom varje cell
         
                    # Hoppar över om den innehåller en mina
                    if minegrid[row][col] == -1:
                        continue
         
                    # kollar upp 
                    if row > 0 and minegrid[row-1][col] == -1:
                        minegrid[row][col] = minegrid[row][col] + 1
                    # kollar ner   
                    if row < rows-1  and minegrid[row+1][col] == -1:
                        minegrid[row][col] = minegrid[row][col] + 1
                    # kollar vänster
                    if col > 0 and minegrid[row][col-1] == -1:
                        minegrid[row][col] = minegrid[row][col] + 1
                    # kollar höger
                    if col < cols-1 and minegrid[row][col+1] == -1:
                        minegrid[row][col] = minegrid[row][col] + 1
                    # kollar upp till vänster   
                    if row > 0 and col > 0 and minegrid[row-1][col-1] == -1:
                        minegrid[row][col] = minegrid[row][col] + 1
                    # kollar upp till höger
                    if row > 0 and col < cols-1 and minegrid[row-1][col+1]== -1:
                        minegrid[row][col] = minegrid[row][col] + 1
                    # kollar ner till vänster
                    if row < rows-1 and col > 0 and minegrid[row+1][col-1]== -1:
                        minegrid[row][col] = minegrid[row][col] + 1
                    # kollar ner till höger
                    if row < rows-1 and col< cols-1 and minegrid[row+1][col+1]==-1:
                        minegrid[row][col] = minegrid[row][col] + 1
        return Button_Setup(cols,rows)

root = Tk() #sätter upp GUI(graphical interface)
root.title('Minesweeper')
root.geometry('360x360')

##menubar = Menu(root)
##menubar.add_command(label="Hello!")
##root.config(menu=menubar)
##root.mainloop()  



cell=[]
li=[]
def Lose(idx): #en funktion som kallas när spelaren har klickat på en mina som signalerar att spelaren har förlorat samt avslöjar spelbrädet
    Lose_window = Tk()
    Lose_window.geometry('+0+0')
    label = Label(Lose_window,text = 'Game Over', fg='red',bg='black')
    label.pack()
    for i in range(len(cell)):
        idx=i
        row = int(idx/cols)
        col = idx-row*cols
        if (cell[idx],minegrid[row][col]) == (cell[idx],-1):
            img = PhotoImage(file='tile_mine.png')
            cell[idx].configure(image = img)
            cell[idx].image= img
        elif (cell[idx],minegrid[row][col]) == (cell[idx],0):
            img = PhotoImage(file='tile_clicked.png')
            cell[idx].configure(image = img)
            cell[idx].image= img
        elif (cell[idx],minegrid[row][col]) == (cell[idx],1):
            img = PhotoImage(file='tile_1.png')
            cell[idx].configure(image = img)
            cell[idx].image= img
        elif (cell[idx],minegrid[row][col]) == (cell[idx],2):
            img = PhotoImage(file='tile_2.png')
            cell[idx].configure(image = img)
            cell[idx].image= img
        elif (cell[idx],minegrid[row][col]) == (cell[idx],3):
            img = PhotoImage(file='tile_3.png')
            cell[idx].configure(image = img)
            cell[idx].image= img
        elif (cell[idx],minegrid[row][col]) == (cell[idx],4):
            img = PhotoImage(file='tile_4.png')
            cell[idx].configure(image = img)
            cell[idx].image= img
        elif (cell[idx],minegrid[row][col]) == (cell[idx],5):
            img = PhotoImage(file='tile_5.png')
            cell[idx].configure(image = img)
            cell[idx].image= img
        elif (cell[idx],minegrid[row][col]) == (cell[idx],6):
            img = PhotoImage(file='tile_6.png')
            cell[idx].configure(image = img)
            cell[idx].image= img
        elif (cell[idx],minegrid[row][col]) == (cell[idx],7):
            img = PhotoImage(file='tile_7.png')
            cell[idx].configure(image = img)
            cell[idx].image= img
        elif (cell[idx],minegrid[row][col]) == (cell[idx],8):
            img = PhotoImage(file='tile_8.png')
            cell[idx].configure(image = img)
            cell[idx].image= img
def left_click(event,idx): #funktion som säger att när man vänsterklickar ska rutan avslöjas 
    row = int(idx/cols)
    col = idx-row*cols
    if (cell[idx],minegrid[row][col]) == (cell[idx],-1):
        img = PhotoImage(file='tile_mine.png')
        cell[idx].configure(image = img)
        cell[idx].image= img
        return Lose(idx)
    elif (cell[idx],minegrid[row][col]) == (cell[idx],0):
        img = PhotoImage(file='tile_clicked.png')
        cell[idx].configure(image = img)
        cell[idx].image= img
    elif (cell[idx],minegrid[row][col]) == (cell[idx],1):
        img = PhotoImage(file='tile_1.png')
        cell[idx].configure(image = img)
        cell[idx].image= img
    elif (cell[idx],minegrid[row][col]) == (cell[idx],2):
        img = PhotoImage(file='tile_2.png')
        cell[idx].configure(image = img)
        cell[idx].image= img
    elif (cell[idx],minegrid[row][col]) == (cell[idx],3):
        img = PhotoImage(file='tile_3.png')
        cell[idx].configure(image = img)
        cell[idx].image= img
    elif (cell[idx],minegrid[row][col]) == (cell[idx],4):
        img = PhotoImage(file='tile_4.png')
        cell[idx].configure(image = img)
        cell[idx].image= img
    elif (cell[idx],minegrid[row][col]) == (cell[idx],5):
        img = PhotoImage(file='tile_5.png')
        cell[idx].configure(image = img)
        cell[idx].image= img
    elif (cell[idx],minegrid[row][col]) == (cell[idx],6):
        img = PhotoImage(file='tile_6.png')
        cell[idx].configure(image = img)
        cell[idx].image= img
    elif (cell[idx],minegrid[row][col]) == (cell[idx],7):
        img = PhotoImage(file='tile_7.png')
        cell[idx].configure(image = img)
        cell[idx].image= img
    elif (cell[idx],minegrid[row][col]) == (cell[idx],8):
        img = PhotoImage(file='tile_8.png')
        cell[idx].configure(image = img)
        cell[idx].image= img



def right_click(event,idx): # en funktion som säger att vid högerklick så ska en flagga placeras vid den cellen
    img =PhotoImage(file='tile_flag.png')
    cell[idx].configure(image = img)
    cell[idx].image= img

def Button_Setup(cols,rows): #sätter upp knapparna/cellerna till GUI 
    for i in range(rows):
        for j in range(cols):
            index = i*cols+j
            cell.append(index)
            img = PhotoImage(file='tile_plain.png')
            cell[index] = Label(root, image = img,borderwidth=0)
            cell[index].image = img
            cell[index].bind('<Button-1>', partial(left_click,idx=index))
            cell[index].bind('<Button-2>', partial(right_click,idx=index))
            cell[index].grid(row=i,column=j)

mine_setup(cols,rows)

#print(Number_of_mines)
##for i in range(len(minegrid)):
##    print(minegrid[i])

    
