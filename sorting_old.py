import random

# an algorithm that attempts sort an array arbitrarily using the least number of move operations
# for this problem, moving an array element from any index n to m is considered a single operation
# other measures of time complexity are not considered

# This algorithm was developed primarily to sort a youtube playlist using the least number of API calls


def main():
    size_of_array = 10

    data = [i for i in range(size_of_array)]
    #random.shuffle(data)
    order = data.copy()
    random.shuffle(data)

    #data=[4, 3, 2, 0, 1]

    print(f"{order=}")
    print(f"{data=}")

    

    ordered = sort(data, order) 
    print(ordered)

    return order,ordered




def sort(data, order):
    groups = []
    traversed = set()

    for idx,element in enumerate(data):
        if element not in traversed:
            biog = biggest_inorder_group(data[idx:])
            groups.append(biog)
            traversed.update(biog)

    for group in groups:
        if len(group) > len(biog):
            biog = group

    print(f"{biog=}")


    #element index equals value for first version
    inorder_elements = biog
    outorder_elements = [e for e in data if e not in inorder_elements]

    print(f"{outorder_elements=}")

    for element in outorder_elements:
        ooi = data.index(element)

        next = inorder_elements[0]
        if element < next:
            # move to front
            # data.insert(new_idx, data.pop(old_idx))
            print(f"mov {ooi}, 0")
            data.insert(0, data.pop(ooi))
            inorder_elements.insert(0, element)
            print(f"{data=}")
            print(f"{inorder_elements=}")
            continue
        prev = next
        for ioi,next in enumerate(inorder_elements[1:],start=1):
            if element > prev and element < next:
                # move to just after prev
                if data.index(prev) < ooi:
                    print(f"mov {ooi}, {data.index(prev)+1}")
                    data.insert(data.index(prev)+1, data.pop(ooi))
                else:
                    print(f"mov {ooi}, {data.index(prev)}")
                    data.insert(data.index(prev), data.pop(ooi))
                inorder_elements.insert(ioi, element)
                print(f"{data=}")
                print(f"{inorder_elements=}")
                break
            prev = next
        else:
            # move to back
            print(f"mov {ooi}, {len(data)}")
            data.append(data.pop(ooi))
            inorder_elements.append(element)
            print(f"{data=}")
            print(f"{inorder_elements=}")
        

    return data



def find_unsorted_indices(data, unsorted_data):
    unsorted_indices = []
    for idx,element in enumerate(data):
        if element in unsorted_data:
            unsorted_indices.append(idx)
    return unsorted_indices


def move(sorting_ops, data, old_idx, new_idx, unsorted_indices):
    sorting_ops.append(("mov", old_idx, new_idx))
    data.insert(new_idx, data.pop(old_idx))

    for idx,u in enumerate(unsorted_indices[1:],start=1):
        if unsorted_indices[0] < u:
            unsorted_indices[idx] = u-1





def biggest_inorder_group(partial_list):
    if len(partial_list) == 1:
        return partial_list
    
    groups = [] # list of sets
    traversed = set()

    partial_set = set(partial_list[1:])

    while not traversed == partial_set:
        min = 999
        found_min = False
        # now find second smallest element
        for item in partial_list[1:]:
            if item > partial_list[0] and item < min and item not in traversed:
                min = item
                found_min = True
        
        if not found_min:
            break

        min_idx = partial_list.index(min)
        to_send = partial_list[min_idx:]
        group = biggest_inorder_group(to_send)
        groups.append(group)
        traversed.update(group)

    longest_group = []
    for group in groups:
        if len(group) > len(longest_group):
            longest_group = group

    longest_group.insert(0, partial_list[0])
    return longest_group



if __name__ == "__main__":
    main()
    quit()

    for _ in range(10000):
        order,ordered = main()
        if order != ordered:
            print("mismatch")
            break
    else:
        print("no errors found")
    input()