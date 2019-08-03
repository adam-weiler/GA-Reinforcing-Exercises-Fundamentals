ballots = [{'gold': 'Smudge', 'silver': 'Tigger', 'bronze': 'Simba'},
           {'gold': 'Bella', 'silver': 'Lucky', 'bronze': 'Tigger'},
           {'gold': 'Bella', 'silver': 'Boots', 'bronze': 'Smudge'},
           {'gold': 'Boots', 'silver': 'Felix', 'bronze': 'Bella'},
           {'gold': 'Lucky', 'silver': 'Felix', 'bronze': 'Bella'},
           {'gold': 'Smudge', 'silver': 'Simba', 'bronze': 'Felix'}]

point_values = {'gold': 3, 'silver': 2, 'bronze': 1}


def tally_ballots(ballots):
    all_scores = {}
    for game in ballots:
        for medal, player in game.items():
            # print(f'A {medal} for {player}: {point_values[medal]} points.')

            if player not in all_scores:  #If player's first score.
                all_scores[player] = point_values[medal]
            else:  #Else player scored already.
                all_scores[player] += point_values[medal]

        # print(f"{game['gold']}, {game['silver']}, {game['bronze']}")
    return all_scores


def pick_winner(all_scores):
    high_scorer = ''
    high_score = 0

    for player, score in all_scores.items():
        # print(f'{player} has {score} points.')
        if score > high_score:
            # print('New high score!!')
            high_score = score
            high_scorer = player

    return f'Player {high_scorer} is the winner with {high_score} points!'


all_scores = tally_ballots(ballots)
print(all_scores)
print(pick_winner(all_scores))
