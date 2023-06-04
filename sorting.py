# an algorithm that attempts sort an array arbitrarily using the least number of move operations
# for this problem, moving an array element from any index n to m is considered a single operation
# other measures of time complexity are not considered

# This algorithm was developed primarily to sort a youtube playlist using the least number of API calls


def main(existing, update):
    """Takes a list of existing items and a list of updated items
    Returns a minimum list of operations required to transform <existing> into <update>"""

    ops = [] # a list of operations to perform on the existing list

    # Step 1: remove items from existing that don't exist in update
    idx = 0
    while idx < len(existing):
        if existing[idx] not in update:
            ops.append(("del", idx))
            existing.pop(idx)
        else:
            idx += 1

    print(f"{ops=}")
    print(f"{existing=}")
    

    #existing, operations = sort(existing, update)
    pass


def sort(unsorted, sorted):
    """unsorted and sorted should be equal sets
    
    items in unsorted listed are mapped to their correct position in the sorted list
    an unsorted item's position in the sorted list is reffered to as ordval
    
    ex:
    correct order: [D, A, C, E, B]
    unsorted order: [C, B, D, A, E]
    item -> ordval
        C : 2
        B : 4
        D : 0
        A : 1
        E : 3
    """

    # step 1: generate ordvals

    ordval = {}
    for i in unsorted:
        ordval[i] = sorted.index(i)

    
    bg = biog(None, unsorted, order, ordval)




def biog(initial_element, partial_list, sorted, ordval):
    """
    Finds largest set of elements that occur in order in <partial_list>
    The time complexity of this function is difficult to compute
    safe to say, it is very bad.
    """

    complete_set = set(partial_list)
    traversed = set()

    if initial_element:
        groups = [[initial_element]]
        initial_ordval = ordval[initial_element]
    else:
        groups = []
        initial_ordval = -1

    while not traversed == complete_set:
        # find smallest in-order element to the right of index 0
        smallest = None
        for e in partial_list:
            if ordval[e] < initial_ordval or e in traversed:
                continue
            if not smallest or ordval[e] < ordval[smallest]:
                smallest = e

        if not smallest:
            break

        if partial_list.index(smallest) == len(partial_list)-1: # smallest element is at end of list
            groups.append([initial_element, smallest])
            traversed.add(smallest)
        else:
            group = biog(smallest, partial_list[partial_list.index(smallest)+1:], sorted, ordval)
            traversed.update(group)
            if initial_element:
                group.insert(0, initial_element)
            groups.append(group)

    # return longest group
    maxidx = 0
    maxlen = 0
    for idx, group in enumerate(groups):
        if len(group) > maxlen:
            maxlen = len(group)
            maxidx = idx
    return groups[maxidx]

    







if __name__ == "__main__":
    order = ["b", "d", "e", "a", "c", "g", "f"]
    existing = ["z", "h", "a", "c", "e", "d", "y"]
    
    main(existing, order)

    order = ["D", "A", "C", "E", "B"]
    #order = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "", "Z"]
    
    unsorted = order.copy()

    import random
    from time import perf_counter
    for _ in range(100):
        random.shuffle(unsorted)
        print(f"{unsorted=}")

        s = perf_counter()

        ordval = sort(unsorted, order)
        bg = biog(None, unsorted, order, ordval)

        e = perf_counter()

        print(f"{bg=}")
        print(f"Took {e-s} seconds")

        input()