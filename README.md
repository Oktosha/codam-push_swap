# codam-push_swap

This repo contains code for a project at [Codam](https://www.codam.nl/) (School 42 in Amstredam).

## Task subject (briefly)

The goal of this project is to write an algo that produces steps to sort a sequence of numbers (numbers fit integer type and don't repeat). The given numbers are stored in a "stack" and you have another such "stack" at your disposal. The allowed operations are:

+ **sa** (swap a): Swap the first 2 elements at the top of stack a. Do nothing if there is only one or no elements.
+ **sb** (swap b): Swap the first 2 elements at the top of stack b. Do nothing if there is only one or no elements.
+ **ss** : sa and sb at the same time.
+ **pa** (push a): Take the first element at the top of b and put it at the top of a. Do nothing if b is empty.
+ **pb** (push b): Take the first element at the top of a and put it at the top of b. Do nothing if a is empty.
+ **ra** (rotate a): Shift up all elements of stack a by 1. The first element becomes the last one.
+ **rb** (rotate b): Shift up all elements of stack b by 1. The first element becomes the last one.
+ **rr** : ra and rb at the same time.
+ **rra** (reverse rotate a): Shift down all elements of stack a by 1. The last element becomes the first one.
+ **rrb** (reverse rotate b): Shift down all elements of stack b by 1. The last element becomes the first one.
+ **rrr** : rra and rrb at the same time.

The algo should be written in C. The created source should compile into a binary that takes the contents of the first stack (aka stack a) as a command line parameter (first number on top) and outputs the sorting steps, one step per line. The steps should result in all elements end up in stack a sorted  in ascending order. And you should strive to use as few steps as you can (more details on efficiency below).

## Example

The resulting binary will be called like this

```bash
ARG="2 1 3 6 5 8"; ./push_swap $ARG
```

It means that there are 6 numbers in stack a, number 2 is on top. Possible output is 

```
sa
pb
pb
pb
sa
pa
pa
pa
```

## Efficiency requirements

I got this part from [another student-generated tutorial](https://medium.com/nerd-for-tech/push-swap-tutorial-fa746e6aba1e), the efficiency requirements aren't stated on the grading system.

The passing solution should be properly optimized for small amounts of elements:

+ use no more than 3 operations for 3 elements
+ use no more than 12 operations for 5 elements

The passing solution should also be effective in sorting bigger amounts of elements. Here is the table on how much steps you are allowed to use for each number of points.

| number of elements | 5 points | 4 points | 3 points | 2 points | 1 point |
|--------------------|----------|----------|----------|----------|---------|
| 100                | 700      | 900      | 1100     | 1300     | 1500    |
| 500                | 5500     | 7000     | 8500     | 10000    | 11500   |

According to unreliable sources it is required to get at least 6 points to pass.

There is also a non-explicit requirement on the amount of the processing time the program can use to generate the steps, I assume it is around a second.

## Efficiency observations

These requirements really force you to apply a lot of non-asymptotic optimizations to reduce the amount of steps in your output.

These requirements don't empathize the value of being asymptotically good.

You can be reasonably inefficient generating steps as long as you don't generate that many steps.

## Efficiency experiments

Before writing the final algo in C, I'm implementing several approaches in python.

### merge sort

see `prototypes/merge.py`

### [TODO] quick sort

...

### [TODO] radix sort

see [this tutorial](https://medium.com/nerd-for-tech/push-swap-tutorial-fa746e6aba1e)

### [TODO] mechanical turk sort

see [this tutorial](https://medium.com/@ayogun/push-swap-c1f5d2d41e97)

### [TODO] lde-ross sort

see [this tutorial](https://medium.com/@lucafischer_11396/two-stacks-one-goal-understanding-the-push-swap-algorithm-e08e5986f657)


### [TODO] other student tutorials

...

### [TODO] comparison of the algos

probably should create a jupyter notebook with plots?

### [TODO] final approach for submission

probably some stuff

## [TODO] Reproducing results

Instructions to install python environment

## [TODO] Other resources

[todo] links to visualizations

