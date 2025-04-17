def all_pairs_equal(list):
    for i in range(len(list)):
        if list[i] != list[-i - 1]:
            return False
    return True

# Test cases
print(all_pairs_equal([7,-2,3,9,3,-2,7]))
print(all_pairs_equal([7,-2,3,9,3,2,7]))
