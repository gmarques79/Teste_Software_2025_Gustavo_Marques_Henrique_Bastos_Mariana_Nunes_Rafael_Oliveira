"""BTC Address."""

# standard
from hashlib import sha256
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


def x__decode_base58__mutmut_orig(addr: str):
    """Decode base58."""
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    return sum((58**enm) * alphabet.index(idx) for enm, idx in enumerate(addr[::-1]))


def x__decode_base58__mutmut_1(addr: str):
    """Decode base58."""
    alphabet = None
    return sum((58**enm) * alphabet.index(idx) for enm, idx in enumerate(addr[::-1]))


def x__decode_base58__mutmut_2(addr: str):
    """Decode base58."""
    alphabet = "XX123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyzXX"
    return sum((58**enm) * alphabet.index(idx) for enm, idx in enumerate(addr[::-1]))


def x__decode_base58__mutmut_3(addr: str):
    """Decode base58."""
    alphabet = "123456789abcdefghjklmnpqrstuvwxyzabcdefghijkmnopqrstuvwxyz"
    return sum((58**enm) * alphabet.index(idx) for enm, idx in enumerate(addr[::-1]))


def x__decode_base58__mutmut_4(addr: str):
    """Decode base58."""
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZABCDEFGHIJKMNOPQRSTUVWXYZ"
    return sum((58**enm) * alphabet.index(idx) for enm, idx in enumerate(addr[::-1]))


def x__decode_base58__mutmut_5(addr: str):
    """Decode base58."""
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    return sum(None)


def x__decode_base58__mutmut_6(addr: str):
    """Decode base58."""
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    return sum((58**enm) / alphabet.index(idx) for enm, idx in enumerate(addr[::-1]))


def x__decode_base58__mutmut_7(addr: str):
    """Decode base58."""
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    return sum((58 * enm) * alphabet.index(idx) for enm, idx in enumerate(addr[::-1]))


def x__decode_base58__mutmut_8(addr: str):
    """Decode base58."""
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    return sum((59**enm) * alphabet.index(idx) for enm, idx in enumerate(addr[::-1]))


def x__decode_base58__mutmut_9(addr: str):
    """Decode base58."""
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    return sum((58**enm) * alphabet.index(None) for enm, idx in enumerate(addr[::-1]))


def x__decode_base58__mutmut_10(addr: str):
    """Decode base58."""
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    return sum((58**enm) * alphabet.rindex(idx) for enm, idx in enumerate(addr[::-1]))


def x__decode_base58__mutmut_11(addr: str):
    """Decode base58."""
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    return sum((58**enm) * alphabet.index(idx) for enm, idx in enumerate(None))


def x__decode_base58__mutmut_12(addr: str):
    """Decode base58."""
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    return sum((58**enm) * alphabet.index(idx) for enm, idx in enumerate(addr[::+1]))


def x__decode_base58__mutmut_13(addr: str):
    """Decode base58."""
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    return sum((58**enm) * alphabet.index(idx) for enm, idx in enumerate(addr[::-2]))

x__decode_base58__mutmut_mutants : ClassVar[MutantDict] = {
'x__decode_base58__mutmut_1': x__decode_base58__mutmut_1, 
    'x__decode_base58__mutmut_2': x__decode_base58__mutmut_2, 
    'x__decode_base58__mutmut_3': x__decode_base58__mutmut_3, 
    'x__decode_base58__mutmut_4': x__decode_base58__mutmut_4, 
    'x__decode_base58__mutmut_5': x__decode_base58__mutmut_5, 
    'x__decode_base58__mutmut_6': x__decode_base58__mutmut_6, 
    'x__decode_base58__mutmut_7': x__decode_base58__mutmut_7, 
    'x__decode_base58__mutmut_8': x__decode_base58__mutmut_8, 
    'x__decode_base58__mutmut_9': x__decode_base58__mutmut_9, 
    'x__decode_base58__mutmut_10': x__decode_base58__mutmut_10, 
    'x__decode_base58__mutmut_11': x__decode_base58__mutmut_11, 
    'x__decode_base58__mutmut_12': x__decode_base58__mutmut_12, 
    'x__decode_base58__mutmut_13': x__decode_base58__mutmut_13
}

def _decode_base58(*args, **kwargs):
    result = _mutmut_trampoline(x__decode_base58__mutmut_orig, x__decode_base58__mutmut_mutants, args, kwargs)
    return result 

_decode_base58.__signature__ = _mutmut_signature(x__decode_base58__mutmut_orig)
x__decode_base58__mutmut_orig.__name__ = 'x__decode_base58'


def x__validate_old_btc_address__mutmut_orig(addr: str):
    """Validate P2PKH and P2SH type address."""
    if len(addr) not in range(25, 35):
        return False
    decoded_bytes = _decode_base58(addr).to_bytes(25, "big")
    header, checksum = decoded_bytes[:-4], decoded_bytes[-4:]
    return checksum == sha256(sha256(header).digest()).digest()[:4]


def x__validate_old_btc_address__mutmut_1(addr: str):
    """Validate P2PKH and P2SH type address."""
    if len(addr) in range(25, 35):
        return False
    decoded_bytes = _decode_base58(addr).to_bytes(25, "big")
    header, checksum = decoded_bytes[:-4], decoded_bytes[-4:]
    return checksum == sha256(sha256(header).digest()).digest()[:4]


def x__validate_old_btc_address__mutmut_2(addr: str):
    """Validate P2PKH and P2SH type address."""
    if len(addr) not in range(None, 35):
        return False
    decoded_bytes = _decode_base58(addr).to_bytes(25, "big")
    header, checksum = decoded_bytes[:-4], decoded_bytes[-4:]
    return checksum == sha256(sha256(header).digest()).digest()[:4]


def x__validate_old_btc_address__mutmut_3(addr: str):
    """Validate P2PKH and P2SH type address."""
    if len(addr) not in range(25, None):
        return False
    decoded_bytes = _decode_base58(addr).to_bytes(25, "big")
    header, checksum = decoded_bytes[:-4], decoded_bytes[-4:]
    return checksum == sha256(sha256(header).digest()).digest()[:4]


def x__validate_old_btc_address__mutmut_4(addr: str):
    """Validate P2PKH and P2SH type address."""
    if len(addr) not in range(35):
        return False
    decoded_bytes = _decode_base58(addr).to_bytes(25, "big")
    header, checksum = decoded_bytes[:-4], decoded_bytes[-4:]
    return checksum == sha256(sha256(header).digest()).digest()[:4]


def x__validate_old_btc_address__mutmut_5(addr: str):
    """Validate P2PKH and P2SH type address."""
    if len(addr) not in range(25, ):
        return False
    decoded_bytes = _decode_base58(addr).to_bytes(25, "big")
    header, checksum = decoded_bytes[:-4], decoded_bytes[-4:]
    return checksum == sha256(sha256(header).digest()).digest()[:4]


def x__validate_old_btc_address__mutmut_6(addr: str):
    """Validate P2PKH and P2SH type address."""
    if len(addr) not in range(26, 35):
        return False
    decoded_bytes = _decode_base58(addr).to_bytes(25, "big")
    header, checksum = decoded_bytes[:-4], decoded_bytes[-4:]
    return checksum == sha256(sha256(header).digest()).digest()[:4]


def x__validate_old_btc_address__mutmut_7(addr: str):
    """Validate P2PKH and P2SH type address."""
    if len(addr) not in range(25, 36):
        return False
    decoded_bytes = _decode_base58(addr).to_bytes(25, "big")
    header, checksum = decoded_bytes[:-4], decoded_bytes[-4:]
    return checksum == sha256(sha256(header).digest()).digest()[:4]


def x__validate_old_btc_address__mutmut_8(addr: str):
    """Validate P2PKH and P2SH type address."""
    if len(addr) not in range(25, 35):
        return True
    decoded_bytes = _decode_base58(addr).to_bytes(25, "big")
    header, checksum = decoded_bytes[:-4], decoded_bytes[-4:]
    return checksum == sha256(sha256(header).digest()).digest()[:4]


def x__validate_old_btc_address__mutmut_9(addr: str):
    """Validate P2PKH and P2SH type address."""
    if len(addr) not in range(25, 35):
        return False
    decoded_bytes = None
    header, checksum = decoded_bytes[:-4], decoded_bytes[-4:]
    return checksum == sha256(sha256(header).digest()).digest()[:4]


def x__validate_old_btc_address__mutmut_10(addr: str):
    """Validate P2PKH and P2SH type address."""
    if len(addr) not in range(25, 35):
        return False
    decoded_bytes = _decode_base58(addr).to_bytes(None, "big")
    header, checksum = decoded_bytes[:-4], decoded_bytes[-4:]
    return checksum == sha256(sha256(header).digest()).digest()[:4]


def x__validate_old_btc_address__mutmut_11(addr: str):
    """Validate P2PKH and P2SH type address."""
    if len(addr) not in range(25, 35):
        return False
    decoded_bytes = _decode_base58(addr).to_bytes(25, None)
    header, checksum = decoded_bytes[:-4], decoded_bytes[-4:]
    return checksum == sha256(sha256(header).digest()).digest()[:4]


def x__validate_old_btc_address__mutmut_12(addr: str):
    """Validate P2PKH and P2SH type address."""
    if len(addr) not in range(25, 35):
        return False
    decoded_bytes = _decode_base58(addr).to_bytes("big")
    header, checksum = decoded_bytes[:-4], decoded_bytes[-4:]
    return checksum == sha256(sha256(header).digest()).digest()[:4]


def x__validate_old_btc_address__mutmut_13(addr: str):
    """Validate P2PKH and P2SH type address."""
    if len(addr) not in range(25, 35):
        return False
    decoded_bytes = _decode_base58(addr).to_bytes(25, )
    header, checksum = decoded_bytes[:-4], decoded_bytes[-4:]
    return checksum == sha256(sha256(header).digest()).digest()[:4]


def x__validate_old_btc_address__mutmut_14(addr: str):
    """Validate P2PKH and P2SH type address."""
    if len(addr) not in range(25, 35):
        return False
    decoded_bytes = _decode_base58(None).to_bytes(25, "big")
    header, checksum = decoded_bytes[:-4], decoded_bytes[-4:]
    return checksum == sha256(sha256(header).digest()).digest()[:4]


def x__validate_old_btc_address__mutmut_15(addr: str):
    """Validate P2PKH and P2SH type address."""
    if len(addr) not in range(25, 35):
        return False
    decoded_bytes = _decode_base58(addr).to_bytes(26, "big")
    header, checksum = decoded_bytes[:-4], decoded_bytes[-4:]
    return checksum == sha256(sha256(header).digest()).digest()[:4]


def x__validate_old_btc_address__mutmut_16(addr: str):
    """Validate P2PKH and P2SH type address."""
    if len(addr) not in range(25, 35):
        return False
    decoded_bytes = _decode_base58(addr).to_bytes(25, "XXbigXX")
    header, checksum = decoded_bytes[:-4], decoded_bytes[-4:]
    return checksum == sha256(sha256(header).digest()).digest()[:4]


def x__validate_old_btc_address__mutmut_17(addr: str):
    """Validate P2PKH and P2SH type address."""
    if len(addr) not in range(25, 35):
        return False
    decoded_bytes = _decode_base58(addr).to_bytes(25, "BIG")
    header, checksum = decoded_bytes[:-4], decoded_bytes[-4:]
    return checksum == sha256(sha256(header).digest()).digest()[:4]


def x__validate_old_btc_address__mutmut_18(addr: str):
    """Validate P2PKH and P2SH type address."""
    if len(addr) not in range(25, 35):
        return False
    decoded_bytes = _decode_base58(addr).to_bytes(25, "big")
    header, checksum = None
    return checksum == sha256(sha256(header).digest()).digest()[:4]


def x__validate_old_btc_address__mutmut_19(addr: str):
    """Validate P2PKH and P2SH type address."""
    if len(addr) not in range(25, 35):
        return False
    decoded_bytes = _decode_base58(addr).to_bytes(25, "big")
    header, checksum = decoded_bytes[:+4], decoded_bytes[-4:]
    return checksum == sha256(sha256(header).digest()).digest()[:4]


def x__validate_old_btc_address__mutmut_20(addr: str):
    """Validate P2PKH and P2SH type address."""
    if len(addr) not in range(25, 35):
        return False
    decoded_bytes = _decode_base58(addr).to_bytes(25, "big")
    header, checksum = decoded_bytes[:-5], decoded_bytes[-4:]
    return checksum == sha256(sha256(header).digest()).digest()[:4]


def x__validate_old_btc_address__mutmut_21(addr: str):
    """Validate P2PKH and P2SH type address."""
    if len(addr) not in range(25, 35):
        return False
    decoded_bytes = _decode_base58(addr).to_bytes(25, "big")
    header, checksum = decoded_bytes[:-4], decoded_bytes[+4:]
    return checksum == sha256(sha256(header).digest()).digest()[:4]


def x__validate_old_btc_address__mutmut_22(addr: str):
    """Validate P2PKH and P2SH type address."""
    if len(addr) not in range(25, 35):
        return False
    decoded_bytes = _decode_base58(addr).to_bytes(25, "big")
    header, checksum = decoded_bytes[:-4], decoded_bytes[-5:]
    return checksum == sha256(sha256(header).digest()).digest()[:4]


def x__validate_old_btc_address__mutmut_23(addr: str):
    """Validate P2PKH and P2SH type address."""
    if len(addr) not in range(25, 35):
        return False
    decoded_bytes = _decode_base58(addr).to_bytes(25, "big")
    header, checksum = decoded_bytes[:-4], decoded_bytes[-4:]
    return checksum != sha256(sha256(header).digest()).digest()[:4]


def x__validate_old_btc_address__mutmut_24(addr: str):
    """Validate P2PKH and P2SH type address."""
    if len(addr) not in range(25, 35):
        return False
    decoded_bytes = _decode_base58(addr).to_bytes(25, "big")
    header, checksum = decoded_bytes[:-4], decoded_bytes[-4:]
    return checksum == sha256(None).digest()[:4]


def x__validate_old_btc_address__mutmut_25(addr: str):
    """Validate P2PKH and P2SH type address."""
    if len(addr) not in range(25, 35):
        return False
    decoded_bytes = _decode_base58(addr).to_bytes(25, "big")
    header, checksum = decoded_bytes[:-4], decoded_bytes[-4:]
    return checksum == sha256(sha256(None).digest()).digest()[:4]


def x__validate_old_btc_address__mutmut_26(addr: str):
    """Validate P2PKH and P2SH type address."""
    if len(addr) not in range(25, 35):
        return False
    decoded_bytes = _decode_base58(addr).to_bytes(25, "big")
    header, checksum = decoded_bytes[:-4], decoded_bytes[-4:]
    return checksum == sha256(sha256(header).digest()).digest()[:5]

x__validate_old_btc_address__mutmut_mutants : ClassVar[MutantDict] = {
'x__validate_old_btc_address__mutmut_1': x__validate_old_btc_address__mutmut_1, 
    'x__validate_old_btc_address__mutmut_2': x__validate_old_btc_address__mutmut_2, 
    'x__validate_old_btc_address__mutmut_3': x__validate_old_btc_address__mutmut_3, 
    'x__validate_old_btc_address__mutmut_4': x__validate_old_btc_address__mutmut_4, 
    'x__validate_old_btc_address__mutmut_5': x__validate_old_btc_address__mutmut_5, 
    'x__validate_old_btc_address__mutmut_6': x__validate_old_btc_address__mutmut_6, 
    'x__validate_old_btc_address__mutmut_7': x__validate_old_btc_address__mutmut_7, 
    'x__validate_old_btc_address__mutmut_8': x__validate_old_btc_address__mutmut_8, 
    'x__validate_old_btc_address__mutmut_9': x__validate_old_btc_address__mutmut_9, 
    'x__validate_old_btc_address__mutmut_10': x__validate_old_btc_address__mutmut_10, 
    'x__validate_old_btc_address__mutmut_11': x__validate_old_btc_address__mutmut_11, 
    'x__validate_old_btc_address__mutmut_12': x__validate_old_btc_address__mutmut_12, 
    'x__validate_old_btc_address__mutmut_13': x__validate_old_btc_address__mutmut_13, 
    'x__validate_old_btc_address__mutmut_14': x__validate_old_btc_address__mutmut_14, 
    'x__validate_old_btc_address__mutmut_15': x__validate_old_btc_address__mutmut_15, 
    'x__validate_old_btc_address__mutmut_16': x__validate_old_btc_address__mutmut_16, 
    'x__validate_old_btc_address__mutmut_17': x__validate_old_btc_address__mutmut_17, 
    'x__validate_old_btc_address__mutmut_18': x__validate_old_btc_address__mutmut_18, 
    'x__validate_old_btc_address__mutmut_19': x__validate_old_btc_address__mutmut_19, 
    'x__validate_old_btc_address__mutmut_20': x__validate_old_btc_address__mutmut_20, 
    'x__validate_old_btc_address__mutmut_21': x__validate_old_btc_address__mutmut_21, 
    'x__validate_old_btc_address__mutmut_22': x__validate_old_btc_address__mutmut_22, 
    'x__validate_old_btc_address__mutmut_23': x__validate_old_btc_address__mutmut_23, 
    'x__validate_old_btc_address__mutmut_24': x__validate_old_btc_address__mutmut_24, 
    'x__validate_old_btc_address__mutmut_25': x__validate_old_btc_address__mutmut_25, 
    'x__validate_old_btc_address__mutmut_26': x__validate_old_btc_address__mutmut_26
}

def _validate_old_btc_address(*args, **kwargs):
    result = _mutmut_trampoline(x__validate_old_btc_address__mutmut_orig, x__validate_old_btc_address__mutmut_mutants, args, kwargs)
    return result 

_validate_old_btc_address.__signature__ = _mutmut_signature(x__validate_old_btc_address__mutmut_orig)
x__validate_old_btc_address__mutmut_orig.__name__ = 'x__validate_old_btc_address'


@validator
def btc_address(value: str, /):
    """Return whether or not given value is a valid bitcoin address.

    Full validation is implemented for P2PKH and P2SH addresses.
    For segwit addresses a regexp is used to provide a reasonable
    estimate on whether the address is valid.

    Examples:
        >>> btc_address('3Cwgr2g7vsi1bXDUkpEnVoRLA9w4FZfC69')
        True
        >>> btc_address('1BvBMsEYstWetqTFn5Au4m4GFg7xJaNVN2')
        ValidationError(func=btc_address, args={'value': '1BvBMsEYstWetqTFn5Au4m4GFg7xJaNVN2'})

    Args:
        value:
            Bitcoin address string to validate.

    Returns:
        (Literal[True]): If `value` is a valid bitcoin address.
        (ValidationError): If `value` is an invalid bitcoin address.
    """
    if not value:
        return False

    return (
        # segwit pattern
        re.compile(r"^(bc|tc)[0-3][02-9ac-hj-np-z]{14,74}$").match(value)
        if value[:2] in ("bc", "tb")
        else _validate_old_btc_address(value)
    )
