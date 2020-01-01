from board import Board
from game import Game


#board = Board()

#board.initDefaultBoard()
#board.printBoard()

num_players = input("How many people are playing? ")

this_player = input("What player number are you? ")


game = Game(int(num_players), int(this_player))

game.game_loop()




quit_game = False

if quit_game:
    #Main game loop
    while True:

        num_options = []
        colour_options = []
        
        num_input = 2

        #Get possible inputs
        if (turn_count < 3) or ((turn_count % num_players) == your_position):
            num_input = 3
        
        print("Enter the colour options:")
        for i in range(0, num_input):
            colour_in = input("pick on of g, b, p, y, o or j(joker): ")
            if colour_in == 'q':
                quit_game = True
                break

            if colour_in == 'g':
                colour_options.append(1)
            elif colour_in == "b":
                colour_options.append(2)
            elif colour_in == "p":
                colour_options.append(3)
            elif colour_in == "y":
                colour_options.append(4)
            elif colour_in == "o":
                colour_options.append(5)
            elif colour_in == "j":
                colour_options.append(0)
        if quit_game:
            break

        print(colour_options)
        
        print("Enter the number options:")
        for i in range(0, num_input):
            num_in = input("Enter number between 1-5, or 0(joker): ")
            if num_in == 'q':
                quit_game = True
                break
            num_options.append(int(num_in))
        
        if quit_game:
            break

        print(num_options)

        best_path = game.decide_best_option(colour_options, num_options)

        for cell in best_path:
            print(cell)

        game.fill_path(best_path)

        game.board.printBoard()
        
