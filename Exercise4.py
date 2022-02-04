from numpy import copy
import matplotlib.pyplot as plt
from random import randint, random


# Randomly generate a bit sequence x
def generate_bits(bit_length):
    final_array = []
    for i in range(0, bit_length):
        final_array.append(randint(0, 1))
    return final_array


# Create a copy of x and invert each of its bits with probability invert_prob. Let xnew be the result.
def invert_bits(invert_prob, x):
    xnew = x.copy()
    for i in range(0, len(x)):
        if random() < invert_prob:
            if x[i] == 0:
                xnew[i] = 1
            else:
                xnew[i] = 0
    return xnew


# If xnew is closer to the goal sequence than x then replace x with xnew.
def determine_new_x(fitness_function, x, xnew):
    if fitness_function(xnew) > fitness_function(x):
        return xnew
    else:
        return x


# Makes a plot of one run
def make_plot_1_run(x_list, iterations):
    plt.plot(list(range(iterations+1)), x_list)
    plt.title("The best fitness for a (1+1)-GA against the 1500 iterations")
    plt.ylabel("fitness as sum of the bits")
    plt.xlabel("iteration")
    plt.savefig('exercise4a.png', bbox_inches='tight')
    plt.clf()


# With bit strings of length 100 and a mutation rate p = 1/100. For a run of 1500
# iterations, we plot the best fitness against the elapsed number of iterations.
def exercise_a(bit_length, iterations):
    invert_prob = 1/bit_length
    x = generate_bits(bit_length)
    f = lambda y: sum(y)
    x_list = [f(x)]
    for i in range(0, iterations):
        xnew = invert_bits(invert_prob, x)
        x = determine_new_x(f, x, xnew)
        x_list.append(f(x))
    make_plot_1_run(x_list, iterations)


# Makes a plot of ten runs
def make_plot_10_runs(runs_list, iterations, exercise_string):
    for j in runs_list:
        plt.plot(list(range(iterations+1)), j)
    plt.title("The best fitness for a (1+1)-GA against the 1500 iterations for 10 runs")
    plt.ylabel("fitness as sum of the bits")
    plt.xlabel("iteration")
    plt.savefig(exercise_string+'.png', bbox_inches='tight')
    plt.clf()


# Performs 10 runs and plots best fitness against elapsed number of iterations of each run in a single figure.
# In the console, we print how many times the algorithm finds the optimum
def exercise_b(bit_length, iterations):
    invert_prob = 1 / bit_length
    runs_list = []
    finds_optimum = 0
    for j in range(0, 10):
        x = generate_bits(bit_length)
        f = lambda y: sum(y)
        x_list = [f(x)]
        for i in range(0, iterations):
            xnew = invert_bits(invert_prob, x)
            x = determine_new_x(f, x, xnew)
            x_list.append(f(x))
        if x_list[-1] is 100:
            finds_optimum += 1
        runs_list.append(x_list)
    print("The number of runs that found the optimum for exercise b: " + str(finds_optimum))
    make_plot_10_runs(runs_list, iterations, 'exercise4b')


# Performs 10 runs and plots best fitness against elapsed number of iterations of each run in a single figure.
# Using an adapted version of step c (determine new x)
# In the console, we print how many times the algorithm finds the optimum
def exercise_c(bit_length, iterations):
    invert_prob = 1 / bit_length
    runs_list = []
    finds_optimum = 0
    for j in range(0, 10):
        x = generate_bits(bit_length)
        f = lambda y: sum(y)
        x_list = [f(x)]
        for i in range(0, iterations):
            xnew = invert_bits(invert_prob, x)
            x = xnew #NOTE: we do not use determine new x here but immediately return the new x
            x_list.append(f(x))
        if x_list[-1] is 100:
            finds_optimum += 1
        runs_list.append(x_list)
    print("The number of runs that found the optimum for exercise c: " + str(finds_optimum))
    make_plot_10_runs(runs_list, iterations, 'exercise4c')


if __name__ == '__main__':
    exercise_a(100, 1500)
    exercise_b(100, 1500)
    exercise_c(100, 1500)