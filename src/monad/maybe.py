from typing import Any, Callable



class Maybe:
    """Wrapper for an optional value.

    It provides a way to handle possible absence of a value by providing default
    behavior when accessed or invoked with missing values instead of raising errors.

    ### Attributes:
        _value (Any): The wrapped value, which could be None.

    """
    def __init__(self, value: Any):
        """Initialize a new Maybe instance.

        ### Args:
            value (Any): The value to wrap in the Maybe class.
        """
        self._value = value

    def unwrap(self) -> Any:
        """Unwrap and return the wrapped value if it exists, otherwise return None.

        ### Returns:
            Any: The wrapped value or None if no value is present.
        """
        return self._value

    def bind(self, func: Callable) -> "Maybe":
        """Applies a function to the value inside the Maybe object.

        ### Args:
            func (Callable): A function tto apply on the wrapped value

        ### Returns:
            Maybe: A new Maybe object that contains the result of applying the function to the value
        """
        if self._value is None:
            return Maybe(None)
        return Maybe(func(self._value))

    def orElse(self, value: Any) -> "Maybe":
        """Returns the current Maybe object or a new one with the given value.

        ### Args:
            value (Any): The value to use if the current value is None.

        ### Returns:
            Maybe: The current Maybe object if it has a value, or a new Maybe object with the given value otherwise.
        """
        if self._value is None:
            return Maybe(value)
        return self

    def __or__(self, other) -> "Maybe":
        return Maybe(self._value or other._value)

    def __str__(self) ->str:
        if self._value is None:
            return str(f'Maybe({None})')
        else:
            return str(f'Maybe({self._value})')

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other) -> bool:
        if isinstance(other, Maybe):
            return self._value == other._value
        else:
            return False

    def __ne__(self, other) -> bool:
        return not (self == other)

    def __bool__(self) -> bool:
        return self._value is not None