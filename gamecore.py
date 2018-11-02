import pygame
import sys
import figures
import const
import move

def main():
    FPS = 5
    screen = pygame.display.set_mode((const.WIDTH, const.HEIGHT))

    pygame.init()
    clock = pygame.time.Clock()
    array = figures.set_array()
    
    move_active = "off" #переменная, отслеживающая что означает клик игрока - выбор фигуры или выбор поля, куда эту фигуру поставить
   
    while True:
        board = figures.draw_board()
        board.blit(figures.draw_figures(array), (0, 0))
        screen.blit(board, (0, 0))
        pygame.display.update()
        
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if i.type == pygame.MOUSEBUTTONUP and i.button == 1:
                if move_active == "off": #если это первый клик мышью, то игрок выбрал фигуру
                    coord_fig = move.which_figure(array, i.pos)
                    if coord_fig != -1:         #coord_fig равен -1, если нет фигуры на поле, куда игрок кликнул
                        move_active = "on"
                else:                    #если это второй клик мышью, то игрок выбрал клетку хода
                    coord_square = move.which_square(i.pos)
                    move.available_move(array, coord_fig, coord_square) #сделать ход, если он возможен
                    move_active = "off"
        
        clock.tick(FPS)


if __name__ == "__main__":
    main()

