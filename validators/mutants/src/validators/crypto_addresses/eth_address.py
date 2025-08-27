"""ETH Address."""

# standard
import re

# local
from validators.utils import validator

_keccak_flag = True
try:
    # external
    from eth_hash.auto import keccak
except ImportError:
    _keccak_flag = False
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


def x__validate_eth_checksum_address__mutmut_orig(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "")
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, 40):
        if (int(addr_hash[i], 16) > 7 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], 16) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_1(addr: str):
    """Validate ETH type checksum address."""
    addr = None
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, 40):
        if (int(addr_hash[i], 16) > 7 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], 16) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_2(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace(None, "")
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, 40):
        if (int(addr_hash[i], 16) > 7 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], 16) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_3(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", None)
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, 40):
        if (int(addr_hash[i], 16) > 7 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], 16) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_4(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("")
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, 40):
        if (int(addr_hash[i], 16) > 7 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], 16) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_5(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", )
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, 40):
        if (int(addr_hash[i], 16) > 7 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], 16) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_6(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("XX0xXX", "")
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, 40):
        if (int(addr_hash[i], 16) > 7 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], 16) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_7(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0X", "")
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, 40):
        if (int(addr_hash[i], 16) > 7 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], 16) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_8(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "XXXX")
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, 40):
        if (int(addr_hash[i], 16) > 7 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], 16) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_9(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "")
    addr_hash = None  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, 40):
        if (int(addr_hash[i], 16) > 7 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], 16) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_10(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "")
    addr_hash = keccak.new(None).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, 40):
        if (int(addr_hash[i], 16) > 7 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], 16) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_11(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "")
    addr_hash = keccak.new(addr.lower().encode(None)).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, 40):
        if (int(addr_hash[i], 16) > 7 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], 16) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_12(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "")
    addr_hash = keccak.new(addr.upper().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, 40):
        if (int(addr_hash[i], 16) > 7 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], 16) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_13(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "")
    addr_hash = keccak.new(addr.lower().encode("XXasciiXX")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, 40):
        if (int(addr_hash[i], 16) > 7 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], 16) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_14(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "")
    addr_hash = keccak.new(addr.lower().encode("ASCII")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, 40):
        if (int(addr_hash[i], 16) > 7 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], 16) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_15(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "")
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) == 40:
        return False

    for i in range(0, 40):
        if (int(addr_hash[i], 16) > 7 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], 16) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_16(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "")
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 41:
        return False

    for i in range(0, 40):
        if (int(addr_hash[i], 16) > 7 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], 16) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_17(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "")
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return True

    for i in range(0, 40):
        if (int(addr_hash[i], 16) > 7 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], 16) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_18(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "")
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(None, 40):
        if (int(addr_hash[i], 16) > 7 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], 16) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_19(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "")
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, None):
        if (int(addr_hash[i], 16) > 7 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], 16) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_20(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "")
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(40):
        if (int(addr_hash[i], 16) > 7 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], 16) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_21(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "")
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, ):
        if (int(addr_hash[i], 16) > 7 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], 16) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_22(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "")
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(1, 40):
        if (int(addr_hash[i], 16) > 7 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], 16) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_23(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "")
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, 41):
        if (int(addr_hash[i], 16) > 7 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], 16) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_24(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "")
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, 40):
        if (int(addr_hash[i], 16) > 7 and addr[i].upper() != addr[i]) and (
            int(addr_hash[i], 16) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_25(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "")
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, 40):
        if (int(addr_hash[i], 16) > 7 or addr[i].upper() != addr[i]) or (
            int(addr_hash[i], 16) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_26(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "")
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, 40):
        if (int(None, 16) > 7 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], 16) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_27(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "")
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, 40):
        if (int(addr_hash[i], None) > 7 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], 16) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_28(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "")
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, 40):
        if (int(16) > 7 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], 16) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_29(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "")
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, 40):
        if (int(addr_hash[i], ) > 7 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], 16) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_30(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "")
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, 40):
        if (int(addr_hash[i], 17) > 7 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], 16) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_31(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "")
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, 40):
        if (int(addr_hash[i], 16) >= 7 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], 16) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_32(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "")
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, 40):
        if (int(addr_hash[i], 16) > 8 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], 16) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_33(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "")
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, 40):
        if (int(addr_hash[i], 16) > 7 and addr[i].lower() != addr[i]) or (
            int(addr_hash[i], 16) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_34(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "")
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, 40):
        if (int(addr_hash[i], 16) > 7 and addr[i].upper() == addr[i]) or (
            int(addr_hash[i], 16) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_35(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "")
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, 40):
        if (int(addr_hash[i], 16) > 7 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], 16) <= 7 or addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_36(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "")
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, 40):
        if (int(addr_hash[i], 16) > 7 and addr[i].upper() != addr[i]) or (
            int(None, 16) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_37(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "")
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, 40):
        if (int(addr_hash[i], 16) > 7 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], None) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_38(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "")
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, 40):
        if (int(addr_hash[i], 16) > 7 and addr[i].upper() != addr[i]) or (
            int(16) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_39(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "")
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, 40):
        if (int(addr_hash[i], 16) > 7 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], ) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_40(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "")
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, 40):
        if (int(addr_hash[i], 16) > 7 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], 17) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_41(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "")
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, 40):
        if (int(addr_hash[i], 16) > 7 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], 16) < 7 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_42(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "")
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, 40):
        if (int(addr_hash[i], 16) > 7 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], 16) <= 8 and addr[i].lower() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_43(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "")
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, 40):
        if (int(addr_hash[i], 16) > 7 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], 16) <= 7 and addr[i].upper() != addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_44(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "")
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, 40):
        if (int(addr_hash[i], 16) > 7 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], 16) <= 7 and addr[i].lower() == addr[i]
        ):
            return False
    return True


def x__validate_eth_checksum_address__mutmut_45(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "")
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, 40):
        if (int(addr_hash[i], 16) > 7 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], 16) <= 7 and addr[i].lower() != addr[i]
        ):
            return True
    return True


def x__validate_eth_checksum_address__mutmut_46(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "")
    addr_hash = keccak.new(addr.lower().encode("ascii")).digest().hex()  # type: ignore

    if len(addr) != 40:
        return False

    for i in range(0, 40):
        if (int(addr_hash[i], 16) > 7 and addr[i].upper() != addr[i]) or (
            int(addr_hash[i], 16) <= 7 and addr[i].lower() != addr[i]
        ):
            return False
    return False

x__validate_eth_checksum_address__mutmut_mutants : ClassVar[MutantDict] = {
'x__validate_eth_checksum_address__mutmut_1': x__validate_eth_checksum_address__mutmut_1, 
    'x__validate_eth_checksum_address__mutmut_2': x__validate_eth_checksum_address__mutmut_2, 
    'x__validate_eth_checksum_address__mutmut_3': x__validate_eth_checksum_address__mutmut_3, 
    'x__validate_eth_checksum_address__mutmut_4': x__validate_eth_checksum_address__mutmut_4, 
    'x__validate_eth_checksum_address__mutmut_5': x__validate_eth_checksum_address__mutmut_5, 
    'x__validate_eth_checksum_address__mutmut_6': x__validate_eth_checksum_address__mutmut_6, 
    'x__validate_eth_checksum_address__mutmut_7': x__validate_eth_checksum_address__mutmut_7, 
    'x__validate_eth_checksum_address__mutmut_8': x__validate_eth_checksum_address__mutmut_8, 
    'x__validate_eth_checksum_address__mutmut_9': x__validate_eth_checksum_address__mutmut_9, 
    'x__validate_eth_checksum_address__mutmut_10': x__validate_eth_checksum_address__mutmut_10, 
    'x__validate_eth_checksum_address__mutmut_11': x__validate_eth_checksum_address__mutmut_11, 
    'x__validate_eth_checksum_address__mutmut_12': x__validate_eth_checksum_address__mutmut_12, 
    'x__validate_eth_checksum_address__mutmut_13': x__validate_eth_checksum_address__mutmut_13, 
    'x__validate_eth_checksum_address__mutmut_14': x__validate_eth_checksum_address__mutmut_14, 
    'x__validate_eth_checksum_address__mutmut_15': x__validate_eth_checksum_address__mutmut_15, 
    'x__validate_eth_checksum_address__mutmut_16': x__validate_eth_checksum_address__mutmut_16, 
    'x__validate_eth_checksum_address__mutmut_17': x__validate_eth_checksum_address__mutmut_17, 
    'x__validate_eth_checksum_address__mutmut_18': x__validate_eth_checksum_address__mutmut_18, 
    'x__validate_eth_checksum_address__mutmut_19': x__validate_eth_checksum_address__mutmut_19, 
    'x__validate_eth_checksum_address__mutmut_20': x__validate_eth_checksum_address__mutmut_20, 
    'x__validate_eth_checksum_address__mutmut_21': x__validate_eth_checksum_address__mutmut_21, 
    'x__validate_eth_checksum_address__mutmut_22': x__validate_eth_checksum_address__mutmut_22, 
    'x__validate_eth_checksum_address__mutmut_23': x__validate_eth_checksum_address__mutmut_23, 
    'x__validate_eth_checksum_address__mutmut_24': x__validate_eth_checksum_address__mutmut_24, 
    'x__validate_eth_checksum_address__mutmut_25': x__validate_eth_checksum_address__mutmut_25, 
    'x__validate_eth_checksum_address__mutmut_26': x__validate_eth_checksum_address__mutmut_26, 
    'x__validate_eth_checksum_address__mutmut_27': x__validate_eth_checksum_address__mutmut_27, 
    'x__validate_eth_checksum_address__mutmut_28': x__validate_eth_checksum_address__mutmut_28, 
    'x__validate_eth_checksum_address__mutmut_29': x__validate_eth_checksum_address__mutmut_29, 
    'x__validate_eth_checksum_address__mutmut_30': x__validate_eth_checksum_address__mutmut_30, 
    'x__validate_eth_checksum_address__mutmut_31': x__validate_eth_checksum_address__mutmut_31, 
    'x__validate_eth_checksum_address__mutmut_32': x__validate_eth_checksum_address__mutmut_32, 
    'x__validate_eth_checksum_address__mutmut_33': x__validate_eth_checksum_address__mutmut_33, 
    'x__validate_eth_checksum_address__mutmut_34': x__validate_eth_checksum_address__mutmut_34, 
    'x__validate_eth_checksum_address__mutmut_35': x__validate_eth_checksum_address__mutmut_35, 
    'x__validate_eth_checksum_address__mutmut_36': x__validate_eth_checksum_address__mutmut_36, 
    'x__validate_eth_checksum_address__mutmut_37': x__validate_eth_checksum_address__mutmut_37, 
    'x__validate_eth_checksum_address__mutmut_38': x__validate_eth_checksum_address__mutmut_38, 
    'x__validate_eth_checksum_address__mutmut_39': x__validate_eth_checksum_address__mutmut_39, 
    'x__validate_eth_checksum_address__mutmut_40': x__validate_eth_checksum_address__mutmut_40, 
    'x__validate_eth_checksum_address__mutmut_41': x__validate_eth_checksum_address__mutmut_41, 
    'x__validate_eth_checksum_address__mutmut_42': x__validate_eth_checksum_address__mutmut_42, 
    'x__validate_eth_checksum_address__mutmut_43': x__validate_eth_checksum_address__mutmut_43, 
    'x__validate_eth_checksum_address__mutmut_44': x__validate_eth_checksum_address__mutmut_44, 
    'x__validate_eth_checksum_address__mutmut_45': x__validate_eth_checksum_address__mutmut_45, 
    'x__validate_eth_checksum_address__mutmut_46': x__validate_eth_checksum_address__mutmut_46
}

def _validate_eth_checksum_address(*args, **kwargs):
    result = _mutmut_trampoline(x__validate_eth_checksum_address__mutmut_orig, x__validate_eth_checksum_address__mutmut_mutants, args, kwargs)
    return result 

_validate_eth_checksum_address.__signature__ = _mutmut_signature(x__validate_eth_checksum_address__mutmut_orig)
x__validate_eth_checksum_address__mutmut_orig.__name__ = 'x__validate_eth_checksum_address'


@validator
def eth_address(value: str, /):
    """Return whether or not given value is a valid ethereum address.

    Full validation is implemented for ERC20 addresses.

    Examples:
        >>> eth_address('0x9cc14ba4f9f68ca159ea4ebf2c292a808aaeb598')
        True
        >>> eth_address('0x8Ba1f109551bD432803012645Ac136ddd64DBa72')
        ValidationError(func=eth_address, args={'value': '0x8Ba1f109551bD432803012645Ac136ddd64DBa72'})

    Args:
        value:
            Ethereum address string to validate.

    Returns:
        (Literal[True]): If `value` is a valid ethereum address.
        (ValidationError): If `value` is an invalid ethereum address.
    """  # noqa: E501
    if not _keccak_flag:
        raise ImportError(
            "Do `pip install validators[crypto-eth-addresses]` to perform `eth_address` validation."
        )

    if not value:
        return False

    return re.compile(r"^0x[0-9a-f]{40}$|^0x[0-9A-F]{40}$").match(
        value
    ) or _validate_eth_checksum_address(value)
