def find_winner(votes):
    """
    Args:
     votes(list_str)
    Returns:
     str
    """
    # Write your code here.
    vote_count = highest_vote_count = 0
    winner = ''

    # step1: find the highest count of the votes
    for name in votes:
        vote_count = votes.count(name)
        highest_vote_count = max(highest_vote_count, vote_count)

    # step2: find the name who has got those highest count of the votes.
    for name in votes:
        vote_count = votes.count(name)
        if vote_count == highest_vote_count:
            # if there is a tie then pick the lexicographically smallest name
            winner = name if winner == '' else min(name, winner)

    return winner

print(find_winner(votes=["sam", "john", "jamie", "sam"]))
print(find_winner(votes=["sam", "john", "sam", "john"]))
print(find_winner(votes=["sam", "sam", "samantha", "samantha"]))