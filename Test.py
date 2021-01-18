import unittest
from Engine import Board, Game
from Pieces import Pawn, Knight, Bishop, Rook, Queen, King

test_board_1 = "qqqqqqqq\\pppppppp\\8\\8\\8\\8\\PPPPPPPP\\QQQQQQQQ"
test_board_2 = "bbbbbbbb\\8\\8\\8\\8\\8\\8\\BBBBBBBB"
test_board_3 = "nnnnnnnn\\pppppppp\\8\\8\\8\\8\\PPPPPPPP\\NNNNNNNN"
test_board_4 = "rrrrrrrr\\rrrrrrrr\\8\\8\\8\\8\\RRRRRRRR\\RRRRRRRR"
test_board_5 = "kkkkkkkk\\kkkkkkkk\\8\\8\\8\\8\\KKKKKKKK\\KKKKKKKK"

def board_print(Game):
    strb = Game.board.str_board()
    print(".")
    for i in strb:
        print("".join(i))

def get_piece(game_engine, pos):
    return game_engine.board.str_board()[pos[0]][pos[1]]

class BoardTesting(unittest.TestCase):
    test = Game("test1", "test2")
    def test_queen_diagonal(self):
        self.test.turn = "white"
        self.test.board.set_board(test_board_1)
        self.test.move_piece(["a2", "a4"])
        self.test.move_piece(["h7", "h5"])
        self.test.move_piece(["a1", "a3"])
        self.test.move_piece(["h8", "h6"])
        self.test.move_piece(["a3", "e7"])
        self.assertEqual(get_piece(self.test, [6, 4]), "q")
    def test_bishop_1(self):
        self.test.turn = "white"
        self.test.board.set_board(test_board_2)
        self.test.move_piece(["h1", "a8"])
        self.assertEqual(get_piece(self.test, [7, 0]), "b")
        self.test.move_piece(["h8", "a1"])
        self.assertEqual(get_piece(self.test, [0, 0]), "B")
    def test_knight_1(self):
        self.test.turn = "white"
        self.test.board.set_board(test_board_3)
        self.test.move_piece(["a1", "b3"])
        self.assertEqual(get_piece(self.test, [2, 1]), "n")
    def test_rook_1(self):
        self.test.turn = "white"
        self.test.board.set_board(test_board_4)
        self.test.move_piece(["b2", "b7"])
        self.test.move_piece(["b7", "e7"]) #should (FAIL)
        self.test.move_piece(["b5", "h5"])
        self.assertEqual(get_piece(self.test, [6, 1]), "r")
        self.assertEqual(get_piece(self.test, [6, 4]), "R") #this tests if b7-e7 failed
    def test_check(self):
        self.test.turn = "white"
        self.test.board.set_board("default")
        self.assertEqual(self.test.is_check("white"), False)
        self.assertEqual(self.test.is_check("black"), False)
        self.test.move_piece(["e2", "e4"])
        self.test.move_piece(["e7", "e5"])
        self.test.move_piece(["g1", "f3"])
        self.test.move_piece(["d7", "d6"])
        self.test.move_piece(["f1", "b5"])
        self.assertEqual(self.test.is_check("white"), False)
        self.assertEqual(self.test.is_check("black"), True)
    def test_undo_move(self):
        self.test.reset_game()
        self.test.move_piece(["a2", "a4"])
        self.test.undo_move()
        self.assertEqual(self.test.board.move_log, [])
        self.assertEqual(self.test.board.str_board()[1][0], "p")
        self.assertEqual(self.test.board.str_board()[3][0], "-")
        self.assertEqual(self.test.turn, "white")
        #self.test.undo_move()
    def test_scholars_mate(self):
        self.test.reset_game()
        self.test.move_piece(["e2", "e4"])
        self.test.move_piece(["e7", "e5"])
        self.test.move_piece(["d1", "h5"])
        self.test.move_piece(["b7", "b6"])
        self.test.move_piece(["f1", "c4"])
        self.test.move_piece(["c8", "b7"])
        self.test.move_piece(["h5", "f7"])
        self.assertEqual(self.test.turn, "black")
        self.assertEqual(self.test.is_check("black"), True)
        self.assertEqual(self.test.is_checkmate(), True)
        
if __name__ == "__main__":
    unittest.main()    
                        
                
