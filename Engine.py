from Pieces import Pawn, Knight, Bishop, Rook, Queen, King

class Game(object):
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.board = Board()
        self.turn = "white"
    def invert_turn(self):
        if self.turn == "white":
            self.turn = "black"
        else:
            self.turn = "white"
    def is_checkmate(self):
        pieces = []
        for i in range(0, len(self.board.board)):
            for j in range(0, len(self.board.board[i])):
                if str(self.board.board[i][j]) != "-" and self.board.board[i][j].color == self.turn:
                    for k in self.all_legal_moves(self.board.board[i][j]):
                        self.board.move_piece(self.board.board[i][j].position[:] + k)
                        if not self.is_check(self.turn):
                            self.board.undo_move() 
                            return False
                        self.board.undo_move() 
                        
        return True                
    def all_legal_moves(self, piece):
        possible_moves = []
        for i in range(0, 8):
            for j in range(0, 8):
                if self.get_valid_move(piece.position + [i, j], "no.turn"):
                    possible_moves.append([i, j])
        return possible_moves
    def clear_path(self, move_cords):
        add_x = 1
        add_y = 1
        move_cords = list(move_cords)
        if (move_cords[2] - move_cords[0]) < 0:
            add_x = -1
        if (move_cords[3] - move_cords[1]) < 0:
            add_y = -1
        if (move_cords[0] - move_cords[2]) == 0:
            add_x = 0
        elif(move_cords[1] - move_cords[3]) == 0:
            add_y = 0
        while 1:
            move_cords[0] += add_x
            move_cords[1] += add_y
            if move_cords[0] == move_cords[2] and move_cords[1] == move_cords[3]:
                break
            if move_cords[0] == move_cords[2]:
                add_x = 0
            if move_cords[1] == move_cords[3]:
                add_y = 0
            if self.board.board[move_cords[0]][move_cords[1]] != "-":
                return False
        return True
    def is_check(self, color):
        if color == "white":
            king_location = self.board.piece_location("k")
        else:
            king_location = self.board.piece_location("K")
        if not king_location:
            return False
        for i in self.board.board:
            for j in i:
                if j == "-" or j.color == color:
                    continue
                if self.get_valid_move(j.position + king_location, "no.turn"):
                    return True
        return False
    def get_valid_move(self, move_cords, special_rules=""):
        is_take = False
        start_piece = self.board.board[move_cords[0]][move_cords[1]]
        end_piece = self.board.board[move_cords[2]][move_cords[3]]
        if start_piece == "-":
            return False
        if "no.turn" not in special_rules.split(" "):
            if start_piece.color.lower() != self.turn.lower():
                return False
        if end_piece != "-":
            if start_piece.color.lower() == end_piece.color.lower():
                return False
            else:
                is_take = True
        if not start_piece.valid_move(move_cords[2:], is_take):
            return False
        if str(start_piece).lower() != "n":
            if not self.clear_path(move_cords):
                return False
        self.board.move_piece(move_cords)
        if self.is_check(self.turn):
            self.board.undo_move()
            return False
        self.board.undo_move()
        return True
    def move_piece(self, move_cords):
        letter_table = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
        f_cords = []
        for i in move_cords:
            for j in i:
                if j.isdigit():
                    f_cords.append(int(j))
                else:
                    f_cords.append(letter_table[j])
        f_cords[0], f_cords[1] = f_cords[1], f_cords[0]
        f_cords[2], f_cords[3] = f_cords[3], f_cords[2]
        f_cords = [x - 1 for x in f_cords]
        if self.get_valid_move(f_cords):
            self.board.move_piece(f_cords)
            self.invert_turn()
            return True
        else:
            return False
    def undo_move(self):
        self.board.undo_move()
        self.invert_turn()
        
    def reset_game(self):
        self.board.set_board("default")
        self.board.move_log = []
        self.turn = "white"
        
        
class Board(object):
    table = {"p": Pawn, "n": Knight, "b": Bishop, "r": Rook, "q": Queen, "k": King}
    def __init__(self):
        self.board = []
        self.move_log = []
        self.set_board("default")
    def bool_color(self, string):
        if string == string.lower():
            return "white"
        return "black"
    def undo_move(self):
        last_move = self.move_log[-1]
        for i in last_move[:]:
            pos = i[0][:]
            if i[1].lower() in self.table:
                self.board[pos[0]][pos[1]] = self.table[str(i[1]).lower()](self.bool_color(str(i)), pos)
            else:
                self.board[pos[0]][pos[1]] = str(i[1])
        del self.move_log[-1]
    def change_piece(self, pos, new_val):
        self.board[pos[0]][pos[1]] = new_val
    def set_board(self, new_board):
        self.board = []
        self.move_log = []
        if new_board == "default":
            self.board = self.default_board()
        elif new_board == str(new_board):
            self.board = self.string_to_board(new_board)[:]
        else:
            self.board = new_board
    def piece_location(self, piece):
        for i in range(0, len(self.board)):
            if piece not in [str(x) for x in self.board[i]]:
                continue
            for j in range(0, len(self.board[i])):
                if str(self.board[i][j]) == piece:
                    return [i, j]
        return False
    def string_to_board(self, string):
        a = [[]]
        axis_n = 0
        for i in string:
            if i.isdigit():
                for j in range(0, int(i)):
                    a[axis_n].append("-")
            elif i == "\\":
                axis_n += 1
                a.append([])
            else:
                if i == i.lower():
                    color = "white"
                else:
                    color = "black"
                a[axis_n].append(self.table[i.lower()](color, [len(a) - 1, len(a[axis_n])]))
        if axis_n == 0:
            return a[0]
        return a       
    def default_board(self):
        new_board = self.string_to_board("rnbqkbnr\\pppppppp\\8\\8\\8\\8\\PPPPPPPP\\RNBQKBNR")
        return new_board
    def move_piece(self, move_cords):
        piece = self.board[move_cords[0]][move_cords[1]]
        self.move_log.append([[move_cords[0:2], str(piece)], [move_cords[2:4], str(self.board[move_cords[2]][move_cords[3]])]])
        piece.position = move_cords[2:4][:]
        self.board[move_cords[2]][move_cords[3]] = piece
        self.board[move_cords[0]][move_cords[1]] = "-"
    def str_board(self):
        str_board = []
        for i in self.board[:]:
            str_board.append(list(map(str, i)))
        return str_board
        
if __name__ == "__main__":
    test = Game("test", "test2")
    print(test.board.piece_location("k"))
    test.move_piece(["a2", "a4"])
    test.move_piece(["h7", "h5"])
    string_test = test.board.str_board()
    for i in string_test:
        print(i)
    
