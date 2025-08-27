"""Cron."""

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


def x__validate_cron_component__mutmut_orig(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_1(component: str, min_val: int, max_val: int):
    if component != "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_2(component: str, min_val: int, max_val: int):
    if component == "XX*XX":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_3(component: str, min_val: int, max_val: int):
    if component == "*":
        return False

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_4(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val < int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_5(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(None) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_6(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) < max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_7(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "XX/XX" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_8(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" not in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_9(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = None
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_10(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split(None)
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_11(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("XX/XX")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_12(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() and int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_13(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 and not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_14(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) == 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_15(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 3 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_16(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_17(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[2].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_18(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(None) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_19(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[2]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_20(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) <= 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_21(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 2:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_22(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return True
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_23(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[1] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_24(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] != "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_25(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "XX*XX":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_26(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return False
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_27(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() or min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_28(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[1].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_29(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val < int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_30(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(None) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_31(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[1]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_32(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) < max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_33(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "XX-XX" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_34(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" not in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_35(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = None
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_36(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split(None)
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_37(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("XX-XX")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_38(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() and not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_39(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 and not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_40(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) == 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_41(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 3 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_42(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_43(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[1].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_44(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_45(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[2].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_46(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return True
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_47(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = None
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_48(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(None), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_49(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[1]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_50(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(None)
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_51(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[2])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_52(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val or start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_53(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val or min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_54(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val < start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_55(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start < max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_56(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val < end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_57(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end < max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_58(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start < end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_59(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "XX,XX" in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_60(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," not in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_61(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(None):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_62(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split("XX,XX"):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_63(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_64(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(None, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_65(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, None, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_66(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, None):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_67(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_68(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_69(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, ):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_70(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return True
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_71(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return False
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return False


def x__validate_cron_component__mutmut_72(component: str, min_val: int, max_val: int):
    if component == "*":
        return True

    if component.isdecimal():
        return min_val <= int(component) <= max_val

    if "/" in component:
        parts = component.split("/")
        if len(parts) != 2 or not parts[1].isdecimal() or int(parts[1]) < 1:
            return False
        if parts[0] == "*":
            return True
        return parts[0].isdecimal() and min_val <= int(parts[0]) <= max_val

    if "-" in component:
        parts = component.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if "," in component:
        for item in component.split(","):
            if not _validate_cron_component(item, min_val, max_val):
                return False
        return True
        # return all(
        #   _validate_cron_component(item, min_val, max_val) for item in component.split(",")
        # ) # throws type error. why?

    return True

x__validate_cron_component__mutmut_mutants : ClassVar[MutantDict] = {
'x__validate_cron_component__mutmut_1': x__validate_cron_component__mutmut_1, 
    'x__validate_cron_component__mutmut_2': x__validate_cron_component__mutmut_2, 
    'x__validate_cron_component__mutmut_3': x__validate_cron_component__mutmut_3, 
    'x__validate_cron_component__mutmut_4': x__validate_cron_component__mutmut_4, 
    'x__validate_cron_component__mutmut_5': x__validate_cron_component__mutmut_5, 
    'x__validate_cron_component__mutmut_6': x__validate_cron_component__mutmut_6, 
    'x__validate_cron_component__mutmut_7': x__validate_cron_component__mutmut_7, 
    'x__validate_cron_component__mutmut_8': x__validate_cron_component__mutmut_8, 
    'x__validate_cron_component__mutmut_9': x__validate_cron_component__mutmut_9, 
    'x__validate_cron_component__mutmut_10': x__validate_cron_component__mutmut_10, 
    'x__validate_cron_component__mutmut_11': x__validate_cron_component__mutmut_11, 
    'x__validate_cron_component__mutmut_12': x__validate_cron_component__mutmut_12, 
    'x__validate_cron_component__mutmut_13': x__validate_cron_component__mutmut_13, 
    'x__validate_cron_component__mutmut_14': x__validate_cron_component__mutmut_14, 
    'x__validate_cron_component__mutmut_15': x__validate_cron_component__mutmut_15, 
    'x__validate_cron_component__mutmut_16': x__validate_cron_component__mutmut_16, 
    'x__validate_cron_component__mutmut_17': x__validate_cron_component__mutmut_17, 
    'x__validate_cron_component__mutmut_18': x__validate_cron_component__mutmut_18, 
    'x__validate_cron_component__mutmut_19': x__validate_cron_component__mutmut_19, 
    'x__validate_cron_component__mutmut_20': x__validate_cron_component__mutmut_20, 
    'x__validate_cron_component__mutmut_21': x__validate_cron_component__mutmut_21, 
    'x__validate_cron_component__mutmut_22': x__validate_cron_component__mutmut_22, 
    'x__validate_cron_component__mutmut_23': x__validate_cron_component__mutmut_23, 
    'x__validate_cron_component__mutmut_24': x__validate_cron_component__mutmut_24, 
    'x__validate_cron_component__mutmut_25': x__validate_cron_component__mutmut_25, 
    'x__validate_cron_component__mutmut_26': x__validate_cron_component__mutmut_26, 
    'x__validate_cron_component__mutmut_27': x__validate_cron_component__mutmut_27, 
    'x__validate_cron_component__mutmut_28': x__validate_cron_component__mutmut_28, 
    'x__validate_cron_component__mutmut_29': x__validate_cron_component__mutmut_29, 
    'x__validate_cron_component__mutmut_30': x__validate_cron_component__mutmut_30, 
    'x__validate_cron_component__mutmut_31': x__validate_cron_component__mutmut_31, 
    'x__validate_cron_component__mutmut_32': x__validate_cron_component__mutmut_32, 
    'x__validate_cron_component__mutmut_33': x__validate_cron_component__mutmut_33, 
    'x__validate_cron_component__mutmut_34': x__validate_cron_component__mutmut_34, 
    'x__validate_cron_component__mutmut_35': x__validate_cron_component__mutmut_35, 
    'x__validate_cron_component__mutmut_36': x__validate_cron_component__mutmut_36, 
    'x__validate_cron_component__mutmut_37': x__validate_cron_component__mutmut_37, 
    'x__validate_cron_component__mutmut_38': x__validate_cron_component__mutmut_38, 
    'x__validate_cron_component__mutmut_39': x__validate_cron_component__mutmut_39, 
    'x__validate_cron_component__mutmut_40': x__validate_cron_component__mutmut_40, 
    'x__validate_cron_component__mutmut_41': x__validate_cron_component__mutmut_41, 
    'x__validate_cron_component__mutmut_42': x__validate_cron_component__mutmut_42, 
    'x__validate_cron_component__mutmut_43': x__validate_cron_component__mutmut_43, 
    'x__validate_cron_component__mutmut_44': x__validate_cron_component__mutmut_44, 
    'x__validate_cron_component__mutmut_45': x__validate_cron_component__mutmut_45, 
    'x__validate_cron_component__mutmut_46': x__validate_cron_component__mutmut_46, 
    'x__validate_cron_component__mutmut_47': x__validate_cron_component__mutmut_47, 
    'x__validate_cron_component__mutmut_48': x__validate_cron_component__mutmut_48, 
    'x__validate_cron_component__mutmut_49': x__validate_cron_component__mutmut_49, 
    'x__validate_cron_component__mutmut_50': x__validate_cron_component__mutmut_50, 
    'x__validate_cron_component__mutmut_51': x__validate_cron_component__mutmut_51, 
    'x__validate_cron_component__mutmut_52': x__validate_cron_component__mutmut_52, 
    'x__validate_cron_component__mutmut_53': x__validate_cron_component__mutmut_53, 
    'x__validate_cron_component__mutmut_54': x__validate_cron_component__mutmut_54, 
    'x__validate_cron_component__mutmut_55': x__validate_cron_component__mutmut_55, 
    'x__validate_cron_component__mutmut_56': x__validate_cron_component__mutmut_56, 
    'x__validate_cron_component__mutmut_57': x__validate_cron_component__mutmut_57, 
    'x__validate_cron_component__mutmut_58': x__validate_cron_component__mutmut_58, 
    'x__validate_cron_component__mutmut_59': x__validate_cron_component__mutmut_59, 
    'x__validate_cron_component__mutmut_60': x__validate_cron_component__mutmut_60, 
    'x__validate_cron_component__mutmut_61': x__validate_cron_component__mutmut_61, 
    'x__validate_cron_component__mutmut_62': x__validate_cron_component__mutmut_62, 
    'x__validate_cron_component__mutmut_63': x__validate_cron_component__mutmut_63, 
    'x__validate_cron_component__mutmut_64': x__validate_cron_component__mutmut_64, 
    'x__validate_cron_component__mutmut_65': x__validate_cron_component__mutmut_65, 
    'x__validate_cron_component__mutmut_66': x__validate_cron_component__mutmut_66, 
    'x__validate_cron_component__mutmut_67': x__validate_cron_component__mutmut_67, 
    'x__validate_cron_component__mutmut_68': x__validate_cron_component__mutmut_68, 
    'x__validate_cron_component__mutmut_69': x__validate_cron_component__mutmut_69, 
    'x__validate_cron_component__mutmut_70': x__validate_cron_component__mutmut_70, 
    'x__validate_cron_component__mutmut_71': x__validate_cron_component__mutmut_71, 
    'x__validate_cron_component__mutmut_72': x__validate_cron_component__mutmut_72
}

def _validate_cron_component(*args, **kwargs):
    result = _mutmut_trampoline(x__validate_cron_component__mutmut_orig, x__validate_cron_component__mutmut_mutants, args, kwargs)
    return result 

_validate_cron_component.__signature__ = _mutmut_signature(x__validate_cron_component__mutmut_orig)
x__validate_cron_component__mutmut_orig.__name__ = 'x__validate_cron_component'


@validator
def cron(value: str, /):
    """Return whether or not given value is a valid cron string.

    Examples:
        >>> cron('*/5 * * * *')
        True
        >>> cron('30-20 * * * *')
        ValidationError(func=cron, args={'value': '30-20 * * * *'})

    Args:
        value:
            Cron string to validate.

    Returns:
        (Literal[True]): If `value` is a valid cron string.
        (ValidationError): If `value` is an invalid cron string.
    """
    if not value:
        return False

    try:
        minutes, hours, days, months, weekdays = value.strip().split()
    except ValueError as err:
        raise ValueError("Badly formatted cron string") from err

    if not _validate_cron_component(minutes, 0, 59):
        return False
    if not _validate_cron_component(hours, 0, 23):
        return False
    if not _validate_cron_component(days, 1, 31):
        return False
    if not _validate_cron_component(months, 1, 12):
        return False
    if not _validate_cron_component(weekdays, 0, 6):
        return False

    return True
