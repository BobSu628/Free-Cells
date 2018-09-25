from Game import Game


def process(game, command):
    command = command.strip().split(' ')
    for i in range(len(command)):
        command[i] = command[i].strip()

    if command[0] == 'f':
        game.free(int(command[1]))

    elif command[0] == 'd':
        game.discard(int(command[1]))

    elif command[0] == 'r':
        game.retrieve(int(command[1]), int(command[2]))

    elif command[0] == 'm':
        if len(command) == 3:
            game.move(int(command[1]), int(command[2]))

        elif len(command) == 4:
            game.move(int(command[1]), int(command[2]), int(command[3]))


def win(game):
    return game.win()


def main():
    game_quit = False
    q = input("Do you wish to continue?")
    if q == 'n':
        game_quit = True

    game = Game()

    while not game_quit:

        print(game)

        command = input("Next Move: ")
        process(game, command)

        if win(game):
            print("Congrats")
            game_quit = True


#main
if __name__ == '__main__':
    main()
