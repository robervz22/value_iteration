# `value_iteration`

An implementation of the **Value Iteration Algorithm** for obtaining the optimal policy of a Markov Decision Process.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Installation

To install the package run in a command line:
```bash
python -m pip install 'git+https://github.com/robervz22/value_iteration'
```

## Usage

Use the module in your Python script:

```python
import value_iteration
```

The package contains only one function called `value_iteration` that implements the **Value Iteration Algorithm** using the pseudo-code in Figure 9.16 of [Artificial Intelligence: Foundations and Computational Agents 2nd edition](https://artint.info/2e/html2e/ArtInt2e.Ch9.S5.SS2.html).

The structure of the function is the following: 
```python
def value_iteration(S: Set[Type], A: Set[Type], P: Callable[[Type, Type, Type], float],
                    R: Callable[[Type, Type], float], gamma=0.9, tol=1e-6, iter_max=1000):
    """Value Iteration algorithm

    Args:
        S (Set[Type]): set of states
        A (Set[Type]): set of actions
        P (Callable[[Type, Type, Type], float]): transition probability function
        R (Callable[[Type, Type], float]): reward function
        gamma (float, optional): discount factor. Defaults to 0.9.
        tol (float, optional): small threshold for stopping condition. Defaults to 1e-6.
        iter_max (int, optional): maximum number of iterations. Defaults to 1000.

    Raises:
        ValueError: Error in the domain of discount factor

    Returns:
        policy (dict): Optimal policy mapping states to actions
        V (dict): Optimal state-value function
    """
```

The function raises a warning if the maximum number of iterations is reached, otherwise, the algorithm converges. 

Thus, to use the function for obtaining the optimal policy of a Markov Decision Process is necessary to provide as arguments:
- The $S$ state space, and the $A$ action space, as `set` structures.
- The expected reward function $R(s,a)$
- The transition probability function $P(s'\mid s,a)$ of moving to state $s'$ given that the agent is in state $s$ and does action $a$. 

The function returns:
- The optimal policy for the corresponding state
- The optimal value function for the corresponding state.

## Example

Here, we exemplify how to use the `value_iteration` function in the package `value_iteration`. 

We use the Example 9.27 of [Artificial Intelligence: Foundations and Computational Agents 2nd edition](https://artint.info/2e/html2e/ArtInt2e.Ch9.S5.html#Ch9.Thmciexamplered27).

In this problem, we the state space is $S=\{"healthy", "sick"\}$ and action space is $A=\{"relax","party"\}$

The transition probability functions and the expected reward function are defined as:
| $s$ | $a$ | $P(s'=healthy\mid s,a)$ |$R(s,a)$|
|-----------|-------------|-------------|-------------|
| $healthy$  |$relax$|0.95| 7| 
| $healthy$  |$party$ |0.7| 10|
| $sick$  | $relax$|0.5| 0|
| $sick$  | $party$|0.1| 2|

We code these functions and pass them as arguments to the `value_iteration` function, then, we obtain the optimal policy and the corresponding optimal value function for this example.
```python
# Import the required module
from value_iteration import value_iteration

# Define expected reward function
def R(s, a):
    """Expected reward function on state s with action a

    Args:
        s (Type): Agent current state 
        a (Type): Agent action in state s 

    Returns:
        _type_: _description_
    """
    if s == "healthy":
        return 7 if a == "relax" else 10 
    if s == "sick":
        return 0 if a == "relax" else 2

# Define transition probability function
def P(s_prime, s, a):
    """Transition probability function

    Args:
        s_prime (Type): Agent next state
        s (Type): Agent current state
        a (Type): Agent action in state s

    Returns:
        float: Probability of the transition
    """
    if s_prime == "healthy":
        if s == "healthy":
            return 0.95 if a == "relax" else 0.7
        elif s == "sick":
            return 0.5 if a == "relax" else 0.1
    if s_prime == "sick":
        if s == "healthy":
            return 0.05 if a == "relax" else 0.3
        elif s == "sick":
            return 0.5 if a == "relax" else 0.9 

# State space
S = {"healthy","sick"}  

# Action space
A = {"relax","party"} 

# Run the value iteration algorithm
policy, V = value_iteration(S, A, P, R, gamma=0.8)
print("Optimal Policy:")
print(policy)
print("\nOptimal Value Function:")
for state, value in V.items():
    print(f"{state}: {value:.2f}")
```
**Output:**

```plaintext
Optimal Policy:
{'healthy': 'party', 'sick': 'relax'}

Optimal Value Function:
healthy: 35.71
sick: 23.81
```
This results agrees with the solution presented in the Example 9.31 of [Artificial Intelligence: Foundations and Computational Agents 2nd edition](https://artint.info/2e/html2e/ArtInt2e.Ch9.S5.SS2.html) 

Therefore, the optimal policy is to party when healthy and relax when sick. 

<!-- ### Example 2: Using a Function

```python
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

# Example usage
result = add(3, 5)
print(f"The result is: {result}")
``` -->

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add a new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

