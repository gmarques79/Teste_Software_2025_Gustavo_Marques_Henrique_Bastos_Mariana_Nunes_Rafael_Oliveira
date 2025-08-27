"""URI."""

# Read: https://stackoverflow.com/questions/176264
# https://www.rfc-editor.org/rfc/rfc3986#section-3

# local
from .email import email
from .url import url
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


def x__file_url__mutmut_orig(value: str):
    if not value.startswith("file:///"):
        return False
    return True


def x__file_url__mutmut_1(value: str):
    if value.startswith("file:///"):
        return False
    return True


def x__file_url__mutmut_2(value: str):
    if not value.startswith(None):
        return False
    return True


def x__file_url__mutmut_3(value: str):
    if not value.startswith("XXfile:///XX"):
        return False
    return True


def x__file_url__mutmut_4(value: str):
    if not value.startswith("FILE:///"):
        return False
    return True


def x__file_url__mutmut_5(value: str):
    if not value.startswith("file:///"):
        return True
    return True


def x__file_url__mutmut_6(value: str):
    if not value.startswith("file:///"):
        return False
    return False

x__file_url__mutmut_mutants : ClassVar[MutantDict] = {
'x__file_url__mutmut_1': x__file_url__mutmut_1, 
    'x__file_url__mutmut_2': x__file_url__mutmut_2, 
    'x__file_url__mutmut_3': x__file_url__mutmut_3, 
    'x__file_url__mutmut_4': x__file_url__mutmut_4, 
    'x__file_url__mutmut_5': x__file_url__mutmut_5, 
    'x__file_url__mutmut_6': x__file_url__mutmut_6
}

def _file_url(*args, **kwargs):
    result = _mutmut_trampoline(x__file_url__mutmut_orig, x__file_url__mutmut_mutants, args, kwargs)
    return result 

_file_url.__signature__ = _mutmut_signature(x__file_url__mutmut_orig)
x__file_url__mutmut_orig.__name__ = 'x__file_url'


def x__ipfs_url__mutmut_orig(value: str):
    if not value.startswith("ipfs://"):
        return False
    return True


def x__ipfs_url__mutmut_1(value: str):
    if value.startswith("ipfs://"):
        return False
    return True


def x__ipfs_url__mutmut_2(value: str):
    if not value.startswith(None):
        return False
    return True


def x__ipfs_url__mutmut_3(value: str):
    if not value.startswith("XXipfs://XX"):
        return False
    return True


def x__ipfs_url__mutmut_4(value: str):
    if not value.startswith("IPFS://"):
        return False
    return True


def x__ipfs_url__mutmut_5(value: str):
    if not value.startswith("ipfs://"):
        return True
    return True


def x__ipfs_url__mutmut_6(value: str):
    if not value.startswith("ipfs://"):
        return False
    return False

x__ipfs_url__mutmut_mutants : ClassVar[MutantDict] = {
'x__ipfs_url__mutmut_1': x__ipfs_url__mutmut_1, 
    'x__ipfs_url__mutmut_2': x__ipfs_url__mutmut_2, 
    'x__ipfs_url__mutmut_3': x__ipfs_url__mutmut_3, 
    'x__ipfs_url__mutmut_4': x__ipfs_url__mutmut_4, 
    'x__ipfs_url__mutmut_5': x__ipfs_url__mutmut_5, 
    'x__ipfs_url__mutmut_6': x__ipfs_url__mutmut_6
}

def _ipfs_url(*args, **kwargs):
    result = _mutmut_trampoline(x__ipfs_url__mutmut_orig, x__ipfs_url__mutmut_mutants, args, kwargs)
    return result 

_ipfs_url.__signature__ = _mutmut_signature(x__ipfs_url__mutmut_orig)
x__ipfs_url__mutmut_orig.__name__ = 'x__ipfs_url'


@validator
def uri(value: str, /):
    """Return whether or not given value is a valid URI.

    Examples:
        >>> uri('mailto:example@domain.com')
        True
        >>> uri('file:path.txt')
        ValidationError(func=uri, args={'value': 'file:path.txt'})

    Args:
        value:
            URI to validate.

    Returns:
        (Literal[True]): If `value` is a valid URI.
        (ValidationError): If `value` is an invalid URI.
    """
    if not value:
        return False

    # TODO: work on various validations

    # url
    if any(
        # fmt: off
        value.startswith(item)
        for item in {
            "ftp",
            "ftps",
            "git",
            "http",
            "https",
            "irc",
            "rtmp",
            "rtmps",
            "rtsp",
            "sftp",
            "ssh",
            "telnet",
        }
        # fmt: on
    ):
        return url(value)

    # email
    if value.startswith("mailto:"):
        return email(value[len("mailto:") :])

    # file
    if value.startswith("file:"):
        return _file_url(value)

    # ipfs
    if value.startswith("ipfs:"):
        return _ipfs_url(value)

    # magnet
    if value.startswith("magnet:?"):
        return True

    # telephone
    if value.startswith("tel:"):
        return True

    # data
    if value.startswith("data:"):
        return True

    # urn
    if value.startswith("urn:"):
        return True

    # urc
    if value.startswith("urc:"):
        return True

    return False
