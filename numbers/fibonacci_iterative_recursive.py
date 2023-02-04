"""
    This program generates the requested fibonacci number.
    Note that this program will run for long if the requested fib number is quite high.
    Ex: 300th Fibonacci number
    This program does not utilize any memory optimization techniques and serves to demonstrate memoization in tandem with the other program
"""
import timeit
import time

def fibo_rec(n):
    assert n > -1

    if n == 0 or n == 1:
        return n
    else:
        return fibo_rec(n-1) + fibo_rec(n-2)

def fibo_it(n):

    a, b = 0, 1

    for i in range(n-1):
        a, b = b, a+b

    if n == 0:
        return 0
    else:
        return b

def main():

    while True:
        try:
            input_val = int(input("which fibonacci number is desired ? "))
        except ValueError:
            print("It isn't a valid input, please enter a number")
        else:
            print("Input is in the correct format")
            break

    start_time = time.time()
    rec_result = fibo_rec(input_val)
    rec_time   = time.time() - start_time
    #rec_time = timeit.timeit("fibo_rec(3)", globals=globals())
    print(f"The result for the recursive is = {rec_result} and it took {rec_time} s")

    start_time = time.time()
    it_result = fibo_it(input_val)
    it_time = time.time() - start_time
    #it_time = timeit.timeit("fibo_it(3)", globals=globals() )
    print(f"The result for the iterative is = {it_result} and it took {it_time} s ")

if __name__ == '__main__':
    main()
# 0 1 1 2 3