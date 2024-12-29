def my_permutations(elements):
    """
    Generate all permutations of the given list of elements.

    :param elements: List of elements to permute
    :return: A list of all permutations
    """
    if len(elements) == 0:
        return [[]]  # Base case: one permutation of an empty list is an empty list
    
    # Recursive case
    permutations = []
    for i in range(len(elements)):
        # Extract the current element
        current = elements[i]
        # Remaining elements
        remaining = elements[:i] + elements[i+1:]
        # Generate permutations for the remaining elements
        for p in my_permutations(remaining):
            permutations.append([current] + p)
    return permutations

# Example usage
if __name__ == "__main__":
    elements = [1, 2, 3]
    result = my_permutations(elements)
    for perm in result:
        print(perm)
