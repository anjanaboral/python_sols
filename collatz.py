def get_collatz_for_all_ints():
    """This method will compute the collatz sequence for all the numbers till 1 million."""
    largest_number = 1000000
    number_having_largest_chain = 1
    longest_sequence = 1
    for i in range(2, largest_number):
        length = collatz_longest_length(i)
        if length > longest_sequence:
            longest_sequence = length
            number_having_largest_chain = i
    print(f'Longest sequence is {longest_sequence} starting with {number_having_largest_chain}')


def collatz_longest_length(n: int):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        print(n, end=' ')
        length += 1
    return length


if __name__ == "__main__":
    starting_value = 837799
    length = collatz_longest_length(starting_value)
    print(f"\nLength of collatz sequence for {starting_value} is {length}")


