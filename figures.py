import pygame
import const

class Figure():
    def __init__(self, color, name):
        image = pygame.image.load(color+name+".png").convert_alpha() #поверхность с изображением
        self.image = pygame.transform.scale(image, (const.WIDTH // 8, 
                                          const.HEIGHT // 8)) #размер фигур настраивается относительно размеров окна, с помощью transform.scale
        self.color = color
        self.name = name
        self.was_move = 0 #ходила ли фигура
        self.sh_castling = 0 #была ли короткая рокировка
        self.l_castling = 0 #была ли длинная

class Square():
    def __init__(self, wh_beaten, bl_beaten):
        self.wh_beaten = wh_beaten #поле бьется для белого короля
        self.bl_beaten = bl_beaten #поле бьется для черного короля
        
def set_array(): #массив 8*8, элемент массива либо фигура, либо пустая клетка с информацией находится ли она под ударом для белого и черного королей
    array = [[0 for x in range(8)] for y in range(8)]
    array[0] = [Figure("Black", "Rook"), Figure("Black", "Knight"), Figure("Black", "Bishop"),
                Figure("Black", "Queen"), Figure("Black", "King"), Figure("Black", "Bishop"),
                Figure("Black", "Knight"), Figure("Black", "Rook")]
    
    array[1] = [Figure("Black", "Pawn") for x in range(8)]

    array[2] = [Square(1, 0) for x in range(8)]
    for y in range(3, 5):
        array[y] = [Square(0, 0) for x in range(8)]
    array[5] = [Square(0, 1) for x in range(8)]

    array[6] = [Figure("White", "Pawn") for x in range(8)]

    array[7] = [Figure("White", "Rook"), Figure("White", "Knight"), Figure("White", "Bishop"),
                Figure("White", "Queen"), Figure("White", "King"), Figure("White", "Bishop"),
                Figure("White", "Knight"), Figure("White", "Rook")]

    return array
    
def draw_board(): #отрисовка доски
    board = pygame.Surface((const.WIDTH, const.HEIGHT))

    for i in range(8):
        for j in range(8):
            x = i * const.WIDTHSQUARE
            y = j * const.HEIGHTSQUARE
            if i % 2 == 0 and j % 2 == 0 or i % 2 == 1 and j % 2 == 1:
                color = (255,255,255)
            else:
                color = (80,80,80)

            rect = (x, y, const.WIDTHSQUARE, const.HEIGHTSQUARE)
            pygame.draw.rect(board, color, rect)

    return board

def draw_figures(array): #отрисовка фигур на каждом ходу
    surf = pygame.Surface((const.WIDTH, const.HEIGHT))
    surf.fill((1, 0, 0))
    surf.set_colorkey((1, 0, 0)) #нужно для прозрачности той части поверхности, где нет изображений фигур
                                #чтобы при наложении этой поверхности на поверхность board последняя не закрашивалась
    for y in range(8):
        for x in range(8):
            if type(array[y][x]) == Figure:
                surf.blit(array[y][x].image, (x*const.WIDTHSQUARE, y*const.HEIGHTSQUARE))
                
    return surf
    
