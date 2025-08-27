"""IP Address."""

# standard
from ipaddress import (
    AddressValueError,
    IPv4Address,
    IPv4Network,
    IPv6Address,
    IPv6Network,
    NetmaskValueError,
)
import re
from typing import Optional

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


def x__check_private_ip__mutmut_orig(value: str, is_private: Optional[bool]):
    if is_private is None:
        return True
    if (
        any(
            value.startswith(l_bit)
            for l_bit in {
                "10.",  # private
                "192.168.",  # private
                "169.254.",  # link-local
                "127.",  # localhost
                "0.0.0.0",  # loopback #nosec
            }
        )
        or re.match(r"^172\.(?:1[6-9]|2\d|3[0-1])\.", value)  # private
        or re.match(r"^(?:22[4-9]|23[0-9]|24[0-9]|25[0-5])\.", value)  # broadcast
    ):
        return is_private

    return not is_private


def x__check_private_ip__mutmut_1(value: str, is_private: Optional[bool]):
    if is_private is not None:
        return True
    if (
        any(
            value.startswith(l_bit)
            for l_bit in {
                "10.",  # private
                "192.168.",  # private
                "169.254.",  # link-local
                "127.",  # localhost
                "0.0.0.0",  # loopback #nosec
            }
        )
        or re.match(r"^172\.(?:1[6-9]|2\d|3[0-1])\.", value)  # private
        or re.match(r"^(?:22[4-9]|23[0-9]|24[0-9]|25[0-5])\.", value)  # broadcast
    ):
        return is_private

    return not is_private


def x__check_private_ip__mutmut_2(value: str, is_private: Optional[bool]):
    if is_private is None:
        return False
    if (
        any(
            value.startswith(l_bit)
            for l_bit in {
                "10.",  # private
                "192.168.",  # private
                "169.254.",  # link-local
                "127.",  # localhost
                "0.0.0.0",  # loopback #nosec
            }
        )
        or re.match(r"^172\.(?:1[6-9]|2\d|3[0-1])\.", value)  # private
        or re.match(r"^(?:22[4-9]|23[0-9]|24[0-9]|25[0-5])\.", value)  # broadcast
    ):
        return is_private

    return not is_private


def x__check_private_ip__mutmut_3(value: str, is_private: Optional[bool]):
    if is_private is None:
        return True
    if (
        any(
            value.startswith(l_bit)
            for l_bit in {
                "10.",  # private
                "192.168.",  # private
                "169.254.",  # link-local
                "127.",  # localhost
                "0.0.0.0",  # loopback #nosec
            }
        )
        or re.match(r"^172\.(?:1[6-9]|2\d|3[0-1])\.", value) and re.match(r"^(?:22[4-9]|23[0-9]|24[0-9]|25[0-5])\.", value)  # broadcast
    ):
        return is_private

    return not is_private


def x__check_private_ip__mutmut_4(value: str, is_private: Optional[bool]):
    if is_private is None:
        return True
    if (
        any(
            value.startswith(l_bit)
            for l_bit in {
                "10.",  # private
                "192.168.",  # private
                "169.254.",  # link-local
                "127.",  # localhost
                "0.0.0.0",  # loopback #nosec
            }
        ) and re.match(r"^172\.(?:1[6-9]|2\d|3[0-1])\.", value)  # private
        or re.match(r"^(?:22[4-9]|23[0-9]|24[0-9]|25[0-5])\.", value)  # broadcast
    ):
        return is_private

    return not is_private


def x__check_private_ip__mutmut_5(value: str, is_private: Optional[bool]):
    if is_private is None:
        return True
    if (
        any(
            None
        )
        or re.match(r"^172\.(?:1[6-9]|2\d|3[0-1])\.", value)  # private
        or re.match(r"^(?:22[4-9]|23[0-9]|24[0-9]|25[0-5])\.", value)  # broadcast
    ):
        return is_private

    return not is_private


def x__check_private_ip__mutmut_6(value: str, is_private: Optional[bool]):
    if is_private is None:
        return True
    if (
        any(
            value.startswith(None)
            for l_bit in {
                "10.",  # private
                "192.168.",  # private
                "169.254.",  # link-local
                "127.",  # localhost
                "0.0.0.0",  # loopback #nosec
            }
        )
        or re.match(r"^172\.(?:1[6-9]|2\d|3[0-1])\.", value)  # private
        or re.match(r"^(?:22[4-9]|23[0-9]|24[0-9]|25[0-5])\.", value)  # broadcast
    ):
        return is_private

    return not is_private


def x__check_private_ip__mutmut_7(value: str, is_private: Optional[bool]):
    if is_private is None:
        return True
    if (
        any(
            value.startswith(l_bit)
            for l_bit in {
                "XX10.XX",  # private
                "192.168.",  # private
                "169.254.",  # link-local
                "127.",  # localhost
                "0.0.0.0",  # loopback #nosec
            }
        )
        or re.match(r"^172\.(?:1[6-9]|2\d|3[0-1])\.", value)  # private
        or re.match(r"^(?:22[4-9]|23[0-9]|24[0-9]|25[0-5])\.", value)  # broadcast
    ):
        return is_private

    return not is_private


def x__check_private_ip__mutmut_8(value: str, is_private: Optional[bool]):
    if is_private is None:
        return True
    if (
        any(
            value.startswith(l_bit)
            for l_bit in {
                "10.",  # private
                "XX192.168.XX",  # private
                "169.254.",  # link-local
                "127.",  # localhost
                "0.0.0.0",  # loopback #nosec
            }
        )
        or re.match(r"^172\.(?:1[6-9]|2\d|3[0-1])\.", value)  # private
        or re.match(r"^(?:22[4-9]|23[0-9]|24[0-9]|25[0-5])\.", value)  # broadcast
    ):
        return is_private

    return not is_private


def x__check_private_ip__mutmut_9(value: str, is_private: Optional[bool]):
    if is_private is None:
        return True
    if (
        any(
            value.startswith(l_bit)
            for l_bit in {
                "10.",  # private
                "192.168.",  # private
                "XX169.254.XX",  # link-local
                "127.",  # localhost
                "0.0.0.0",  # loopback #nosec
            }
        )
        or re.match(r"^172\.(?:1[6-9]|2\d|3[0-1])\.", value)  # private
        or re.match(r"^(?:22[4-9]|23[0-9]|24[0-9]|25[0-5])\.", value)  # broadcast
    ):
        return is_private

    return not is_private


def x__check_private_ip__mutmut_10(value: str, is_private: Optional[bool]):
    if is_private is None:
        return True
    if (
        any(
            value.startswith(l_bit)
            for l_bit in {
                "10.",  # private
                "192.168.",  # private
                "169.254.",  # link-local
                "XX127.XX",  # localhost
                "0.0.0.0",  # loopback #nosec
            }
        )
        or re.match(r"^172\.(?:1[6-9]|2\d|3[0-1])\.", value)  # private
        or re.match(r"^(?:22[4-9]|23[0-9]|24[0-9]|25[0-5])\.", value)  # broadcast
    ):
        return is_private

    return not is_private


def x__check_private_ip__mutmut_11(value: str, is_private: Optional[bool]):
    if is_private is None:
        return True
    if (
        any(
            value.startswith(l_bit)
            for l_bit in {
                "10.",  # private
                "192.168.",  # private
                "169.254.",  # link-local
                "127.",  # localhost
                "XX0.0.0.0XX",  # loopback #nosec
            }
        )
        or re.match(r"^172\.(?:1[6-9]|2\d|3[0-1])\.", value)  # private
        or re.match(r"^(?:22[4-9]|23[0-9]|24[0-9]|25[0-5])\.", value)  # broadcast
    ):
        return is_private

    return not is_private


def x__check_private_ip__mutmut_12(value: str, is_private: Optional[bool]):
    if is_private is None:
        return True
    if (
        any(
            value.startswith(l_bit)
            for l_bit in {
                "10.",  # private
                "192.168.",  # private
                "169.254.",  # link-local
                "127.",  # localhost
                "0.0.0.0",  # loopback #nosec
            }
        )
        or re.match(None, value)  # private
        or re.match(r"^(?:22[4-9]|23[0-9]|24[0-9]|25[0-5])\.", value)  # broadcast
    ):
        return is_private

    return not is_private


def x__check_private_ip__mutmut_13(value: str, is_private: Optional[bool]):
    if is_private is None:
        return True
    if (
        any(
            value.startswith(l_bit)
            for l_bit in {
                "10.",  # private
                "192.168.",  # private
                "169.254.",  # link-local
                "127.",  # localhost
                "0.0.0.0",  # loopback #nosec
            }
        )
        or re.match(r"^172\.(?:1[6-9]|2\d|3[0-1])\.", None)  # private
        or re.match(r"^(?:22[4-9]|23[0-9]|24[0-9]|25[0-5])\.", value)  # broadcast
    ):
        return is_private

    return not is_private


def x__check_private_ip__mutmut_14(value: str, is_private: Optional[bool]):
    if is_private is None:
        return True
    if (
        any(
            value.startswith(l_bit)
            for l_bit in {
                "10.",  # private
                "192.168.",  # private
                "169.254.",  # link-local
                "127.",  # localhost
                "0.0.0.0",  # loopback #nosec
            }
        )
        or re.match(value)  # private
        or re.match(r"^(?:22[4-9]|23[0-9]|24[0-9]|25[0-5])\.", value)  # broadcast
    ):
        return is_private

    return not is_private


def x__check_private_ip__mutmut_15(value: str, is_private: Optional[bool]):
    if is_private is None:
        return True
    if (
        any(
            value.startswith(l_bit)
            for l_bit in {
                "10.",  # private
                "192.168.",  # private
                "169.254.",  # link-local
                "127.",  # localhost
                "0.0.0.0",  # loopback #nosec
            }
        )
        or re.match(r"^172\.(?:1[6-9]|2\d|3[0-1])\.", )  # private
        or re.match(r"^(?:22[4-9]|23[0-9]|24[0-9]|25[0-5])\.", value)  # broadcast
    ):
        return is_private

    return not is_private


def x__check_private_ip__mutmut_16(value: str, is_private: Optional[bool]):
    if is_private is None:
        return True
    if (
        any(
            value.startswith(l_bit)
            for l_bit in {
                "10.",  # private
                "192.168.",  # private
                "169.254.",  # link-local
                "127.",  # localhost
                "0.0.0.0",  # loopback #nosec
            }
        )
        or re.match(r"XX^172\.(?:1[6-9]|2\d|3[0-1])\.XX", value)  # private
        or re.match(r"^(?:22[4-9]|23[0-9]|24[0-9]|25[0-5])\.", value)  # broadcast
    ):
        return is_private

    return not is_private


def x__check_private_ip__mutmut_17(value: str, is_private: Optional[bool]):
    if is_private is None:
        return True
    if (
        any(
            value.startswith(l_bit)
            for l_bit in {
                "10.",  # private
                "192.168.",  # private
                "169.254.",  # link-local
                "127.",  # localhost
                "0.0.0.0",  # loopback #nosec
            }
        )
        or re.match(r"^172\.(?:1[6-9]|2\d|3[0-1])\.", value)  # private
        or re.match(r"^(?:22[4-9]|23[0-9]|24[0-9]|25[0-5])\.", value)  # broadcast
    ):
        return is_private

    return not is_private


def x__check_private_ip__mutmut_18(value: str, is_private: Optional[bool]):
    if is_private is None:
        return True
    if (
        any(
            value.startswith(l_bit)
            for l_bit in {
                "10.",  # private
                "192.168.",  # private
                "169.254.",  # link-local
                "127.",  # localhost
                "0.0.0.0",  # loopback #nosec
            }
        )
        or re.match(r"^172\.(?:1[6-9]|2\d|3[0-1])\.", value)  # private
        or re.match(r"^(?:22[4-9]|23[0-9]|24[0-9]|25[0-5])\.", value)  # broadcast
    ):
        return is_private

    return not is_private


def x__check_private_ip__mutmut_19(value: str, is_private: Optional[bool]):
    if is_private is None:
        return True
    if (
        any(
            value.startswith(l_bit)
            for l_bit in {
                "10.",  # private
                "192.168.",  # private
                "169.254.",  # link-local
                "127.",  # localhost
                "0.0.0.0",  # loopback #nosec
            }
        )
        or re.match(r"^172\.(?:1[6-9]|2\d|3[0-1])\.", value)  # private
        or re.match(None, value)  # broadcast
    ):
        return is_private

    return not is_private


def x__check_private_ip__mutmut_20(value: str, is_private: Optional[bool]):
    if is_private is None:
        return True
    if (
        any(
            value.startswith(l_bit)
            for l_bit in {
                "10.",  # private
                "192.168.",  # private
                "169.254.",  # link-local
                "127.",  # localhost
                "0.0.0.0",  # loopback #nosec
            }
        )
        or re.match(r"^172\.(?:1[6-9]|2\d|3[0-1])\.", value)  # private
        or re.match(r"^(?:22[4-9]|23[0-9]|24[0-9]|25[0-5])\.", None)  # broadcast
    ):
        return is_private

    return not is_private


def x__check_private_ip__mutmut_21(value: str, is_private: Optional[bool]):
    if is_private is None:
        return True
    if (
        any(
            value.startswith(l_bit)
            for l_bit in {
                "10.",  # private
                "192.168.",  # private
                "169.254.",  # link-local
                "127.",  # localhost
                "0.0.0.0",  # loopback #nosec
            }
        )
        or re.match(r"^172\.(?:1[6-9]|2\d|3[0-1])\.", value)  # private
        or re.match(value)  # broadcast
    ):
        return is_private

    return not is_private


def x__check_private_ip__mutmut_22(value: str, is_private: Optional[bool]):
    if is_private is None:
        return True
    if (
        any(
            value.startswith(l_bit)
            for l_bit in {
                "10.",  # private
                "192.168.",  # private
                "169.254.",  # link-local
                "127.",  # localhost
                "0.0.0.0",  # loopback #nosec
            }
        )
        or re.match(r"^172\.(?:1[6-9]|2\d|3[0-1])\.", value)  # private
        or re.match(r"^(?:22[4-9]|23[0-9]|24[0-9]|25[0-5])\.", )  # broadcast
    ):
        return is_private

    return not is_private


def x__check_private_ip__mutmut_23(value: str, is_private: Optional[bool]):
    if is_private is None:
        return True
    if (
        any(
            value.startswith(l_bit)
            for l_bit in {
                "10.",  # private
                "192.168.",  # private
                "169.254.",  # link-local
                "127.",  # localhost
                "0.0.0.0",  # loopback #nosec
            }
        )
        or re.match(r"^172\.(?:1[6-9]|2\d|3[0-1])\.", value)  # private
        or re.match(r"XX^(?:22[4-9]|23[0-9]|24[0-9]|25[0-5])\.XX", value)  # broadcast
    ):
        return is_private

    return not is_private


def x__check_private_ip__mutmut_24(value: str, is_private: Optional[bool]):
    if is_private is None:
        return True
    if (
        any(
            value.startswith(l_bit)
            for l_bit in {
                "10.",  # private
                "192.168.",  # private
                "169.254.",  # link-local
                "127.",  # localhost
                "0.0.0.0",  # loopback #nosec
            }
        )
        or re.match(r"^172\.(?:1[6-9]|2\d|3[0-1])\.", value)  # private
        or re.match(r"^(?:22[4-9]|23[0-9]|24[0-9]|25[0-5])\.", value)  # broadcast
    ):
        return is_private

    return not is_private


def x__check_private_ip__mutmut_25(value: str, is_private: Optional[bool]):
    if is_private is None:
        return True
    if (
        any(
            value.startswith(l_bit)
            for l_bit in {
                "10.",  # private
                "192.168.",  # private
                "169.254.",  # link-local
                "127.",  # localhost
                "0.0.0.0",  # loopback #nosec
            }
        )
        or re.match(r"^172\.(?:1[6-9]|2\d|3[0-1])\.", value)  # private
        or re.match(r"^(?:22[4-9]|23[0-9]|24[0-9]|25[0-5])\.", value)  # broadcast
    ):
        return is_private

    return not is_private


def x__check_private_ip__mutmut_26(value: str, is_private: Optional[bool]):
    if is_private is None:
        return True
    if (
        any(
            value.startswith(l_bit)
            for l_bit in {
                "10.",  # private
                "192.168.",  # private
                "169.254.",  # link-local
                "127.",  # localhost
                "0.0.0.0",  # loopback #nosec
            }
        )
        or re.match(r"^172\.(?:1[6-9]|2\d|3[0-1])\.", value)  # private
        or re.match(r"^(?:22[4-9]|23[0-9]|24[0-9]|25[0-5])\.", value)  # broadcast
    ):
        return is_private

    return is_private

x__check_private_ip__mutmut_mutants : ClassVar[MutantDict] = {
'x__check_private_ip__mutmut_1': x__check_private_ip__mutmut_1, 
    'x__check_private_ip__mutmut_2': x__check_private_ip__mutmut_2, 
    'x__check_private_ip__mutmut_3': x__check_private_ip__mutmut_3, 
    'x__check_private_ip__mutmut_4': x__check_private_ip__mutmut_4, 
    'x__check_private_ip__mutmut_5': x__check_private_ip__mutmut_5, 
    'x__check_private_ip__mutmut_6': x__check_private_ip__mutmut_6, 
    'x__check_private_ip__mutmut_7': x__check_private_ip__mutmut_7, 
    'x__check_private_ip__mutmut_8': x__check_private_ip__mutmut_8, 
    'x__check_private_ip__mutmut_9': x__check_private_ip__mutmut_9, 
    'x__check_private_ip__mutmut_10': x__check_private_ip__mutmut_10, 
    'x__check_private_ip__mutmut_11': x__check_private_ip__mutmut_11, 
    'x__check_private_ip__mutmut_12': x__check_private_ip__mutmut_12, 
    'x__check_private_ip__mutmut_13': x__check_private_ip__mutmut_13, 
    'x__check_private_ip__mutmut_14': x__check_private_ip__mutmut_14, 
    'x__check_private_ip__mutmut_15': x__check_private_ip__mutmut_15, 
    'x__check_private_ip__mutmut_16': x__check_private_ip__mutmut_16, 
    'x__check_private_ip__mutmut_17': x__check_private_ip__mutmut_17, 
    'x__check_private_ip__mutmut_18': x__check_private_ip__mutmut_18, 
    'x__check_private_ip__mutmut_19': x__check_private_ip__mutmut_19, 
    'x__check_private_ip__mutmut_20': x__check_private_ip__mutmut_20, 
    'x__check_private_ip__mutmut_21': x__check_private_ip__mutmut_21, 
    'x__check_private_ip__mutmut_22': x__check_private_ip__mutmut_22, 
    'x__check_private_ip__mutmut_23': x__check_private_ip__mutmut_23, 
    'x__check_private_ip__mutmut_24': x__check_private_ip__mutmut_24, 
    'x__check_private_ip__mutmut_25': x__check_private_ip__mutmut_25, 
    'x__check_private_ip__mutmut_26': x__check_private_ip__mutmut_26
}

def _check_private_ip(*args, **kwargs):
    result = _mutmut_trampoline(x__check_private_ip__mutmut_orig, x__check_private_ip__mutmut_mutants, args, kwargs)
    return result 

_check_private_ip.__signature__ = _mutmut_signature(x__check_private_ip__mutmut_orig)
x__check_private_ip__mutmut_orig.__name__ = 'x__check_private_ip'


@validator
def ipv4(
    value: str,
    /,
    *,
    cidr: bool = True,
    strict: bool = False,
    private: Optional[bool] = None,
    host_bit: bool = True,
):
    """Returns whether a given value is a valid IPv4 address.

    From Python version 3.9.5 leading zeros are no longer tolerated
    and are treated as an error. The initial version of ipv4 validator
    was inspired from [WTForms IPAddress validator][1].

    [1]: https://github.com/wtforms/wtforms/blob/master/src/wtforms/validators.py

    Examples:
        >>> ipv4('123.0.0.7')
        True
        >>> ipv4('1.1.1.1/8')
        True
        >>> ipv4('900.80.70.11')
        ValidationError(func=ipv4, args={'value': '900.80.70.11'})

    Args:
        value:
            IP address string to validate.
        cidr:
            IP address string may contain CIDR notation.
        strict:
            IP address string is strictly in CIDR notation.
        private:
            IP address is public if `False`, private/local/loopback/broadcast if `True`.
        host_bit:
            If `False` and host bits (along with network bits) _are_ set in the supplied
            address, this function raises a validation error. ref [IPv4Network][2].
            [2]: https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network

    Returns:
        (Literal[True]): If `value` is a valid IPv4 address.
        (ValidationError): If `value` is an invalid IPv4 address.
    """
    if not value:
        return False
    try:
        if cidr:
            if strict and value.count("/") != 1:
                raise ValueError("IPv4 address was expected in CIDR notation")
            return IPv4Network(value, strict=not host_bit) and _check_private_ip(value, private)
        return IPv4Address(value) and _check_private_ip(value, private)
    except (ValueError, AddressValueError, NetmaskValueError):
        return False


@validator
def ipv6(value: str, /, *, cidr: bool = True, strict: bool = False, host_bit: bool = True):
    """Returns if a given value is a valid IPv6 address.

    Including IPv4-mapped IPv6 addresses. The initial version of ipv6 validator
    was inspired from [WTForms IPAddress validator][1].

    [1]: https://github.com/wtforms/wtforms/blob/master/src/wtforms/validators.py

    Examples:
        >>> ipv6('::ffff:192.0.2.128')
        True
        >>> ipv6('::1/128')
        True
        >>> ipv6('abc.0.0.1')
        ValidationError(func=ipv6, args={'value': 'abc.0.0.1'})

    Args:
        value:
            IP address string to validate.
        cidr:
            IP address string may contain CIDR annotation.
        strict:
            IP address string is strictly in CIDR notation.
        host_bit:
            If `False` and host bits (along with network bits) _are_ set in the supplied
            address, this function raises a validation error. ref [IPv6Network][2].
            [2]: https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network

    Returns:
        (Literal[True]): If `value` is a valid IPv6 address.
        (ValidationError): If `value` is an invalid IPv6 address.
    """
    if not value:
        return False
    try:
        if cidr:
            if strict and value.count("/") != 1:
                raise ValueError("IPv6 address was expected in CIDR notation")
            return IPv6Network(value, strict=not host_bit)
        return IPv6Address(value)
    except (ValueError, AddressValueError, NetmaskValueError):
        return False
