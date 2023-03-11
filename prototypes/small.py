from dataclasses import dataclass
from typing import Tuple, Iterable, Callable
from collections import deque
from functools import total_ordering

@total_ordering
@dataclass(frozen=True)
class State:
    '''
    a - state of stack a, a[0] is the top element
    b - state of stack b, b[0] is the top element
    '''
    a: Tuple[int]
    b: Tuple[int]
    def __lt__(self, other):
        return (self.a, self.b) < (other.a, other.b)

@dataclass(frozen=True)
class Transition:
    name: str
    apply: Callable[[State], State]
    reverse: Callable[[State], State]

def sa(state: State) -> State:
    """
    >>> sa(State(a=(0, 1, 2), b=(3, 4, 5)))
    State(a=(1, 0, 2), b=(3, 4, 5))
    """
    if len(state.a) < 2:
        return state
    return State(a=(state.a[1],) + (state.a[0],) + state.a[2:], b=state.b)

def sb(state: State) -> State:
    """
    >>> sb(State(a=(0, 1, 2), b=(3, 4, 5)))
    State(a=(0, 1, 2), b=(4, 3, 5))
    """
    if len(state.b) < 2:
        return state
    return State(a=state.a, b=(state.b[1],) + (state.b[0],) + state.b[2:])

def ss(state: State) -> State:
    """
    >>> ss(State(a=(0, 1, 2), b=(3, 4, 5)))
    State(a=(1, 0, 2), b=(4, 3, 5))
    """
    return sa(sb(state))

def pa(state: State) -> State:
    """
    >>> pa(State(a=(0, 1, 2), b=(3, 4, 5)))
    State(a=(3, 0, 1, 2), b=(4, 5))
    """
    if len(state.b) < 1:
        return state
    return State(a=(state.b[0],) + state.a, b=state.b[1:])

def pb(state: State) -> State:
    """
    >>> pb(State(a=(0, 1, 2), b=(3, 4, 5)))
    State(a=(1, 2), b=(0, 3, 4, 5))
    """
    if len(state.a) < 1:
        return state
    return State(a=state.a[1:], b=(state.a[0],) + state.b)

def ra(state: State) -> State:
    """
    >>> ra(State(a=(0, 1, 2), b=(3, 4, 5)))
    State(a=(1, 2, 0), b=(3, 4, 5))
    """
    if len(state.a) < 2:
        return state
    return State(a=state.a[1:] + (state.a[0],), b=state.b)

def rb(state: State) -> State:
    """
    >>> rb(State(a=(0, 1, 2), b=(3, 4, 5)))
    State(a=(0, 1, 2), b=(4, 5, 3))
    """
    if len(state.b) < 2:
        return state
    return State(a=state.a, b=state.b[1:] + (state.b[0],))

def rr(state: State) -> State:
    """
    >>> rr(State(a=(0, 1, 2), b=(3, 4, 5)))
    State(a=(1, 2, 0), b=(4, 5, 3))
    """
    return ra(rb(state))

def rra(state: State) -> State:
    """
    >>> rra(State(a=(0, 1, 2), b=(3, 4, 5)))
    State(a=(2, 0, 1), b=(3, 4, 5))
    """
    if len(state.a) < 2:
        return state
    return State(a=(state.a[-1],) + state.a[:-1], b=state.b)

def rrb(state: State) -> State:
    """
    >>> rrb(State(a=(0, 1, 2), b=(3, 4, 5)))
    State(a=(0, 1, 2), b=(5, 3, 4))
    """
    if len(state.b) < 2:
        return state
    return State(a=state.a, b=(state.b[-1],) + state.b[:-1])

def rrr(state: State) -> State:
    """
    >>> rrr(State(a=(0, 1, 2), b=(3, 4, 5)))
    State(a=(2, 0, 1), b=(5, 3, 4))
    """
    return rra(rrb(state))

def neigbours(state: State) -> Iterable[Tuple[State, str]]:
    '''
    returns a list of pairs containing:
    + neigbourting state
    + transition from this neigbouring state to the given state
    >>> print("\\n".join(map(str, sorted(neigbours(State(a=(1, 2, 3), b=(4, 5, 6)))))))
    (State(a=(1, 2, 3), b=(5, 4, 6)), 'sb')
    (State(a=(1, 2, 3), b=(5, 6, 4)), 'rrb')
    (State(a=(1, 2, 3), b=(6, 4, 5)), 'rb')
    (State(a=(2, 1, 3), b=(4, 5, 6)), 'sa')
    (State(a=(2, 1, 3), b=(5, 4, 6)), 'ss')
    (State(a=(2, 3), b=(1, 4, 5, 6)), 'pa')
    (State(a=(2, 3, 1), b=(4, 5, 6)), 'rra')
    (State(a=(2, 3, 1), b=(5, 6, 4)), 'rrr')
    (State(a=(3, 1, 2), b=(4, 5, 6)), 'ra')
    (State(a=(3, 1, 2), b=(6, 4, 5)), 'rr')
    (State(a=(4, 1, 2, 3), b=(5, 6)), 'pb')
    '''
    transitions = [
        Transition("sa", sa, sa),
        Transition("sb", sb, sb),
        Transition("ss", ss, ss),
        Transition("pa", pa, pb),
        Transition("pb", pb, pa),
        Transition("ra", ra, rra),
        Transition("rb", rb, rrb),
        Transition("rr", rr, rrr),
        Transition("rra", rra, ra),
        Transition("rrb", rrb, rb),
        Transition("rrr", rrr, rr)]
    return map(lambda transition: (transition.reverse(state), transition.name), transitions)

def solve(length: int) -> dict[State, list[str]]:
    sorted_state = State(a=tuple(list(range(length))), b=())
    paths_to_sorted_state = {sorted_state: []}
    queue = deque([sorted_state])
    while len(queue) > 0:
        current = queue.popleft()
        for state, transition in neigbours(current):
            if state not in paths_to_sorted_state:
                paths_to_sorted_state[state] = [transition] + paths_to_sorted_state[current]
                queue.append(state)
    return paths_to_sorted_state

if __name__ == "__main__":
    import doctest
    doctest.testmod()
