def count_votes():
    votes = {'candidate1': 100, 'candidate2': 150}
    winner = max(votes, key=votes.get)
    return f"The winner is {winner} with {votes[winner]} votes."