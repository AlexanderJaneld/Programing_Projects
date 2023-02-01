from tkinter import *
import random
from functools import partial
from time import *
from tkinter import ttk
cols = 16
rows = 16
mines = 40
cell=[]

def Window_setup(cols,rows):
    global root, SettingsFrame,GridFrame, mines_flagged
    mines_flagged = 0
    root = Tk() #sätter upp GUI(graphical interface)
    root.title('Minesweeper')
    WindowHeight = 18*rows + 185
    if cols >= 30:
        WindowWidth = 18*cols+10
    else:
        WindowWidth = 500
    ScreenHeight = root.winfo_screenheight()
    ScreenWidth = root.winfo_screenheight()
    x = (ScreenWidth/2)-(WindowWidth/2)
    y = (ScreenHeight/2)-(WindowHeight/2)
    root.geometry(f'{WindowWidth}x{WindowHeight}+{int(x)}+{int(y)}')
    SettingsFrame = LabelFrame(root, borderwidth = 0, highlightthickness = 0)
    SettingsFrame.pack()
    GridFrame = LabelFrame(root)
    GridFrame.pack()
    
    HighScoreFrame = LabelFrame(root, borderwidth = 0, highlightthickness = 0)
    HighScoreFrame.pack()
    
    ExpertFrame = LabelFrame(HighScoreFrame, borderwidth = 0, highlightthickness = 0)
    ExpertFrame.pack(side=LEFT)
    ExpertLabel = Label(ExpertFrame, text = 'Expert', width = 15,font='Helvetica 15 bold')
    ExpertLabel.pack()
    ExpertFile = open('HighScores_Expert.txt','r')
    HighscoreList(ExpertFile)
    for i in range(5):
        Text =i+1, HighList[i]
        label=Label(ExpertFrame, text = Text)
        label.pack()
    
    IntermediateFrame = LabelFrame(HighScoreFrame, borderwidth = 0, highlightthickness = 0)
    IntermediateFrame.pack(side=LEFT)
    IntermediateLabel = Label(IntermediateFrame, text = 'Intermediate', width = 15,font='Helvetica 15 bold')
    IntermediateLabel.pack()
    IntermediateFile = open('HighScores_Intermediate.txt','r')
    HighscoreList(IntermediateFile)
    for i in range(5):
        Text = i+1, HighList[i]
        label=Label(IntermediateFrame, text = Text)
        label.pack()
    
    BeginnerFrame = LabelFrame(HighScoreFrame, borderwidth = 0, highlightthickness = 0)
    BeginnerFrame.pack(side=LEFT)
    BeginnerLabel = Label(BeginnerFrame, text = 'Beginner', width = 15,font='Helvetica 15 bold')
    BeginnerLabel.pack()
    BeginnerFile = open('HighScores_Beginner.txt','r')
    HighscoreList(BeginnerFile)
    for i in range(5):
        Text = i+1,  HighList[i]
        label=Label(BeginnerFrame, text = Text)
        label.pack()
    
    
    Start_Time()
    Images()

def Images():
    global img_Mine,img_Plain,img_Flagged, img_GameOver
    img_Mine = PhotoImage(file='tile_mine.png')
    img_Plain = PhotoImage(file = 'tile_plain.png')
    img_Flagged = PhotoImage(file = 'tile_flag.png')
    #img_GameOver = PhotoImage(file = 'giphy.png')

    mine_setup(cols,rows)
    
def mine_setup(cols,rows): #sätter ut minor på rutnätet
    global minegrid, RevealState
    RevealState = [[0 for i in range(cols)]for i in range(rows)]
    minegrid= [[0 for i in range(cols)]for i in range(rows)]
    Number_of_Mines = 0
    while Number_of_Mines < mines:
        row = random.randint(0,rows-1)
        col = random.randint(0,cols-1)
        if minegrid[row][col] != -1:
            minegrid[row][col] = -1
            Number_of_Mines += 1
        else:
            minegrid[row][col] = 0
    return neighbors_setup(cols,rows)

def neighbors_setup(cols,rows): # sätter upp hur många minor som varje cell har intill sig (om cellen inte själv är en mina)
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
    ButtonGrid_Setup(cols,rows)

def ButtonGrid_Setup(cols,rows): #sätter upp knapparna/cellerna till GUI 
    for i in range(rows):
        for j in range(cols):
            index = i*cols+j
            cell.append(index)
            cell[index] = Label(GridFrame, image = img_Plain,borderwidth=0)
            cell[index].image = img_Plain
            cell[index].bind('<Button-1>', partial(left_click,idx=index))
            cell[index].bind('<Enter>', partial(FocusCell,idx = index))
            cell[index].grid(row=i+1,column=j)
    SettingsButtons_setup()

def SettingsButtons_setup():
    Options = Button(SettingsFrame, text = 'Options',command = CallOptions)

    Options.pack(side = LEFT)
    Restart = Button(SettingsFrame, text = 'Restart', command = restart)
    Restart.pack(side = LEFT)
    Quit = Button(SettingsFrame, text = 'Quit',command = Exit)
    Quit.pack(side = LEFT)
    

def CallPlay_Time():
    Name = NameEntry.get()
    Win_window.destroy()
    Play_Time(Name)

def CallOptions():
    try:
        GameSetting_window.destroy()
    except Exception:
        pass
    options()
    
def options():
    global HeightEntry,WidthEntry,MineEntry, GameSetting_window
    GameSetting_window =Tk()
    GameSetting_window.title('Options')
    GameSetting_window.geometry('+0+0')

    Difficulty = Label(GameSetting_window,text = 'Difficulty',width=10,font='Helvetica 14 bold')
    Difficulty.grid(row=0,column=0)
    Height = Label(GameSetting_window,text = 'height',width=10,font='Helvetica 14 bold')
    Height.grid(row=0,column=2)
    Width = Label(GameSetting_window,text = 'Width',width=10,font='Helvetica 14 bold')
    Width.grid(row=0,column=3)
    Mines = Label(GameSetting_window,text = 'Mines',width=10,font='Helvetica 14 bold')
    Mines.grid(row=0,column=4)
    
    separator = ttk.Separator(GameSetting_window,orient=HORIZONTAL)
    separator.grid(row=1,columnspan=5,sticky=EW)                   

    Beginner = Button(GameSetting_window,text = 'Beginner',width=10,command = lambda: custom(9,9,10))
    Beginner.grid(row=2,column=0)
    BeginnerHeight = Label(GameSetting_window,text = '9',width=10)
    BeginnerHeight.grid(row=2,column=2)
    BeginnerWidth = Label(GameSetting_window,text = '9',width=10)
    BeginnerWidth.grid(row=2,column=3)
    BeginnerMines = Label(GameSetting_window,text = '10',width=10)
    BeginnerMines.grid(row=2,column=4)

    separator = ttk.Separator(GameSetting_window,orient=HORIZONTAL)
    separator.grid(row=3,columnspan=5,sticky=EW)
    
    Intermediate = Button(GameSetting_window,text = 'Intermediate',width=10,command = lambda: custom(16,16,40))
    Intermediate.grid(row=4,column=0)
    IntermediateHeight = Label(GameSetting_window,text = '16',width=10)
    IntermediateHeight.grid(row=4,column=2)
    IntermediateWidth = Label(GameSetting_window,text = '16',width=10)
    IntermediateWidth.grid(row=4,column=3)
    IntermediateMines = Label(GameSetting_window,text = '40',width=10)
    IntermediateMines.grid(row=4,column=4)
    
    separator = ttk.Separator(GameSetting_window,orient=HORIZONTAL)
    separator.grid(row=5,columnspan=5,sticky=EW)
    
    Expert = Button(GameSetting_window,text = 'Expert',width=10,command = lambda: custom(16,30,99))
    Expert.grid(row=6,column=0)
    ExpertHeight = Label(GameSetting_window,text = '16',width=10)
    ExpertHeight.grid(row=6,column=2)
    ExpertWidth = Label(GameSetting_window,text = '30',width=10)
    ExpertWidth.grid(row=6,column=3)
    ExpertMines = Label(GameSetting_window,text = '99',width=10)
    ExpertMines.grid(row=6,column=4)
    
    separator = ttk.Separator(GameSetting_window,orient=HORIZONTAL)
    separator.grid(row=7,columnspan=5,sticky=EW)
    
    Custom = Button(GameSetting_window,text = 'Custom',width = 10, command = customEntry)
    Custom.grid(row=8,column=0)
    HeightEntry = Entry(GameSetting_window, width = 9)
    HeightEntry.focus()
    HeightEntry.grid(row=8,column=2)
    WidthEntry = Entry(GameSetting_window,width=9)
    WidthEntry.grid(row=8,column=3)
    MineEntry = Entry(GameSetting_window,width=9)
    MineEntry.grid(row=8,column=4)
    
def custom(CustomRows,CustomCols,CustomMines):
    global minegrid,cell,rows,cols,mines
    rows = CustomRows
    cols = CustomCols
    mines = CustomMines
    minegrid = []
    cell = []
    root.destroy()
    try:
        Win_window.destroy()
    except Exception:
        pass
    try:
        Lose_window.destroy()
    except Exception:
        pass
    return Window_setup(cols,rows)

def customEntry():
    global minegrid,cell,rows,cols,mines

    try:
        CustomRows = int(HeightEntry.get())
    except ValueError:
        return Error_Window()
    try:
        CustomCols = int(WidthEntry.get())
    except ValueError:
        return Error_Window()
    try:
        CustomMines = int(MineEntry.get())
    except ValueError:
        return Error_Window()
    
    if CustomRows < 40:
        rows = 40
    if CustomRows == 0:
        rows = 1
    else:
        rows = CustomRows
        
    if CustomCols < 40:
        cols = 40
    if CustomCols == 0:
        cols = 1
    else:
        cols = CustomCols
        
    if CustomMines < CustomRows*CustomCols/2:
        mines = CustomMines
    #if CustomMines == 0:
        #mines = 1
    else:
        mines = int(CustomRows*CustomCols/2)
    minegrid = []
    cell = []
    root.destroy()
    try:
        Win_window.destroy()
    except Exception:
        pass
    try:
        Lose_window.destroy()
    except Exception:
        pass
    try:
        ErrorWindow.destroy()
    except Exception:
        pass
    return Window_setup(cols,rows)

def Error_Window():
    global ErrorWindow
    ErrorWindow = Tk()
    WindowHeight = 30
    WindowWidth = 70
    ScreenHeight = ErrorWindow.winfo_screenheight()
    ScreenWidth = ErrorWindow.winfo_screenheight()
    x = (ScreenWidth/2)-(WindowWidth/2)
    y = (ScreenHeight/2)-(WindowHeight/2)
    ErrorWindow.geometry(f'{WindowWidth}x{WindowHeight}+{int(x)}+{int(y)}')
    label = Label(ErrorWindow,text = 'Error!')
    label.pack()
    
def restart():
    global minegrid,cell
    minegrid = []
    cell = []
    root.destroy()
    try:
        Win_window.destroy()
    except Exception:
        pass
    try:
        Lose_window.destroy()
    except Exception:
        pass
    return Window_setup(cols,rows)

def Exit():
    root.destroy()
    try:
        Win_window.destroy()
    except Exception:
        pass
    try:
        Lose_window.Destroy()
    except Exception:
        pass
    try:
        GameSetting_window.destroy()
    except Exception:
        pass
        
def floodfill(minegrid,idx):
    row = int(idx/cols)
    col = idx-row*cols
    if RevealState[row][col] != -1:
        value = minegrid[row][col]
        if value != 0:
            RevealState[row][col] = 1
        img = PhotoImage(file = 'tile_' + str(value) + '.png')
        cell[idx].configure(image = img)
        cell[idx].image = img
        if minegrid[row][col] == 0 and RevealState[row][col] == 0:
            RevealState[row][col] = 1
            if row > 0: #upp
                floodfill(minegrid,idx-cols)
                
            if row < rows-1:#ner
                floodfill(minegrid,idx+cols)
                
            if col > 0: #vänster
                floodfill(minegrid,idx-1)
                
            if col < cols-1: #höger
                floodfill(minegrid,idx+1)

            if row > 0 and col > 0: #upp till vänster
                floodfill(minegrid,idx-cols-1)

            if row > 0 and col < cols-1: #upp till höger
                floodfill(minegrid,idx-cols+1)

            if row < rows-1 and col > 0: #ner till vänster
                floodfill(minegrid,idx+cols-1)

            if row < rows-1 and col < cols-1: #ner till höger
                floodfill(minegrid,idx+cols+1)

        CellsClicked = sum(row.count(1) for row in RevealState)
        if CellsClicked == (rows*cols-mines):
            Win(idx)
        
    
def left_click(event,idx): #funktion som säger att när man vänsterklickar ska rutan avslöjas 
    row = int(idx/cols)
    col = idx-row*cols
    value = minegrid[row][col]
    if  RevealState[row][col] != -1:
        if value == 0:
            floodfill(minegrid,idx)
        else:
            RevealState[row][col] = 1
            if value >= 0:
                img = PhotoImage(file = 'tile_' + str(value) + '.png')
            
            if (cell[idx],minegrid[row][col]) == (cell[idx],-1):
                cell[idx].configure(image = img_Mine)
                cell[idx].image= img_Mine
                Lose(idx)
            else:
                cell[idx].configure(image = img)
                cell[idx].image= img
            CellsClicked = sum(row.count(1) for row in RevealState)
            if CellsClicked == (rows*cols-mines):
                Win(idx)
            
def FocusCell(event,idx):
    cell[idx].focus()
    cell[idx].bind('<space>', partial(right_click,idx=idx))

def right_click(event,idx): # en funktion som säger att vid högerklick så ska en flagga placeras vid den cellen
    row = int(idx/cols)
    col = idx-row*cols
    if RevealState[row][col] == 0:
        cell[idx].configure(image = img_Flagged)
        cell[idx].image= img_Flagged
        RevealState[row][col] = -1
        global mines_flagged
        row = int(idx/cols)
        col = idx-row*cols
        
        if (cell[idx],minegrid[row][col]) == (cell[idx],-1):
            mines_flagged += 1
            if mines_flagged == mines:
                Win(idx)

    elif RevealState[row][col] != 0 and RevealState[row][col] != 1:
        cell[idx].configure(image = img_Plain)
        cell[idx].image= img_Plain
        RevealState[row][col] = 0
        
def Start_Time():
    global StartTime
    StartTime = time()

def Stop_Time():
    global StopTime
    StopTime = time()

def Play_Time(Name):
    Time = round(StopTime-StartTime,1)
    if rows == 9 and cols == 9 and mines == 10:
        file = open('HighScores_Beginner.txt','a')
        text = str(Time) + ' ' + str(Name) + '\n'
        file.write(text)
    if rows == 16 and cols == 16 and mines == 40:
        file = open('HighScores_Intermediate.txt','a')
        text = Time + ' ' + Name + '\n'
        file.write(text)
    if cols == 16 and rows == 30 and mines == 99:
        file = open('HighScores_Expert.txt','a')
        text = Time + ' ' + Name + '\n'
        file.write(text)
    else:
        file = open('HighScores.txt','a')
        text ='Name:'+ Name + ' Rows:' + str(rows) + ' Cols:' + str(cols) +' Mines:' + str(mines)+' Time:'+str(Time)+'s'+'\n'
        file.write(text)


def Win(idx): #En funktion som ska ge ett meddelande till spelaren när den har vunnit, genom att alla minor är flaggade eller alla icke minor är röjda
    global Win_window, StopTime, NameEntry 
    Stop_Time()
    Win_window = Tk()
    Win_window.title('')
    WindowHeight = 50
    WindowWidth = 150
    ScreenHeight = Win_window.winfo_screenheight()
    ScreenWidth = Win_window.winfo_screenheight()
    x = (ScreenWidth/2)-(WindowWidth/2)
    y = (ScreenHeight/2)-(WindowHeight/2)
    Win_window.geometry(f'{WindowWidth}x{WindowHeight}+{int(x)}+{int(y)}')
    label = Label(Win_window,text = 'You Won', fg='green')
    label.pack()
    frame = Frame(Win_window)
    frame.pack()
    label = Button(Win_window, text = 'Enter Name', command = CallPlay_Time)
    #label.bind('<button-1>', Win_window.destroy()
    label.pack(side = LEFT)
    NameEntry = Entry(Win_window, width = 10)
    NameEntry.pack(side = LEFT)
    
    
    
def Lose(idx): #en funktion som kallas när spelaren har klickat på en mina som signalerar att spelaren har förlorat samt avslöjar spelbrädet
    global Lose_window
    Lose_window = Tk()
    Lose_window.title('')
    WindowHeight = 50
    WindowWidth = 150
    ScreenHeight = Lose_window.winfo_screenheight()
    ScreenWidth = Lose_window.winfo_screenheight()
    x = (ScreenWidth/2)-(WindowWidth/2)
    y = (ScreenHeight/2)-(WindowHeight/2)
    Lose_window.geometry(f'{WindowWidth}x{WindowHeight}+{int(x)}+{int(y)}')
    label = Label(Lose_window,text = 'Game Over')
    label.pack()
    Restart = Button(Lose_window, text = 'Restart',command = restart)
    Restart.pack()
    for i in range(len(cell)):
        idx=i
        row = int(idx/cols)
        col = idx-row*cols
        value = minegrid[row][col]
        #if value >= 0:
            #img = PhotoImage(file = 'tile_' + str(value) + '.png')
    
        if RevealState[row][col] != -1 and (cell[idx],minegrid[row][col]) == (cell[idx],-1):
            cell[idx].configure(image = img_Mine)
            cell[idx].image= img_Mine
        elif RevealState[row][col] == -1:
            cell[idx].configure(image = img_Flagged)
            cell[idx].image= img_Flagged
        else:
            pass
            #cell[idx].configure(image = img)
            #cell[idx].image= img
        
class Highscore:
    def __init__(self,tid, namn):
        self.namn = namn
        self.tid = tid
    def namn(self):
        return self.namn
    def tid(self):
        return self.tid
    def __str__(self):
        return str(self.namn) + ' ' + str(self.tid)
    
def HighscoreList(file):
    global HighList
    li = []
    HighList = []
    elements = 0
    for i in file:
        i = i.split()
        for j in i:
            li.append(j)
            elements += 1
    for i in range(len(li)):
        if i < elements/2:
            Scores = Highscore(li[i*2],li[i*2+1])
            HighList.append(Scores)
    HighList.sort(key=lambda Highscore: Highscore.tid) 


Window_setup(cols,rows)
