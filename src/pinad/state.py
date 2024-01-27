from typing import Callable, Any, Collection, Self

class State:
  def __init__(self, state: tuple[Any, Collection[Any] | Any]):
    """Initialize the state object with a given state.

    ### Args:
      state (tuple): A pair of values representing the state.
    """
    self.state = state

  def __call__(self, value: Any) -> tuple[Collection[Any], "State"]:
    """Return a new state object with an updated state.

    ### Args:
        value (Any): The value to be added to the second element of the state.

    ### Returns:
        tuple: A pair of the new state object and the updated value.
    """
    return (self.state[1], State((self.state[0] + 1, value)))

  @staticmethod
  def unit(value: Any) -> "State":
    """Create a new state."""
    return State((0, value))

  def __rshift__(self, func: Callable[[Collection[Any] | Any], "State"]):
    """Apply a callable to the """
    result, new_state = self(self.state[1])
    return new_state(func(result))


if __name__ == "__main__":
    # create a stateful computation that counts the number of times it is called
    counter = State((0, 0))
    f = lambda x: x * 2
    counter >> f

    # call the computation multiple times and print the current count
    for i in range(5):

        result, counter = (counter >> f)
        print(f"Computation result: {result}, count: {counter.state[0]}")