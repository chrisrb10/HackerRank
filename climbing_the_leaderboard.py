
# climbing the leaderboard


from bisect import bisect


def climbingLeaderboard(scores, alice):
    a_rank=[]
    r_scores = list(set(scores))
    r_scores.sort()
    for a_score in alice:
        a_rank.append((len(r_scores) - bisect(r_scores, a_score))+1)
    return a_rank
