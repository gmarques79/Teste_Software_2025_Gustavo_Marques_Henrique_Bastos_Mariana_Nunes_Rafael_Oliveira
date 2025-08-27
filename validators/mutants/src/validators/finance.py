"""Finance."""

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


def x__cusip_checksum__mutmut_orig(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_1(cusip: str):
    check, val = None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_2(cusip: str):
    check, val = 1, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_3(cusip: str):
    check, val = 0, None

    for idx in range(None):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_4(cusip: str):
    check, val = 0, None

    for idx in range(10):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_5(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = None
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_6(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" or c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_7(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c > "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_8(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "XX0XX" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_9(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c < "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_10(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "XX9XX":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_11(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = None
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_12(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) + ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_13(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(None) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_14(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord(None)
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_15(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("XX0XX")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_16(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" or c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_17(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c > "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_18(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "XXAXX" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_19(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "a" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_20(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c < "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_21(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "XXZXX":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_22(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_23(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = None
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_24(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) + ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_25(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 - ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_26(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 11 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_27(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(None) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_28(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord(None)
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_29(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("XXAXX")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_30(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("a")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_31(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" or c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_32(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c > "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_33(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "XXaXX" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_34(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "A" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_35(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c < "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_36(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "XXzXX":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_37(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "Z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_38(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = None
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_39(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) + ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_40(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 - ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_41(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 11 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_42(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(None) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_43(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord(None)
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_44(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("XXaXX")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_45(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("A")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_46(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c != "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_47(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "XX*XX":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_48(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = None
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_49(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 37
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_50(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c != "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_51(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "XX@XX":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_52(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = None
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_53(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 38
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_54(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c != "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_55(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "XX#XX":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_56(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = None
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_57(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 39
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_58(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return True

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_59(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx | 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_60(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 2:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_61(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val = val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_62(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val -= val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_63(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = None

    return (check % 10) == 0


def x__cusip_checksum__mutmut_64(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) - (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_65(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check - (val // 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_66(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val / 10) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_67(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 11) + (val % 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_68(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val / 10)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_69(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 11)

    return (check % 10) == 0


def x__cusip_checksum__mutmut_70(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check / 10) == 0


def x__cusip_checksum__mutmut_71(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 11) == 0


def x__cusip_checksum__mutmut_72(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) != 0


def x__cusip_checksum__mutmut_73(cusip: str):
    check, val = 0, None

    for idx in range(9):
        c = cusip[idx]
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        elif c == "*":
            val = 36
        elif c == "@":
            val = 37
        elif c == "#":
            val = 38
        else:
            return False

        if idx & 1:
            val += val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 1

x__cusip_checksum__mutmut_mutants : ClassVar[MutantDict] = {
'x__cusip_checksum__mutmut_1': x__cusip_checksum__mutmut_1, 
    'x__cusip_checksum__mutmut_2': x__cusip_checksum__mutmut_2, 
    'x__cusip_checksum__mutmut_3': x__cusip_checksum__mutmut_3, 
    'x__cusip_checksum__mutmut_4': x__cusip_checksum__mutmut_4, 
    'x__cusip_checksum__mutmut_5': x__cusip_checksum__mutmut_5, 
    'x__cusip_checksum__mutmut_6': x__cusip_checksum__mutmut_6, 
    'x__cusip_checksum__mutmut_7': x__cusip_checksum__mutmut_7, 
    'x__cusip_checksum__mutmut_8': x__cusip_checksum__mutmut_8, 
    'x__cusip_checksum__mutmut_9': x__cusip_checksum__mutmut_9, 
    'x__cusip_checksum__mutmut_10': x__cusip_checksum__mutmut_10, 
    'x__cusip_checksum__mutmut_11': x__cusip_checksum__mutmut_11, 
    'x__cusip_checksum__mutmut_12': x__cusip_checksum__mutmut_12, 
    'x__cusip_checksum__mutmut_13': x__cusip_checksum__mutmut_13, 
    'x__cusip_checksum__mutmut_14': x__cusip_checksum__mutmut_14, 
    'x__cusip_checksum__mutmut_15': x__cusip_checksum__mutmut_15, 
    'x__cusip_checksum__mutmut_16': x__cusip_checksum__mutmut_16, 
    'x__cusip_checksum__mutmut_17': x__cusip_checksum__mutmut_17, 
    'x__cusip_checksum__mutmut_18': x__cusip_checksum__mutmut_18, 
    'x__cusip_checksum__mutmut_19': x__cusip_checksum__mutmut_19, 
    'x__cusip_checksum__mutmut_20': x__cusip_checksum__mutmut_20, 
    'x__cusip_checksum__mutmut_21': x__cusip_checksum__mutmut_21, 
    'x__cusip_checksum__mutmut_22': x__cusip_checksum__mutmut_22, 
    'x__cusip_checksum__mutmut_23': x__cusip_checksum__mutmut_23, 
    'x__cusip_checksum__mutmut_24': x__cusip_checksum__mutmut_24, 
    'x__cusip_checksum__mutmut_25': x__cusip_checksum__mutmut_25, 
    'x__cusip_checksum__mutmut_26': x__cusip_checksum__mutmut_26, 
    'x__cusip_checksum__mutmut_27': x__cusip_checksum__mutmut_27, 
    'x__cusip_checksum__mutmut_28': x__cusip_checksum__mutmut_28, 
    'x__cusip_checksum__mutmut_29': x__cusip_checksum__mutmut_29, 
    'x__cusip_checksum__mutmut_30': x__cusip_checksum__mutmut_30, 
    'x__cusip_checksum__mutmut_31': x__cusip_checksum__mutmut_31, 
    'x__cusip_checksum__mutmut_32': x__cusip_checksum__mutmut_32, 
    'x__cusip_checksum__mutmut_33': x__cusip_checksum__mutmut_33, 
    'x__cusip_checksum__mutmut_34': x__cusip_checksum__mutmut_34, 
    'x__cusip_checksum__mutmut_35': x__cusip_checksum__mutmut_35, 
    'x__cusip_checksum__mutmut_36': x__cusip_checksum__mutmut_36, 
    'x__cusip_checksum__mutmut_37': x__cusip_checksum__mutmut_37, 
    'x__cusip_checksum__mutmut_38': x__cusip_checksum__mutmut_38, 
    'x__cusip_checksum__mutmut_39': x__cusip_checksum__mutmut_39, 
    'x__cusip_checksum__mutmut_40': x__cusip_checksum__mutmut_40, 
    'x__cusip_checksum__mutmut_41': x__cusip_checksum__mutmut_41, 
    'x__cusip_checksum__mutmut_42': x__cusip_checksum__mutmut_42, 
    'x__cusip_checksum__mutmut_43': x__cusip_checksum__mutmut_43, 
    'x__cusip_checksum__mutmut_44': x__cusip_checksum__mutmut_44, 
    'x__cusip_checksum__mutmut_45': x__cusip_checksum__mutmut_45, 
    'x__cusip_checksum__mutmut_46': x__cusip_checksum__mutmut_46, 
    'x__cusip_checksum__mutmut_47': x__cusip_checksum__mutmut_47, 
    'x__cusip_checksum__mutmut_48': x__cusip_checksum__mutmut_48, 
    'x__cusip_checksum__mutmut_49': x__cusip_checksum__mutmut_49, 
    'x__cusip_checksum__mutmut_50': x__cusip_checksum__mutmut_50, 
    'x__cusip_checksum__mutmut_51': x__cusip_checksum__mutmut_51, 
    'x__cusip_checksum__mutmut_52': x__cusip_checksum__mutmut_52, 
    'x__cusip_checksum__mutmut_53': x__cusip_checksum__mutmut_53, 
    'x__cusip_checksum__mutmut_54': x__cusip_checksum__mutmut_54, 
    'x__cusip_checksum__mutmut_55': x__cusip_checksum__mutmut_55, 
    'x__cusip_checksum__mutmut_56': x__cusip_checksum__mutmut_56, 
    'x__cusip_checksum__mutmut_57': x__cusip_checksum__mutmut_57, 
    'x__cusip_checksum__mutmut_58': x__cusip_checksum__mutmut_58, 
    'x__cusip_checksum__mutmut_59': x__cusip_checksum__mutmut_59, 
    'x__cusip_checksum__mutmut_60': x__cusip_checksum__mutmut_60, 
    'x__cusip_checksum__mutmut_61': x__cusip_checksum__mutmut_61, 
    'x__cusip_checksum__mutmut_62': x__cusip_checksum__mutmut_62, 
    'x__cusip_checksum__mutmut_63': x__cusip_checksum__mutmut_63, 
    'x__cusip_checksum__mutmut_64': x__cusip_checksum__mutmut_64, 
    'x__cusip_checksum__mutmut_65': x__cusip_checksum__mutmut_65, 
    'x__cusip_checksum__mutmut_66': x__cusip_checksum__mutmut_66, 
    'x__cusip_checksum__mutmut_67': x__cusip_checksum__mutmut_67, 
    'x__cusip_checksum__mutmut_68': x__cusip_checksum__mutmut_68, 
    'x__cusip_checksum__mutmut_69': x__cusip_checksum__mutmut_69, 
    'x__cusip_checksum__mutmut_70': x__cusip_checksum__mutmut_70, 
    'x__cusip_checksum__mutmut_71': x__cusip_checksum__mutmut_71, 
    'x__cusip_checksum__mutmut_72': x__cusip_checksum__mutmut_72, 
    'x__cusip_checksum__mutmut_73': x__cusip_checksum__mutmut_73
}

def _cusip_checksum(*args, **kwargs):
    result = _mutmut_trampoline(x__cusip_checksum__mutmut_orig, x__cusip_checksum__mutmut_mutants, args, kwargs)
    return result 

_cusip_checksum.__signature__ = _mutmut_signature(x__cusip_checksum__mutmut_orig)
x__cusip_checksum__mutmut_orig.__name__ = 'x__cusip_checksum'


def x__isin_checksum__mutmut_orig(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_1(value: str):
    check, val = None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_2(value: str):
    check, val = 1, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_3(value: str):
    check, val = 0, None

    for idx in range(None):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_4(value: str):
    check, val = 0, None

    for idx in range(13):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_5(value: str):
    check, val = 0, None

    for idx in range(12):
        c = None
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_6(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" or idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_7(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" or c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_8(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c > "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_9(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "XX0XX" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_10(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c < "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_11(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "XX9XX" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_12(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx >= 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_13(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 2:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_14(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = None
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_15(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) + ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_16(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(None) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_17(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord(None)
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_18(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("XX0XX")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_19(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" or c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_20(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c > "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_21(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "XXAXX" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_22(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "a" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_23(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c < "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_24(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "XXZXX":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_25(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_26(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = None
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_27(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) + ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_28(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 - ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_29(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 11 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_30(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(None) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_31(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord(None)
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_32(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("XXAXX")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_33(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("a")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_34(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" or c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_35(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c > "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_36(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "XXaXX" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_37(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "A" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_38(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c < "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_39(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "XXzXX":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_40(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "Z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_41(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = None
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_42(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) + ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_43(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 - ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_44(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 11 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_45(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(None) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_46(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord(None)
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_47(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("XXaXX")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_48(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("A")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_49(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return True

        if idx & 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_50(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx | 1:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_51(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 2:
            val += val

    return (check % 10) == 0


def x__isin_checksum__mutmut_52(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val = val

    return (check % 10) == 0


def x__isin_checksum__mutmut_53(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val -= val

    return (check % 10) == 0


def x__isin_checksum__mutmut_54(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check / 10) == 0


def x__isin_checksum__mutmut_55(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 11) == 0


def x__isin_checksum__mutmut_56(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) != 0


def x__isin_checksum__mutmut_57(value: str):
    check, val = 0, None

    for idx in range(12):
        c = value[idx]
        if c >= "0" and c <= "9" and idx > 1:
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        elif c >= "a" and c <= "z":
            val = 10 + ord(c) - ord("a")
        else:
            return False

        if idx & 1:
            val += val

    return (check % 10) == 1

x__isin_checksum__mutmut_mutants : ClassVar[MutantDict] = {
'x__isin_checksum__mutmut_1': x__isin_checksum__mutmut_1, 
    'x__isin_checksum__mutmut_2': x__isin_checksum__mutmut_2, 
    'x__isin_checksum__mutmut_3': x__isin_checksum__mutmut_3, 
    'x__isin_checksum__mutmut_4': x__isin_checksum__mutmut_4, 
    'x__isin_checksum__mutmut_5': x__isin_checksum__mutmut_5, 
    'x__isin_checksum__mutmut_6': x__isin_checksum__mutmut_6, 
    'x__isin_checksum__mutmut_7': x__isin_checksum__mutmut_7, 
    'x__isin_checksum__mutmut_8': x__isin_checksum__mutmut_8, 
    'x__isin_checksum__mutmut_9': x__isin_checksum__mutmut_9, 
    'x__isin_checksum__mutmut_10': x__isin_checksum__mutmut_10, 
    'x__isin_checksum__mutmut_11': x__isin_checksum__mutmut_11, 
    'x__isin_checksum__mutmut_12': x__isin_checksum__mutmut_12, 
    'x__isin_checksum__mutmut_13': x__isin_checksum__mutmut_13, 
    'x__isin_checksum__mutmut_14': x__isin_checksum__mutmut_14, 
    'x__isin_checksum__mutmut_15': x__isin_checksum__mutmut_15, 
    'x__isin_checksum__mutmut_16': x__isin_checksum__mutmut_16, 
    'x__isin_checksum__mutmut_17': x__isin_checksum__mutmut_17, 
    'x__isin_checksum__mutmut_18': x__isin_checksum__mutmut_18, 
    'x__isin_checksum__mutmut_19': x__isin_checksum__mutmut_19, 
    'x__isin_checksum__mutmut_20': x__isin_checksum__mutmut_20, 
    'x__isin_checksum__mutmut_21': x__isin_checksum__mutmut_21, 
    'x__isin_checksum__mutmut_22': x__isin_checksum__mutmut_22, 
    'x__isin_checksum__mutmut_23': x__isin_checksum__mutmut_23, 
    'x__isin_checksum__mutmut_24': x__isin_checksum__mutmut_24, 
    'x__isin_checksum__mutmut_25': x__isin_checksum__mutmut_25, 
    'x__isin_checksum__mutmut_26': x__isin_checksum__mutmut_26, 
    'x__isin_checksum__mutmut_27': x__isin_checksum__mutmut_27, 
    'x__isin_checksum__mutmut_28': x__isin_checksum__mutmut_28, 
    'x__isin_checksum__mutmut_29': x__isin_checksum__mutmut_29, 
    'x__isin_checksum__mutmut_30': x__isin_checksum__mutmut_30, 
    'x__isin_checksum__mutmut_31': x__isin_checksum__mutmut_31, 
    'x__isin_checksum__mutmut_32': x__isin_checksum__mutmut_32, 
    'x__isin_checksum__mutmut_33': x__isin_checksum__mutmut_33, 
    'x__isin_checksum__mutmut_34': x__isin_checksum__mutmut_34, 
    'x__isin_checksum__mutmut_35': x__isin_checksum__mutmut_35, 
    'x__isin_checksum__mutmut_36': x__isin_checksum__mutmut_36, 
    'x__isin_checksum__mutmut_37': x__isin_checksum__mutmut_37, 
    'x__isin_checksum__mutmut_38': x__isin_checksum__mutmut_38, 
    'x__isin_checksum__mutmut_39': x__isin_checksum__mutmut_39, 
    'x__isin_checksum__mutmut_40': x__isin_checksum__mutmut_40, 
    'x__isin_checksum__mutmut_41': x__isin_checksum__mutmut_41, 
    'x__isin_checksum__mutmut_42': x__isin_checksum__mutmut_42, 
    'x__isin_checksum__mutmut_43': x__isin_checksum__mutmut_43, 
    'x__isin_checksum__mutmut_44': x__isin_checksum__mutmut_44, 
    'x__isin_checksum__mutmut_45': x__isin_checksum__mutmut_45, 
    'x__isin_checksum__mutmut_46': x__isin_checksum__mutmut_46, 
    'x__isin_checksum__mutmut_47': x__isin_checksum__mutmut_47, 
    'x__isin_checksum__mutmut_48': x__isin_checksum__mutmut_48, 
    'x__isin_checksum__mutmut_49': x__isin_checksum__mutmut_49, 
    'x__isin_checksum__mutmut_50': x__isin_checksum__mutmut_50, 
    'x__isin_checksum__mutmut_51': x__isin_checksum__mutmut_51, 
    'x__isin_checksum__mutmut_52': x__isin_checksum__mutmut_52, 
    'x__isin_checksum__mutmut_53': x__isin_checksum__mutmut_53, 
    'x__isin_checksum__mutmut_54': x__isin_checksum__mutmut_54, 
    'x__isin_checksum__mutmut_55': x__isin_checksum__mutmut_55, 
    'x__isin_checksum__mutmut_56': x__isin_checksum__mutmut_56, 
    'x__isin_checksum__mutmut_57': x__isin_checksum__mutmut_57
}

def _isin_checksum(*args, **kwargs):
    result = _mutmut_trampoline(x__isin_checksum__mutmut_orig, x__isin_checksum__mutmut_mutants, args, kwargs)
    return result 

_isin_checksum.__signature__ = _mutmut_signature(x__isin_checksum__mutmut_orig)
x__isin_checksum__mutmut_orig.__name__ = 'x__isin_checksum'


@validator
def cusip(value: str):
    """Return whether or not given value is a valid CUSIP.

    Checks if the value is a valid [CUSIP][1].
    [1]: https://en.wikipedia.org/wiki/CUSIP

    Examples:
        >>> cusip('037833DP2')
        True
        >>> cusip('037833DP3')
        ValidationError(func=cusip, args={'value': '037833DP3'})

    Args:
        value: CUSIP string to validate.

    Returns:
        (Literal[True]): If `value` is a valid CUSIP string.
        (ValidationError): If `value` is an invalid CUSIP string.
    """
    return len(value) == 9 and _cusip_checksum(value)


@validator
def isin(value: str):
    """Return whether or not given value is a valid ISIN.

    Checks if the value is a valid [ISIN][1].
    [1]: https://en.wikipedia.org/wiki/International_Securities_Identification_Number

    Examples:
        >>> isin('037833DP2')
        ValidationError(func=isin, args={'value': '037833DP2'})
        >>> isin('037833DP3')
        ValidationError(func=isin, args={'value': '037833DP3'})

    Args:
        value: ISIN string to validate.

    Returns:
        (Literal[True]): If `value` is a valid ISIN string.
        (ValidationError): If `value` is an invalid ISIN string.
    """
    return len(value) == 12 and _isin_checksum(value)


@validator
def sedol(value: str):
    """Return whether or not given value is a valid SEDOL.

    Checks if the value is a valid [SEDOL][1].
    [1]: https://en.wikipedia.org/wiki/SEDOL

    Examples:
        >>> sedol('2936921')
        True
        >>> sedol('29A6922')
        ValidationError(func=sedol, args={'value': '29A6922'})

    Args:
        value: SEDOL string to validate.

    Returns:
        (Literal[True]): If `value` is a valid SEDOL string.
        (ValidationError): If `value` is an invalid SEDOL string.
    """
    if len(value) != 7:
        return False

    weights = [1, 3, 1, 7, 3, 9, 1]
    check = 0
    for idx in range(7):
        c = value[idx]
        if c in "AEIOU":
            return False

        val = None
        if c >= "0" and c <= "9":
            val = ord(c) - ord("0")
        elif c >= "A" and c <= "Z":
            val = 10 + ord(c) - ord("A")
        else:
            return False
        check += val * weights[idx]

    return (check % 10) == 0
