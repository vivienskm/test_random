# test_random
Python script that tests various methods from the random module

## Random Module Functions and Methods

1. **random()**: Returns a random float in the range [0.0, 1.0).
    ```python
    random.random()
    ```

2. **seed(a=None, version=2)**: Initializes the random number generator. If `a` is omitted or `None`, the current system time is used.
    ```python
    random.seed(42)
    ```

3. **randrange([start,] stop[, step])**: Returns a randomly selected element from the specified range.
    ```python
    random.randrange(1, 10, 2)
    ```

4. **randint(a, b)**: Returns a random integer from the specified range [a, b].
    ```python
    random.randint(1, 100)
    ```

5. **uniform(a, b)**: Returns a random float in the range [a, b).
    ```python
    random.uniform(1.0, 10.0)
    ```

6. **choice(seq)**: Returns a randomly selected element from the non-empty sequence.
    ```python
    random.choice(['apple', 'banana', 'orange'])
    ```

7. **shuffle(x)**: Shuffles the elements of a sequence in place.
    ```python
    my_list = [1, 2, 3, 4, 5]
    random.shuffle(my_list)
    ```

8. **sample(population, k)**: Returns a k-length list of unique elements chosen from the population sequence.
    ```python
    random.sample(range(1, 10), 3)
    ```

9. **choices(population, weights=None, cum_weights=None, k=1)**: Returns a k-length list with elements chosen from the specified population. Weights can be provided to bias the selection.
    ```python
    random.choices(['cat', 'dog', 'fish'], weights=[1, 1, 2], k=2)
    ```

10. **gauss(mu, sigma)**: Returns a random float drawn from a normal (Gaussian) distribution with a specified mean (`mu`) and standard deviation (`sigma`).
    ```python
    random.gauss(0, 1)
    ```

11. **getrandbits(k)**: Returns an integer with k random bits.
    ```python
    random.getrandbits(4)
    ```

This is not an exhaustive list, but it covers some of the commonly used functions and methods in the `random` module.
