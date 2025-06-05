from collections import defaultdict

def find_winner(votes):
    """
    Args:
     votes(list_str)
    Returns:
     str
    """
    # Write your code here.
    highest_vote_count = 0
    winnersList = set()
    count_names_dict = defaultdict(int)

    # step1: find the highest count of the votes
    for name in votes:
        count_names_dict[name] += 1

    # step2: find the highest count from the dictionary
    highest_vote_count = max(count_names_dict.values())

    # step3: find the name who has got those highest count of the votes.
    for name, vote_count in count_names_dict.items():
        if vote_count == highest_vote_count:
            # if there is a tie then pick the lexicographically smallest name
            winnersList.add(name)

    return min(winnersList)

print(find_winner(votes=["sam", "john", "jamie", "sam"]))
print(find_winner(votes=["sam", "john", "sam", "john"]))
print(find_winner(votes=["sam", "sam", "samantha", "samantha"]))