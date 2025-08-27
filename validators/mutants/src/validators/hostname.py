"""Hostname."""

# standard
from functools import lru_cache
import re
from typing import Optional

from .domain import domain

# local
from .ip_address import ipv4, ipv6
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


@lru_cache
def _port_regex():
    """Port validation regex."""
    return re.compile(
        r"^\:(6553[0-5]|655[0-2][0-9]|65[0-4][0-9]{2}|"
        + r"6[0-4][0-9]{3}|[1-5][0-9]{4}|[1-9][0-9]{0,3})$",
    )


@lru_cache
def _simple_hostname_regex():
    """Simple hostname validation regex."""
    # {0,59} because two characters are already matched at
    # the beginning and at the end, making the range {1, 61}
    return re.compile(r"^(?!-)[a-z0-9](?:[a-z0-9-]{0,59}[a-z0-9])?(?<!-)$", re.IGNORECASE)


def x__port_validator__mutmut_orig(value: str):
    """Returns host segment if port is valid."""
    if value.count("]:") == 1:
        # with ipv6
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg.lstrip("[").rstrip("]")

    if value.count(":") == 1:
        # with ipv4 or simple hostname
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg

    return None


def x__port_validator__mutmut_1(value: str):
    """Returns host segment if port is valid."""
    if value.count(None) == 1:
        # with ipv6
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg.lstrip("[").rstrip("]")

    if value.count(":") == 1:
        # with ipv4 or simple hostname
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg

    return None


def x__port_validator__mutmut_2(value: str):
    """Returns host segment if port is valid."""
    if value.count("XX]:XX") == 1:
        # with ipv6
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg.lstrip("[").rstrip("]")

    if value.count(":") == 1:
        # with ipv4 or simple hostname
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg

    return None


def x__port_validator__mutmut_3(value: str):
    """Returns host segment if port is valid."""
    if value.count("]:") != 1:
        # with ipv6
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg.lstrip("[").rstrip("]")

    if value.count(":") == 1:
        # with ipv4 or simple hostname
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg

    return None


def x__port_validator__mutmut_4(value: str):
    """Returns host segment if port is valid."""
    if value.count("]:") == 2:
        # with ipv6
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg.lstrip("[").rstrip("]")

    if value.count(":") == 1:
        # with ipv4 or simple hostname
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg

    return None


def x__port_validator__mutmut_5(value: str):
    """Returns host segment if port is valid."""
    if value.count("]:") == 1:
        # with ipv6
        host_seg, port_seg = None
        if _port_regex().match(f":{port_seg}"):
            return host_seg.lstrip("[").rstrip("]")

    if value.count(":") == 1:
        # with ipv4 or simple hostname
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg

    return None


def x__port_validator__mutmut_6(value: str):
    """Returns host segment if port is valid."""
    if value.count("]:") == 1:
        # with ipv6
        host_seg, port_seg = value.rsplit(None, 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg.lstrip("[").rstrip("]")

    if value.count(":") == 1:
        # with ipv4 or simple hostname
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg

    return None


def x__port_validator__mutmut_7(value: str):
    """Returns host segment if port is valid."""
    if value.count("]:") == 1:
        # with ipv6
        host_seg, port_seg = value.rsplit(":", None)
        if _port_regex().match(f":{port_seg}"):
            return host_seg.lstrip("[").rstrip("]")

    if value.count(":") == 1:
        # with ipv4 or simple hostname
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg

    return None


def x__port_validator__mutmut_8(value: str):
    """Returns host segment if port is valid."""
    if value.count("]:") == 1:
        # with ipv6
        host_seg, port_seg = value.rsplit(1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg.lstrip("[").rstrip("]")

    if value.count(":") == 1:
        # with ipv4 or simple hostname
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg

    return None


def x__port_validator__mutmut_9(value: str):
    """Returns host segment if port is valid."""
    if value.count("]:") == 1:
        # with ipv6
        host_seg, port_seg = value.rsplit(":", )
        if _port_regex().match(f":{port_seg}"):
            return host_seg.lstrip("[").rstrip("]")

    if value.count(":") == 1:
        # with ipv4 or simple hostname
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg

    return None


def x__port_validator__mutmut_10(value: str):
    """Returns host segment if port is valid."""
    if value.count("]:") == 1:
        # with ipv6
        host_seg, port_seg = value.split(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg.lstrip("[").rstrip("]")

    if value.count(":") == 1:
        # with ipv4 or simple hostname
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg

    return None


def x__port_validator__mutmut_11(value: str):
    """Returns host segment if port is valid."""
    if value.count("]:") == 1:
        # with ipv6
        host_seg, port_seg = value.rsplit("XX:XX", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg.lstrip("[").rstrip("]")

    if value.count(":") == 1:
        # with ipv4 or simple hostname
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg

    return None


def x__port_validator__mutmut_12(value: str):
    """Returns host segment if port is valid."""
    if value.count("]:") == 1:
        # with ipv6
        host_seg, port_seg = value.rsplit(":", 2)
        if _port_regex().match(f":{port_seg}"):
            return host_seg.lstrip("[").rstrip("]")

    if value.count(":") == 1:
        # with ipv4 or simple hostname
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg

    return None


def x__port_validator__mutmut_13(value: str):
    """Returns host segment if port is valid."""
    if value.count("]:") == 1:
        # with ipv6
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(None):
            return host_seg.lstrip("[").rstrip("]")

    if value.count(":") == 1:
        # with ipv4 or simple hostname
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg

    return None


def x__port_validator__mutmut_14(value: str):
    """Returns host segment if port is valid."""
    if value.count("]:") == 1:
        # with ipv6
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg.lstrip("[").rstrip(None)

    if value.count(":") == 1:
        # with ipv4 or simple hostname
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg

    return None


def x__port_validator__mutmut_15(value: str):
    """Returns host segment if port is valid."""
    if value.count("]:") == 1:
        # with ipv6
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg.lstrip("[").lstrip("]")

    if value.count(":") == 1:
        # with ipv4 or simple hostname
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg

    return None


def x__port_validator__mutmut_16(value: str):
    """Returns host segment if port is valid."""
    if value.count("]:") == 1:
        # with ipv6
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg.lstrip(None).rstrip("]")

    if value.count(":") == 1:
        # with ipv4 or simple hostname
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg

    return None


def x__port_validator__mutmut_17(value: str):
    """Returns host segment if port is valid."""
    if value.count("]:") == 1:
        # with ipv6
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg.rstrip("[").rstrip("]")

    if value.count(":") == 1:
        # with ipv4 or simple hostname
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg

    return None


def x__port_validator__mutmut_18(value: str):
    """Returns host segment if port is valid."""
    if value.count("]:") == 1:
        # with ipv6
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg.lstrip("XX[XX").rstrip("]")

    if value.count(":") == 1:
        # with ipv4 or simple hostname
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg

    return None


def x__port_validator__mutmut_19(value: str):
    """Returns host segment if port is valid."""
    if value.count("]:") == 1:
        # with ipv6
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg.lstrip("[").rstrip("XX]XX")

    if value.count(":") == 1:
        # with ipv4 or simple hostname
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg

    return None


def x__port_validator__mutmut_20(value: str):
    """Returns host segment if port is valid."""
    if value.count("]:") == 1:
        # with ipv6
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg.lstrip("[").rstrip("]")

    if value.count(None) == 1:
        # with ipv4 or simple hostname
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg

    return None


def x__port_validator__mutmut_21(value: str):
    """Returns host segment if port is valid."""
    if value.count("]:") == 1:
        # with ipv6
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg.lstrip("[").rstrip("]")

    if value.count("XX:XX") == 1:
        # with ipv4 or simple hostname
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg

    return None


def x__port_validator__mutmut_22(value: str):
    """Returns host segment if port is valid."""
    if value.count("]:") == 1:
        # with ipv6
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg.lstrip("[").rstrip("]")

    if value.count(":") != 1:
        # with ipv4 or simple hostname
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg

    return None


def x__port_validator__mutmut_23(value: str):
    """Returns host segment if port is valid."""
    if value.count("]:") == 1:
        # with ipv6
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg.lstrip("[").rstrip("]")

    if value.count(":") == 2:
        # with ipv4 or simple hostname
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg

    return None


def x__port_validator__mutmut_24(value: str):
    """Returns host segment if port is valid."""
    if value.count("]:") == 1:
        # with ipv6
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg.lstrip("[").rstrip("]")

    if value.count(":") == 1:
        # with ipv4 or simple hostname
        host_seg, port_seg = None
        if _port_regex().match(f":{port_seg}"):
            return host_seg

    return None


def x__port_validator__mutmut_25(value: str):
    """Returns host segment if port is valid."""
    if value.count("]:") == 1:
        # with ipv6
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg.lstrip("[").rstrip("]")

    if value.count(":") == 1:
        # with ipv4 or simple hostname
        host_seg, port_seg = value.rsplit(None, 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg

    return None


def x__port_validator__mutmut_26(value: str):
    """Returns host segment if port is valid."""
    if value.count("]:") == 1:
        # with ipv6
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg.lstrip("[").rstrip("]")

    if value.count(":") == 1:
        # with ipv4 or simple hostname
        host_seg, port_seg = value.rsplit(":", None)
        if _port_regex().match(f":{port_seg}"):
            return host_seg

    return None


def x__port_validator__mutmut_27(value: str):
    """Returns host segment if port is valid."""
    if value.count("]:") == 1:
        # with ipv6
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg.lstrip("[").rstrip("]")

    if value.count(":") == 1:
        # with ipv4 or simple hostname
        host_seg, port_seg = value.rsplit(1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg

    return None


def x__port_validator__mutmut_28(value: str):
    """Returns host segment if port is valid."""
    if value.count("]:") == 1:
        # with ipv6
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg.lstrip("[").rstrip("]")

    if value.count(":") == 1:
        # with ipv4 or simple hostname
        host_seg, port_seg = value.rsplit(":", )
        if _port_regex().match(f":{port_seg}"):
            return host_seg

    return None


def x__port_validator__mutmut_29(value: str):
    """Returns host segment if port is valid."""
    if value.count("]:") == 1:
        # with ipv6
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg.lstrip("[").rstrip("]")

    if value.count(":") == 1:
        # with ipv4 or simple hostname
        host_seg, port_seg = value.split(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg

    return None


def x__port_validator__mutmut_30(value: str):
    """Returns host segment if port is valid."""
    if value.count("]:") == 1:
        # with ipv6
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg.lstrip("[").rstrip("]")

    if value.count(":") == 1:
        # with ipv4 or simple hostname
        host_seg, port_seg = value.rsplit("XX:XX", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg

    return None


def x__port_validator__mutmut_31(value: str):
    """Returns host segment if port is valid."""
    if value.count("]:") == 1:
        # with ipv6
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg.lstrip("[").rstrip("]")

    if value.count(":") == 1:
        # with ipv4 or simple hostname
        host_seg, port_seg = value.rsplit(":", 2)
        if _port_regex().match(f":{port_seg}"):
            return host_seg

    return None


def x__port_validator__mutmut_32(value: str):
    """Returns host segment if port is valid."""
    if value.count("]:") == 1:
        # with ipv6
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(f":{port_seg}"):
            return host_seg.lstrip("[").rstrip("]")

    if value.count(":") == 1:
        # with ipv4 or simple hostname
        host_seg, port_seg = value.rsplit(":", 1)
        if _port_regex().match(None):
            return host_seg

    return None

x__port_validator__mutmut_mutants : ClassVar[MutantDict] = {
'x__port_validator__mutmut_1': x__port_validator__mutmut_1, 
    'x__port_validator__mutmut_2': x__port_validator__mutmut_2, 
    'x__port_validator__mutmut_3': x__port_validator__mutmut_3, 
    'x__port_validator__mutmut_4': x__port_validator__mutmut_4, 
    'x__port_validator__mutmut_5': x__port_validator__mutmut_5, 
    'x__port_validator__mutmut_6': x__port_validator__mutmut_6, 
    'x__port_validator__mutmut_7': x__port_validator__mutmut_7, 
    'x__port_validator__mutmut_8': x__port_validator__mutmut_8, 
    'x__port_validator__mutmut_9': x__port_validator__mutmut_9, 
    'x__port_validator__mutmut_10': x__port_validator__mutmut_10, 
    'x__port_validator__mutmut_11': x__port_validator__mutmut_11, 
    'x__port_validator__mutmut_12': x__port_validator__mutmut_12, 
    'x__port_validator__mutmut_13': x__port_validator__mutmut_13, 
    'x__port_validator__mutmut_14': x__port_validator__mutmut_14, 
    'x__port_validator__mutmut_15': x__port_validator__mutmut_15, 
    'x__port_validator__mutmut_16': x__port_validator__mutmut_16, 
    'x__port_validator__mutmut_17': x__port_validator__mutmut_17, 
    'x__port_validator__mutmut_18': x__port_validator__mutmut_18, 
    'x__port_validator__mutmut_19': x__port_validator__mutmut_19, 
    'x__port_validator__mutmut_20': x__port_validator__mutmut_20, 
    'x__port_validator__mutmut_21': x__port_validator__mutmut_21, 
    'x__port_validator__mutmut_22': x__port_validator__mutmut_22, 
    'x__port_validator__mutmut_23': x__port_validator__mutmut_23, 
    'x__port_validator__mutmut_24': x__port_validator__mutmut_24, 
    'x__port_validator__mutmut_25': x__port_validator__mutmut_25, 
    'x__port_validator__mutmut_26': x__port_validator__mutmut_26, 
    'x__port_validator__mutmut_27': x__port_validator__mutmut_27, 
    'x__port_validator__mutmut_28': x__port_validator__mutmut_28, 
    'x__port_validator__mutmut_29': x__port_validator__mutmut_29, 
    'x__port_validator__mutmut_30': x__port_validator__mutmut_30, 
    'x__port_validator__mutmut_31': x__port_validator__mutmut_31, 
    'x__port_validator__mutmut_32': x__port_validator__mutmut_32
}

def _port_validator(*args, **kwargs):
    result = _mutmut_trampoline(x__port_validator__mutmut_orig, x__port_validator__mutmut_mutants, args, kwargs)
    return result 

_port_validator.__signature__ = _mutmut_signature(x__port_validator__mutmut_orig)
x__port_validator__mutmut_orig.__name__ = 'x__port_validator'


@validator
def hostname(
    value: str,
    /,
    *,
    skip_ipv6_addr: bool = False,
    skip_ipv4_addr: bool = False,
    may_have_port: bool = True,
    maybe_simple: bool = True,
    consider_tld: bool = False,
    private: Optional[bool] = None,  # only for ip-addresses
    rfc_1034: bool = False,
    rfc_2782: bool = False,
):
    """Return whether or not given value is a valid hostname.

    Examples:
        >>> hostname("ubuntu-pc:443")
        True
        >>> hostname("this-pc")
        True
        >>> hostname("xn----gtbspbbmkef.xn--p1ai:65535")
        True
        >>> hostname("_example.com")
        ValidationError(func=hostname, args={'value': '_example.com'})
        >>> hostname("123.5.77.88:31000")
        True
        >>> hostname("12.12.12.12")
        True
        >>> hostname("[::1]:22")
        True
        >>> hostname("dead:beef:0:0:0:0000:42:1")
        True
        >>> hostname("[0:0:0:0:0:ffff:1.2.3.4]:-65538")
        ValidationError(func=hostname, args={'value': '[0:0:0:0:0:ffff:1.2.3.4]:-65538'})
        >>> hostname("[0:&:b:c:@:e:f::]:9999")
        ValidationError(func=hostname, args={'value': '[0:&:b:c:@:e:f::]:9999'})

    Args:
        value:
            Hostname string to validate.
        skip_ipv6_addr:
            When hostname string cannot be an IPv6 address.
        skip_ipv4_addr:
            When hostname string cannot be an IPv4 address.
        may_have_port:
            Hostname string may contain port number.
        maybe_simple:
            Hostname string maybe only hyphens and alpha-numerals.
        consider_tld:
            Restrict domain to TLDs allowed by IANA.
        private:
            Embedded IP address is public if `False`, private/local if `True`.
        rfc_1034:
            Allow trailing dot in domain/host name.
            Ref: [RFC 1034](https://www.rfc-editor.org/rfc/rfc1034).
        rfc_2782:
            Domain/Host name is of type service record.
            Ref: [RFC 2782](https://www.rfc-editor.org/rfc/rfc2782).

    Returns:
        (Literal[True]): If `value` is a valid hostname.
        (ValidationError): If `value` is an invalid hostname.
    """
    if not value:
        return False

    if may_have_port and (host_seg := _port_validator(value)):
        return (
            (_simple_hostname_regex().match(host_seg) if maybe_simple else False)
            or domain(host_seg, consider_tld=consider_tld, rfc_1034=rfc_1034, rfc_2782=rfc_2782)
            or (False if skip_ipv4_addr else ipv4(host_seg, cidr=False, private=private))
            or (False if skip_ipv6_addr else ipv6(host_seg, cidr=False))
        )

    return (
        (_simple_hostname_regex().match(value) if maybe_simple else False)
        or domain(value, consider_tld=consider_tld, rfc_1034=rfc_1034, rfc_2782=rfc_2782)
        or (False if skip_ipv4_addr else ipv4(value, cidr=False, private=private))
        or (False if skip_ipv6_addr else ipv6(value, cidr=False))
    )
