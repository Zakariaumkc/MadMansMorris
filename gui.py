from hashlib import blake2b
from string import whitespace
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QGraphicsScene, QGraphicsView, QSizePolicy
from PyQt6.QtGui import QBrush, QColor, QPen, QPainter, QPaintEvent, QMouseEvent
from PyQt6.QtSvgWidgets import QGraphicsSvgItem
from PyQt6.QtSvg import QSvgRenderer
from PyQt6.QtCore import QRect

import MadMansMorris


black_piece_render = QSvgRenderer("images/black_piece.svg")
white_piece_render = QSvgRenderer("images/white_piece.svg")
empty_space_render = QSvgRenderer("images/empty_space.svg")

class QBoardSpace(QGraphicsSvgItem):
    def __init__(self, board_space: MadMansMorris.BoardSpace):
        super().__init__()
        self.board_space : MadMansMorris = board_space

        if self.board_space.state == MadMansMorris.BoardSpace.BLACK_SPACE:
            self.setSharedRenderer(black_piece_render)
        elif self.board_space.state == MadMansMorris.BoardSpace.WHITE_SPACE:
            self.setSharedRenderer(white_piece_render)

        self.x, self.y = self.__position_from_space_name(self.board_space.space_name)

        self.setPos(self.x * 100.0 -354.0 / 2.0, self.y * 100.0 - 354.0 / 2.0)

        self.setTransformOriginPoint(self.boundingRect().center())
        self.setScale(0.15)

        self.setFlag(QGraphicsSvgItem.GraphicsItemFlag.ItemIsMovable, True)
        
    
    def __position_from_space_name(self, space_name: str):
        x = ord(space_name[0]) - 65
        y = 7 - int(space_name[1]) 
        return x, y


class MainWindow(QMainWindow):
    def __init__(self):
        self.game = MadMansMorris.Game()

        self.game.place_piece("A7")
        self.second_player = self.game.current_player

        self.game.place_piece("D7")

        self.game.place_piece("G7")
        self.game.place_piece("B6")

        self.game.place_piece("D6")
        self.game.place_piece("F6")
        
        self.game.place_piece("B4")
        self.game.place_piece("E4")

        self.game.place_piece("F4")   
        self.game.place_piece("G4")

        self.game.place_piece("G1")
        self.game.place_piece("D1")

        self.game.place_piece("A1")
        self.game.place_piece("A4")

        self.game.place_piece("B2")
        self.game.place_piece("D2")

        self.game.place_piece("D3")
        self.game.place_piece("F2")

        self.game.move_piece("D3", "C3")
        self.game.move_piece("E4", "E3")
        self.game.move_piece("C3", "C4")
        self.game.move_piece("E3", "D3")

        self.game.move_piece("C3", "C4")
        self.game.move_piece("D3", "E3")
        self.game.move_piece("C4", "C3")
        self.game.move_piece("E3", "D3")


        super().__init__()
        self.setWindowTitle("Mad Man's Morris")

        self.view = QGraphicsView()
        self.setCentralWidget(self.view)

        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)

        self.draw_board()

        for space in self.game.board.spaces.values():
            self.scene.addItem(QBoardSpace(space))
        

        self.setMinimumHeight(700)
        self.setMinimumWidth(700)

        self.sizePolicy().setHorizontalPolicy(QSizePolicy.Policy.Minimum)
        self.sizePolicy().setVerticalPolicy(QSizePolicy.Policy.Minimum)




    def draw_board(self):
        self.scene.addRect(0, 0, 600, 600, QPen(QColor(0, 0, 0)))
        self.scene.addRect(100, 100, 400, 400, QPen(QColor(0, 0, 0)))
        self.scene.addRect(200, 200, 200, 200, QPen(QColor(0, 0, 0)))

        self.scene.addLine(300, 0, 300, 200, QPen(QColor(0, 0, 0)))
        self.scene.addLine(300, 400, 300, 600, QPen(QColor(0, 0, 0)))

        self.scene.addLine(0, 300, 200, 300, QPen(QColor(0, 0, 0)))
        self.scene.addLine(400, 300, 600, 300, QPen(QColor(0, 0, 0)))

        for y in range(0, 7):
            for x in range(0, 7):
                space_name = chr(x + 65) + str(y + 1)
                if space_name in self.game.board.spaces:
                    self.scene.addEllipse(x * 100 - 6, y * 100 - 6, 12, 12, QPen(QColor(0, 0, 0)), QBrush(QColor(0, 0, 0)))








app = QApplication([])

window = MainWindow()
window.show()

app.exec()