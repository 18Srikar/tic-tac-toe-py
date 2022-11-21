import math
from plane import Plane


def bot_move(game_plane):
    best_score = -math.inf
    best_move = ()
    for i in range(1, game_plane.length + 1):
        for j in range(1, game_plane.length + 1):
            if game_plane.cellIsEmpty(i, j):
                game_plane.markCell(i, j, 'bot')
                score = min_max(game_plane, False)
                game_plane.clearCell(i, j)
                if score > best_score:
                    best_move = (i, j)
                    best_score = score
    return best_move


def min_max(game_plane, bot_turn):
    win = game_plane.isComplete()

    if win is not None:
        return map_state(win)

    if bot_turn:
        best_score = -math.inf
        for i in range(1, game_plane.length + 1):
            for j in range(1, game_plane.length + 1):
                if game_plane.cellIsEmpty(i, j):
                    game_plane.markCell(i, j, 'bot')
                    score = min_max(game_plane, False)
                    game_plane.clearCell(i, j)
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(1, game_plane.length + 1):
            for j in range(1, game_plane.length + 1):
                if game_plane.cellIsEmpty(i, j):
                    game_plane.markCell(i, j, 'user')
                    score = min_max(game_plane, True)
                    game_plane.clearCell(i, j)
                    best_score = min(score, best_score)
        return best_score


def map_state(win):
    if win:
        return 10
    if not win:
        return -10
    return 0


def check_if_won(game_plane):
    win = game_plane.isComplete()
    if win == "DRAW":
        raise Exception('It is a draw!')
    if win is not None:
        raise Exception('The match ends\n' + ('You won' if (not win) else 'The bot won'))


level = int(input('enter number of rows and columns\n'))
game_plane = Plane(level)
while True:
    inp = input('type \'end\' to exit\nYour move: \n\'row\' \'col\'\n')
    if inp == 'end':
        print("you exited the game")
        break

    try:
        x, y = map(int, inp.split())
    except:
        if inp == 'end':
            break

    try:
        game_plane.markCell(x, y, "user")
        game_plane.printInstance()
        print()
    except Exception as e:
        print(e)
        continue

    try:
        check_if_won(game_plane)
    except Exception as e:
        print(e)
        break

    x, y = bot_move(game_plane)
    game_plane.markCell(x, y, 'bot')
    game_plane.printInstance()
    try:
        check_if_won(game_plane)
    except Exception as e:
        print(e)
        break
    finally:
        print()
