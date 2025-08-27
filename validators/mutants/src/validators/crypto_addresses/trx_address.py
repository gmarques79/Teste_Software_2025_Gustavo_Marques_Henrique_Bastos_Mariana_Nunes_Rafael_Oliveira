"""TRX Address."""

# standard
import hashlib
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


def x__base58_decode__mutmut_orig(addr: str) -> bytes:
    """Decode a base58 encoded address."""
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    num = 0
    for char in addr:
        num = num * 58 + alphabet.index(char)
    return num.to_bytes(25, byteorder="big")


def x__base58_decode__mutmut_1(addr: str) -> bytes:
    """Decode a base58 encoded address."""
    alphabet = None
    num = 0
    for char in addr:
        num = num * 58 + alphabet.index(char)
    return num.to_bytes(25, byteorder="big")


def x__base58_decode__mutmut_2(addr: str) -> bytes:
    """Decode a base58 encoded address."""
    alphabet = "XX123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyzXX"
    num = 0
    for char in addr:
        num = num * 58 + alphabet.index(char)
    return num.to_bytes(25, byteorder="big")


def x__base58_decode__mutmut_3(addr: str) -> bytes:
    """Decode a base58 encoded address."""
    alphabet = "123456789abcdefghjklmnpqrstuvwxyzabcdefghijkmnopqrstuvwxyz"
    num = 0
    for char in addr:
        num = num * 58 + alphabet.index(char)
    return num.to_bytes(25, byteorder="big")


def x__base58_decode__mutmut_4(addr: str) -> bytes:
    """Decode a base58 encoded address."""
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZABCDEFGHIJKMNOPQRSTUVWXYZ"
    num = 0
    for char in addr:
        num = num * 58 + alphabet.index(char)
    return num.to_bytes(25, byteorder="big")


def x__base58_decode__mutmut_5(addr: str) -> bytes:
    """Decode a base58 encoded address."""
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    num = None
    for char in addr:
        num = num * 58 + alphabet.index(char)
    return num.to_bytes(25, byteorder="big")


def x__base58_decode__mutmut_6(addr: str) -> bytes:
    """Decode a base58 encoded address."""
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    num = 1
    for char in addr:
        num = num * 58 + alphabet.index(char)
    return num.to_bytes(25, byteorder="big")


def x__base58_decode__mutmut_7(addr: str) -> bytes:
    """Decode a base58 encoded address."""
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    num = 0
    for char in addr:
        num = None
    return num.to_bytes(25, byteorder="big")


def x__base58_decode__mutmut_8(addr: str) -> bytes:
    """Decode a base58 encoded address."""
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    num = 0
    for char in addr:
        num = num * 58 - alphabet.index(char)
    return num.to_bytes(25, byteorder="big")


def x__base58_decode__mutmut_9(addr: str) -> bytes:
    """Decode a base58 encoded address."""
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    num = 0
    for char in addr:
        num = num / 58 + alphabet.index(char)
    return num.to_bytes(25, byteorder="big")


def x__base58_decode__mutmut_10(addr: str) -> bytes:
    """Decode a base58 encoded address."""
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    num = 0
    for char in addr:
        num = num * 59 + alphabet.index(char)
    return num.to_bytes(25, byteorder="big")


def x__base58_decode__mutmut_11(addr: str) -> bytes:
    """Decode a base58 encoded address."""
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    num = 0
    for char in addr:
        num = num * 58 + alphabet.index(None)
    return num.to_bytes(25, byteorder="big")


def x__base58_decode__mutmut_12(addr: str) -> bytes:
    """Decode a base58 encoded address."""
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    num = 0
    for char in addr:
        num = num * 58 + alphabet.rindex(char)
    return num.to_bytes(25, byteorder="big")


def x__base58_decode__mutmut_13(addr: str) -> bytes:
    """Decode a base58 encoded address."""
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    num = 0
    for char in addr:
        num = num * 58 + alphabet.index(char)
    return num.to_bytes(None, byteorder="big")


def x__base58_decode__mutmut_14(addr: str) -> bytes:
    """Decode a base58 encoded address."""
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    num = 0
    for char in addr:
        num = num * 58 + alphabet.index(char)
    return num.to_bytes(25, byteorder=None)


def x__base58_decode__mutmut_15(addr: str) -> bytes:
    """Decode a base58 encoded address."""
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    num = 0
    for char in addr:
        num = num * 58 + alphabet.index(char)
    return num.to_bytes(byteorder="big")


def x__base58_decode__mutmut_16(addr: str) -> bytes:
    """Decode a base58 encoded address."""
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    num = 0
    for char in addr:
        num = num * 58 + alphabet.index(char)
    return num.to_bytes(25, )


def x__base58_decode__mutmut_17(addr: str) -> bytes:
    """Decode a base58 encoded address."""
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    num = 0
    for char in addr:
        num = num * 58 + alphabet.index(char)
    return num.to_bytes(26, byteorder="big")


def x__base58_decode__mutmut_18(addr: str) -> bytes:
    """Decode a base58 encoded address."""
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    num = 0
    for char in addr:
        num = num * 58 + alphabet.index(char)
    return num.to_bytes(25, byteorder="XXbigXX")


def x__base58_decode__mutmut_19(addr: str) -> bytes:
    """Decode a base58 encoded address."""
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    num = 0
    for char in addr:
        num = num * 58 + alphabet.index(char)
    return num.to_bytes(25, byteorder="BIG")

x__base58_decode__mutmut_mutants : ClassVar[MutantDict] = {
'x__base58_decode__mutmut_1': x__base58_decode__mutmut_1, 
    'x__base58_decode__mutmut_2': x__base58_decode__mutmut_2, 
    'x__base58_decode__mutmut_3': x__base58_decode__mutmut_3, 
    'x__base58_decode__mutmut_4': x__base58_decode__mutmut_4, 
    'x__base58_decode__mutmut_5': x__base58_decode__mutmut_5, 
    'x__base58_decode__mutmut_6': x__base58_decode__mutmut_6, 
    'x__base58_decode__mutmut_7': x__base58_decode__mutmut_7, 
    'x__base58_decode__mutmut_8': x__base58_decode__mutmut_8, 
    'x__base58_decode__mutmut_9': x__base58_decode__mutmut_9, 
    'x__base58_decode__mutmut_10': x__base58_decode__mutmut_10, 
    'x__base58_decode__mutmut_11': x__base58_decode__mutmut_11, 
    'x__base58_decode__mutmut_12': x__base58_decode__mutmut_12, 
    'x__base58_decode__mutmut_13': x__base58_decode__mutmut_13, 
    'x__base58_decode__mutmut_14': x__base58_decode__mutmut_14, 
    'x__base58_decode__mutmut_15': x__base58_decode__mutmut_15, 
    'x__base58_decode__mutmut_16': x__base58_decode__mutmut_16, 
    'x__base58_decode__mutmut_17': x__base58_decode__mutmut_17, 
    'x__base58_decode__mutmut_18': x__base58_decode__mutmut_18, 
    'x__base58_decode__mutmut_19': x__base58_decode__mutmut_19
}

def _base58_decode(*args, **kwargs):
    result = _mutmut_trampoline(x__base58_decode__mutmut_orig, x__base58_decode__mutmut_mutants, args, kwargs)
    return result 

_base58_decode.__signature__ = _mutmut_signature(x__base58_decode__mutmut_orig)
x__base58_decode__mutmut_orig.__name__ = 'x__base58_decode'


def x__validate_trx_checksum_address__mutmut_orig(addr: str) -> bool:
    """Validate TRX type checksum address."""
    if len(addr) != 34:
        return False

    try:
        address = _base58_decode(addr)
    except ValueError:
        return False

    if len(address) != 25 or address[0] != 0x41:
        return False

    check_sum = hashlib.sha256(hashlib.sha256(address[:-4]).digest()).digest()[:4]
    return address[-4:] == check_sum


def x__validate_trx_checksum_address__mutmut_1(addr: str) -> bool:
    """Validate TRX type checksum address."""
    if len(addr) == 34:
        return False

    try:
        address = _base58_decode(addr)
    except ValueError:
        return False

    if len(address) != 25 or address[0] != 0x41:
        return False

    check_sum = hashlib.sha256(hashlib.sha256(address[:-4]).digest()).digest()[:4]
    return address[-4:] == check_sum


def x__validate_trx_checksum_address__mutmut_2(addr: str) -> bool:
    """Validate TRX type checksum address."""
    if len(addr) != 35:
        return False

    try:
        address = _base58_decode(addr)
    except ValueError:
        return False

    if len(address) != 25 or address[0] != 0x41:
        return False

    check_sum = hashlib.sha256(hashlib.sha256(address[:-4]).digest()).digest()[:4]
    return address[-4:] == check_sum


def x__validate_trx_checksum_address__mutmut_3(addr: str) -> bool:
    """Validate TRX type checksum address."""
    if len(addr) != 34:
        return True

    try:
        address = _base58_decode(addr)
    except ValueError:
        return False

    if len(address) != 25 or address[0] != 0x41:
        return False

    check_sum = hashlib.sha256(hashlib.sha256(address[:-4]).digest()).digest()[:4]
    return address[-4:] == check_sum


def x__validate_trx_checksum_address__mutmut_4(addr: str) -> bool:
    """Validate TRX type checksum address."""
    if len(addr) != 34:
        return False

    try:
        address = None
    except ValueError:
        return False

    if len(address) != 25 or address[0] != 0x41:
        return False

    check_sum = hashlib.sha256(hashlib.sha256(address[:-4]).digest()).digest()[:4]
    return address[-4:] == check_sum


def x__validate_trx_checksum_address__mutmut_5(addr: str) -> bool:
    """Validate TRX type checksum address."""
    if len(addr) != 34:
        return False

    try:
        address = _base58_decode(None)
    except ValueError:
        return False

    if len(address) != 25 or address[0] != 0x41:
        return False

    check_sum = hashlib.sha256(hashlib.sha256(address[:-4]).digest()).digest()[:4]
    return address[-4:] == check_sum


def x__validate_trx_checksum_address__mutmut_6(addr: str) -> bool:
    """Validate TRX type checksum address."""
    if len(addr) != 34:
        return False

    try:
        address = _base58_decode(addr)
    except ValueError:
        return True

    if len(address) != 25 or address[0] != 0x41:
        return False

    check_sum = hashlib.sha256(hashlib.sha256(address[:-4]).digest()).digest()[:4]
    return address[-4:] == check_sum


def x__validate_trx_checksum_address__mutmut_7(addr: str) -> bool:
    """Validate TRX type checksum address."""
    if len(addr) != 34:
        return False

    try:
        address = _base58_decode(addr)
    except ValueError:
        return False

    if len(address) != 25 and address[0] != 0x41:
        return False

    check_sum = hashlib.sha256(hashlib.sha256(address[:-4]).digest()).digest()[:4]
    return address[-4:] == check_sum


def x__validate_trx_checksum_address__mutmut_8(addr: str) -> bool:
    """Validate TRX type checksum address."""
    if len(addr) != 34:
        return False

    try:
        address = _base58_decode(addr)
    except ValueError:
        return False

    if len(address) == 25 or address[0] != 0x41:
        return False

    check_sum = hashlib.sha256(hashlib.sha256(address[:-4]).digest()).digest()[:4]
    return address[-4:] == check_sum


def x__validate_trx_checksum_address__mutmut_9(addr: str) -> bool:
    """Validate TRX type checksum address."""
    if len(addr) != 34:
        return False

    try:
        address = _base58_decode(addr)
    except ValueError:
        return False

    if len(address) != 26 or address[0] != 0x41:
        return False

    check_sum = hashlib.sha256(hashlib.sha256(address[:-4]).digest()).digest()[:4]
    return address[-4:] == check_sum


def x__validate_trx_checksum_address__mutmut_10(addr: str) -> bool:
    """Validate TRX type checksum address."""
    if len(addr) != 34:
        return False

    try:
        address = _base58_decode(addr)
    except ValueError:
        return False

    if len(address) != 25 or address[1] != 0x41:
        return False

    check_sum = hashlib.sha256(hashlib.sha256(address[:-4]).digest()).digest()[:4]
    return address[-4:] == check_sum


def x__validate_trx_checksum_address__mutmut_11(addr: str) -> bool:
    """Validate TRX type checksum address."""
    if len(addr) != 34:
        return False

    try:
        address = _base58_decode(addr)
    except ValueError:
        return False

    if len(address) != 25 or address[0] == 0x41:
        return False

    check_sum = hashlib.sha256(hashlib.sha256(address[:-4]).digest()).digest()[:4]
    return address[-4:] == check_sum


def x__validate_trx_checksum_address__mutmut_12(addr: str) -> bool:
    """Validate TRX type checksum address."""
    if len(addr) != 34:
        return False

    try:
        address = _base58_decode(addr)
    except ValueError:
        return False

    if len(address) != 25 or address[0] != 66:
        return False

    check_sum = hashlib.sha256(hashlib.sha256(address[:-4]).digest()).digest()[:4]
    return address[-4:] == check_sum


def x__validate_trx_checksum_address__mutmut_13(addr: str) -> bool:
    """Validate TRX type checksum address."""
    if len(addr) != 34:
        return False

    try:
        address = _base58_decode(addr)
    except ValueError:
        return False

    if len(address) != 25 or address[0] != 0x41:
        return True

    check_sum = hashlib.sha256(hashlib.sha256(address[:-4]).digest()).digest()[:4]
    return address[-4:] == check_sum


def x__validate_trx_checksum_address__mutmut_14(addr: str) -> bool:
    """Validate TRX type checksum address."""
    if len(addr) != 34:
        return False

    try:
        address = _base58_decode(addr)
    except ValueError:
        return False

    if len(address) != 25 or address[0] != 0x41:
        return False

    check_sum = None
    return address[-4:] == check_sum


def x__validate_trx_checksum_address__mutmut_15(addr: str) -> bool:
    """Validate TRX type checksum address."""
    if len(addr) != 34:
        return False

    try:
        address = _base58_decode(addr)
    except ValueError:
        return False

    if len(address) != 25 or address[0] != 0x41:
        return False

    check_sum = hashlib.sha256(None).digest()[:4]
    return address[-4:] == check_sum


def x__validate_trx_checksum_address__mutmut_16(addr: str) -> bool:
    """Validate TRX type checksum address."""
    if len(addr) != 34:
        return False

    try:
        address = _base58_decode(addr)
    except ValueError:
        return False

    if len(address) != 25 or address[0] != 0x41:
        return False

    check_sum = hashlib.sha256(hashlib.sha256(None).digest()).digest()[:4]
    return address[-4:] == check_sum


def x__validate_trx_checksum_address__mutmut_17(addr: str) -> bool:
    """Validate TRX type checksum address."""
    if len(addr) != 34:
        return False

    try:
        address = _base58_decode(addr)
    except ValueError:
        return False

    if len(address) != 25 or address[0] != 0x41:
        return False

    check_sum = hashlib.sha256(hashlib.sha256(address[:+4]).digest()).digest()[:4]
    return address[-4:] == check_sum


def x__validate_trx_checksum_address__mutmut_18(addr: str) -> bool:
    """Validate TRX type checksum address."""
    if len(addr) != 34:
        return False

    try:
        address = _base58_decode(addr)
    except ValueError:
        return False

    if len(address) != 25 or address[0] != 0x41:
        return False

    check_sum = hashlib.sha256(hashlib.sha256(address[:-5]).digest()).digest()[:4]
    return address[-4:] == check_sum


def x__validate_trx_checksum_address__mutmut_19(addr: str) -> bool:
    """Validate TRX type checksum address."""
    if len(addr) != 34:
        return False

    try:
        address = _base58_decode(addr)
    except ValueError:
        return False

    if len(address) != 25 or address[0] != 0x41:
        return False

    check_sum = hashlib.sha256(hashlib.sha256(address[:-4]).digest()).digest()[:5]
    return address[-4:] == check_sum


def x__validate_trx_checksum_address__mutmut_20(addr: str) -> bool:
    """Validate TRX type checksum address."""
    if len(addr) != 34:
        return False

    try:
        address = _base58_decode(addr)
    except ValueError:
        return False

    if len(address) != 25 or address[0] != 0x41:
        return False

    check_sum = hashlib.sha256(hashlib.sha256(address[:-4]).digest()).digest()[:4]
    return address[+4:] == check_sum


def x__validate_trx_checksum_address__mutmut_21(addr: str) -> bool:
    """Validate TRX type checksum address."""
    if len(addr) != 34:
        return False

    try:
        address = _base58_decode(addr)
    except ValueError:
        return False

    if len(address) != 25 or address[0] != 0x41:
        return False

    check_sum = hashlib.sha256(hashlib.sha256(address[:-4]).digest()).digest()[:4]
    return address[-5:] == check_sum


def x__validate_trx_checksum_address__mutmut_22(addr: str) -> bool:
    """Validate TRX type checksum address."""
    if len(addr) != 34:
        return False

    try:
        address = _base58_decode(addr)
    except ValueError:
        return False

    if len(address) != 25 or address[0] != 0x41:
        return False

    check_sum = hashlib.sha256(hashlib.sha256(address[:-4]).digest()).digest()[:4]
    return address[-4:] != check_sum

x__validate_trx_checksum_address__mutmut_mutants : ClassVar[MutantDict] = {
'x__validate_trx_checksum_address__mutmut_1': x__validate_trx_checksum_address__mutmut_1, 
    'x__validate_trx_checksum_address__mutmut_2': x__validate_trx_checksum_address__mutmut_2, 
    'x__validate_trx_checksum_address__mutmut_3': x__validate_trx_checksum_address__mutmut_3, 
    'x__validate_trx_checksum_address__mutmut_4': x__validate_trx_checksum_address__mutmut_4, 
    'x__validate_trx_checksum_address__mutmut_5': x__validate_trx_checksum_address__mutmut_5, 
    'x__validate_trx_checksum_address__mutmut_6': x__validate_trx_checksum_address__mutmut_6, 
    'x__validate_trx_checksum_address__mutmut_7': x__validate_trx_checksum_address__mutmut_7, 
    'x__validate_trx_checksum_address__mutmut_8': x__validate_trx_checksum_address__mutmut_8, 
    'x__validate_trx_checksum_address__mutmut_9': x__validate_trx_checksum_address__mutmut_9, 
    'x__validate_trx_checksum_address__mutmut_10': x__validate_trx_checksum_address__mutmut_10, 
    'x__validate_trx_checksum_address__mutmut_11': x__validate_trx_checksum_address__mutmut_11, 
    'x__validate_trx_checksum_address__mutmut_12': x__validate_trx_checksum_address__mutmut_12, 
    'x__validate_trx_checksum_address__mutmut_13': x__validate_trx_checksum_address__mutmut_13, 
    'x__validate_trx_checksum_address__mutmut_14': x__validate_trx_checksum_address__mutmut_14, 
    'x__validate_trx_checksum_address__mutmut_15': x__validate_trx_checksum_address__mutmut_15, 
    'x__validate_trx_checksum_address__mutmut_16': x__validate_trx_checksum_address__mutmut_16, 
    'x__validate_trx_checksum_address__mutmut_17': x__validate_trx_checksum_address__mutmut_17, 
    'x__validate_trx_checksum_address__mutmut_18': x__validate_trx_checksum_address__mutmut_18, 
    'x__validate_trx_checksum_address__mutmut_19': x__validate_trx_checksum_address__mutmut_19, 
    'x__validate_trx_checksum_address__mutmut_20': x__validate_trx_checksum_address__mutmut_20, 
    'x__validate_trx_checksum_address__mutmut_21': x__validate_trx_checksum_address__mutmut_21, 
    'x__validate_trx_checksum_address__mutmut_22': x__validate_trx_checksum_address__mutmut_22
}

def _validate_trx_checksum_address(*args, **kwargs):
    result = _mutmut_trampoline(x__validate_trx_checksum_address__mutmut_orig, x__validate_trx_checksum_address__mutmut_mutants, args, kwargs)
    return result 

_validate_trx_checksum_address.__signature__ = _mutmut_signature(x__validate_trx_checksum_address__mutmut_orig)
x__validate_trx_checksum_address__mutmut_orig.__name__ = 'x__validate_trx_checksum_address'


@validator
def trx_address(value: str, /):
    """Return whether or not given value is a valid tron address.

    Full validation is implemented for TRC20 tron addresses.

    Examples:
        >>> trx_address('TLjfbTbpZYDQ4EoA4N5CLNgGjfbF8ZWz38')
        True
        >>> trx_address('TR2G7Rm4vFqF8EpY4U5xdLdQ7XgJ2U8Vd')
        ValidationError(func=trx_address, args={'value': 'TR2G7Rm4vFqF8EpY4U5xdLdQ7XgJ2U8Vd'})

    Args:
        value:
            Tron address string to validate.

    Returns:
        (Literal[True]): If `value` is a valid tron address.
        (ValidationError): If `value` is an invalid tron address.
    """
    if not value:
        return False

    return re.compile(r"^[T][a-km-zA-HJ-NP-Z1-9]{33}$").match(
        value
    ) and _validate_trx_checksum_address(value)
