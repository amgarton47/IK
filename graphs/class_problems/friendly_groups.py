# same as checking if is bipartite
def can_be_divided(num_of_people, dislike1, dislike2):
    adj_list = [[] for _ in range(num_of_people)]

    for i in range(len(dislike2)):
        s, e = dislike1[i], dislike2[i]
        adj_list[s].append(e)
        adj_list[e].append(s)

    color = [-1 for _ in range(num_of_people)]

    def is_bipartite(s, s_color):
        color[s] = s_color

        for w in adj_list[s]:
            if color[w] == -1:
                if not is_bipartite(w, 1 - s_color):
                    return False
            elif color[s] == color[w]:
                return False
        return True

    for i in range(num_of_people):
        if color[i] == -1:
            if not is_bipartite(i, 0):
                return False

    return True
