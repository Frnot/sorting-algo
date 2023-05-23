import random

# an algorithm that attempts sort an array arbitrarily using the least number of move operations
# for this problem, moving an array element from any index n to m is considered a single operation
# other measures of time complexity are not considered

# This algorithm was developed primarily to sort a youtube playlist using the least number of API calls


def main():
    size_of_array = 10

    data = [i for i in range(size_of_array)]
    random.shuffle(data)
    order = data.copy()
    random.shuffle(data)

    #data = [7, 3, 1, 0, 8, 2, 5, 9, 4, 6]

    print(f"{order=}")
    print(f"{data=}")

    

    biog = sort(data, order) 




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

    # find the final indices these elements will have:
    biog_order = []
    for element in biog:
        biog_order.append(order.index(element))

    print(f"{biog=}")
    print(f"{biog_order=}")


    # the elements in biog are already sorted so they will not move
    # all the other elements needed to be sorted accordingly

    unsorted_data = [e for e in data if e not in biog]
    # find indices of nonsorted elements
    unsorted_indices = find_unsorted_indices(data, unsorted_data)

    print(f"{unsorted_indices=}")


    ###### TODO:
    # everytime un unsorted list is sorted, a new list of sorted items needs to be generated
    # and the list of unsorted indices needs to be updated

    # sort the unsorted elements, keeping a record of operations performed
    sorting_ops = []
    while unsorted_indices: # is not empty
        # translate the order for this element
        # order index is where the current unsorted index (i) is located in the final sorted list
        i = unsorted_indices[0]
        order_idx = order.index(data[i])

        # find where this element should be moved relatived to the sorted group
        if order_idx < biog_order[0]: # special case for beginning of list
            move(sorting_ops,data,i,0,unsorted_indices)
            unsorted_data.pop(0)
            unsorted_indices = find_unsorted_indices(data, unsorted_data)
        else:
            prev = biog_order[0] # todo update biog on every move
            for s in biog_order[1:]:
                next = s
                if order_idx < next:
                    new_idx = data.index(prev)
                    move(sorting_ops,data,i,new_idx,unsorted_indices)
                    unsorted_data.pop(0)
                    unsorted_indices = find_unsorted_indices(data, unsorted_data)
                    break
                prev = next
            else: # special case for end of list
                new_idx = data.index(next)+1
                move(sorting_ops,data,i,new_idx,unsorted_indices)
                unsorted_data.pop(0)
                unsorted_indices = find_unsorted_indices(data, unsorted_data)

        print()
        print(f"{sorting_ops=}")
        print(f"{data=}")
        print(f"{unsorted_indices=}")

    #TODO regenerate out of order indices every time we make a move

    print(f"{data=}")
    print(f"{sorting_ops=}")



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