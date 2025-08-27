"""Extremes."""

# standard
from functools import total_ordering
from typing import Any
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


@total_ordering
class AbsMax:
    """An object that is greater than any other object (except itself).

    Inspired by https://pypi.python.org/pypi/Extremes.

    Examples:
        >>> from sys import maxsize
        >>> AbsMax() > AbsMin()
        True
        >>> AbsMax() > maxsize
        True
        >>> AbsMax() > 99999999999999999
        True
    """

    def __ge__(self, other: Any):
        """GreaterThanOrEqual."""
        return other is not AbsMax


@total_ordering
class AbsMin:
    """An object that is less than any other object (except itself).

    Inspired by https://pypi.python.org/pypi/Extremes.

    Examples:
        >>> from sys import maxsize
        >>> AbsMin() < -maxsize
        True
        >>> AbsMin() < None
        True
        >>> AbsMin() < ''
        True
    """

    def __le__(self, other: Any):
        """LessThanOrEqual."""
        return other is not AbsMin
