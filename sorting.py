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

    print(f"{existing=}")
    print(f"{update=}")
    

    # Step 2: sort existing items
    existing, operations = sort(existing, update)

    ops.extend(operations)
    
    print(f"{existing=}")
    print(f"{ops=}")


    # Step 3: add missing items to the correct indexes
    for idx,e in enumerate(update):
        if e not in existing:
            ops.append(("add", e, idx))
            existing.insert(idx, e)

    print(f"{existing=}")
    print(f"{ops=}")

    return ops




def sort(unsorted, sorted):
    """    
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

    ops = []

    # step 1: generate ordvals

    ordval = {}
    for i in unsorted:
        ordval[i] = sorted.index(i)

    # find the largest set of in-order elements
    # unsorted and sorted should be equal sets
    sorted_lim = [i for i in sorted if i in unsorted]
    ordered = biog(None, unsorted, sorted_lim, ordval)

    # generate list of unordered elements
    unordered = [i for i in unsorted if i not in ordered]

    # sort the unordered elements, keeping track of the state of the list in the process
    while len(unordered) > 0:
        e = unordered.pop(0)
        old_idx = unsorted.index(e)
        last_se = ordered[0]

        if ordval[e] < ordval[last_se]: # beginning
            new_idx = unsorted.index(last_se)
            ops.append(("mov", old_idx, new_idx))

            unsorted.pop(old_idx)
            unsorted.insert(new_idx, e)

            ordered.insert(0, e)
            continue

        for next_se in ordered[1:]: # middle
            if ordval[last_se] < ordval[e] and ordval[e] < ordval[next_se]:
                # sort main list
                new_idx = unsorted.index(last_se) + 1
                ops.append(("mov", old_idx, new_idx))

                unsorted.pop(old_idx)
                if old_idx < new_idx:
                    unsorted.insert(new_idx-1, e)
                else:
                    unsorted.insert(new_idx, e)

                # update ordered list
                ordered.insert(ordered.index(last_se) + 1, e)
                break
            last_se = next_se

        else: # last
            if ordval[last_se] < ordval[e]:
                new_idx = unsorted.index(last_se) + 1
                ops.append(("mov", old_idx, new_idx))

                unsorted.pop(old_idx)
                if old_idx < new_idx:
                    unsorted.insert(new_idx-1, e)
                else:
                    unsorted.insert(new_idx, e)

                # update ordered list
                ordered.insert(ordered.index(last_se) + 1, e)

    return unsorted, ops




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
            if initial_element:
                groups.append([initial_element, smallest])
            else:
                groups.append([smallest])

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