def is_family(tree):
    family = {tree[0][0]}

    children = [x[1] for x in tree]
    if len(children) != len(set(children)):
        return False

    while tree:
        nothing = True

        for relationship in tree.copy():
            if len(family & set(relationship)) == 1:
                family |= set(relationship)

                nothing = False
                tree.remove(relationship)

        if nothing:
            break
    else:
        return True

    return False


# fromfrom  collectionscollecti  import defaultdict
#
# def is_family(tree):
#     anscestor = defaultdict(set)
#     for father, son in tree:
#         if father == son: return False
#         if father in anscestor[son]: return False
#         if son in anscestor[father]: return False
#         if anscestor[father] & anscestor[son]: return False
#         anscestor[son] |= {father} | anscestor[father]
#     adam = [person for person in anscestor if not anscestor[person]]
#     return len(adam) == 1



if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_family([
        ['Logan', 'Mike']
    ]) == True, 'One father, one son'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack']
    ]) == True, 'Two sons'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack'],
        ['Mike', 'Alexander']
    ]) == True, 'Grandfather'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack'],
        ['Mike', 'Logan']
    ]) == False, 'Can you be a father for your father?'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack'],
        ['Mike', 'Jack']
    ]) == False, 'Can you be a father for your brather?'
    assert is_family([
        ['Logan', 'William'],
        ['Logan', 'Jack'],
        ['Mike', 'Alexander']
    ]) == False, 'Looks like Mike is stranger in Logan\'s family'
    print("Looks like you know everything. It is time for 'Check'!")
