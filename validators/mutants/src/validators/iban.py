"""IBAN."""

# standard
import re

# local
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


def x__char_value__mutmut_orig(char: str):
    """A=10, B=11, ..., Z=35."""
    return char if char.isdigit() else str(10 + ord(char) - ord("A"))


def x__char_value__mutmut_1(char: str):
    """A=10, B=11, ..., Z=35."""
    return char if char.isdigit() else str(None)


def x__char_value__mutmut_2(char: str):
    """A=10, B=11, ..., Z=35."""
    return char if char.isdigit() else str(10 + ord(char) + ord("A"))


def x__char_value__mutmut_3(char: str):
    """A=10, B=11, ..., Z=35."""
    return char if char.isdigit() else str(10 - ord(char) - ord("A"))


def x__char_value__mutmut_4(char: str):
    """A=10, B=11, ..., Z=35."""
    return char if char.isdigit() else str(11 + ord(char) - ord("A"))


def x__char_value__mutmut_5(char: str):
    """A=10, B=11, ..., Z=35."""
    return char if char.isdigit() else str(10 + ord(None) - ord("A"))


def x__char_value__mutmut_6(char: str):
    """A=10, B=11, ..., Z=35."""
    return char if char.isdigit() else str(10 + ord(char) - ord(None))


def x__char_value__mutmut_7(char: str):
    """A=10, B=11, ..., Z=35."""
    return char if char.isdigit() else str(10 + ord(char) - ord("XXAXX"))


def x__char_value__mutmut_8(char: str):
    """A=10, B=11, ..., Z=35."""
    return char if char.isdigit() else str(10 + ord(char) - ord("a"))

x__char_value__mutmut_mutants : ClassVar[MutantDict] = {
'x__char_value__mutmut_1': x__char_value__mutmut_1, 
    'x__char_value__mutmut_2': x__char_value__mutmut_2, 
    'x__char_value__mutmut_3': x__char_value__mutmut_3, 
    'x__char_value__mutmut_4': x__char_value__mutmut_4, 
    'x__char_value__mutmut_5': x__char_value__mutmut_5, 
    'x__char_value__mutmut_6': x__char_value__mutmut_6, 
    'x__char_value__mutmut_7': x__char_value__mutmut_7, 
    'x__char_value__mutmut_8': x__char_value__mutmut_8
}

def _char_value(*args, **kwargs):
    result = _mutmut_trampoline(x__char_value__mutmut_orig, x__char_value__mutmut_mutants, args, kwargs)
    return result 

_char_value.__signature__ = _mutmut_signature(x__char_value__mutmut_orig)
x__char_value__mutmut_orig.__name__ = 'x__char_value'


def x__mod_check__mutmut_orig(value: str):
    """Check if the value string passes the mod97-test."""
    # move country code and check numbers to end
    rearranged = value[4:] + value[:4]
    return int("".join(_char_value(char) for char in rearranged)) % 97 == 1


def x__mod_check__mutmut_1(value: str):
    """Check if the value string passes the mod97-test."""
    # move country code and check numbers to end
    rearranged = None
    return int("".join(_char_value(char) for char in rearranged)) % 97 == 1


def x__mod_check__mutmut_2(value: str):
    """Check if the value string passes the mod97-test."""
    # move country code and check numbers to end
    rearranged = value[4:] - value[:4]
    return int("".join(_char_value(char) for char in rearranged)) % 97 == 1


def x__mod_check__mutmut_3(value: str):
    """Check if the value string passes the mod97-test."""
    # move country code and check numbers to end
    rearranged = value[5:] + value[:4]
    return int("".join(_char_value(char) for char in rearranged)) % 97 == 1


def x__mod_check__mutmut_4(value: str):
    """Check if the value string passes the mod97-test."""
    # move country code and check numbers to end
    rearranged = value[4:] + value[:5]
    return int("".join(_char_value(char) for char in rearranged)) % 97 == 1


def x__mod_check__mutmut_5(value: str):
    """Check if the value string passes the mod97-test."""
    # move country code and check numbers to end
    rearranged = value[4:] + value[:4]
    return int("".join(_char_value(char) for char in rearranged)) / 97 == 1


def x__mod_check__mutmut_6(value: str):
    """Check if the value string passes the mod97-test."""
    # move country code and check numbers to end
    rearranged = value[4:] + value[:4]
    return int(None) % 97 == 1


def x__mod_check__mutmut_7(value: str):
    """Check if the value string passes the mod97-test."""
    # move country code and check numbers to end
    rearranged = value[4:] + value[:4]
    return int("".join(None)) % 97 == 1


def x__mod_check__mutmut_8(value: str):
    """Check if the value string passes the mod97-test."""
    # move country code and check numbers to end
    rearranged = value[4:] + value[:4]
    return int("XXXX".join(_char_value(char) for char in rearranged)) % 97 == 1


def x__mod_check__mutmut_9(value: str):
    """Check if the value string passes the mod97-test."""
    # move country code and check numbers to end
    rearranged = value[4:] + value[:4]
    return int("".join(_char_value(None) for char in rearranged)) % 97 == 1


def x__mod_check__mutmut_10(value: str):
    """Check if the value string passes the mod97-test."""
    # move country code and check numbers to end
    rearranged = value[4:] + value[:4]
    return int("".join(_char_value(char) for char in rearranged)) % 98 == 1


def x__mod_check__mutmut_11(value: str):
    """Check if the value string passes the mod97-test."""
    # move country code and check numbers to end
    rearranged = value[4:] + value[:4]
    return int("".join(_char_value(char) for char in rearranged)) % 97 != 1


def x__mod_check__mutmut_12(value: str):
    """Check if the value string passes the mod97-test."""
    # move country code and check numbers to end
    rearranged = value[4:] + value[:4]
    return int("".join(_char_value(char) for char in rearranged)) % 97 == 2

x__mod_check__mutmut_mutants : ClassVar[MutantDict] = {
'x__mod_check__mutmut_1': x__mod_check__mutmut_1, 
    'x__mod_check__mutmut_2': x__mod_check__mutmut_2, 
    'x__mod_check__mutmut_3': x__mod_check__mutmut_3, 
    'x__mod_check__mutmut_4': x__mod_check__mutmut_4, 
    'x__mod_check__mutmut_5': x__mod_check__mutmut_5, 
    'x__mod_check__mutmut_6': x__mod_check__mutmut_6, 
    'x__mod_check__mutmut_7': x__mod_check__mutmut_7, 
    'x__mod_check__mutmut_8': x__mod_check__mutmut_8, 
    'x__mod_check__mutmut_9': x__mod_check__mutmut_9, 
    'x__mod_check__mutmut_10': x__mod_check__mutmut_10, 
    'x__mod_check__mutmut_11': x__mod_check__mutmut_11, 
    'x__mod_check__mutmut_12': x__mod_check__mutmut_12
}

def _mod_check(*args, **kwargs):
    result = _mutmut_trampoline(x__mod_check__mutmut_orig, x__mod_check__mutmut_mutants, args, kwargs)
    return result 

_mod_check.__signature__ = _mutmut_signature(x__mod_check__mutmut_orig)
x__mod_check__mutmut_orig.__name__ = 'x__mod_check'


@validator
def iban(value: str, /):
    """Return whether or not given value is a valid IBAN code.

    Examples:
        >>> iban('DE29100500001061045672')
        True
        >>> iban('123456')
        ValidationError(func=iban, args={'value': '123456'})

    Args:
        value:
            IBAN string to validate.

    Returns:
        (Literal[True]): If `value` is a valid IBAN code.
        (ValidationError): If `value` is an invalid IBAN code.
    """
    return (
        (re.match(r"^[a-z]{2}[0-9]{2}[a-z0-9]{11,30}$", value, re.IGNORECASE) and _mod_check(value))
        if value
        else False
    )
