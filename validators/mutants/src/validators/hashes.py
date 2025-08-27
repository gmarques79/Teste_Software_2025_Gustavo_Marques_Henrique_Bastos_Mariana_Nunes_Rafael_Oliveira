"""Hashes."""

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
def md5(value: str, /):
    """Return whether or not given value is a valid MD5 hash.

    Examples:
        >>> md5('d41d8cd98f00b204e9800998ecf8427e')
        True
        >>> md5('900zz11')
        ValidationError(func=md5, args={'value': '900zz11'})

    Args:
        value:
            MD5 string to validate.

    Returns:
        (Literal[True]): If `value` is a valid MD5 hash.
        (ValidationError): If `value` is an invalid MD5 hash.
    """
    return re.match(r"^[0-9a-f]{32}$", value, re.IGNORECASE) if value else False


@validator
def sha1(value: str, /):
    """Return whether or not given value is a valid SHA1 hash.

    Examples:
        >>> sha1('da39a3ee5e6b4b0d3255bfef95601890afd80709')
        True
        >>> sha1('900zz11')
        ValidationError(func=sha1, args={'value': '900zz11'})

    Args:
        value:
            SHA1 string to validate.

    Returns:
        (Literal[True]): If `value` is a valid SHA1 hash.
        (ValidationError): If `value` is an invalid SHA1 hash.
    """
    return re.match(r"^[0-9a-f]{40}$", value, re.IGNORECASE) if value else False


@validator
def sha224(value: str, /):
    """Return whether or not given value is a valid SHA224 hash.

    Examples:
        >>> sha224('d14a028c2a3a2bc9476102bb288234c415a2b01f828ea62ac5b3e42f')
        True
        >>> sha224('900zz11')
        ValidationError(func=sha224, args={'value': '900zz11'})

    Args:
        value:
            SHA224 string to validate.

    Returns:
        (Literal[True]): If `value` is a valid SHA224 hash.
        (ValidationError): If `value` is an invalid SHA224 hash.
    """
    return re.match(r"^[0-9a-f]{56}$", value, re.IGNORECASE) if value else False


@validator
def sha256(value: str, /):
    """Return whether or not given value is a valid SHA256 hash.

    Examples:
        >>> sha256(
        ...     'e3b0c44298fc1c149afbf4c8996fb924'
        ...     '27ae41e4649b934ca495991b7852b855'
        ... )
        True
        >>> sha256('900zz11')
        ValidationError(func=sha256, args={'value': '900zz11'})

    Args:
        value:
            SHA256 string to validate.

    Returns:
        (Literal[True]): If `value` is a valid SHA256 hash.
        (ValidationError): If `value` is an invalid SHA256 hash.
    """
    return re.match(r"^[0-9a-f]{64}$", value, re.IGNORECASE) if value else False


@validator
def sha384(value: str, /):
    """Return whether or not given value is a valid SHA384 hash.

    Examples:
        >>> sha384(
        ...     'cb00753f45a35e8bb5a03d699ac65007272c32ab0eded163'
        ...     '1a8b605a43ff5bed8086072ba1e7cc2358baeca134c825a7'
        ... )
        True
        >>> sha384('900zz11')
        ValidationError(func=sha384, args={'value': '900zz11'})

    Args:
        value:
            SHA384 string to validate.

    Returns:
        (Literal[True]): If `value` is a valid SHA384 hash.
        (ValidationError): If `value` is an invalid SHA384 hash.
    """
    return re.match(r"^[0-9a-f]{96}$", value, re.IGNORECASE) if value else False


@validator
def sha512(value: str, /):
    """Return whether or not given value is a valid SHA512 hash.

    Examples:
        >>> sha512(
        ...     'cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce'
        ...     '9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af9'
        ...     '27da3e'
        ... )
        True
        >>> sha512('900zz11')
        ValidationError(func=sha512, args={'value': '900zz11'})

    Args:
        value:
            SHA512 string to validate.

    Returns:
        (Literal[True]): If `value` is a valid SHA512 hash.
        (ValidationError): If `value` is an invalid SHA512 hash.
    """
    return re.match(r"^[0-9a-f]{128}$", value, re.IGNORECASE) if value else False
