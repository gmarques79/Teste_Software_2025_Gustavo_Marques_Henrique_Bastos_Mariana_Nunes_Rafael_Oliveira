"""India."""

# standard
import re

# local
from validators.utils import validator
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
def ind_aadhar(value: str):
    """Validate an indian aadhar card number.

    Examples:
        >>> ind_aadhar('3675 9834 6015')
        True
        >>> ind_aadhar('3675 ABVC 2133')
        ValidationError(func=ind_aadhar, args={'value': '3675 ABVC 2133'})

    Args:
        value: Aadhar card number string to validate.

    Returns:
        (Literal[True]): If `value` is a valid aadhar card number.
        (ValidationError): If `value` is an invalid aadhar card number.
    """
    return re.match(r"^[2-9]{1}\d{3}\s\d{4}\s\d{4}$", value)


@validator
def ind_pan(value: str):
    """Validate a pan card number.

    Examples:
        >>> ind_pan('ABCDE9999K')
        True
        >>> ind_pan('ABC5d7896B')
        ValidationError(func=ind_pan, args={'value': 'ABC5d7896B'})

    Args:
        value: PAN card number string to validate.

    Returns:
        (Literal[True]): If `value` is a valid PAN card number.
        (ValidationError): If `value` is an invalid PAN card number.
    """
    return re.match(r"[A-Z]{5}\d{4}[A-Z]{1}", value)
