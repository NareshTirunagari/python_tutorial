from collections import defaultdict

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
    #count_names_dict = {}
    count_names_dict = defaultdict(int)

    # step1: find the highest count of the votes
    for name in votes:
        count_names_dict[name] += 1
        #count_names_dict[name] = count_names_dict.get(name, 0) + 1
        highest_vote_count = max(highest_vote_count, votes.count(name))

    # step2: find the name who has got those highest count of the votes.
    for name, vote_count in count_names_dict.items():
        if vote_count == highest_vote_count:
            # if there is a tie then pick the lexicographically smallest name
            winner = name if winner == '' else min(name, winner)

    return winner

print(find_winner(votes=["sam", "john", "jamie", "sam"]))
print(find_winner(votes=["sam", "john", "sam", "john"]))
print(find_winner(votes=["sam", "sam", "samantha", "samantha"]))