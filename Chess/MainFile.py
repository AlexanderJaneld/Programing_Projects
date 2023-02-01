from tkinter import *
from functools import partial


cell = []
PiecesClicked = 0
Pieces = []
WhoTurn = 'white'
def Board_Setup():
    global tile_array
    #List1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    tile_array = []

    for i in range(8):
        L = []
        for j in range(8):
            # Bestämmer positionen av brickan, genom standardiserade shack nomenklaturen
            #position = str(List1[j]) + str(i+1)
            index = i*8 + j
            # bestämmer färgen på brickan så att vi får ett rut mönster
            if i % 2 == 0:
                if j % 2 == 0:
                    colour = 'dark'
                else:
                    colour = 'light'
            else:
                if j % 2 == 0:
                    colour = 'light'
                else:
                    colour = 'dark'

            L.append(tile('null',colour, index, 'empty'))
        tile_array.append(L)
    tile_array.reverse()
    white_piece_setup()

def white_piece_setup():
    # White pieces
    global Queen_d1, Rook_a1, Rook_h1, Bishop_c1, Bishop_f1, King_e1, Knight_b1, Knight_g1, white_pawns
    colour = 'white'
    status = 'alive'
    white_pawns = []
    # Queen
    Queen_d1 = Queen(status,'d1',colour,59,4)
    tile_array[7][3].status = 'taken'
    Pieces.append(Queen_d1)

    # Rooks
    Rook_a1 = Rook(status,'a1',colour,56,1)
    Rook_h1 = Rook(status,'h1',colour,63,8)
    tile_array[7][0].status = 'taken'
    tile_array[7][7].status = 'taken'
    Pieces.append(Rook_a1)
    Pieces.append(Rook_h1)

    # Bishop
    Bishop_c1 = Bishop(status,'c1',colour,58,3)
    Bishop_f1 = Bishop(status,'f1',colour,61,6)
    tile_array[7][2].status = 'taken'
    tile_array[7][5].status = 'taken'
    Pieces.append(Bishop_c1)
    Pieces.append(Bishop_f1)

    # King
    King_e1 = King(status,'e1',colour,60,5)
    tile_array[7][4].status = 'taken'
    Pieces.append(King_e1)

    # Knights
    Knight_b1 = Knight(status,'b1',colour,57,2)
    Knight_g1 = Knight(status,'g1',colour,62,7)
    tile_array[7][1].status = 'taken'
    tile_array[7][6].status = 'taken'
    Pieces.append(Knight_b1)
    Pieces.append(Knight_g1)

    # Pawns
    for i in range(8):
        position = 'null'
        index = 48 + i
        id = 9 + i
        white_pawns.append(Pawn(status, position, colour, index, id,'true'))
        tile_array[6][i].status = 'taken'
    for i in range(8):
        Pieces.append(white_pawns[i])
    black_piece_setup()

def black_piece_setup():
    # White pieces
    global Queen_d8, Rook_a8, Rook_h8, Bishop_c8, Bishop_f8, King_e8, Knight_b8, Knight_g8, black_pawns
    colour = 'black'
    status = 'alive'
    black_pawns = []
    # Queen
    Queen_d8 = Queen(status,'d8',colour,3,28)
    tile_array[0][3].status = 'taken'
    Pieces.append(Queen_d8)

    # Rooks
    Rook_a8 = Rook(status,'a8',colour,0,25)
    Rook_h8 = Rook(status,'h8',colour,7,32)
    tile_array[0][0].status = 'taken'
    tile_array[0][7].status = 'taken'
    Pieces.append(Rook_a8)
    Pieces.append(Rook_h8)

    # Bishop
    Bishop_c8 = Bishop(status,'c8',colour,2,27)
    Bishop_f8 = Bishop(status,'f8',colour,5,30)
    tile_array[0][2].status = 'taken'
    tile_array[0][5].status = 'taken'
    Pieces.append(Bishop_c8)
    Pieces.append(Bishop_f8)

    # King
    King_e8 = King(status,'e8',colour,4,29)
    tile_array[0][4].status = 'taken'
    Pieces.append(King_e8)

    # Knights
    Knight_b8 = Knight(status,'b8',colour,1,26)
    Knight_g8 = Knight(status,'g8',colour,6,31)
    tile_array[0][1].status = 'taken'
    tile_array[0][6].status = 'taken'
    Pieces.append(Knight_b8)
    Pieces.append(Knight_g8)

    # Pawns
    for i in range(8):
        position = 'null'
        index = 8 + i
        id = 17 + i
        black_pawns.append(Pawn(status, position, colour, index, id,'true'))
        tile_array[1][i].status = 'taken'
    for i in range(8):
        Pieces.append(black_pawns[i])
    window_setup()

def window_setup():
    global EmptyDark, EmptyLight, WhitePawnOnDark, WhitePawnOnWhite, BlackPawnOnWhite, BlackPawnOnDark
    global WhiteRookOnWhite, WhiteRookOnDark, BlackRookOnWhite, BlackRookOnDark
    global WhiteKnightOnWhite, WhiteKnightOnDark, BlackKnightOnWhite, BlackKnightOnDark
    global WhiteBishopOnWhite, WhiteBishopOnDark, BlackBishopOnWhite, BlackBishopOnDark
    global WhiteKingOnWhite, WhiteKingOnDark, BlackKingOnWhite, BlackKingOnDark
    global WhiteQueenOnWhite, WhiteQueenOnDark, BlackQueenOnWhite, BlackQueenOnDark

    root = Tk()
    root.title('Chess')
    Board_frame = LabelFrame(root)
    Board_frame.pack()
    EmptyDark = PhotoImage(file='EmptyDark.png')
    EmptyLight = PhotoImage(file='EmptyLight.png')
    # Pawns
    WhitePawnOnDark = PhotoImage(file ='WhitePawnOnDark.png' )
    WhitePawnOnWhite = PhotoImage(file='WhitePawnOnWhite.png')
    BlackPawnOnWhite = PhotoImage(file='BlackPawnOnWhite.png')
    BlackPawnOnDark = PhotoImage(file='BlackPawnOnDark.png')
    for i in range(8):
        for j in range(8):
            index = i * 8 + j
            cell.append(index)
            if i % 2 == 0:
                if j % 2 == 0:
                    cell[index] = Label(Board_frame,image = EmptyLight, borderwidth=0)
                    cell[index].image = EmptyLight
                else:
                    cell[index] = Label(Board_frame, image=EmptyDark, borderwidth=0)
                    cell[index].image = EmptyDark
            else:
                if j % 2 == 0:
                    cell[index] = Label(Board_frame, image=EmptyDark, borderwidth=0)
                    cell[index].image = EmptyDark
                else:
                    cell[index] = Label(Board_frame, image=EmptyLight, borderwidth=0)
                    cell[index].image = EmptyLight
            cell[index].bind('<Button-1>', partial(left_click, idx=index))
            cell[index].grid(row=i + 1, column=j)
    for j in range(48,56):
        if j % 2 == 0:
            cell[j].configure(image = WhitePawnOnWhite)
        else:
            cell[j].configure(image=WhitePawnOnDark)
    for j in range(8,16):
        if j % 2 == 0:
            cell[j].configure(image = BlackPawnOnDark)
        else:
            cell[j].configure(image=BlackPawnOnWhite)
    # Rooks
    WhiteRookOnWhite = PhotoImage(file='WhiteRookOnWhite.png')
    WhiteRookOnDark = PhotoImage(file='WhiteRookOnDark.png')
    BlackRookOnWhite = PhotoImage( file = 'BlackRookOnWhite.png')
    BlackRookOnDark = PhotoImage(file='BlackRookOnDark.png')
    cell[56].configure(image = WhiteRookOnDark)
    cell[63].configure(image = WhiteRookOnWhite)
    cell[0].configure(image = BlackRookOnWhite)
    cell[7].configure(image = BlackRookOnDark)

    # Knights
    WhiteKnightOnWhite = PhotoImage(file='WhiteKnightOnWhite.png' )
    WhiteKnightOnDark = PhotoImage(file='WhiteKnightOnDark.png')
    BlackKnightOnWhite = PhotoImage(file='BlackKnightOnwhite.png')
    BlackKnightOnDark = PhotoImage(file='BlackKnightOnDark.png')
    cell[57].configure(image = WhiteKnightOnWhite)
    cell[62].configure(image = WhiteKnightOnDark)
    cell[1].configure(image = BlackKnightOnDark)
    cell[6].configure(image = BlackKnightOnWhite)

    # Bishops
    WhiteBishopOnWhite = PhotoImage(file='WhiteBishopOnWhite.png')
    WhiteBishopOnDark = PhotoImage(file='WhiteBishopOnDark.png')
    BlackBishopOnWhite = PhotoImage(file='BlackBishopOnWhite.png')
    BlackBishopOnDark = PhotoImage(file='BlackBishopOnDark.png')

    cell[58].configure(image = WhiteBishopOnDark)
    cell[61].configure(image = WhiteBishopOnWhite)
    cell[2].configure(image = BlackBishopOnWhite)
    cell[5].configure(image = BlackBishopOnDark)

    # Queen
    WhiteQueenOnWhite = PhotoImage(file='WhiteQueenOnWhite.png')
    WhiteQueenOnDark = PhotoImage(file='WhiteQueenOnDark.png')
    BlackQueenOnWhite = PhotoImage(file='BlackQueenOnWhite.png')
    BlackQueenOnDark = PhotoImage(file='BlackQueenOnDark.png')

    cell[59].configure(image = WhiteQueenOnWhite)
    cell[3].configure(image = BlackQueenOnDark)

    # King
    WhiteKingOnWhite = PhotoImage(file='WhiteKingOnWhite.png')
    WhiteKingOnDark = PhotoImage(file='WhiteKingOnDark.png')
    BlackKingOnWhite = PhotoImage(file='BlackkingOnWhite.png')
    BlackKingOnDark = PhotoImage(file='BlackKingOnDark.png')

    cell[60].configure(image = WhiteKingOnDark)
    cell[4].configure(image = BlackKingOnWhite)
    root.mainloop()



def left_click(event, idx):
    global ClickedWhiteKingOnWhite, ClickedWhiteKingOnDark, ClickedBlackKingOnWhite, ClickedBlackKingOnDark
    global MovementOnWhite, MovementOnDark, PiecesClicked, WhoTurn
    ClickedWhiteKingOnWhite = PhotoImage(file='ClickedWhiteKingOnWhite.png')
    ClickedWhiteKingOnDark = PhotoImage(file='ClickedWhiteKingOnDark.png')
    ClickedBlackKingOnWhite = PhotoImage(file='ClickedBlackKingOnWhite.png')
    ClickedBlackKingOnDark = PhotoImage(file='ClickedBlackKingOnDark.png')
    MovementOnWhite = PhotoImage(file='MovementOnWhite.png')
    MovementOnDark = PhotoImage(file='MovementOnDark.png')
    ClickedWhiteQueenOnWhite = PhotoImage(file='ClickedWhiteQueenOnWhite.png')
    ClickedWhiteQueenOnDark = PhotoImage(file='ClickedWhiteQueenOnDark.png')
    ClickedBlackQueenOnWhite = PhotoImage(file='ClickedBlackQueenOnWhite.png')
    ClickedBlackQueenOnDark = PhotoImage(file='ClickedBlackQueenOnDark.png')
    ClickedWhitePawnOnWhite = PhotoImage(file='ClickedWhitePawnOnWhite.png')
    ClickedWhitePawnOnDark = PhotoImage(file='ClickedWhitePawnOnDark.png')
    ClickedBlackPawnOnWhite = PhotoImage(file='ClickedBlackPawnOnWhite.png')
    ClickedBlackPawnOnDark = PhotoImage(file='ClickedBlackPawnOnDark.png')
    ClickedWhiteBishopOnWhite = PhotoImage(file='ClickedWhiteBishopOnWhite.png')
    ClickedWhiteBishopOnDark = PhotoImage(file='ClickedWhiteBishopOnDark.png')
    ClickedBlackBishopOnWhite = PhotoImage(file='ClickedBlackBishopOnWhite.png')
    ClickedBlackBishopOnDark = PhotoImage(file='ClickedBlackBishopOnDark.png')
    ClickedWhiteKnightOnWhite = PhotoImage(file='ClickedWhiteKnightOnWhite.png')
    ClickedWhiteKnightOnDark = PhotoImage(file='CLickedWhiteKnightOnDark.png')
    ClickedBlackKnightOnWhite = PhotoImage(file='CLickedBlackKnightOnWhite.png')
    ClickedBlackKnightOnDark = PhotoImage(file='CLickedBlackKnightOnDark.png')
    ClickedWhiteRookOnWhite = PhotoImage(file='ClickedWhiteRookOnWhite.png')
    ClickedWhiteRookOnDark = PhotoImage(file='ClickedWhiteRookOnDark.png')
    ClickedBlackRookOnWhite = PhotoImage(file='ClickedBlackRookOnWhite.png')
    ClickedBlackRookOnDark = PhotoImage(file='ClickedBlackRookOnDark.png')
    cols = 8
    rows = 8
    row = int(idx / cols)
    col = idx - row * cols

    for i in range(len(Pieces)):
        if Pieces[i].index == idx:
            KillPiece = Pieces[i]
    if PiecesClicked == 1:
        for i in range(len(Pieces)):
            if Pieces[i].status == 'clicked':
                ClickedPiece = Pieces[i]

    if tile_array[row][col].status == 'taken':
        for i in range(len(Pieces)):
            if Pieces[i].index == idx:
                Piece = Pieces[i]
                if Piece.id == 1 or Piece.id == 8:  # White Rooks
                    if PiecesClicked == 0 and WhoTurn == 'white':
                        if tile_array[row][col].colour == 'light':
                            cell[idx].configure(image=ClickedWhiteRookOnWhite)
                            cell[idx].image = ClickedWhiteRookOnWhite
                        else:
                            cell[idx].configure(image=ClickedWhiteRookOnDark)
                            cell[idx].image = ClickedWhiteRookOnDark
                        Piece.status = 'clicked'
                        PiecesClicked = 1
                        AxialPossibleMoves(idx)
                    elif Piece.status == 'clicked' and WhoTurn == 'white':
                        if tile_array[row][col].colour == 'light':
                            cell[idx].configure(image=WhiteRookOnWhite)
                            cell[idx].image = WhiteRookOnWhite
                        else:
                            cell[idx].configure(image=WhiteRookOnDark)
                            cell[idx].image = WhiteRookOnDark
                        Piece.status = 'alive'
                        PiecesClicked = 0
                        RemoveMovementImages()

                if Piece.id == 25 or Piece.id == 32:  # Black Rooks
                    if PiecesClicked == 0 and WhoTurn == 'black':
                        if tile_array[row][col].colour == 'light':
                            cell[idx].configure(image=ClickedBlackRookOnWhite)
                            cell[idx].image = ClickedBlackRookOnWhite
                        else:
                            cell[idx].configure(image=ClickedBlackRookOnDark)
                            cell[idx].image = ClickedBlackRookOnDark
                        Piece.status = 'clicked'
                        PiecesClicked = 1
                        AxialPossibleMoves(idx)
                    elif Piece.status == 'clicked' and WhoTurn == 'black':
                        if tile_array[row][col].colour == 'light':
                            cell[idx].configure(image=BlackRookOnWhite)
                            cell[idx].image = BlackRookOnWhite
                        else:
                            cell[idx].configure(image=BlackRookOnDark)
                            cell[idx].image = BlackRookOnDark
                        Piece.status = 'alive'
                        PiecesClicked = 0
                        RemoveMovementImages()


                if Piece.id == 5 and WhoTurn == 'white': # White King
                    if PiecesClicked == 0:
                        if tile_array[row][col].colour == 'light':
                            cell[idx].configure(image=ClickedWhiteKingOnWhite)
                            cell[idx].image = ClickedWhiteKingOnWhite
                        else:
                            cell[idx].configure(image=ClickedWhiteKingOnDark)
                            cell[idx].image = ClickedWhiteKingOnDark
                        Piece.status = 'clicked'
                        PiecesClicked = 1
                        for i in range(64):
                            MoveRow = int(i / cols)
                            MoveCol = i - MoveRow * cols
                            if tile_array[MoveRow][MoveCol].status == 'empty':
                                if col == MoveCol or col - 1 == MoveCol or col + 1 == MoveCol:
                                    if row == MoveRow or row - 1 == MoveRow or row + 1 == MoveRow:
                                        if tile_array[MoveRow][MoveCol].colour == 'light':
                                            cell[i].configure(image=MovementOnWhite)
                                            cell[i].image = MovementOnWhite
                                        else:
                                            cell[i].configure(image=MovementOnDark)
                                            cell[i].image = MovementOnDark
                                        tile_array[MoveRow][MoveCol].status = 'movable'
                            elif tile_array[MoveRow][MoveCol].status == 'taken':
                                if col == MoveCol or col - 1 == MoveCol or col + 1 == MoveCol:
                                    if row == MoveRow or row - 1 == MoveRow or row + 1 == MoveRow:
                                        tile_array[MoveRow][MoveCol].status = 'killable'
                    elif Piece.status == 'clicked' and WhoTurn == 'white':
                        if tile_array[row][col].colour == 'light':
                            cell[idx].configure(image=WhiteKingOnWhite)
                            cell[idx].image = WhiteKingOnWhite
                        else:
                            cell[idx].configure(image=WhiteKingOnDark)
                            cell[idx].image = WhiteKingOnDark
                        Piece.status = 'alive'
                        PiecesClicked = 0
                        RemoveMovementImages()

                if Piece.id == 29 and WhoTurn == 'black':  # Black King
                    if PiecesClicked == 0:
                        if tile_array[row][col].colour == 'light':
                            cell[idx].configure(image=ClickedBlackKingOnWhite)
                            cell[idx].image = ClickedBlackKingOnWhite
                        else:
                            cell[idx].configure(image=ClickedBlackKingOnDark)
                            cell[idx].image = ClickedBlackKingOnDark
                        Piece.status = 'clicked'
                        PiecesClicked = 1
                        for i in range(64):
                            MoveRow = int(i / cols)
                            MoveCol = i - MoveRow * cols
                            if tile_array[MoveRow][MoveCol].status == 'empty':
                                if col == MoveCol or col - 1 == MoveCol or col + 1 == MoveCol:
                                    if row == MoveRow or row - 1 == MoveRow or row + 1 == MoveRow:
                                        if tile_array[MoveRow][MoveCol].colour == 'light':
                                            cell[i].configure(image=MovementOnWhite)
                                            cell[i].image = MovementOnWhite
                                        else:
                                            cell[i].configure(image=MovementOnDark)
                                            cell[i].image = MovementOnDark
                                        tile_array[MoveRow][MoveCol].status = 'movable'
                            elif tile_array[MoveRow][MoveCol].status == 'taken':
                                if col == MoveCol or col - 1 == MoveCol or col + 1 == MoveCol:
                                    if row == MoveRow or row - 1 == MoveRow or row + 1 == MoveRow:
                                        tile_array[MoveRow][MoveCol].status = 'killable'
                    elif Piece.status == 'clicked' and WhoTurn == 'black':
                        print('made it here')
                        if tile_array[row][col].colour == 'light':
                            cell[idx].configure(image=BlackKingOnWhite)
                            cell[idx].image = BlackKingOnWhite
                        else:
                            cell[idx].configure(image=BlackKingOnDark)
                            cell[idx].image = BlackKingOnDark
                        Piece.status = 'alive'
                        PiecesClicked = 0
                        RemoveMovementImages()

                if Piece.id == 2 or Piece.id == 7: # White Knight
                    if PiecesClicked == 0 and  WhoTurn == 'white':
                        if tile_array[row][col].colour == 'light':
                            cell[idx].configure(image=ClickedWhiteKnightOnWhite)
                            cell[idx].image = ClickedWhiteKnightOnWhite
                        else:
                            cell[idx].configure(image=ClickedWhiteKnightOnDark)
                            cell[idx].image = ClickedWhiteKnightOnDark
                        Piece.status = 'clicked'
                        PiecesClicked = 1
                        for i in range(64):
                            MoveRow = int(i / cols)
                            MoveCol = i - MoveRow * cols
                            if tile_array[MoveRow][MoveCol].status == 'empty':
                                if row + 2 == MoveRow or row - 2 == MoveRow:
                                    if col + 1 == MoveCol or col - 1 == MoveCol:
                                        if tile_array[MoveRow][MoveCol].colour == 'light':
                                            cell[i].configure(image=MovementOnWhite)
                                            cell[i].image = MovementOnWhite
                                        else:
                                            cell[i].configure(image=MovementOnDark)
                                            cell[i].image = MovementOnDark
                                        tile_array[MoveRow][MoveCol].status = 'movable'
                                if row + 1 == MoveRow or row - 1 == MoveRow:
                                    if col + 2 == MoveCol or col - 2 == MoveCol:
                                        if tile_array[MoveRow][MoveCol].colour == 'light':
                                            cell[i].configure(image=MovementOnWhite)
                                            cell[i].image = MovementOnWhite
                                        else:
                                            cell[i].configure(image=MovementOnDark)
                                            cell[i].image = MovementOnDark
                                        tile_array[MoveRow][MoveCol].status = 'movable'
                            elif tile_array[MoveRow][MoveCol].status == 'taken':
                                if row + 2 == MoveRow or row - 2 == MoveRow:
                                    if col + 1 == MoveCol or col - 1 == MoveCol:
                                        tile_array[MoveRow][MoveCol].status = 'killable'
                                if row + 1 == MoveRow or row - 1 == MoveRow:
                                    if col + 2 == MoveCol or col - 2 == MoveCol:
                                        tile_array[MoveRow][MoveCol].status = 'killable'
                    elif Piece.status == 'clicked' and WhoTurn == 'white':
                        if tile_array[row][col].colour == 'light':
                            cell[idx].configure(image=WhiteKnightOnWhite)
                            cell[idx].image = WhiteKnightOnWhite
                        else:
                            cell[idx].configure(image=WhiteKnightOnDark)
                            cell[idx].image = WhiteKnightOnDark
                        Piece.status = 'alive'
                        PiecesClicked = 0
                        RemoveMovementImages()
                if Piece.id == 26 or Piece.id == 31: # Black Knight
                    if PiecesClicked == 0 and  WhoTurn == 'black':
                        if tile_array[row][col].colour == 'light':
                            cell[idx].configure(image=ClickedBlackKnightOnWhite)
                            cell[idx].image = ClickedBlackKnightOnWhite
                        else:
                            cell[idx].configure(image=ClickedBlackKnightOnDark)
                            cell[idx].image = ClickedBlackKnightOnDark
                        Piece.status = 'clicked'
                        PiecesClicked = 1
                        for i in range(64):
                            MoveRow = int(i / cols)
                            MoveCol = i - MoveRow * cols
                            if tile_array[MoveRow][MoveCol].status == 'empty':
                                if row + 2 == MoveRow or row - 2 == MoveRow:
                                    if col + 1 == MoveCol or col - 1 == MoveCol:
                                        if tile_array[MoveRow][MoveCol].colour == 'light':
                                            cell[i].configure(image=MovementOnWhite)
                                            cell[i].image = MovementOnWhite
                                        else:
                                            cell[i].configure(image=MovementOnDark)
                                            cell[i].image = MovementOnDark
                                        tile_array[MoveRow][MoveCol].status = 'movable'
                                if row + 1 == MoveRow or row - 1 == MoveRow:
                                    if col + 2 == MoveCol or col - 2 == MoveCol:
                                        if tile_array[MoveRow][MoveCol].colour == 'light':
                                            cell[i].configure(image=MovementOnWhite)
                                            cell[i].image = MovementOnWhite
                                        else:
                                            cell[i].configure(image=MovementOnDark)
                                            cell[i].image = MovementOnDark
                                        tile_array[MoveRow][MoveCol].status = 'movable'
                            elif tile_array[MoveRow][MoveCol].status == 'taken':
                                if row + 2 == MoveRow or row - 2 == MoveRow:
                                    if col + 1 == MoveCol or col - 1 == MoveCol:
                                        tile_array[MoveRow][MoveCol].status = 'killable'
                                if row + 1 == MoveRow or row - 1 == MoveRow:
                                    if col + 2 == MoveCol or col - 2 == MoveCol:
                                        tile_array[MoveRow][MoveCol].status = 'killable'
                    elif Piece.status == 'clicked' and WhoTurn == 'black':
                        if tile_array[row][col].colour == 'light':
                            cell[idx].configure(image=BlackKnightOnWhite)
                            cell[idx].image = BlackKnightOnWhite
                        else:
                            cell[idx].configure(image=BlackKnightOnDark)
                            cell[idx].image = BlackKnightOnDark
                        Piece.status = 'alive'
                        PiecesClicked = 0
                        RemoveMovementImages()

                if Piece.id >= 9 and Piece.id <=16 and WhoTurn == 'white': # White Pawns
                    if PiecesClicked == 0:
                        if tile_array[row][col].colour == 'light':
                            cell[idx].configure(image=ClickedWhitePawnOnWhite)
                            cell[idx].image = ClickedWhitePawnOnWhite
                        else:
                            cell[idx].configure(image=ClickedWhitePawnOnDark)
                            cell[idx].image = ClickedWhitePawnOnDark
                        Piece.status = 'clicked'
                        PiecesClicked = 1
                        for i in range(64):
                            MoveRow = int(i / cols)
                            MoveCol = i - MoveRow * cols
                            if tile_array[MoveRow][MoveCol].status == 'empty':
                                if Piece.firstmove == 'true':
                                    if col == MoveCol:
                                        if row == MoveRow + 2 or row == MoveRow + 1:
                                            if tile_array[MoveRow][MoveCol].colour == 'light':
                                                cell[i].configure(image=MovementOnWhite)
                                                cell[i].image = MovementOnWhite
                                            else:
                                                cell[i].configure(image=MovementOnDark)
                                                cell[i].image = MovementOnDark
                                            tile_array[MoveRow][MoveCol].status = 'movable'
                                else:
                                    if col == MoveCol and row == MoveRow + 1:
                                        if tile_array[MoveRow][MoveCol].colour == 'light':
                                            cell[i].configure(image=MovementOnWhite)
                                            cell[i].image = MovementOnWhite
                                        else:
                                            cell[i].configure(image=MovementOnDark)
                                            cell[i].image = MovementOnDark
                                        tile_array[MoveRow][MoveCol].status = 'movable'
                            elif tile_array[MoveRow][MoveCol].status == 'taken':
                                if row == MoveRow + 1:
                                    if col == MoveCol - 1 or col == MoveCol + 1:
                                        tile_array[MoveRow][MoveCol].status = 'killable'
                    elif Piece.status == 'clicked':
                        if tile_array[row][col].colour == 'light':
                            cell[idx].configure(image=WhitePawnOnWhite)
                            cell[idx].image = WhitePawnOnWhite
                        else:
                            cell[idx].configure(image=WhitePawnOnDark)
                            cell[idx].image = WhitePawnOnDark
                        Piece.status = 'alive'
                        PiecesClicked = 0
                        RemoveMovementImages()

                if Piece.id >= 17 and Piece.id <=24 and WhoTurn == 'black': # Black Pawns
                    if PiecesClicked == 0:
                        if tile_array[row][col].colour == 'light':
                            cell[idx].configure(image=ClickedBlackPawnOnWhite)
                            cell[idx].image = ClickedBlackPawnOnWhite
                        else:
                            cell[idx].configure(image=ClickedBlackPawnOnDark)
                            cell[idx].image = ClickedBlackPawnOnDark
                        Piece.status = 'clicked'
                        PiecesClicked = 1
                        for i in range(64):
                            MoveRow = int(i / cols)
                            MoveCol = i - MoveRow * cols
                            if tile_array[MoveRow][MoveCol].status == 'empty':
                                if Piece.firstmove == 'true':
                                    if col == MoveCol:
                                        if row == MoveRow - 2 or row == MoveRow - 1:
                                            if tile_array[MoveRow][MoveCol].colour == 'light':
                                                cell[i].configure(image=MovementOnWhite)
                                                cell[i].image = MovementOnWhite
                                            else:
                                                cell[i].configure(image=MovementOnDark)
                                                cell[i].image = MovementOnDark
                                            tile_array[MoveRow][MoveCol].status = 'movable'
                                else:
                                    if col == MoveCol and row == MoveRow - 1:
                                        if tile_array[MoveRow][MoveCol].colour == 'light':
                                            cell[i].configure(image=MovementOnWhite)
                                            cell[i].image = MovementOnWhite
                                        else:
                                            cell[i].configure(image=MovementOnDark)
                                            cell[i].image = MovementOnDark
                                        tile_array[MoveRow][MoveCol].status = 'movable'
                            elif tile_array[MoveRow][MoveCol].status == 'taken':
                                if row == MoveRow - 1:
                                    if col == MoveCol - 1 or col == MoveCol + 1:
                                        tile_array[MoveRow][MoveCol].status = 'killable'
                    elif Piece.status == 'clicked':
                        if tile_array[row][col].colour == 'light':
                            cell[idx].configure(image=BlackPawnOnWhite)
                            cell[idx].image = BlackPawnOnWhite
                        else:
                            cell[idx].configure(image=BlackPawnOnDark)
                            cell[idx].image = BlackPawnOnDark
                        Piece.status = 'alive'
                        PiecesClicked = 0
                        RemoveMovementImages()

                if Piece.id == 4 and WhoTurn == 'white': # White Queen
                    if PiecesClicked == 0:
                        if tile_array[row][col].colour == 'light':
                            cell[idx].configure(image=ClickedWhiteQueenOnWhite)
                            cell[idx].image = ClickedWhiteQueenOnWhite
                        else:
                            cell[idx].configure(image=ClickedWhiteQueenOnDark)
                            cell[idx].image = ClickedWhiteQueenOnDark
                        Piece.status = 'clicked'
                        PiecesClicked = 1
                        DiagonalPossibleMoves(idx)
                        AxialPossibleMoves(idx)
                    elif idx == Queen_d1.index and Queen_d1.status == 'clicked':
                        if tile_array[row][col].colour == 'light':
                            cell[idx].configure(image=WhiteQueenOnWhite)
                            cell[idx].image = WhiteQueenOnWhite
                        else:
                            cell[idx].configure(image=WhiteQueenOnDark)
                            cell[idx].image = WhiteQueenOnDark
                        Piece.status = 'alive'
                        PiecesClicked = 0
                        RemoveMovementImages()

                if Piece.id == 28 and WhoTurn == 'black': # Black Queen
                    if PiecesClicked == 0:
                        if tile_array[row][col].colour == 'light':
                            cell[idx].configure(image=ClickedBlackQueenOnWhite)
                            cell[idx].image = ClickedBlackQueenOnWhite
                        else:
                            cell[idx].configure(image=ClickedBlackQueenOnDark)
                            cell[idx].image = ClickedBlackQueenOnDark
                        Piece.status = 'clicked'
                        PiecesClicked = 1
                        DiagonalPossibleMoves(idx)
                        AxialPossibleMoves(idx)
                    elif Piece.status == 'clicked':
                        if tile_array[row][col].colour == 'light':
                            cell[idx].configure(image=BlackQueenOnWhite)
                            cell[idx].image = BlackQueenOnWhite
                        else:
                            cell[idx].configure(image=BlackQueenOnDark)
                            cell[idx].image = BlackQueenOnDark
                        Piece.status = 'alive'
                        PiecesClicked = 0
                        RemoveMovementImages()

                if Piece.id == 3 or Piece.id == 6: # White Bishop
                    if PiecesClicked == 0 and WhoTurn == 'white':
                        if tile_array[row][col].colour == 'light':
                            cell[idx].configure(image=ClickedWhiteBishopOnWhite)
                            cell[idx].image = ClickedWhiteBishopOnWhite
                        else:
                            cell[idx].configure(image=ClickedWhiteBishopOnDark)
                            cell[idx].image = ClickedWhiteBishopOnDark
                        Piece.status = 'clicked'
                        PiecesClicked = 1
                        DiagonalPossibleMoves(idx)
                    elif Piece.status == 'clicked' and WhoTurn == 'white':
                        if tile_array[row][col].colour == 'light':
                            cell[idx].configure(image=WhiteBishopOnWhite)
                            cell[idx].image = WhiteBishopOnWhite
                        else:
                            cell[idx].configure(image=WhiteBishopOnDark)
                            cell[idx].image = WhiteBishopOnDark
                        Piece.status = 'alive'
                        PiecesClicked = 0
                        RemoveMovementImages()

                if Piece.id == 27 or Piece.id == 30: # Black Bishop
                    if PiecesClicked == 0 and WhoTurn == 'black':
                        if tile_array[row][col].colour == 'light':
                            cell[idx].configure(image=ClickedBlackBishopOnWhite)
                            cell[idx].image = ClickedBlackBishopOnWhite
                        else:
                            cell[idx].configure(image=ClickedBlackBishopOnDark)
                            cell[idx].image = ClickedBlackBishopOnDark
                        Piece.status = 'clicked'
                        PiecesClicked = 1
                        DiagonalPossibleMoves(idx)
                    elif Piece.status == 'clicked' and WhoTurn == 'black':
                        if tile_array[row][col].colour == 'light':
                            cell[idx].configure(image=BlackBishopOnWhite)
                            cell[idx].image = BlackBishopOnWhite
                        else:
                            cell[idx].configure(image=BlackBishopOnDark)
                            cell[idx].image = BlackBishopOnDark
                        Bishop_c8.status = 'alive'
                        PiecesClicked = 0
                        RemoveMovementImages()

    try:
        if tile_array[row][col].status == 'movable' or (KillPiece.colour != ClickedPiece.colour
                                                        and tile_array[row][col].status == 'killable'):
            RemoveMovementImages()
            for i in range(len(Pieces)):
                if Pieces[i].status == 'clicked':
                    Piece = Pieces[i]
                    ClickedRow = int(Piece.index / cols)
                    ClickedCol = Piece.index - ClickedRow * cols
                    if tile_array[ClickedRow][ClickedCol].colour == 'light':
                        cell[Piece.index].configure(image=EmptyLight)
                        cell[Piece.index].image = EmptyLight
                    else:
                        cell[Piece.index].configure(image=EmptyDark)
                        cell[Piece.index].image = EmptyDark

                    PiecesClicked = 0
                    tile_array[ClickedRow][ClickedCol].status = 'empty'
                    tile_array[row][col].status = 'taken'
                    Piece.status = 'alive'
                    Piece.index = idx
                    if Piece.id == 1 or Piece.id == 8: # White Rooks
                        if tile_array[row][col].colour == 'light':
                            cell[idx].configure(image=WhiteRookOnWhite)
                            cell[idx].image = WhiteRookOnWhite
                        else:
                            cell[idx].configure(image=WhiteRookOnDark)
                            cell[idx].image = WhiteRookOnDark
                        WhoTurn = 'black'
                    if Piece.id == 25 or Piece.id == 32: # Black Rooks
                        if tile_array[row][col].colour == 'light':
                            cell[idx].configure(image=BlackRookOnWhite)
                            cell[idx].image = BlackRookOnWhite
                        else:
                            cell[idx].configure(image=BlackRookOnDark)
                            cell[idx].image = BlackRookOnDark
                        WhoTurn = 'white'

                    if Piece.id == 2 or Piece.id == 7: # White Knights
                        if tile_array[row][col].colour == 'light':
                            cell[idx].configure(image=WhiteKnightOnWhite)
                            cell[idx].image = WhiteKnightOnWhite
                        else:
                            cell[idx].configure(image=WhiteKnightOnDark)
                            cell[idx].image = WhiteKnightOnDark
                        WhoTurn = 'black'
                    if Piece.id == 26 or Piece.id == 31: # Black Knights
                        if tile_array[row][col].colour == 'light':
                            cell[idx].configure(image=BlackKnightOnWhite)
                            cell[idx].image = BlackKnightOnWhite
                        else:
                            cell[idx].configure(image=BlackKnightOnDark)
                            cell[idx].image = BlackKnightOnDark
                        WhoTurn = 'white'

                    if Piece.id == 3 or Piece.id == 6: # White Bishops
                        if tile_array[row][col].colour == 'light':
                            cell[idx].configure(image=WhiteBishopOnWhite)
                            cell[idx].image = WhiteBishopOnWhite
                        else:
                            cell[idx].configure(image=WhiteBishopOnDark)
                            cell[idx].image = WhiteBishopOnDark
                        WhoTurn = 'black'
                    if Piece.id == 27 or Piece.id == 30: # Black Bishops
                        if tile_array[row][col].colour == 'light':
                            cell[idx].configure(image=BlackBishopOnWhite)
                            cell[idx].image = BlackBishopOnWhite
                        else:
                            cell[idx].configure(image=BlackBishopOnDark)
                            cell[idx].image = BlackBishopOnDark
                        WhoTurn = 'white'

                    if Piece.id == 4: # White Queen
                        if tile_array[row][col].colour == 'light':
                            cell[idx].configure(image=WhiteQueenOnWhite)
                            cell[idx].image = WhiteQueenOnWhite
                        else:
                            cell[idx].configure(image=WhiteQueenOnDark)
                            cell[idx].image = WhiteQueenOnDark
                        WhoTurn = 'black'
                    if Piece.id == 28: # Black Queen
                        if tile_array[row][col].colour == 'light':
                            cell[idx].configure(image=BlackQueenOnWhite)
                            cell[idx].image = BlackQueenOnWhite
                        else:
                            cell[idx].configure(image=BlackQueenOnDark)
                            cell[idx].image = BlackQueenOnDark
                        WhoTurn = 'white'

                    if Piece.id == 5: # White King
                        if tile_array[row][col].colour == 'light':
                            cell[idx].configure(image=WhiteKingOnWhite)
                            cell[idx].image = WhiteKingOnWhite
                        else:
                            cell[idx].configure(image=WhiteKingOnDark)
                            cell[idx].image = WhiteKingOnDark
                        WhoTurn = 'black'
                    if Piece.id == 29: # Black King
                        if tile_array[row][col].colour == 'light':
                            cell[idx].configure(image=BlackKingOnWhite)
                            cell[idx].image = BlackKingOnWhite
                        else:
                            cell[idx].configure(image=BlackKingOnDark)
                            cell[idx].image = BlackKingOnDark
                        WhoTurn = 'white'

                    if Piece.id >= 9 and Piece.id <=16: # White Pawns
                        if tile_array[row][col].colour == 'light':
                            cell[idx].configure(image=WhitePawnOnWhite)
                            cell[idx].image = WhitePawnOnWhite
                        else:
                            cell[idx].configure(image=WhitePawnOnDark)
                            cell[idx].image = WhitePawnOnDark
                        WhoTurn = 'black'
                        Piece.firstmove = 'false'


                    if Piece.id >= 17 and Piece.id <=24: # Black Pawns
                        if tile_array[row][col].colour == 'light':
                            cell[idx].configure(image=BlackPawnOnWhite)
                            cell[idx].image = BlackPawnOnWhite
                        else:
                            cell[idx].configure(image=BlackPawnOnDark)
                            cell[idx].image = BlackPawnOnDark
                        WhoTurn = 'white'
                        Piece.firstmove = 'false'
                else:
                    pass
            if KillPiece.colour != ClickedPiece.colour:
                KillPiece.status = 'dead'
                KillPiece.index = 100
    except Exception:
        pass


def AxialPossibleMoves(index):
    cols = 8
    rows = 8
    row = int(index / cols)
    col = index - row * cols
    try:
        if tile_array[row][col].MoveDirection == 'Up' or tile_array[row][col].status == 'taken':
            if tile_array[row - 1][col].status == 'empty' and row != 0:
                tile_array[row - 1][col].status = 'movable'
                i = (row -1)*cols + col
                Row = int(i / cols)
                Col = i - Row * cols
                if Row == row -1 and Col == col:
                    if tile_array[row - 1][col].colour == 'light':
                        cell[i].configure(image=MovementOnWhite)
                        cell[i].image = MovementOnWhite
                    else:
                        cell[i].configure(image=MovementOnDark)
                        cell[i].image = MovementOnDark
                    tile_array[row - 1][col].MoveDirection = 'Up'
                    AxialPossibleMoves(i)
            elif tile_array[row - 1][col].status == 'taken' and row != 0:
                tile_array[row - 1][col].status = 'killable'
    except Exception:
        pass
    try:
        if tile_array[row][col].MoveDirection == 'Right' or tile_array[row][col].status == 'taken':
            if tile_array[row][col + 1].status == 'empty' and col != 7:
                tile_array[row][col + 1].status = 'movable'
                i = (row)*cols + col + 1
                Row = int(i / cols)
                Col = i - Row * cols
                if Row == row and Col == col + 1:
                    if tile_array[row][col + 1].colour == 'light':
                        cell[i].configure(image=MovementOnWhite)
                        cell[i].image = MovementOnWhite
                    else:
                        cell[i].configure(image=MovementOnDark)
                        cell[i].image = MovementOnDark
                    tile_array[row][col + 1].MoveDirection = 'Right'
                    AxialPossibleMoves(i)
            elif tile_array[row][col + 1].status == 'taken' and col != 7:
                tile_array[row][col + 1].status = 'killable'
    except Exception:
        pass
    try:
        if tile_array[row][col].MoveDirection == 'Down' or tile_array[row][col].status == 'taken':
            if tile_array[row + 1][col].status == 'empty' and row != 7:
                tile_array[row + 1][col].status = 'movable'
                i = (row + 1)*cols + col
                Row = int(i / cols)
                Col = i - Row * cols
                if Row == row + 1 and Col == col:
                    if tile_array[row - 1][col].colour == 'light':
                        cell[i].configure(image=MovementOnWhite)
                        cell[i].image = MovementOnWhite
                    else:
                        cell[i].configure(image=MovementOnDark)
                        cell[i].image = MovementOnDark
                    tile_array[row + 1][col].MoveDirection = 'Down'
                    AxialPossibleMoves(i)
            elif tile_array[row + 1][col].status == 'taken' and row != 7:
                tile_array[row + 1][col].status = 'killable'
    except Exception:
        pass
    try:
        if tile_array[row][col].MoveDirection == 'Left' or tile_array[row][col].status == 'taken':
            if tile_array[row][col - 1].status == 'empty' and col != 0:
                tile_array[row][col - 1].status = 'movable'
                i = (row)*cols + col - 1
                Row = int(i / cols)
                Col = i - Row * cols
                if Row == row and Col == col - 1:
                    if tile_array[row][col - 1].colour == 'light':
                        cell[i].configure(image=MovementOnWhite)
                        cell[i].image = MovementOnWhite
                    else:
                        cell[i].configure(image=MovementOnDark)
                        cell[i].image = MovementOnDark
                    tile_array[row][col - 1].MoveDirection = 'Left'
                    AxialPossibleMoves(i)
            if tile_array[row][col - 1].status == 'taken' and col != 0:
                tile_array[row][col - 1].status = 'killable'
    except Exception:
        pass
def DiagonalPossibleMoves(index):
    cols = 8
    rows = 8
    row = int(index / cols)
    col = index - row * cols
    try:
        if tile_array[row][col].MoveDirection == 'UpRight' or tile_array[row][col].status == 'taken':
            if tile_array[row - 1 ][col + 1].status == 'empty' and row != 0 and col != 7:
                tile_array[row - 1][col + 1].status = 'movable'
                i = (row - 1)*cols + col +1
                Row = int(i / cols)
                Col = i - Row * cols
                if Row == row -1 and Col == col +1:
                    if tile_array[row - 1][col + 1].colour == 'light':
                        cell[i].configure(image=MovementOnWhite)
                        cell[i].image = MovementOnWhite
                    else:
                        cell[i].configure(image=MovementOnDark)
                        cell[i].image = MovementOnDark
                    tile_array[row - 1][col + 1].MoveDirection = 'UpRight'
                    DiagonalPossibleMoves(i)
            elif tile_array[row - 1 ][col + 1].status == 'taken' and row != 0 and col != 7:
                tile_array[row - 1][col + 1].status = 'killable'
        if tile_array[row][col].MoveDirection == 'UpLeft' or tile_array[row][col].status == 'taken':
            if tile_array[row - 1 ][col - 1].status == 'empty' and row != 0 and col != 0:
                tile_array[row - 1][col - 1].status = 'movable'
                i = (row - 1)*cols + col -1
                Row = int(i / cols)
                Col = i - Row * cols
                if Row == row - 1 and Col == col -1:
                    if tile_array[row - 1][col - 1].colour == 'light':
                        cell[i].configure(image=MovementOnWhite)
                        cell[i].image = MovementOnWhite
                    else:
                        cell[i].configure(image=MovementOnDark)
                        cell[i].image = MovementOnDark
                    tile_array[row - 1][col - 1].MoveDirection = 'UpLeft'
                    DiagonalPossibleMoves(i)
            elif tile_array[row - 1 ][col - 1].status == 'taken' and row != 0 and col != 0:
                tile_array[row - 1][col - 1].status = 'killable'
        if tile_array[row][col].MoveDirection == 'DownRight' or tile_array[row][col].status == 'taken':
            if tile_array[row + 1][col + 1].status == 'empty' and row != 7 and col != 7:
                tile_array[row + 1][col + 1].status = 'movable'
                i = (row + 1) * cols + col + 1
                Row = int(i / cols)
                Col = i - Row * cols
                if Row == row + 1 and Col == col + 1:
                    if tile_array[row + 1][col + 1].colour == 'light':
                        cell[i].configure(image=MovementOnWhite)
                        cell[i].image = MovementOnWhite
                    else:
                        cell[i].configure(image=MovementOnDark)
                        cell[i].image = MovementOnDark
                    tile_array[row + 1][col + 1].MoveDirection = 'DownRight'
                    DiagonalPossibleMoves(i)
            elif tile_array[row + 1][col + 1].status == 'taken' and row != 7 and col != 7:
                tile_array[row + 1][col + 1].status = 'killable'
        if tile_array[row][col].MoveDirection == 'DownLeft' or tile_array[row][col].status == 'taken':
            if tile_array[row + 1][col - 1].status == 'empty' and row != 7 and col != 0:
                tile_array[row + 1][col - 1].status = 'movable'
                i = (row + 1) * cols + col - 1
                Row = int(i / cols)
                Col = i - Row * cols
                if Row == row + 1 and Col == col - 1:
                    if tile_array[row + 1][col - 1].colour == 'light':
                        cell[i].configure(image=MovementOnWhite)
                        cell[i].image = MovementOnWhite
                    else:
                        cell[i].configure(image=MovementOnDark)
                        cell[i].image = MovementOnDark
                    tile_array[row + 1][col - 1].MoveDirection = 'DownLeft'
                    DiagonalPossibleMoves(i)
            elif tile_array[row + 1][col - 1].status == 'taken' and row != 7 and col != 0:
                tile_array[row + 1][col - 1].status = 'killable'
    except Exception:
        pass

def RemoveMovementImages():
    cols = 8
    for i in range(64):
        MoveRow = int(i / cols)
        MoveCol = i - MoveRow * cols
        if tile_array[MoveRow][MoveCol].status == 'movable':
            if tile_array[MoveRow][MoveCol].colour == 'light':  # If even the tile is a white tile, else a dark
                cell[i].configure(image=EmptyLight)
                cell[i].image = EmptyLight
            else:
                cell[i].configure(image=EmptyDark)
                cell[i].image = EmptyDark
            tile_array[MoveRow][MoveCol].status = 'empty'
            tile_array[MoveRow][MoveCol].position = 'null'
        elif tile_array[MoveRow][MoveCol].status == 'killable':
            tile_array[MoveRow][MoveCol].status = 'taken'

class tile:
    def __init__(self,MoveDirection,colour, index, status):
        self.MoveDirection = MoveDirection
        self.colour = colour
        self.index = index
        self.status = status

class King:
    def __init__(self, status, position, colour, index, id):
        self.status = status
        self.position = position
        self.colour = colour
        self.index = index
        self.id = id

class Rook:
    def __init__(self, status, position, colour, index, id):
        self.status = status
        self.position = position
        self.colour = colour
        self.index = index
        self.id = id

class Bishop:
    def __init__(self, status, position, colour, index, id):
        self.status = status
        self.position = position
        self.colour = colour
        self.index = index
        self.id = id

class Queen:
    def __init__(self, status, position, colour, index, id):
        self.status = status
        self.position = position
        self.colour = colour
        self.index = index
        self.id = id

class Knight:
    def __init__(self, status, position, colour, index, id):
        self.status = status
        self.position = position
        self.colour = colour
        self.index = index
        self.id = id

class Pawn:
    def __init__(self, status, position, colour, index, id, firstmove):
        self.status = status
        self.position = position
        self.colour = colour
        self.index = index
        self.id = id
        self.firstmove = firstmove

Board_Setup()
#L1 = []
#for i in range(8):
#    L = []
#    for j in range(8):
#        L.append((tile_array[i][j].colour))
#    L1.append(L)
#for i in range(len(Pieces)):
#   print(Pieces[i].id)
#print(Pieces)
