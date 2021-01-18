
class Piece(object):
    piece_str = "n/a"
    def __init__(self, color, position):
        self.position = position
        self.color = color.lower()
    def valid_move(self, move_pos):
        distance = [abs(self.position[0] - move_pos[0]), abs(self.position[1] - move_pos[1])]
        if move_pos[0] < 0 or move_pos[0] > 7 or move_pos[1] < 0 or move_pos[1] > 7:
            return False
        if distance[0] == 0 and distance[1] == 0:
            return False
        return True
    def diagonal_valid(self, distance):
        if abs(distance[0]) == abs(distance[1]):
            return True
        return False
    def vh_valid(self, distance):
        if abs(distance[0]) > 0 and abs(distance[1]) > 0:
            return False
        return True
    def __str__(self):
        if self.color == "white":
            return self.piece_str.lower()
        return self.piece_str.upper()
    
class Pawn(Piece):
    piece_str = "p"
    def valid_move(self, move_pos, is_take):
        distance = [abs(self.position[0] - move_pos[0]), abs(self.position[1] - move_pos[1])]
        if distance[0] < 0:
            return False
        if is_take == True:
            if distance[0] == 1 and distance[1] == 1:
                return True
            else:
                return False
        elif distance[1] > 0:
            return False
        if super().valid_move(move_pos) == False:
            return False
        if self.up_two_valid(move_pos) == True:
            return True
        if distance[0] + distance[1] > 1:
            return False
        return True  
    def up_two_valid(self, move_pos):
        if self.color == "black":
            if self.position[0] == 6 and move_pos[0] == 4:
                return True
        else:
            if self.position[0] == 1 and move_pos[0] == 3:
                return True
        return False

class Queen(Piece):
    piece_str = "q"
    def valid_move(self, move_pos, is_take):
        distance = [abs(self.position[0] - move_pos[0]), abs(self.position[1] - move_pos[1])]
        if super().valid_move(move_pos) and (self.vh_valid(distance) or self.diagonal_valid(distance)):
            return True
        return False
    
class Bishop(Piece):
    piece_str = "b"
    def valid_move(self, move_pos, is_take):
        distance = [abs(self.position[0] - move_pos[0]), abs(self.position[1] - move_pos[1])]
        if super().valid_move(move_pos) and self.diagonal_valid(distance):
            return True
        return False

class Knight(Piece):
    piece_str = "n"
    def valid_move(self, move_pos, is_take):
        distance = [abs(self.position[0] - move_pos[0]), abs(self.position[1] - move_pos[1])]
        if (distance[0] != 2 and distance[1] !=  2) or (distance[0] != 1 and distance[1] != 1):
            return False
        if super().valid_move(move_pos) and distance[0] + distance[1] == 3:
            return True
        return False

class Rook(Piece):
    piece_str = "r"
    def valid_move(self, move_pos, is_take):
        distance = [abs(self.position[0] - move_pos[0]), abs(self.position[1] - move_pos[1])]
        if super().valid_move(move_pos) and self.vh_valid(distance):
            return True
        return False
    
class King(Piece):
    piece_str = "k"
    def valid_move(self, move_pos, is_take):
        distance = [abs(self.position[0] - move_pos[0]), abs(self.position[1] - move_pos[1])]
        if super().valid_move(move_pos) and (self.vh_valid(distance) or self.diagonal_valid(distance)):
            if distance[0] < 2 and distance[1] < 2:
                return True
        return False

if __name__ == "__main__":
    testing = Pawn("white", [3, 4])
    testing2 = Pawn("Black", [5, 7])
    print(str(testing) + str(testing2))
    print(testing.valid_move([2, 4], False))
