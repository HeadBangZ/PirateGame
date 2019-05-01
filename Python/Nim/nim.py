from flask import Flask, render_template, request, Markup

app = Flask(__name__)

# Get the first time
@app.route('/', methods=['GET'])
def hello():
    global my_title, game_history
    return render_template('nim.html', title=my_title, history=game_history)

# POST when playing
@app.route('/', methods=['POST'])
def play():
    global my_title, game_history, xp, pile, current_game, pc_win, disabled_btn
    if request.form['myaction'] == 'Send':
        # take from pile, no input check
        taken = int(request.form['mytake'])
        pile = pile - taken
        current_game[pile] = -1
        game_history.append(Markup('You took ' + str(taken) + ' from the pile now there are this many left: ' + str(pile)))
        pc_move()
    else:
        reset_game()
    return render_template('nim.html', title=my_title, history=game_history, disabled=disabled_btn)

def pc_move():
    global my_title, game_history, xp, pile, current_game, pc_win, disabled_btn
    if pile == 0:
        game_history.append(Markup('You win!'))
        update_xp()
    else:
        # take a number, max 3, min 1, max number in pile
        if pile >= 3 and xp[pile-3] > xp[pile-1] and xp[pile-3] > xp[pile-2]:
            taken = 3
        elif pile >= 2 and xp[pile-2] > xp[pile-1]:
            taken = 2
        else:
            taken = 1
        pile = pile - taken
        current_game[pile] = 1
        game_history.append(Markup('PC took ' + str(taken) + ' from the pile now there are this many left: ' + str(pile)))
        if pile == 0:
            game_history.append(Markup('PC win!'))
            pc_win = True
            update_xp()

def update_xp():
    global my_title, game_history, xp, pile, current_game, pc_win, disabled_btn
    for i in range(1, 22):
        if pc_win:
            xp[i] += current_game[i]
        else:
            xp[i] -= current_game[i]
        xp[i] = min(10, xp[i])
        xp[i] = max(-10, xp[i])
    print(current_game)
    print(xp)

def reset_game():
    global my_title, game_history, xp, pile, current_game, pc_win, disabled_btn
    my_title = "Game of Nim"
    game_history = []
    pile = 21
    current_game = [0] * 22
    # Markup is needed to display a string as html with e.g. &nbsp;
    game_history.append(Markup('You start: ' + str(pile) + ' items in pile'))
    pc_win = False
    disabled_btn = ""

xp = [0] * 22
xp[0] = 11

reset_game()

if __name__ == '__main__':
    app.run('localhost', 4449)