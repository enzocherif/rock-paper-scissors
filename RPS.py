def player(prev_play, opponent_history=[], state={"memory": {}, "last_n": 3, "losses": 0, "total": 0}):
    import random
    from collections import Counter

    if prev_play:
        opponent_history.append(prev_play)

    def predict_next_move(history, n):
        if len(history) < n:
            return None
        pattern = "".join(history[-n:])
        counts = {}
        for i in range(len(history) - n):
            if "".join(history[i:i+n]) == pattern:
                next_move = history[i+n]
                if next_move in counts:
                    counts[next_move] += 1
                else:
                    counts[next_move] = 1
        if counts:
            return max(counts, key=counts.get)
        return None

    # Try to predict from n=4,3,2
    prediction = None
    for n in [4, 3, 2]:
        prediction = predict_next_move(opponent_history, n)
        if prediction:
            break

    # Fallback: most frequent move
    if not prediction and opponent_history:
        freq = Counter(opponent_history)
        prediction = freq.most_common(1)[0][0]

    # Default random
    if not prediction:
        guess = random.choice(["R", "P", "S"])
    else:
        if prediction == "R":
            guess = "P"
        elif prediction == "P":
            guess = "S"
        elif prediction == "S":
            guess = "R"

    # Save result and adjust if many recent losses
    if state["total"] > 5:
        recent_win_rate = 1 - state["losses"] / state["total"]
        if recent_win_rate < 0.55:
            # flip the counter occasionally if we’re failing
            flip = {"R": "S", "P": "R", "S": "P"}
            guess = flip.get(guess, guess)
        state["losses"] = 0
        state["total"] = 0

    if len(opponent_history) > 0 and len(opponent_history) == len(state.get("my_moves", [])) + 1:
        my_prev = state.get("my_moves", [])[0] if state.get("my_moves") else None
        if my_prev:
            beaten_by_opp = (
                (my_prev == "R" and opponent_history[-1] == "P") or
                (my_prev == "P" and opponent_history[-1] == "S") or
                (my_prev == "S" and opponent_history[-1] == "R")
            )
            if beaten_by_opp:
                state["losses"] += 1
        state["total"] += 1

    # Sauvegarde du coup joué
    if "my_moves" not in state:
        state["my_moves"] = []
    state["my_moves"].append(guess)

    return guess
