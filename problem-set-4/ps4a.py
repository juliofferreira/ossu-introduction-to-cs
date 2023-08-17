# Problem Set 4A

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    if len(sequence) <= 1:
        return [sequence]

    first_letter = sequence[0]
    permutations_remaining_letters = get_permutations(sequence[1:])
    list_permutations = []
    for permutation in permutations_remaining_letters:
        for index in range(len(permutation) + 1):
            list_permutations.append(permutation[:index] + first_letter + permutation[index:])
            
    return list_permutations

            


if __name__ == '__main__':
#    TEST CASES
   example_input_a = 'abc'
   print('Input:', example_input_a)
   print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
   print('Actual Output:', get_permutations(example_input_a))
   
   print('')

   example_input_b = 'xyz'
   print('Input:', example_input_b)
   print('Expected Output:', ['xyz', 'yxz', 'yzx', 'xzy', 'zxy', 'zyx'])
   print('Actual Output:', get_permutations(example_input_b))

   print('')

   example_input_c = 'fg'
   print('Input:', example_input_c)
   print('Expected Output:', ['fg', 'gf'])
   print('Actual Output:', get_permutations(example_input_c))



