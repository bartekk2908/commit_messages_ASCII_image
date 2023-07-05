from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pg


class Board:
    def __init__(self, size):
        self.size = size
        self.set_board()

    def set_board(self):
        self.board = []
        for row in range(self.size[0]):
            row = []
            for col in range(self.size[1]):
                row.append(1)
            self.board.append(row)

    def get_size(self):
        return self.size

    def get_value(self, index):
        return self.board[index[0]][index[1]]

    def handle_click(self, index, white, black):
        if white:
            self.board[index[0]][index[1]] = 1
        if black:
            self.board[index[0]][index[1]] = 0

    def save_board(self):
        with open("ascii_art.txt", "w") as file:
            for i in range(self.size[1]):
                file.write("".join(list(map(str, self.board[i]))) + "\n")


class Interface:
    def __init__(self, board, screen_size):
        self.board = board
        self.screen_size = screen_size
        self.piece_size = self.screen_size[0] // self.board.get_size()[1], self.screen_size[1] // self.board.get_size()[0]

    def run(self):
        pg.init()
        self.screen = pg.display.set_mode(self.screen_size)
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if pg.mouse.get_pressed()[0] or pg.mouse.get_pressed()[2]:
                    position = pg.mouse.get_pos()
                    left_click, middle_click, right_click = pg.mouse.get_pressed(3)
                    self.handle_click(self.get_index_of_position(position), left_click, right_click)
            self.draw()
            pg.display.flip()
        self.board.save_board()
        pg.quit()

    def draw(self):
        top_left = (0, 0)
        for row in range(self.board.get_size()[0]):
            for col in range(self.board.get_size()[1]):
                color = "white" if self.board.get_value((row, col)) else "black"
                pg.draw.rect(self.screen, color, pg.Rect(top_left[0], top_left[1], self.piece_size[0], self.piece_size[1]))
                top_left = top_left[0] + self.piece_size[0], top_left[1]
            top_left = 0, top_left[1] + self.piece_size[1]

    def get_index_of_position(self, position):
        return position[1] // self.piece_size[1], position[0] // self.piece_size[0]

    def handle_click(self, index, left_click, right_click):
        self.board.handle_click(index, left_click, right_click)


if __name__ == "__main__":
    window = Interface(Board((10, 10)), (700, 500))
    window.run()
