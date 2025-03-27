from typing import Callable, Type, Set
import warnings

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
        policy (dict): Optimal policy mapping sates to actions
        V (dict): Optimal state-value function
    """

    if not (0 < gamma < 1):  # Validate gamma
        raise ValueError(f"Value {gamma} is out of range (0, 1)")

    V = {s: 0 for s in S}  # Initialize value function
    policy = {s: None for s in S}  # Initialize policy
    iteration_count = 1

    while True:
        delta = 0  # Track the maximum change in value function
        new_V = V.copy()
        
        for s in S:
            action_values = []
            for a in A:
                value = R(s, a) + gamma * sum(P(s_prime, s, a) * V[s_prime] for s_prime in S)
                action_values.append(value)
            
            best_value = max(action_values)
            new_V[s] = best_value
            delta = max(delta, abs(V[s] - new_V[s]))
        
        V = new_V
        iteration_count += 1
        
        if delta < tol or iteration_count >= iter_max:
            if iteration_count >= iter_max:
                warnings.warn(f"Maximum number of iterations ({iter_max}) reached!", RuntimeWarning)
            break  # Stop if values converge
    
    # Extract the optimal policy
    for s in S:
        best_action = max(A, key=lambda a: R(s, a) + gamma * sum(P(s_prime, s, a) * V[s_prime] for s_prime in S))
        policy[s] = best_action
    
    return policy, V