"""Russia."""

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
def ru_inn(value: str):
    """Validate a Russian INN (Taxpayer Identification Number).

    The INN can be either 10 digits (for companies) or 12 digits (for individuals).
    The function checks both the length and the control digits according to Russian tax rules.

    Examples:
        >>> ru_inn('500100732259')  # Valid 12-digit INN
        True
        >>> ru_inn('7830002293')    # Valid 10-digit INN
        True
        >>> ru_inn('1234567890')    # Invalid INN
        ValidationError(func=ru_inn, args={'value': '1234567890'})

    Args:
        value: Russian INN string to validate. Can contain only digits.

    Returns:
        (Literal[True]): If `value` is a valid Russian INN.
        (ValidationError): If `value` is an invalid Russian INN.

    Note:
        The validation follows the official algorithm:
        - For 10-digit INN: checks 10th control digit
        - For 12-digit INN: checks both 11th and 12th control digits
    """
    if not value:
        return False

    try:
        digits = list(map(int, value))
        # company
        if len(digits) == 10:
            weight_coefs = [2, 4, 10, 3, 5, 9, 4, 6, 8, 0]
            control_number = sum([d * w for d, w in zip(digits, weight_coefs)]) % 11
            return (
                (control_number % 10) == digits[-1]
                if control_number > 9
                else control_number == digits[-1]
            )
        # person
        elif len(digits) == 12:
            weight_coefs1 = [7, 2, 4, 10, 3, 5, 9, 4, 6, 8, 0, 0]
            control_number1 = sum([d * w for d, w in zip(digits, weight_coefs1)]) % 11
            weight_coefs2 = [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8, 0]
            control_number2 = sum([d * w for d, w in zip(digits, weight_coefs2)]) % 11
            return (
                (control_number1 % 10) == digits[-2]
                if control_number1 > 9
                else control_number1 == digits[-2] and (control_number2 % 10) == digits[-1]
                if control_number2 > 9
                else control_number2 == digits[-1]
            )
        else:
            return False
    except ValueError:
        return False
