"""Domain."""

# standard
from os import environ
from pathlib import Path
import re
from typing import Optional, Set

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


class _IanaTLD:
    """Read IANA TLDs, and optionally cache them."""

    _full_cache: Optional[Set[str]] = None
    # source: https://www.statista.com/statistics/265677
    _popular_cache = {"COM", "ORG", "RU", "DE", "NET", "BR", "UK", "JP", "FR", "IT"}
    _popular_cache.add("ONION")

    @classmethod
    def _retrieve(cls):
        with Path(__file__).parent.joinpath("_tld.txt").open() as tld_f:
            _ = next(tld_f)  # ignore the first line
            for line in tld_f:
                yield line.strip()

    @classmethod
    def check(cls, tld: str):
        if tld in cls._popular_cache:
            return True
        if cls._full_cache is None:
            if environ.get("PYVLD_CACHE_TLD") == "True":
                cls._full_cache = set(cls._retrieve())
            else:
                return tld in cls._retrieve()
        return tld in cls._full_cache


@validator
def domain(
    value: str, /, *, consider_tld: bool = False, rfc_1034: bool = False, rfc_2782: bool = False
):
    """Return whether or not given value is a valid domain.

    Examples:
        >>> domain('example.com')
        True
        >>> domain('example.com/')
        ValidationError(func=domain, args={'value': 'example.com/'})
        >>> # Supports IDN domains as well::
        >>> domain('xn----gtbspbbmkef.xn--p1ai')
        True

    Args:
        value:
            Domain string to validate.
        consider_tld:
            Restrict domain to TLDs allowed by IANA.
        rfc_1034:
            Allows optional trailing dot in the domain name.
            Ref: [RFC 1034](https://www.rfc-editor.org/rfc/rfc1034).
        rfc_2782:
            Domain name is of type service record.
            Allows optional underscores in the domain name.
            Ref: [RFC 2782](https://www.rfc-editor.org/rfc/rfc2782).


    Returns:
        (Literal[True]): If `value` is a valid domain name.
        (ValidationError): If `value` is an invalid domain name.

    Raises:
        (UnicodeError): If `value` cannot be encoded into `idna` or decoded into `utf-8`.
    """
    if not value:
        return False

    if consider_tld and not _IanaTLD.check(value.rstrip(".").rsplit(".", 1)[-1].upper()):
        return False

    try:
        service_record = r"_" if rfc_2782 else ""
        trailing_dot = r"\.?$" if rfc_1034 else r"$"

        return not re.search(r"\s|__+", value) and re.match(
            # First character of the domain
            rf"^(?:[a-z0-9{service_record}]"
            # Sub-domain
            + rf"(?:[a-z0-9-{service_record}]{{0,61}}"
            # Hostname
            + rf"[a-z0-9{service_record}])?\.)"
            # First 61 characters of the gTLD
            + r"+[a-z0-9][a-z0-9-_]{0,61}"
            # Last character of the gTLD
            + rf"[a-z]{trailing_dot}",
            value.encode("idna").decode("utf-8"),
            re.IGNORECASE,
        )
    except UnicodeError as err:
        raise UnicodeError(f"Unable to encode/decode {value}") from err
