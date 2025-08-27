"""Length."""

# standard
from typing import Union

# local
from .between import between
from .utils import validator
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result


@validator
def length(value: str, /, *, min_val: Union[int, None] = None, max_val: Union[int, None] = None):
    """Return whether or not the length of given string is within a specified range.

    Examples:
        >>> length('something', min_val=2)
        True
        >>> length('something', min_val=9, max_val=9)
        True
        >>> length('something', max_val=5)
        ValidationError(func=length, args={'value': 'something', 'max_val': 5})

    Args:
        value:
            The string to validate.
        min_val:
            The minimum required length of the string. If not provided,
            minimum length will not be checked.
        max_val:
            The maximum length of the string. If not provided,
            maximum length will not be checked.

    Returns:
        (Literal[True]): If `len(value)` is in between the given conditions.
        (ValidationError): If `len(value)` is not in between the given conditions.

    Raises:
        (ValueError): If either `min_val` or `max_val` is negative.
    """
    if min_val is not None and min_val < 0:
        raise ValueError("Length cannot be negative. `min_val` is less than zero.")
    if max_val is not None and max_val < 0:
        raise ValueError("Length cannot be negative. `max_val` is less than zero.")

    return bool(between(len(value), min_val=min_val, max_val=max_val))
