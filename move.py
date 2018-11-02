import const
from figures import Figure as Figure
from figures import Square as Square
from math import fabs as fabs

def which_figure(array, coord_fig):
    #функция, определяющая какую фигуру игрок выбрал
    x, y = coord_fig
    x = x // const.WIDTHSQUARE
    y = y // const.HEIGHTSQUARE
    if type(array[y][x]) == Figure:     
        return (x, y)
    else:
        return -1

def which_square(coord_square):
    #функция, определяющая на какую клетку игрок хочет поставить фигуру
    x, y = coord_square
    x = x // const.WIDTHSQUARE
    y = y // const.HEIGHTSQUARE
    return (x, y)

def move(array, coord_fig, coord_square, consume): #consume указывает ход с поеданием или без
    #стремная функция, ее точно нужно как-то переделать
    #просто нужно постоянно отслеживать какие поля находятся под ударом, эта информация нужна для ходов королей, а здесь это почти не учтено
    x0, y0 = coord_fig
    x1, y1 = coord_square
    if (consume == 0) or (consume == 1 and array[y1][x1].name != "King"):
        array[y1][x1] = array[y0][x0]
        #if <функция, определяющая бьется ли поле, с которого ушла фигура, для короля противника>:
        if False: #False я поставил, чтобы программа запускалась, т.к. функция выше не написана, допустим, что поле, с которого ушла фигура не бьется для короля противника
            if array[y0][x0].color == "White":
               array[y0][x0] = Square(0, 1)
            else:
                array[y0][x0] = Square(1, 0)
        else:
            array[y0][x0] = Square(0, 0)
    else:
        #шах
        True
    return
        
        

def available_move(array, coord_fig, coord_square):
    #функция, проверяющая возможен ли ход, если возможен, то вызывается функция move
    x0, y0 = coord_fig
    x1, y1 = coord_square
    figure = array[y0][x0]
    
    if figure.name == "King":
        if (fabs(x1 - x0) == 1 or fabs(y1 - y0) == 1) and (fabs(x1 - x0) < 2 and fabs(y1 - y0) < 2): #ход на соседнюю клетку
            if (type(array[y1][x1]) == Square):
                if (figure.color == "White") and (array[y1][x1].wh_beaten == 0): #если клетка не под ударом ход возможен
                    move(array, coord_fig, coord_square, 0)
                elif (figure.color == "Black") and (array[y1][x1].bl_beaten == 0):
                    move(array, coord_fig, coord_square, 0) #ноль в конце - ход без поедания
            elif (type(array[y1][x1]) == Figure) and (array[y1][x1].color != figure.color): #ход с поеданием вражеской фигуры
                move(array, coord_fig, coord_square, 1) #единица в конце - ход с поеданием
            
    elif figure.name == "Queen":
        if (fabs(x1 - x0) > 0) and (y1 == y0): #ход по горизонтали
            if x1 > x0:
                begin_x = x0 + 1
                end_x = x1
                step_x = 1
            elif x1 < x0:
                begin_x = x0 - 1
                end_x = x1
                step_x = -1
                
            for x in range(begin_x, end_x, step_x): #проверяется, нет ли между текущей и желаемой клеткой фигур
                if (type(array[y0][x]) == Figure):
                    return -1

            if (type(array[y1][x1]) == Figure) and (array[y1][x1].color != figure.color):
                move(array, coord_fig, coord_square, 1)
            elif type(array[y1][x1]) == Square:
                move(array, coord_fig, coord_square, 0)
            else:
                return -1
        if (fabs(y1 - y0) > 0) and (x1 == x0): #ход по вертикали
            if y1 > y0:
                begin_y = y0 + 1
                end_y = y1
                step_y = 1
            elif y1 < y0:
                begin_y = y0 - 1
                end_y = y1
                step_y = -1
            
            for y in range(begin_y, end_y, step_y):
                if (type(array[y][x0]) == Figure):
                    return -1
            
            if (type(array[y1][x1]) == Figure) and (array[y1][x1].color != figure.color):
                move(array, coord_fig, coord_square, 1)
            elif type(array[y1][x1]) == Square:
                move(array, coord_fig, coord_square, 0)
            else:
                return -1
            
        elif (fabs(x1 - x0) == fabs(y1 - y0)) and (x1 != x0): #ход по диагонали
            if (x1 > x0) and (y1 > y0):
                begin_x = x0 + 1
                end_x = x1
                step_x = 1

                begin_y = y0 + 1
                step_y = 1
            elif (x1 > x0) and (y1 < y0):
                begin_x = x0 + 1
                end_x = x1
                step_x = 1

                begin_y = y0 - 1
                step_y = -1
            elif (x1 < x0) and (y1 < y0):
                begin_x = x0 - 1
                end_x = x1
                step_x = -1

                begin_y = y0 - 1
                step_y = -1
            elif (x1 < x0) and (y1 > y0):
                begin_x = x0 - 1
                end_x = x1
                step_x = -1

                begin_y = y0 + 1
                step_y = 1
                
            y = begin_y #точно также проверяется, нет ли фигур на пути
            for x in range(begin_x, end_x, step_x):
                if (type(array[y][x]) == Figure):
                    return -1
                y += step_y
                
            if (type(array[y1][x1]) == Figure) and (array[y1][x1].color != figure.color):
                move(array, coord_fig, coord_square, 1)
            elif type(array[y1][x1]) == Square:
                move(array, coord_fig, coord_square, 0)
            else:
                return -1
            
    elif figure.name == "Rook": #описание ходов ладьи и слона по сути уже сделано при описании ходов ферзя
        if (fabs(x1 - x0) > 0) and (y1 == y0):
            if x1 > x0:
                begin_x = x0 + 1
                end_x = x1
                step_x = 1
            elif x1 < x0:
                begin_x = x0 - 1
                end_x = x1
                step_x = -1
                
            for x in range(begin_x, end_x, step_x):
                if (type(array[y0][x]) == Figure):
                    return -1

            if (type(array[y1][x1]) == Figure) and (array[y1][x1].color != figure.color):
                move(array, coord_fig, coord_square, 1)
            elif type(array[y1][x1]) == Square:
                move(array, coord_fig, coord_square, 0)
            else:
                return -1
        if (fabs(y1 - y0) > 0) and (x1 == x0):
            if y1 > y0:
                begin_y = y0 + 1
                end_y = y1
                step_y = 1
            elif y1 < y0:
                begin_y = y0 - 1
                end_y = y1
                step_y = -1
            
            for y in range(begin_y, end_y, step_y):
                if (type(array[y][x0]) == Figure):
                    return -1
            
            if (type(array[y1][x1]) == Figure) and (array[y1][x1].color != figure.color):
                move(array, coord_fig, coord_square, 1)
            elif type(array[y1][x1]) == Square:
                move(array, coord_fig, coord_square, 0)
            else:
                return -1
            
    elif figure.name == "Bishop":
        if (fabs(x1 - x0) == fabs(y1 - y0)) and (x1 != x0):
            if (x1 > x0) and (y1 > y0):
                begin_x = x0 + 1
                end_x = x1
                step_x = 1

                begin_y = y0 + 1
                step_y = 1
            elif (x1 > x0) and (y1 < y0):
                begin_x = x0 + 1
                end_x = x1
                step_x = 1

                begin_y = y0 - 1
                step_y = -1
            elif (x1 < x0) and (y1 < y0):
                begin_x = x0 - 1
                end_x = x1 - 1
                step_x = -1

                begin_y = y0 - 1
                step_y = -1
            elif (x1 < x0) and (y1 > y0):
                begin_x = x0 - 1
                end_x = x1
                step_x = -1

                begin_y = y0 + 1
                step_y = 1
                
            y = begin_y
            for x in range(begin_x, end_x, step_x):
                if (type(array[y][x]) == Figure):
                    return -1
                y += step_y
                
            if (type(array[y1][x1]) == Figure) and (array[y1][x1].color != figure.color):
                move(array, coord_fig, coord_square, 1)
            elif type(array[y1][x1]) == Square:
                move(array, coord_fig, coord_square, 0)
            else:
                return -1
        
    elif figure.name == "Knight":
        if (fabs(x1 - x0) == 2 and fabs(y1 - y0) == 1) or (fabs(y1 - y0) == 2 and fabs(x1 - x0) == 1): #ход коня
                if (type(array[y1][x1]) == Figure) and (array[y1][x1].color != figure.color):
                    move(array, coord_fig, coord_square, 1)
                elif type(array[y1][x1]) == Square:
                    move(array, coord_fig, coord_square, 0)
                else:
                    return -1
            
    elif figure.name == "Pawn":
        if figure.color == "Black": ch_y = y1 - y0
        else: ch_y = y0 - y1
        
        if (ch_y == 1) and (x1 == x0):
            if type(array[y1][x1]) == Square:
                move(array, coord_fig, coord_square, 0)
            else:
                return -1
        elif (ch_y == 2) and (x1 == x0) and (figure.was_move == 0): #если пешка не ходила, ход через одну клетку возможен
            if type(array[y1][x1]) == Square:
                move(array, coord_fig, coord_square, 0)
                figure.was_move = 1
            else:
                return -1
        elif (ch_y == 1) and (fabs(x1 - x0) == 1):
            if (type(array[y1][x1]) == Figure) and (array[y1][x1].color != figure.color):
                move(array, coord_fig, coord_square, 1)
            else:
                return -1
        """Для пешки необходимо обработать взятие на проходе"""


