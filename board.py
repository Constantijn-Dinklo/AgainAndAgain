import numpy as np


class Piece:
    x = -1
    y = -1
    colour = -1
    block_num = -1
    star = False

    crossed_out = False
    
    reachable = False

    def __init__(self, x, y, colour, block_num, star=False):
        self.x = x
        self.y = y
        self.colour = colour
        self.block_num = block_num

        self.star = star

class Block:

    colour = -1
    size = 0
    open_cells = 0

    def __init__(self):
        self.pieces = []
        self.reachable = False

    def setColour(self, colour):
        self.colour = colour

    def addPiece(self, piece):
        #Should check if the piece is of the same colour as block is
        self.pieces.append(piece)
        self.size = self.size + 1
        self.open_cells = self.open_cells + 1

    def printBlock(self):
        print("Block size: " + str(self.size))

        for piece in self.pieces:
            reachable_str = "not reachable"
            if piece.reachable:
                reachable_str = "reachable"
            crossed = "not crossed out"
            if piece.crossed_out:
                crossed = "crossed out"
            print("Piece " + str(piece.x) + ", " + str(piece.y) + " is " + reachable_str + " and is " + crossed)

class Board:

    #Colours
    GREEN = 1
    BLUE = 2
    PINK = 3
    YELLOW = 4
    ORANGE = 5
    JOKER = 0
    
    width = 15
    height = 7


    points_for_column_first =   [5,3,3,3,2,2,2,1,2,2,2,3,3,3,5]
    points_for_column_second =  [3,2,2,2,1,1,1,0,1,1,1,2,2,2,3]
    cells_left_in_column =      [7,7,7,7,7,7,7,7,7,7,7,7,7,7,7]
    overall_completed_column =  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    completed_column =          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    points_for_colour_first =   [5,5,5,5,5]
    points_for_colour_second =  [3,3,3,3,3]
    overall_completed_colour =  [0,0,0,0,0]
    completed_colour =          [0,0,0,0,0]
    num_left_of_colour =        [21, 21, 21, 21, 21]


    possible_coords = set()
    possible_blocks = set()
    crossed_out_pieces = set()

    pieces = np.empty((height, width), dtype=Piece)

    blocks = []

    def initDefaultBoard(self):

        #Block 1
        block1 = Block()

        piece = Piece(0, 0, self.GREEN, 1)
        self.pieces[piece.x][piece.y] = piece
        block1.addPiece(piece)
        piece = Piece(0, 1, self.GREEN, 1)
        self.pieces[piece.x][piece.y] = piece
        block1.addPiece(piece)
        piece = Piece(0, 2, self.GREEN, 1)
        self.pieces[piece.x][piece.y] = piece
        block1.addPiece(piece)
        piece = Piece(1, 1, self.GREEN, 1)
        self.pieces[piece.x][piece.y] = piece
        block1.addPiece(piece)
        piece = Piece(2, 1, self.GREEN, 1)
        self.pieces[piece.x][piece.y] = piece
        block1.addPiece(piece)

        #Block 2
        block2 = Block()

        piece = Piece(0, 3, self.YELLOW, 2)
        self.pieces[piece.x][piece.y] = piece
        block2.addPiece(piece)
        piece = Piece(0, 4, self.YELLOW, 2)
        self.pieces[piece.x][piece.y] = piece
        block2.addPiece(piece)
        piece = Piece(0, 5, self.YELLOW, 2)
        self.pieces[piece.x][piece.y] = piece
        block2.addPiece(piece)
        piece = Piece(0, 6, self.YELLOW, 2)
        self.pieces[piece.x][piece.y] = piece
        block2.addPiece(piece)
        piece = Piece(1, 4, self.YELLOW, 2, True)
        self.pieces[piece.x][piece.y] = piece
        block2.addPiece(piece)
        piece = Piece(1, 5, self.YELLOW, 2)
        self.pieces[piece.x][piece.y] = piece
        block2.addPiece(piece)

        #block 3
        block3 = Block()
        piece = Piece(0, 7, self.GREEN, 3, True)
        self.pieces[piece.x][piece.y] = piece
        block3.addPiece(piece)

        #block 4
        block4 = Block()

        piece = Piece(0, 8, self.BLUE, 4)
        self.pieces[piece.x][piece.y] = piece
        block4.addPiece(piece)
        piece = Piece(0, 9, self.BLUE, 4)
        self.pieces[piece.x][piece.y] = piece
        block4.addPiece(piece)
        piece = Piece(0, 10, self.BLUE, 4)
        self.pieces[piece.x][piece.y] = piece
        block4.addPiece(piece)
        piece = Piece(1, 9, self.BLUE, 4, True)
        self.pieces[piece.x][piece.y] = piece
        block4.addPiece(piece)
        piece = Piece(1, 10, self.BLUE, 4)
        self.pieces[piece.x][piece.y] = piece
        block4.addPiece(piece)

        #block 5
        block5 = Block()

        piece = Piece(0, 11, self.ORANGE, 5, True)
        self.pieces[piece.x][piece.y] = piece
        block5.addPiece(piece)
        piece = Piece(1, 11, self.ORANGE, 5)
        self.pieces[piece.x][piece.y] = piece
        block5.addPiece(piece)
        piece = Piece(1, 12, self.ORANGE, 5)
        self.pieces[piece.x][piece.y] = piece
        block5.addPiece(piece)
        piece = Piece(2, 12, self.ORANGE, 5)
        self.pieces[piece.x][piece.y] = piece
        block5.addPiece(piece)
        piece = Piece(3, 12, self.ORANGE, 5)
        self.pieces[piece.x][piece.y] = piece
        block5.addPiece(piece)
        piece = Piece(4, 12, self.ORANGE, 5)
        self.pieces[piece.x][piece.y] = piece
        block5.addPiece(piece)

        #block 6
        block6 = Block()

        piece = Piece(0, 12, self.YELLOW, 6)
        self.pieces[piece.x][piece.y] = piece
        block6.addPiece(piece)
        piece = Piece(0, 13, self.YELLOW, 6)
        self.pieces[piece.x][piece.y] = piece
        block6.addPiece(piece)
        piece = Piece(0, 14, self.YELLOW, 6)
        self.pieces[piece.x][piece.y] = piece
        block6.addPiece(piece)

        #block 7
        block7 = Block()
        piece = Piece(1, 0, self.ORANGE, 7)
        self.pieces[piece.x][piece.y] = piece
        block7.addPiece(piece)

        #block 8
        block8 = Block()
        piece = Piece(1, 2, self.YELLOW, 8, True)
        self.pieces[piece.x][piece.y] = piece
        block8.addPiece(piece)

        #block 9 
        block9 = Block()

        piece = Piece(1, 3, self.GREEN, 9)
        self.pieces[piece.x][piece.y] = piece
        block9.addPiece(piece)
        piece = Piece(2, 3, self.GREEN, 9)
        self.pieces[piece.x][piece.y] = piece
        block9.addPiece(piece)
        piece = Piece(2, 4, self.GREEN, 9)
        self.pieces[piece.x][piece.y] = piece
        block9.addPiece(piece)
        piece = Piece(2, 5, self.GREEN, 9)
        self.pieces[piece.x][piece.y] = piece
        block9.addPiece(piece)
        piece = Piece(2, 6, self.GREEN, 9, True)
        self.pieces[piece.x][piece.y] = piece
        block9.addPiece(piece)
        piece = Piece(3, 3, self.GREEN, 9)
        self.pieces[piece.x][piece.y] = piece
        block9.addPiece(piece)

        #block 10
        block10 = Block()

        piece = Piece(1, 6, self.ORANGE, 10)
        self.pieces[piece.x][piece.y] = piece
        block10.addPiece(piece)
        piece = Piece(1, 7, self.ORANGE, 10)
        self.pieces[piece.x][piece.y] = piece
        block10.addPiece(piece)

        #block 11
        block11 = Block()

        piece = Piece(1, 8, self.PINK, 11)
        self.pieces[piece.x][piece.y] = piece
        block11.addPiece(piece)
        piece = Piece(2, 7, self.PINK, 11)
        self.pieces[piece.x][piece.y] = piece
        block11.addPiece(piece)
        piece = Piece(2, 8, self.PINK, 11)
        self.pieces[piece.x][piece.y] = piece
        block11.addPiece(piece)
        piece = Piece(2, 9, self.PINK, 11)
        self.pieces[piece.x][piece.y] = piece
        block11.addPiece(piece)

        #block 12
        block12 = Block()

        piece = Piece(1, 13, self.GREEN, 12)
        self.pieces[piece.x][piece.y] = piece
        block12.addPiece(piece)
        piece = Piece(1, 14, self.GREEN, 12)
        self.pieces[piece.x][piece.y] = piece
        block12.addPiece(piece)
        piece = Piece(2, 13, self.GREEN, 12)
        self.pieces[piece.x][piece.y] = piece
        block12.addPiece(piece)
        piece = Piece(2, 14, self.GREEN, 12)
        self.pieces[piece.x][piece.y] = piece
        block12.addPiece(piece)

        #block 13
        block13 = Block()

        piece = Piece(2, 0, self.BLUE, 13, True)
        self.pieces[piece.x][piece.y] = piece
        block13.addPiece(piece)
        piece = Piece(3, 0, self.BLUE, 13)
        self.pieces[piece.x][piece.y] = piece
        block13.addPiece(piece)

        #block 14
        block14 = Block()

        piece = Piece(2, 2, self.PINK, 14)
        self.pieces[piece.x][piece.y] = piece
        block14.addPiece(piece)
        piece = Piece(3, 1, self.PINK, 14)
        self.pieces[piece.x][piece.y] = piece
        block14.addPiece(piece)
        piece = Piece(3, 2, self.PINK, 14)
        self.pieces[piece.x][piece.y] = piece
        block14.addPiece(piece)

        #block 15
        block15 = Block()

        piece = Piece(2, 10, self.YELLOW, 15)
        self.pieces[piece.x][piece.y] = piece
        block15.addPiece(piece)
        piece = Piece(2, 11, self.YELLOW, 15)
        self.pieces[piece.x][piece.y] = piece
        block15.addPiece(piece)
        piece = Piece(3, 10, self.YELLOW, 15)
        self.pieces[piece.x][piece.y] = piece
        block15.addPiece(piece)
        piece = Piece(3, 11, self.YELLOW, 15)
        self.pieces[piece.x][piece.y] = piece
        block15.addPiece(piece)

        #block 16
        block16 = Block()

        piece = Piece(3, 4, self.ORANGE, 16)
        self.pieces[piece.x][piece.y] = piece
        block16.addPiece(piece)
        piece = Piece(3, 5, self.ORANGE, 16, True)
        self.pieces[piece.x][piece.y] = piece
        block16.addPiece(piece)
        piece = Piece(4, 1, self.ORANGE, 16)
        self.pieces[piece.x][piece.y] = piece
        block16.addPiece(piece)
        piece = Piece(4, 2, self.ORANGE, 16)
        self.pieces[piece.x][piece.y] = piece
        block16.addPiece(piece)
        piece = Piece(4, 3, self.ORANGE, 16)
        self.pieces[piece.x][piece.y] = piece
        block16.addPiece(piece)
        piece = Piece(4, 4, self.ORANGE, 16)
        self.pieces[piece.x][piece.y] = piece
        block16.addPiece(piece)

        #block 17
        block17 = Block()

        piece = Piece(3, 6, self.BLUE, 17)
        self.pieces[piece.x][piece.y] = piece
        block17.addPiece(piece)
        piece = Piece(3, 7, self.BLUE, 17)
        self.pieces[piece.x][piece.y] = piece
        block17.addPiece(piece)
        piece = Piece(4, 6, self.BLUE, 17)
        self.pieces[piece.x][piece.y] = piece
        block17.addPiece(piece)
        piece = Piece(4, 7, self.BLUE, 17)
        self.pieces[piece.x][piece.y] = piece
        block17.addPiece(piece)

        #block 18
        block18 = Block()

        piece = Piece(3, 8, self.GREEN, 18)
        self.pieces[piece.x][piece.y] = piece
        block18.addPiece(piece)
        piece = Piece(3, 9, self.GREEN, 18)
        self.pieces[piece.x][piece.y] = piece
        block18.addPiece(piece)

        #block 19
        block19 = Block()

        piece = Piece(3, 13, self.PINK, 19, True)
        self.pieces[piece.x][piece.y] = piece
        block19.addPiece(piece)
        piece = Piece(4, 11, self.PINK, 19)
        self.pieces[piece.x][piece.y] = piece
        block19.addPiece(piece)
        piece = Piece(4, 12, self.PINK, 19)
        self.pieces[piece.x][piece.y] = piece
        block19.addPiece(piece)
        piece = Piece(4, 13, self.PINK, 19)
        self.pieces[piece.x][piece.y] = piece
        block19.addPiece(piece)
        piece = Piece(4, 14, self.PINK, 19)
        self.pieces[piece.x][piece.y] = piece
        block19.addPiece(piece)

        #block 20
        block20 = Block()
        piece = Piece(3, 14, self.BLUE, 20)
        self.pieces[piece.x][piece.y] = piece
        block20.addPiece(piece)

        #block 21
        block21 = Block()
        
        piece = Piece(4, 0, self.PINK, 21)
        self.pieces[piece.x][piece.y] = piece
        block21.addPiece(piece)
        piece = Piece(5, 0, self.PINK, 21)
        self.pieces[piece.x][piece.y] = piece
        block21.addPiece(piece)

        #block 22
        block22 = Block()
        
        piece = Piece(4, 5, self.PINK, 22)
        self.pieces[piece.x][piece.y] = piece
        block22.addPiece(piece)
        piece = Piece(5, 3, self.PINK, 22, True)
        self.pieces[piece.x][piece.y] = piece
        block22.addPiece(piece)
        piece = Piece(5, 4, self.PINK, 22)
        self.pieces[piece.x][piece.y] = piece
        block22.addPiece(piece)
        piece = Piece(5, 5, self.PINK, 22)
        self.pieces[piece.x][piece.y] = piece
        block22.addPiece(piece)
        piece = Piece(5, 6, self.PINK, 22)
        self.pieces[piece.x][piece.y] = piece
        block22.addPiece(piece)
        piece = Piece(6, 6, self.PINK, 22)
        self.pieces[piece.x][piece.y] = piece
        block22.addPiece(piece)

        #block 23
        block23 = Block()

        piece = Piece(4, 8, self.ORANGE, 23)
        self.pieces[piece.x][piece.y] = piece
        block23.addPiece(piece)
        piece = Piece(4, 9, self.ORANGE, 23)
        self.pieces[piece.x][piece.y] = piece
        block23.addPiece(piece)
        piece = Piece(4, 10, self.ORANGE, 23)
        self.pieces[piece.x][piece.y] = piece
        block23.addPiece(piece)
        piece = Piece(5, 9, self.ORANGE, 23)
        self.pieces[piece.x][piece.y] = piece
        block23.addPiece(piece)

        #block 24
        block24 = Block()

        piece = Piece(5, 1, self.BLUE, 24, True)
        self.pieces[piece.x][piece.y] = piece
        block24.addPiece(piece)
        piece = Piece(5, 2, self.BLUE, 24)
        self.pieces[piece.x][piece.y] = piece
        block24.addPiece(piece)
        piece = Piece(6, 2, self.BLUE, 24)
        self.pieces[piece.x][piece.y] = piece
        block24.addPiece(piece)
        piece = Piece(6, 3, self.BLUE, 24)
        self.pieces[piece.x][piece.y] = piece
        block24.addPiece(piece)
        piece = Piece(6, 4, self.BLUE, 24)
        self.pieces[piece.x][piece.y] = piece
        block24.addPiece(piece)
        piece = Piece(6, 5, self.BLUE, 24)
        self.pieces[piece.x][piece.y] = piece
        block24.addPiece(piece)

        #block 25
        block25 = Block()

        piece = Piece(5, 7, self.YELLOW, 25)
        self.pieces[piece.x][piece.y] = piece
        block25.addPiece(piece)
        piece = Piece(5, 8, self.YELLOW, 25, True)
        self.pieces[piece.x][piece.y] = piece
        block25.addPiece(piece)
        piece = Piece(6, 7, self.YELLOW, 25)
        self.pieces[piece.x][piece.y] = piece
        block25.addPiece(piece)
        piece = Piece(6, 8, self.YELLOW, 25)
        self.pieces[piece.x][piece.y] = piece
        block25.addPiece(piece)
        piece = Piece(6, 9, self.YELLOW, 25)
        self.pieces[piece.x][piece.y] = piece
        block25.addPiece(piece)
        
        #block 26
        block26 = Block()
        piece = Piece(5, 10, self.PINK, 26, True)
        self.pieces[piece.x][piece.y] = piece
        block26.addPiece(piece)

        #block 27
        block27 = Block()

        piece = Piece(5, 11, self.BLUE, 27)
        self.pieces[piece.x][piece.y] = piece
        block27.addPiece(piece)
        piece = Piece(5, 12, self.BLUE, 27)
        self.pieces[piece.x][piece.y] = piece
        block27.addPiece(piece)
        piece = Piece(5, 13, self.BLUE, 27)
        self.pieces[piece.x][piece.y] = piece
        block27.addPiece(piece)

        #block 28
        block28 = Block()

        piece = Piece(5, 14, self.ORANGE, 28, True)
        self.pieces[piece.x][piece.y] = piece
        block28.addPiece(piece)
        piece = Piece(6, 13, self.ORANGE, 28)
        self.pieces[piece.x][piece.y] = piece
        block28.addPiece(piece)
        piece = Piece(6, 14, self.ORANGE, 28)
        self.pieces[piece.x][piece.y] = piece
        block28.addPiece(piece)

        #block 29
        block29 = Block()

        piece = Piece(6, 0, self.YELLOW, 29)
        self.pieces[piece.x][piece.y] = piece
        block29.addPiece(piece)
        piece = Piece(6, 1, self.YELLOW, 29)
        self.pieces[piece.x][piece.y] = piece
        block29.addPiece(piece)

        #block 30
        block30 = Block()

        piece = Piece(6, 10, self.GREEN, 30)
        self.pieces[piece.x][piece.y] = piece
        block30.addPiece(piece)
        piece = Piece(6, 11, self.GREEN, 30)
        self.pieces[piece.x][piece.y] = piece
        block30.addPiece(piece)
        piece = Piece(6, 12, self.GREEN, 30, True)
        self.pieces[piece.x][piece.y] = piece
        block30.addPiece(piece)

        self.blocks.append(block1)
        self.blocks.append(block2)
        self.blocks.append(block3)
        self.blocks.append(block4)
        self.blocks.append(block5)
        self.blocks.append(block6)
        self.blocks.append(block7)
        self.blocks.append(block8)
        self.blocks.append(block9)
        self.blocks.append(block10)
        self.blocks.append(block11)
        self.blocks.append(block12)
        self.blocks.append(block13)
        self.blocks.append(block14)
        self.blocks.append(block15)
        self.blocks.append(block16)
        self.blocks.append(block17)
        self.blocks.append(block18)
        self.blocks.append(block19)
        self.blocks.append(block20)
        self.blocks.append(block21)
        self.blocks.append(block22)
        self.blocks.append(block23)
        self.blocks.append(block24)
        self.blocks.append(block25)
        self.blocks.append(block26)
        self.blocks.append(block27)
        self.blocks.append(block28)
        self.blocks.append(block29)
        self.blocks.append(block30)

        #Set all square in h (column 7) to be reachable
        for i in range(0, self.height):
            self.pieces[i][7].reachable = True
            self.possible_coords.add((i, 7))
            self.blocks[self.pieces[i][7].block_num - 1].reachable = True
            self.possible_blocks.add(self.pieces[i][7])

    def cross_cell(self, coord):
        x = coord[0]
        y = coord[1]

        self.pieces[x][y].crossed_out = True
        self.crossed_out_pieces.add((x,y))

        #Update number of colours left
        colour_of_piece = self.pieces[x][y].colour
        self.num_left_of_colour[colour_of_piece - 1] = self.num_left_of_colour[colour_of_piece - 1] - 1
        if self.num_left_of_colour[colour_of_piece - 1] == 0:
            colour_text = self.colour_num_to_text(colour_of_piece)
            print("We finished colour " + colour_text)

            if self.overall_completed_colour[colour_completed_num] == 0:
                self.completed_colour[colour_completed_num] = 1
            else:
                self.completed_colour[colour_completed_num] = 2
            self.overall_completed_colour[colour_completed_num] = 1 

        #Update number of cells in column left
        self.cells_left_in_column[y] = self.cells_left_in_column[y] - 1
        if self.cells_left_in_column[y] == 0:
            column_text = self.column_num_to_text(y)
            print("We finished column " + column_text)

            if self.overall_completed_column[column_filled_num] == 0:
                self.completed_column[column_filled_num] == 1
            else:
                self.completed_column[column_filled_num] == 2
            self.overall_completed_column[column_filled_num] = 1


        #Update block to have 1 less cell available
        block_id = self.pieces[x][y].block_num
        self.blocks[block_id - 1].open_cells = self.blocks[block_id - 1].open_cells - 1

        #Set all adjacent cells to be reachable now
        x_offset = [1, 0, -1, 0]
        y_offset = [0, 1, 0, -1]
        for i in range(0, len(x_offset)):
            new_x = x + x_offset[i]
            new_y = y + y_offset[i]

            if (new_x >= 0 and new_x < self.height and new_y >= 0 and new_y < self.width):
                self.pieces[new_x][new_y].reachable = True
                if not self.pieces[new_x][new_y].crossed_out:
                    self.possible_coords.add((new_x, new_y))

        self.possible_coords.remove(coord)
        
    def addBlock(self, block):
        self.blocks.append(block)

    def score_of_cell(self, coord):
        score = 0
        
        x = coord[0]
        y = coord[1]

        print("Finding score for cell (" + str(x) + ", " + str(y) + "):")

        piece = self.pieces[x][y]
        piece_colour = piece.colour

        #More points for a cell that is a star
        if piece.star:
            score = score + 2

        #Colour score
        colour_value = self.points_for_colour_first[piece_colour - 1]
        if self.overall_completed_colour[piece_colour - 1] == 1:
            colour_value = self.points_for_colour_second[piece_colour - 1]
        colour_score = colour_value / self.num_left_of_colour[piece_colour - 1]
        score = score + colour_score

        #Column score
        column_value = self.points_for_column_first[y]
        if self.overall_completed_column[y] == 1:
            column_value = self.points_for_column_second[y]
        column_score = column_value / self.cells_left_in_column[y]
        score = score + column_score


        #Score for making new block reachable
        block_id = piece.block_num
        x_offset = [1, 0, -1, 0]
        y_offset = [0, 1, 0, -1]
        new_blocks = set()
        for i in range(0, len(x_offset)):
            new_x = x + x_offset[i]
            new_y = y + y_offset[i]

            if (new_x >= 0 and new_x < self.height and new_y >= 0 and new_y < self.width):
                neighbour_piece = self.pieces[new_x][new_y]
                block_id_neighbour = neighbour_piece.block_num
                #Make sure the 2 pieces are not in the same block
                if block_id_neighbour != block_id:
                    #Make sure we haven't already gained access to this block
                    if block_id_neighbour not in new_blocks:
                        neighbour_block = self.blocks[block_id_neighbour - 1]
                        #Make sure this block is not already reachable
                        if not neighbour_block.reachable:
                            new_blocks.add(block_id_neighbour)
                            score = score + 1 #For now we give a new block a score of 1
        print(score)
        return score

    def best_possible_path(self, block_id, cells_to_fill, current_path):
        print("Trying to fill " + str(cells_to_fill) + " using this path:")
        print(current_path)

        current_cell = current_path[-1]

        start_x = current_cell[0]
        start_y = current_cell[1]

        cell_score = self.score_of_cell((start_x, start_y))

        if cells_to_fill <= 0:
            return cell_score, current_path

        #Grab the block
        block_to_fill = self.blocks[block_id - 1]

        max_score = -1000000000
        max_score_path = []

        for piece in block_to_fill.pieces:
            #Make sure this piece isn't already crossed out
            if piece.crossed_out:
                continue
            piece_coords = (piece.x, piece.y)

            #Make sure this piece is not already in our path
            if piece_coords not in current_path:
                #Make sure this piece is adjacent to one of the pieces in the current path
                if self.adjacent_to_path(piece_coords, current_path):

                    next_path = []
                    for coord in current_path:
                        next_path.append(coord)
                    next_path.append(piece_coords)

                    cell_left_to_fill = cells_to_fill - 1

                    path_score, path = self.best_possible_path(block_id, cell_left_to_fill, next_path)

                    #print("The score for this path is " + str(path_score))
                    #print(path)

                    overall_score = path_score + cell_score
                    if overall_score > max_score:
                        max_score = overall_score
                        max_score_path = path
        
        return max_score, max_score_path

    def max_block_score(self, block_id, cells_to_fill):
        score = 0
        
        block_to_fill = self.blocks[block_id - 1]

        #block_to_fill.printBlock()

        possible_starting_locations = []
        for piece_in_block in block_to_fill.pieces:
            if (piece_in_block.reachable) and (not piece_in_block.crossed_out):
                possible_starting_locations.append((piece_in_block.x, piece_in_block.y))
        
        max_score = -1000000000
        max_score_path = []
        
        block_made_available = set() #TODO: Add logic to not count a new reachable block twice!
        for possible_starting_location in possible_starting_locations:
            start_x = possible_starting_location[0]
            start_y = possible_starting_location[1]

            next_path = [(start_x, start_y)]

            #print(possible_starting_location)
            print("Enter 'Best_possible_path' with " + str(cells_to_fill - 1) + " cells to fill at location (" + str(start_x) + ", " + str(start_y) + ")")

            score, path = self.best_possible_path(block_id, cells_to_fill - 1, next_path)

            if len(path) != cells_to_fill:
                print("We found a path that is not of sufficient length")
                print(path)
                continue
            
            #modify score for block based on some conditions
            
            #We want a large part of the block to be left open if we are going to fill it at all
            cells_open_in_block = block_to_fill.open_cells
            cells_left_after_fill = cells_open_in_block - cells_to_fill
            #If we fill the entire block, it's pretty conveniant
            if cells_left_after_fill > 0:
                block_size = block_to_fill.size

                inconveniance_score = block_size / cells_left_after_fill
                score = score - inconveniance_score #Remove these points as it will be very inconveniant to fill it up later
            
            if score > max_score:
                max_score = score
                max_score_path = path

        return max_score, max_score_path

    def fill_path(self, path):
        for cell in path:
            self.cross_cell(cell)


    def fill_block(self, block_id, cells_to_fill):
        cells_filled = []

        block_to_fill = self.blocks[block_id - 1]

        #Find start index of this bloc
        current_index = -1
        index = 0
        for piece_in_block in block_to_fill:
            if piece_in_block.reachable:
                current_index = index
                break
            index = index + 1

        #Fill the cell up a much as possible 
        while cells_to_fill > 0:
            next_cell = block_to_fill.pieces[current_index]
            if next_cell.reachable and (not next_cell.crossed_out):
                next_cell_x = next_cell.x
                next_cell_y = next_cell.y

                self.cross_cell((next_cell_x, next_cell_y))
                cells_to_fill = cells_to_fill - 1
                cells_filled.append((next_cell_x, next_cell_y))
            
            current_index = current_index + 1
            if current_index >= block_to_fill.size:
                current_index = 0

        return cells_filled
        
    def adjacent_to_path(self, coord, path):
        for path_coord in path:
            x = path_coord[0]
            y = path_coord[1]
            x_offset = [1, 0, -1, 0]
            y_offset = [0, 1, 0, -1]
            for i in range(0, len(x_offset)):
                new_x = x + x_offset[i]
                new_y = y + y_offset[i]
                if (new_x == coord[0]) and (new_y == coord[1]):
                    return True
        
        return False
    
    def column_num_to_text(self, column_num):
        if column_num == 0:
            return "A"
        if column_num == 1:
            return "B"
        if column_num == 2:
            return "C"
        if column_num == 3:
            return "D"
        if column_num == 4:
            return "E"
        if column_num == 5:
            return "F"
        if column_num == 6:
            return "G"
        if column_num == 7:
            return "H"
        if column_num == 8:
            return "I"
        if column_num == 9:
            return "J"
        if column_num == 10:
            return "K"
        if column_num == 11:
            return "L"
        if column_num == 12:
            return "M"
        if column_num == 13:
            return "N"
        if column_num == 14:
            return "O"

    def colour_num_to_text(self, colour_num):
        if colour_num == self.GREEN:
            return "green"
        if colour_num == self.BLUE:
            return "blue"
        if colour_num == self.PINK:
            return "pink"
        if colour_num == self.YELLOW:
            return "yellow"
        if colour_num == self.ORANGE:
            return "orange"
        if colour_num == self.JOKER:
            return "joker"

    def printBoard(self):
        for row in range(0, self.height):
            column_print = ""
            for column in range(0, self.width):
                if self.pieces[row][column].crossed_out:
                    column_print = column_print + "x"
                else:
                    column_print = column_print + str(self.pieces[row][column].colour)
            #column_print = column_print + "\n"
            print(column_print)

                

