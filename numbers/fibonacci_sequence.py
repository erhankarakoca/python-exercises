# Fibonacci Sequence Generator
# Take a input for the size of the fibonacci sequence from user
# and compute the corresponding fibonacci sequence with that size
# you can also print the sequence

def fibSequence(seq_len):
    """
    Generates a fibonacci sequence
    with the size of seq_len

    The size should be larger than 0
    """
    assert seq_len > 0

    sequence = [0]

    while len(sequence) < seq_len:
        if len(sequence) == 1:
            sequence.append(1)
        else:
            sequence.append(sequence[-1] + sequence[-2])

    # The sequence can be converted to the str

    sequence_str = [str(elements) for elements in sequence]

    return (', '.join(sequence_str))


def main():
    """
    Wrapper function
    """
    while True:

        try:
            user_input = int(input('Please enter length of the fibonacci sequence : '))
        except ValueError:
            print("That's not a valid number. Please enter a number")
        else:
            print('That is a valid input')
            break
        # finally:
        #     print("I'm executed anyway!")

    print(fibSequence(user_input))


if __name__ == '__main__':
    main()
