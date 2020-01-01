import board
from board import Board

class Game: 

    board = 0
    turn_count = 1

    num_players = 0
    this_player = 0

    current_points = 0

    num_jokers_left = 8

    def __init__(self, num_players, this_player):
        self.num_players = num_players
        self.this_player = this_player

        self.board = Board()
        self.board.initDefaultBoard()

    def game_loop(self):

        #Main game loop
        playing = True
        while playing:

            print("This is turn " + str(self.turn_count))

            num_options = []
            colour_options = []
            
            num_input = 2
            this_player_turn = False

            #Get possible inputs
            if (self.turn_count <= 3):
                num_input = 3
            if ((self.turn_count % self.num_players) == self.this_player):
                num_input = 3
                this_player_turn = True
            
            print("Enter the colour options:")
            i = 0
            while i < num_input:
                colour_in = input("pick on of g, b, p, y, o or j(joker): ")
                if colour_in == 'q':
                    return

                colour_in_num = self.character_to_colour_num(colour_in)
                if colour_in_num == -1:
                    print("Please enter a valid input")
                    i = i - 1
                else:
                    colour_options.append(colour_in_num)
                i = i + 1

            print(colour_options)
            
            print("Enter the number options:")
            i = 0
            while i < num_input:
                num_in = input("Enter number between 1-5, or 0(joker): ")
                if num_in == 'q':
                    return
                if (num_in == '1') or (num_in == '2') or (num_in == '3') or (num_in == '4') or (num_in == '5') or (num_in == '0'):
                    num_options.append(int(num_in))
                else:
                    print("Please enter a valid input")
                    i = i - 1
                i = i + 1

            print(num_options)


            best_path, colour_used, number_used, colour_joker_used, number_joker_used = self.decide_best_option(colour_options, num_options)

            if len(best_path) > 0: 
                colour_used_text = self.board.colour_num_to_text(colour_used)
                print(colour_options)
                print(num_options)
                print(self.board.crossed_out_pieces)
                
                print("Used colour '" + colour_used_text + "' filling in " + str(number_used) + " cells")
                for cell in best_path:
                    print(cell)

                self.fill_path(best_path)

                if colour_joker_used:
                    self.num_jokers_left = self.num_jokers_left - 1
                if number_joker_used:
                    self.num_jokers_left = self.num_jokers_left - 1

            self.board.printBoard()
            print("You've got " + str(self.num_jokers_left) + " left to use.")

            #Check to see if you completed any columns (this should probs be done in the program it self)
            while False:
                column_filled = input("Did you complete any columns? (a-o) or x for none: ")
                if column_filled == 'x':
                    break

                column_filled_num = self.character_to_column_num(column_filled)
                if column_filled_num == -1:
                    print("Please enter a valid input")
                else:
                    if self.board.overall_completed_column[column_filled_num] == 0:
                        self.board.completed_column[column_filled_num] == 1
                    else:
                        self.board.completed_column[column_filled_num] == 2
                    self.board.overall_completed_column[column_filled_num] = 1

            #Check to see if anyone else completed any columns
            while True:
                column_filled = input("Did anyone else complete any columns? (a-o) or x for none: ")
                if column_filled == 'x':
                    break

                column_filled_num = self.character_to_column_num(column_filled)
                if column_filled_num == -1:
                    print("Please enter a valid input")
                else:
                    self.board.overall_completed_column[column_filled_num] = 1

            #Check to see if you completed any colours (this should probs be doen in the program it self)
            while False:
                colour_completed = input("Did you complete any colours? b, g, p, y, o or n(none): ")
                if colour_completed == 'n':
                    break

                colour_completed_num = self.character_to_colour_num(colour_completed)
                if colour_completed_num == -1:
                    print("Please enter a valid input")
                else:
                    if self.board.overall_completed_colour[colour_completed_num] == 0:
                        self.board.completed_colour[colour_completed_num] = 1
                    else:
                        self.board.completed_colour[colour_completed_num] = 2
                    self.board.overall_completed_colour[colour_completed_num] = 1 

            #Check to see if anyone else completed any columns
            while True:
                colour_completed = input("Did anyone else complete any colours? b, g, p, y, o or n(none): ")
                if colour_completed == 'n':
                    break

                colour_completed_num = self.character_to_colour_num(colour_completed)
                if colour_completed_num == -1:
                    print("Please enter a valid input")
                else:
                    self.board.overall_completed_colour[colour_completed_num] = 1 
    
            #Determine whether game has ended
            while True:
                game_ended = input("Has the game ended? (y or n): ")
                if game_ended == 'y':
                    #Calculate score
                    playing = False
                    break
                elif game_ended == 'n':
                    break
                else:
                    print("Please enter a valid input")

            self.turn_count = self.turn_count + 1

        total_score = self.calculate_score()

        #Print the game score
        print("Your final score is: " + str(total_score))

    def decide_best_option(self, colour_options, num_options):
        print(colour_options)
        print(num_options)
        
        options = self.board.possible_coords
        print(options)

        has_answer = False
        answer_coords = []

        has_colour_joker = False
        if 0 in colour_options:
            has_colour_joker = True
        
        has_num_joker = False
        if 0 in num_options:
            has_num_joker = True

        max_score = -1000000000
        max_score_path = []
        colour_used = None
        number_used = -1
        colour_joker_used = False
        number_joker_used = False

        for option in options:
            print("Checking option " + str(option[0]) + ", " + str(option[1]))
            x = option[0]
            y = option[1]

            piece = self.board.pieces[x][y]
            
            #Make sure this piece has not been crossed out. We should never get here!
            if piece.crossed_out:
                print("Piece " + str(piece.x) + ", " + str(piece.y) + " has already been crossed out")
                continue

            colour_of_option = piece.colour
            is_colour_possible = False
            using_colour_joker = False

            #Make sure this block can be filled with the colour options provided
            if (colour_of_option in colour_options):
                is_colour_possible = True
            elif has_colour_joker and (self.num_jokers_left > 0):
                is_colour_possible = True
                using_colour_joker = True
            
            if is_colour_possible:
                colour_text = self.board.colour_num_to_text(colour_of_option)
                print("We can use colour " + colour_text)
                block_id = piece.block_num #TODO: Give all blocks their own id's, they currently don't know what id they are
                block_of_piece = self.board.blocks[block_id - 1]
                block_open_cells = block_of_piece.open_cells

                #Add all numbers to the set of possible number of cells to fill if a joker is possible
                new_num_options = set(num_options)
                if has_num_joker:
                    new_num_options.remove(0)
                    if (self.num_jokers_left > 0):
                            all_nums = [1,2,3,4,5]
                            for num in all_nums:
                                new_num_options.add(num)

                print("The number of options after taking into account the joker: ")
                print(new_num_options)

                #Go through all number options to find the best result
                for num_option in new_num_options:
                    if num_option <= block_open_cells:
                        cells_to_fill = num_option

                        print("Finding the max score for block " + str(block_id) + " while trying to fill " + str(cells_to_fill) + " cells")

                        score, path = self.board.max_block_score(block_id, cells_to_fill)

                        if using_colour_joker:
                            score = score - 1

                        #If the original set of number options did not include this possible number, we are using a joker, subtract 1 from it's score
                        if num_option not in num_options:
                            score = score - 1

                        if score > max_score:
                            max_score = score
                            max_score_path = path
                            
                            colour_used = colour_of_option
                            if using_colour_joker:
                                colour_used = self.board.JOKER
                            
                            number_used = num_option

                            colour_joker_used = using_colour_joker
                            if num_option not in num_options:
                                number_joker_used = True
                            else:
                                number_joker_used = False

                        
        #Make sure we actually found a possible solution
        if max_score > -1000000000:
            print("Found a possible solution with score " + str(max_score))
        else:
            print("There are no possible solutions")
            max_score_path = [] #Make sure the path is set to length of 0

        return max_score_path, colour_used, number_used, colour_joker_used, number_joker_used

    def calculate_score(self):
        #Get number of colour scores
        colour_score = 0
        for i in range(0, len(self.board.completed_colour)):
            if self.board.completed_colour[i] == 1:
                colour_score = colour_score + self.board.points_for_colour_first[i]
            elif self.board.completed_colour[i] == 2:
                colour_score = colour_score + self.board.points_for_colour_second[i]
        
        #Get number of column scores
        column_score = 0
        for i in range(0, len(self.board.completed_column)):
            if self.board.completed_column[i] == 1:
                column_score = column_score + self.board.points_for_column_first[i]
            elif self.board.completed_column[i] == 2:
                column_score = column_score + self.board.points_for_column_second[i]
        
        #Get joker score
        joker_score = self.num_jokers_left

        #Get star score
        star_score = 0
        for row in range(0, self.board.height):
            for column in range(0, self.board.width):
                piece = self.board.pieces[row][column]
                if piece.star:
                    if not piece.crossed_out:
                        star_score = star_score - 2
        
        #Get the total score
        total_score = colour_score + column_score + joker_score + star_score

        return total_score
    
    def fill_path(self, path):
        self.board.fill_path(path)
    
    def character_to_column_num(self, character):

        column_filled_num = -1
        if (character == 'a'):
            column_filled_num = 0
        elif (character == 'b'):
            column_filled_num = 1
        elif (character == 'c'):
            column_filled_num = 2
        elif (character == 'd'):
            column_filled_num = 3
        elif (character == 'e'):
            column_filled_num = 4
        elif (character == 'f'):
            column_filled_num = 5
        elif (character == 'g'):
            column_filled_num = 6
        elif (character == 'h'):
            column_filled_num = 7
        elif (character == 'i'):
            column_filled_num = 8
        elif (character == 'j'):
            column_filled_num = 9
        elif (character == 'k'):
            column_filled_num = 10
        elif (character == 'l'):
            column_filled_num = 1
        elif (character == 'm'):
            column_filled_num = 12
        elif (character == 'n'):
            column_filled_num = 13
        elif (character == 'o'):
            column_filled_num = 14
        
        return column_filled_num

    def character_to_colour_num(self, character):
        colour_num = -1
        if character == 'g':
            colour_num = self.board.GREEN
        elif character == "b":
            colour_num = self.board.BLUE
        elif character == "p":
            colour_num = self.board.PINK
        elif character == "y":
            colour_num = self.board.YELLOW
        elif character == "o":
            colour_num = self.board.ORANGE
        elif character == 'j':
            colour_num = self.board.JOKER
        
        return colour_num