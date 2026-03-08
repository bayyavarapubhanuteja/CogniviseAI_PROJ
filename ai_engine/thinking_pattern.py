from collections import defaultdict


def thinking_distribution(sessions):

    pattern_counts = defaultdict(int)

    for s in sessions:
        pattern_counts[s["thinking_pattern"]] += 1

    return dict(pattern_counts)
