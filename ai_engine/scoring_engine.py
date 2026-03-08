def calculate_score(first_attempt, final_attempt, correct_answer):

    if correct_answer == 0:
        return 0

    improvement = final_attempt - first_attempt

    score = (final_attempt / correct_answer) * 70
    score += max(improvement, 0) * 3

    return round(score, 2)
