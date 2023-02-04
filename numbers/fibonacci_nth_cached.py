"""
    Program to generate requested fibonacci number.
    Program uses Memoization to determine even higher fibonacci numbers.
    For higher fibo numbers, take adv of memoization instead of searching them directly
    Ex: Finding 1000th fibo number directly will cause recursion depth problem
    but searching for 300, 500, 750 then 1000 will give you needed result
"""

def cached_execuation(cache, proc, proc_input):
    """
        Method to cache execution and make program execute faster
    """

    if proc_input not in cache:
        cache[proc_input] = proc(proc_input)

    return cache[proc_input]

def cached_fibo(nth_fibo):

    assert nth_fibo > -1

    if nth_fibo == 0 or nth_fibo == 1:
        return nth_fibo
    else:
        return cached_execuation(cache, cached_fibo, nth_fibo-1) + \
                cached_execuation(cache, cached_fibo, nth_fibo-2)


def main():
    """
        Wrapper function
    """

    while True:

        while True:

            try:
                user_input = int(input('Please enter which nth fibonacci number you want : '))
            except ValueError:
                print("That's not a valid number. Please enter a number")
            else:
                print('That is a valid input')
                break

        print(cached_fibo(user_input))

if __name__ == '__main__':
    cache = {}  # initial cache to store computed fibo numbers.
    main()