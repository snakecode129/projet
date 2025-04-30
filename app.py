from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Initialisation du plateau et du jeu
board = ["-" for _ in range(9)]
current_player = "X"
winner = None
game_running = True

# Affichage du plateau (texte)
def print_board():
    return f"{board[0]}|{board[1]}|{board[2]}\n{board[3]}|{board[4]}|{board[5]}\n{board[6]}|{board[7]}|{board[8]}\n"

# Vérifications des victoires et égalité
def check_win():
    global winner
    # Check lignes, colonnes, et diagonales
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # lignes
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # colonnes
        [0, 4, 8], [2, 4, 6]              # diagonales
    ]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != "-":
            winner = board[condition[0]]
            return True
    return False

def check_tie():
    return "-" not in board

# API pour récupérer l'état du jeu
@app.route('/board', methods=['GET'])
def get_board():
    return jsonify(board=board, current_player=current_player)

# API pour jouer un coup
@app.route('/play', methods=['POST'])
def play():
    global current_player, winner, game_running
    data = request.get_json()
    position = data.get('position')

    # Validation de l'entrée
    if position < 0 or position > 8 or board[position] != "-":
        return jsonify(message="Position invalide ou déjà occupée"), 400

    # Jouer le coup
    board[position] = current_player

    # Vérification de victoire ou égalité
    if check_win():
        game_running = False
        return jsonify(message=f"Le joueur {winner} a gagné ! 🎉", winner=winner)

    if check_tie():
        game_running = False
        return jsonify(message="Match nul 🤝", winner=None)

    # Changer de joueur
    current_player = "O" if current_player == "X" else "X"
    return jsonify(message="Coup joué avec succès", current_player=current_player)

# Redémarrer le jeu
@app.route('/reset', methods=['POST'])
def reset_game():
    global board, current_player, game_running, winner
    board = ["-" for _ in range(9)]
    current_player = "X"
    game_running = True
    winner = None
    return jsonify(message="Jeu réinitialisé", board=board, current_player=current_player)

if __name__ == "__main__":
    app.run(debug=True)

    