
"""
From Leetcode: https://leetcode.com/problems/find-the-town-judge/
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the
person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
"""
num = 4
trust1 = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]

# Solution 1


def find_judge(n, trust):
    """
    initialize the trust of everyone as zero.
    For every a minus 1 trust score and add to corresponding b
    It follows that, the judge must have n - 1 people trusting him/her
    :param n: number of people in the city
    :param trust: who trusts who i.e. a trusts b
    :return: judge or -1 if none
    """
    trust_scores = [0] * n

    for a, b in trust:
        trust_scores[a - 1] -= 1
        trust_scores[b - 1] += 1

    for p in range(n):
        if trust_scores[p] == n - 1:
            return p + 1
    return -1


print(find_judge(num, trust1))


"""
Since this is a graph, if you want to build and visualize this well:
directional graph made by below fn 
"""


def build_graph(trust):
    graph = {}
    for node in trust:
        [a, b] = node

        if a not in graph:
            graph[a] = []
        graph[a].append(b)
    return graph
