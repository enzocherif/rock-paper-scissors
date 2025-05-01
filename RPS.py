# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    import random

    # Ajouter le dernier coup de l'adversaire à l'historique
    if prev_play:
        opponent_history.append(prev_play)

    guess = "R"  # Valeur par défaut

    if len(opponent_history) >= 3:
        # Prendre les 3 derniers coups
        last_moves = "".join(opponent_history[-3:])
        patterns = {}

        # Rechercher ce motif dans l'historique
        for i in range(len(opponent_history) - 3):
            pattern = "".join(opponent_history[i:i+3])
            next_move = opponent_history[i+3]
            if pattern == last_moves:
                if next_move in patterns:
                    patterns[next_move] += 1
                else:
                    patterns[next_move] = 1

        # Trouver le coup le plus probable
        if patterns:
            prediction = max(patterns, key=patterns.get)

            # Contrer ce coup
            if prediction == "R":
                guess = "P"
            elif prediction == "P":
                guess = "S"
            else:
                guess = "R"
        else:
            guess = random.choice(["R", "P", "S"])
    else:
        guess = random.choice(["R", "P", "S"])

    return guess

