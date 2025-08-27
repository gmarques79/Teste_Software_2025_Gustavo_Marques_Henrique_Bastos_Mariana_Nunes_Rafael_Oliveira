"""BSC Address."""

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
def bsc_address(value: str, /):
    """Return whether or not given value is a valid binance smart chain address.

    Full validation is implemented for BSC addresses.

    Examples:
        >>> bsc_address('0x4e5acf9684652BEa56F2f01b7101a225Ee33d23f')
        True
        >>> bsc_address('0x4g5acf9684652BEa56F2f01b7101a225Eh33d23z')
        ValidationError(func=bsc_address, args={'value': '0x4g5acf9684652BEa56F2f01b7101a225Eh33d23z'})

    Args:
        value:
            BSC address string to validate.

    Returns:
        (Literal[True]): If `value` is a valid bsc address.
        (ValidationError): If `value` is an invalid bsc address.
    """  # noqa: E501
    if not value:
        return False

    if not re.fullmatch(r"0x[a-fA-F0-9]{40}", value):
        return False

    return True
