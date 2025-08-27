"""UUID."""

# standard
import re
from typing import Union
from uuid import UUID

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
def uuid(value: Union[str, UUID], /):
    """Return whether or not given value is a valid UUID-v4 string.

    This validator is based on [WTForms UUID validator][1].

    [1]: https://github.com/wtforms/wtforms/blob/master/src/wtforms/validators.py#L539

    Examples:
        >>> uuid('2bc1c94f-0deb-43e9-92a1-4775189ec9f8')
        True
        >>> uuid('2bc1c94f 0deb-43e9-92a1-4775189ec9f8')
        ValidationError(func=uuid, args={'value': '2bc1c94f 0deb-43e9-92a1-4775189ec9f8'})

    Args:
        value:
            UUID string or object to validate.

    Returns:
        (Literal[True]): If `value` is a valid UUID.
        (ValidationError): If `value` is an invalid UUID.
    """
    if not value:
        return False
    if isinstance(value, UUID):
        return True
    try:
        return UUID(value) or re.match(
            r"^[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}$", value
        )
    except ValueError:
        return False
