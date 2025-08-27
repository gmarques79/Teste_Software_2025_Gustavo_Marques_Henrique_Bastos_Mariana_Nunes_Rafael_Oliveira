"""Slug."""

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


@validator
def slug(value: str, /):
    """Validate whether or not given value is valid slug.

    Valid slug can contain only lowercase alphanumeric characters and hyphens.
    It starts and ends with these lowercase alphanumeric characters.

    Examples:
        >>> slug('my-slug-2134')
        True
        >>> slug('my.slug')
        ValidationError(func=slug, args={'value': 'my.slug'})

    Args:
        value: Slug string to validate.

    Returns:
        (Literal[True]): If `value` is a valid slug.
        (ValidationError): If `value` is an invalid slug.
    """
    return re.match(r"^[a-z0-9]+(?:-[a-z0-9]+)*$", value) if value else False
