import random

# Seed the random number generator for reproducibility
random.seed(42)

# Method 1: random()
random_number = random.random()
print(f"Method 1 - random(): {random_number}")

# Method 2: randint(a, b)
random_integer = random.randint(1, 100)
print(f"Method 2 - randint(1, 100): {random_integer}")

# Method 3: uniform(a, b)
random_float = random.uniform(1.0, 10.0)
print(f"Method 3 - uniform(1.0, 10.0): {random_float}")

# Method 4: choice(seq)
random_choice = random.choice(['apple', 'banana', 'orange'])
print(f"Method 4 - choice(['apple', 'banana', 'orange']): {random_choice}")

# Method 5: shuffle(x)
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(f"Method 5 - shuffle([1, 2, 3, 4, 5]): {my_list}")

# Method 6: sample(population, k)
random_sample = random.sample(range(1, 10), 3)
print(f"Method 6 - sample(range(1, 10), 3): {random_sample}")

# Method 7: randrange(stop)
random_range = random.randrange(10)
print(f"Method 7 - randrange(10): {random_range}")

# Method 8: randrange(start, stop, step)
random_range_step = random.randrange(1, 10, 2)
print(f"Method 8 - randrange(1, 10, 2): {random_range_step}")

# Method 9: choices(population, weights=None, cum_weights=None, k=1)
random_choices = random.choices(['cat', 'dog', 'fish'], weights=[1, 1, 2], k=2)
print(f"Method 9 - choices(['cat', 'dog', 'fish'], weights=[1, 1, 2], k=2): {random_choices}")
