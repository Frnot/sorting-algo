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

    print(f"{order=}")
    print(f"{data=}")

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