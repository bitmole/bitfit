def permute(s):
    """ Permutes given string

    :s: string to permute
    :returns: list of permutations

    """
    result = []
    if len(s) == 0: return result
    if len(s) == 1: 
        result.append(s)
        return result

    for i, c in enumerate(s):
        rest_perms = permute(rest(s, i))
        # concat & append
        result += [c + el for el in rest_perms]

    return result

def rest(s, i):
    return s[:i] + s[i+1:]
