"""URL."""

# standard
from functools import lru_cache
import re
from typing import Callable, Optional
from urllib.parse import parse_qs, unquote, urlsplit

# local
from .hostname import hostname
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
def _username_regex():
    return re.compile(
        # extended latin
        r"(^[\u0100-\u017F\u0180-\u024F]"
        # dot-atom
        + r"|[-!#$%&'*+/=?^_`{}|~0-9a-z]+(\.[-!#$%&'*+/=?^_`{}|~0-9a-z]+)*$"
        # non-quoted-string
        + r"|^([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\011.])*$)",
        re.IGNORECASE,
    )


@lru_cache
def _path_regex():
    return re.compile(
        # allowed symbols
        r"^[\/a-z0-9\-\.\_\~\!\$\&\'\(\)\*\+\,\;\=\:\@\%"
        # symbols / pictographs
        + r"\U0001F300-\U0001F5FF"
        # emoticons / emoji
        + r"\U0001F600-\U0001F64F"
        # multilingual unicode ranges
        + r"\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]+$",
        re.IGNORECASE,
    )


def x__validate_scheme__mutmut_orig(value: str):
    """Validate scheme."""
    # More schemes will be considered later.
    return (
        value
        # fmt: off
        in {
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
        if value
        else False
    )


def x__validate_scheme__mutmut_1(value: str):
    """Validate scheme."""
    # More schemes will be considered later.
    return (
        value not in {
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
        if value
        else False
    )


def x__validate_scheme__mutmut_2(value: str):
    """Validate scheme."""
    # More schemes will be considered later.
    return (
        value
        # fmt: off
        in {
            "XXftpXX",
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
        if value
        else False
    )


def x__validate_scheme__mutmut_3(value: str):
    """Validate scheme."""
    # More schemes will be considered later.
    return (
        value
        # fmt: off
        in {
            "FTP",
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
        if value
        else False
    )


def x__validate_scheme__mutmut_4(value: str):
    """Validate scheme."""
    # More schemes will be considered later.
    return (
        value
        # fmt: off
        in {
            "ftp",
            "XXftpsXX",
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
        if value
        else False
    )


def x__validate_scheme__mutmut_5(value: str):
    """Validate scheme."""
    # More schemes will be considered later.
    return (
        value
        # fmt: off
        in {
            "ftp",
            "FTPS",
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
        if value
        else False
    )


def x__validate_scheme__mutmut_6(value: str):
    """Validate scheme."""
    # More schemes will be considered later.
    return (
        value
        # fmt: off
        in {
            "ftp",
            "ftps",
            "XXgitXX",
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
        if value
        else False
    )


def x__validate_scheme__mutmut_7(value: str):
    """Validate scheme."""
    # More schemes will be considered later.
    return (
        value
        # fmt: off
        in {
            "ftp",
            "ftps",
            "GIT",
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
        if value
        else False
    )


def x__validate_scheme__mutmut_8(value: str):
    """Validate scheme."""
    # More schemes will be considered later.
    return (
        value
        # fmt: off
        in {
            "ftp",
            "ftps",
            "git",
            "XXhttpXX",
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
        if value
        else False
    )


def x__validate_scheme__mutmut_9(value: str):
    """Validate scheme."""
    # More schemes will be considered later.
    return (
        value
        # fmt: off
        in {
            "ftp",
            "ftps",
            "git",
            "HTTP",
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
        if value
        else False
    )


def x__validate_scheme__mutmut_10(value: str):
    """Validate scheme."""
    # More schemes will be considered later.
    return (
        value
        # fmt: off
        in {
            "ftp",
            "ftps",
            "git",
            "http",
            "XXhttpsXX",
            "irc",
            "rtmp",
            "rtmps",
            "rtsp",
            "sftp",
            "ssh",
            "telnet",
        }
        # fmt: on
        if value
        else False
    )


def x__validate_scheme__mutmut_11(value: str):
    """Validate scheme."""
    # More schemes will be considered later.
    return (
        value
        # fmt: off
        in {
            "ftp",
            "ftps",
            "git",
            "http",
            "HTTPS",
            "irc",
            "rtmp",
            "rtmps",
            "rtsp",
            "sftp",
            "ssh",
            "telnet",
        }
        # fmt: on
        if value
        else False
    )


def x__validate_scheme__mutmut_12(value: str):
    """Validate scheme."""
    # More schemes will be considered later.
    return (
        value
        # fmt: off
        in {
            "ftp",
            "ftps",
            "git",
            "http",
            "https",
            "XXircXX",
            "rtmp",
            "rtmps",
            "rtsp",
            "sftp",
            "ssh",
            "telnet",
        }
        # fmt: on
        if value
        else False
    )


def x__validate_scheme__mutmut_13(value: str):
    """Validate scheme."""
    # More schemes will be considered later.
    return (
        value
        # fmt: off
        in {
            "ftp",
            "ftps",
            "git",
            "http",
            "https",
            "IRC",
            "rtmp",
            "rtmps",
            "rtsp",
            "sftp",
            "ssh",
            "telnet",
        }
        # fmt: on
        if value
        else False
    )


def x__validate_scheme__mutmut_14(value: str):
    """Validate scheme."""
    # More schemes will be considered later.
    return (
        value
        # fmt: off
        in {
            "ftp",
            "ftps",
            "git",
            "http",
            "https",
            "irc",
            "XXrtmpXX",
            "rtmps",
            "rtsp",
            "sftp",
            "ssh",
            "telnet",
        }
        # fmt: on
        if value
        else False
    )


def x__validate_scheme__mutmut_15(value: str):
    """Validate scheme."""
    # More schemes will be considered later.
    return (
        value
        # fmt: off
        in {
            "ftp",
            "ftps",
            "git",
            "http",
            "https",
            "irc",
            "RTMP",
            "rtmps",
            "rtsp",
            "sftp",
            "ssh",
            "telnet",
        }
        # fmt: on
        if value
        else False
    )


def x__validate_scheme__mutmut_16(value: str):
    """Validate scheme."""
    # More schemes will be considered later.
    return (
        value
        # fmt: off
        in {
            "ftp",
            "ftps",
            "git",
            "http",
            "https",
            "irc",
            "rtmp",
            "XXrtmpsXX",
            "rtsp",
            "sftp",
            "ssh",
            "telnet",
        }
        # fmt: on
        if value
        else False
    )


def x__validate_scheme__mutmut_17(value: str):
    """Validate scheme."""
    # More schemes will be considered later.
    return (
        value
        # fmt: off
        in {
            "ftp",
            "ftps",
            "git",
            "http",
            "https",
            "irc",
            "rtmp",
            "RTMPS",
            "rtsp",
            "sftp",
            "ssh",
            "telnet",
        }
        # fmt: on
        if value
        else False
    )


def x__validate_scheme__mutmut_18(value: str):
    """Validate scheme."""
    # More schemes will be considered later.
    return (
        value
        # fmt: off
        in {
            "ftp",
            "ftps",
            "git",
            "http",
            "https",
            "irc",
            "rtmp",
            "rtmps",
            "XXrtspXX",
            "sftp",
            "ssh",
            "telnet",
        }
        # fmt: on
        if value
        else False
    )


def x__validate_scheme__mutmut_19(value: str):
    """Validate scheme."""
    # More schemes will be considered later.
    return (
        value
        # fmt: off
        in {
            "ftp",
            "ftps",
            "git",
            "http",
            "https",
            "irc",
            "rtmp",
            "rtmps",
            "RTSP",
            "sftp",
            "ssh",
            "telnet",
        }
        # fmt: on
        if value
        else False
    )


def x__validate_scheme__mutmut_20(value: str):
    """Validate scheme."""
    # More schemes will be considered later.
    return (
        value
        # fmt: off
        in {
            "ftp",
            "ftps",
            "git",
            "http",
            "https",
            "irc",
            "rtmp",
            "rtmps",
            "rtsp",
            "XXsftpXX",
            "ssh",
            "telnet",
        }
        # fmt: on
        if value
        else False
    )


def x__validate_scheme__mutmut_21(value: str):
    """Validate scheme."""
    # More schemes will be considered later.
    return (
        value
        # fmt: off
        in {
            "ftp",
            "ftps",
            "git",
            "http",
            "https",
            "irc",
            "rtmp",
            "rtmps",
            "rtsp",
            "SFTP",
            "ssh",
            "telnet",
        }
        # fmt: on
        if value
        else False
    )


def x__validate_scheme__mutmut_22(value: str):
    """Validate scheme."""
    # More schemes will be considered later.
    return (
        value
        # fmt: off
        in {
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
            "XXsshXX",
            "telnet",
        }
        # fmt: on
        if value
        else False
    )


def x__validate_scheme__mutmut_23(value: str):
    """Validate scheme."""
    # More schemes will be considered later.
    return (
        value
        # fmt: off
        in {
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
            "SSH",
            "telnet",
        }
        # fmt: on
        if value
        else False
    )


def x__validate_scheme__mutmut_24(value: str):
    """Validate scheme."""
    # More schemes will be considered later.
    return (
        value
        # fmt: off
        in {
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
            "XXtelnetXX",
        }
        # fmt: on
        if value
        else False
    )


def x__validate_scheme__mutmut_25(value: str):
    """Validate scheme."""
    # More schemes will be considered later.
    return (
        value
        # fmt: off
        in {
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
            "TELNET",
        }
        # fmt: on
        if value
        else False
    )


def x__validate_scheme__mutmut_26(value: str):
    """Validate scheme."""
    # More schemes will be considered later.
    return (
        value
        # fmt: off
        in {
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
        if value
        else True
    )

x__validate_scheme__mutmut_mutants : ClassVar[MutantDict] = {
'x__validate_scheme__mutmut_1': x__validate_scheme__mutmut_1, 
    'x__validate_scheme__mutmut_2': x__validate_scheme__mutmut_2, 
    'x__validate_scheme__mutmut_3': x__validate_scheme__mutmut_3, 
    'x__validate_scheme__mutmut_4': x__validate_scheme__mutmut_4, 
    'x__validate_scheme__mutmut_5': x__validate_scheme__mutmut_5, 
    'x__validate_scheme__mutmut_6': x__validate_scheme__mutmut_6, 
    'x__validate_scheme__mutmut_7': x__validate_scheme__mutmut_7, 
    'x__validate_scheme__mutmut_8': x__validate_scheme__mutmut_8, 
    'x__validate_scheme__mutmut_9': x__validate_scheme__mutmut_9, 
    'x__validate_scheme__mutmut_10': x__validate_scheme__mutmut_10, 
    'x__validate_scheme__mutmut_11': x__validate_scheme__mutmut_11, 
    'x__validate_scheme__mutmut_12': x__validate_scheme__mutmut_12, 
    'x__validate_scheme__mutmut_13': x__validate_scheme__mutmut_13, 
    'x__validate_scheme__mutmut_14': x__validate_scheme__mutmut_14, 
    'x__validate_scheme__mutmut_15': x__validate_scheme__mutmut_15, 
    'x__validate_scheme__mutmut_16': x__validate_scheme__mutmut_16, 
    'x__validate_scheme__mutmut_17': x__validate_scheme__mutmut_17, 
    'x__validate_scheme__mutmut_18': x__validate_scheme__mutmut_18, 
    'x__validate_scheme__mutmut_19': x__validate_scheme__mutmut_19, 
    'x__validate_scheme__mutmut_20': x__validate_scheme__mutmut_20, 
    'x__validate_scheme__mutmut_21': x__validate_scheme__mutmut_21, 
    'x__validate_scheme__mutmut_22': x__validate_scheme__mutmut_22, 
    'x__validate_scheme__mutmut_23': x__validate_scheme__mutmut_23, 
    'x__validate_scheme__mutmut_24': x__validate_scheme__mutmut_24, 
    'x__validate_scheme__mutmut_25': x__validate_scheme__mutmut_25, 
    'x__validate_scheme__mutmut_26': x__validate_scheme__mutmut_26
}

def _validate_scheme(*args, **kwargs):
    result = _mutmut_trampoline(x__validate_scheme__mutmut_orig, x__validate_scheme__mutmut_mutants, args, kwargs)
    return result 

_validate_scheme.__signature__ = _mutmut_signature(x__validate_scheme__mutmut_orig)
x__validate_scheme__mutmut_orig.__name__ = 'x__validate_scheme'


def x__confirm_ipv6_skip__mutmut_orig(value: str, skip_ipv6_addr: bool):
    """Confirm skip IPv6 check."""
    return skip_ipv6_addr or value.count(":") < 2 or not value.startswith("[")


def x__confirm_ipv6_skip__mutmut_1(value: str, skip_ipv6_addr: bool):
    """Confirm skip IPv6 check."""
    return skip_ipv6_addr or value.count(":") < 2 and not value.startswith("[")


def x__confirm_ipv6_skip__mutmut_2(value: str, skip_ipv6_addr: bool):
    """Confirm skip IPv6 check."""
    return skip_ipv6_addr and value.count(":") < 2 or not value.startswith("[")


def x__confirm_ipv6_skip__mutmut_3(value: str, skip_ipv6_addr: bool):
    """Confirm skip IPv6 check."""
    return skip_ipv6_addr or value.count(None) < 2 or not value.startswith("[")


def x__confirm_ipv6_skip__mutmut_4(value: str, skip_ipv6_addr: bool):
    """Confirm skip IPv6 check."""
    return skip_ipv6_addr or value.count("XX:XX") < 2 or not value.startswith("[")


def x__confirm_ipv6_skip__mutmut_5(value: str, skip_ipv6_addr: bool):
    """Confirm skip IPv6 check."""
    return skip_ipv6_addr or value.count(":") <= 2 or not value.startswith("[")


def x__confirm_ipv6_skip__mutmut_6(value: str, skip_ipv6_addr: bool):
    """Confirm skip IPv6 check."""
    return skip_ipv6_addr or value.count(":") < 3 or not value.startswith("[")


def x__confirm_ipv6_skip__mutmut_7(value: str, skip_ipv6_addr: bool):
    """Confirm skip IPv6 check."""
    return skip_ipv6_addr or value.count(":") < 2 or value.startswith("[")


def x__confirm_ipv6_skip__mutmut_8(value: str, skip_ipv6_addr: bool):
    """Confirm skip IPv6 check."""
    return skip_ipv6_addr or value.count(":") < 2 or not value.startswith(None)


def x__confirm_ipv6_skip__mutmut_9(value: str, skip_ipv6_addr: bool):
    """Confirm skip IPv6 check."""
    return skip_ipv6_addr or value.count(":") < 2 or not value.startswith("XX[XX")

x__confirm_ipv6_skip__mutmut_mutants : ClassVar[MutantDict] = {
'x__confirm_ipv6_skip__mutmut_1': x__confirm_ipv6_skip__mutmut_1, 
    'x__confirm_ipv6_skip__mutmut_2': x__confirm_ipv6_skip__mutmut_2, 
    'x__confirm_ipv6_skip__mutmut_3': x__confirm_ipv6_skip__mutmut_3, 
    'x__confirm_ipv6_skip__mutmut_4': x__confirm_ipv6_skip__mutmut_4, 
    'x__confirm_ipv6_skip__mutmut_5': x__confirm_ipv6_skip__mutmut_5, 
    'x__confirm_ipv6_skip__mutmut_6': x__confirm_ipv6_skip__mutmut_6, 
    'x__confirm_ipv6_skip__mutmut_7': x__confirm_ipv6_skip__mutmut_7, 
    'x__confirm_ipv6_skip__mutmut_8': x__confirm_ipv6_skip__mutmut_8, 
    'x__confirm_ipv6_skip__mutmut_9': x__confirm_ipv6_skip__mutmut_9
}

def _confirm_ipv6_skip(*args, **kwargs):
    result = _mutmut_trampoline(x__confirm_ipv6_skip__mutmut_orig, x__confirm_ipv6_skip__mutmut_mutants, args, kwargs)
    return result 

_confirm_ipv6_skip.__signature__ = _mutmut_signature(x__confirm_ipv6_skip__mutmut_orig)
x__confirm_ipv6_skip__mutmut_orig.__name__ = 'x__confirm_ipv6_skip'


def x__validate_auth_segment__mutmut_orig(value: str):
    """Validate authentication segment."""
    if not value:
        return True
    if (colon_count := value.count(":")) > 1:
        # everything before @ is then considered as a username
        # this is a bad practice, but syntactically valid URL
        return _username_regex().match(unquote(value))
    if colon_count < 1:
        return _username_regex().match(value)
    username, password = value.rsplit(":", 1)
    return _username_regex().match(username) and all(
        char_to_avoid not in password for char_to_avoid in ("/", "?", "#", "@")
    )


def x__validate_auth_segment__mutmut_1(value: str):
    """Validate authentication segment."""
    if value:
        return True
    if (colon_count := value.count(":")) > 1:
        # everything before @ is then considered as a username
        # this is a bad practice, but syntactically valid URL
        return _username_regex().match(unquote(value))
    if colon_count < 1:
        return _username_regex().match(value)
    username, password = value.rsplit(":", 1)
    return _username_regex().match(username) and all(
        char_to_avoid not in password for char_to_avoid in ("/", "?", "#", "@")
    )


def x__validate_auth_segment__mutmut_2(value: str):
    """Validate authentication segment."""
    if not value:
        return False
    if (colon_count := value.count(":")) > 1:
        # everything before @ is then considered as a username
        # this is a bad practice, but syntactically valid URL
        return _username_regex().match(unquote(value))
    if colon_count < 1:
        return _username_regex().match(value)
    username, password = value.rsplit(":", 1)
    return _username_regex().match(username) and all(
        char_to_avoid not in password for char_to_avoid in ("/", "?", "#", "@")
    )


def x__validate_auth_segment__mutmut_3(value: str):
    """Validate authentication segment."""
    if not value:
        return True
    if (colon_count := value.count(None)) > 1:
        # everything before @ is then considered as a username
        # this is a bad practice, but syntactically valid URL
        return _username_regex().match(unquote(value))
    if colon_count < 1:
        return _username_regex().match(value)
    username, password = value.rsplit(":", 1)
    return _username_regex().match(username) and all(
        char_to_avoid not in password for char_to_avoid in ("/", "?", "#", "@")
    )


def x__validate_auth_segment__mutmut_4(value: str):
    """Validate authentication segment."""
    if not value:
        return True
    if (colon_count := value.count("XX:XX")) > 1:
        # everything before @ is then considered as a username
        # this is a bad practice, but syntactically valid URL
        return _username_regex().match(unquote(value))
    if colon_count < 1:
        return _username_regex().match(value)
    username, password = value.rsplit(":", 1)
    return _username_regex().match(username) and all(
        char_to_avoid not in password for char_to_avoid in ("/", "?", "#", "@")
    )


def x__validate_auth_segment__mutmut_5(value: str):
    """Validate authentication segment."""
    if not value:
        return True
    if (colon_count := value.count(":")) >= 1:
        # everything before @ is then considered as a username
        # this is a bad practice, but syntactically valid URL
        return _username_regex().match(unquote(value))
    if colon_count < 1:
        return _username_regex().match(value)
    username, password = value.rsplit(":", 1)
    return _username_regex().match(username) and all(
        char_to_avoid not in password for char_to_avoid in ("/", "?", "#", "@")
    )


def x__validate_auth_segment__mutmut_6(value: str):
    """Validate authentication segment."""
    if not value:
        return True
    if (colon_count := value.count(":")) > 2:
        # everything before @ is then considered as a username
        # this is a bad practice, but syntactically valid URL
        return _username_regex().match(unquote(value))
    if colon_count < 1:
        return _username_regex().match(value)
    username, password = value.rsplit(":", 1)
    return _username_regex().match(username) and all(
        char_to_avoid not in password for char_to_avoid in ("/", "?", "#", "@")
    )


def x__validate_auth_segment__mutmut_7(value: str):
    """Validate authentication segment."""
    if not value:
        return True
    if (colon_count := value.count(":")) > 1:
        # everything before @ is then considered as a username
        # this is a bad practice, but syntactically valid URL
        return _username_regex().match(None)
    if colon_count < 1:
        return _username_regex().match(value)
    username, password = value.rsplit(":", 1)
    return _username_regex().match(username) and all(
        char_to_avoid not in password for char_to_avoid in ("/", "?", "#", "@")
    )


def x__validate_auth_segment__mutmut_8(value: str):
    """Validate authentication segment."""
    if not value:
        return True
    if (colon_count := value.count(":")) > 1:
        # everything before @ is then considered as a username
        # this is a bad practice, but syntactically valid URL
        return _username_regex().match(unquote(None))
    if colon_count < 1:
        return _username_regex().match(value)
    username, password = value.rsplit(":", 1)
    return _username_regex().match(username) and all(
        char_to_avoid not in password for char_to_avoid in ("/", "?", "#", "@")
    )


def x__validate_auth_segment__mutmut_9(value: str):
    """Validate authentication segment."""
    if not value:
        return True
    if (colon_count := value.count(":")) > 1:
        # everything before @ is then considered as a username
        # this is a bad practice, but syntactically valid URL
        return _username_regex().match(unquote(value))
    if colon_count <= 1:
        return _username_regex().match(value)
    username, password = value.rsplit(":", 1)
    return _username_regex().match(username) and all(
        char_to_avoid not in password for char_to_avoid in ("/", "?", "#", "@")
    )


def x__validate_auth_segment__mutmut_10(value: str):
    """Validate authentication segment."""
    if not value:
        return True
    if (colon_count := value.count(":")) > 1:
        # everything before @ is then considered as a username
        # this is a bad practice, but syntactically valid URL
        return _username_regex().match(unquote(value))
    if colon_count < 2:
        return _username_regex().match(value)
    username, password = value.rsplit(":", 1)
    return _username_regex().match(username) and all(
        char_to_avoid not in password for char_to_avoid in ("/", "?", "#", "@")
    )


def x__validate_auth_segment__mutmut_11(value: str):
    """Validate authentication segment."""
    if not value:
        return True
    if (colon_count := value.count(":")) > 1:
        # everything before @ is then considered as a username
        # this is a bad practice, but syntactically valid URL
        return _username_regex().match(unquote(value))
    if colon_count < 1:
        return _username_regex().match(None)
    username, password = value.rsplit(":", 1)
    return _username_regex().match(username) and all(
        char_to_avoid not in password for char_to_avoid in ("/", "?", "#", "@")
    )


def x__validate_auth_segment__mutmut_12(value: str):
    """Validate authentication segment."""
    if not value:
        return True
    if (colon_count := value.count(":")) > 1:
        # everything before @ is then considered as a username
        # this is a bad practice, but syntactically valid URL
        return _username_regex().match(unquote(value))
    if colon_count < 1:
        return _username_regex().match(value)
    username, password = None
    return _username_regex().match(username) and all(
        char_to_avoid not in password for char_to_avoid in ("/", "?", "#", "@")
    )


def x__validate_auth_segment__mutmut_13(value: str):
    """Validate authentication segment."""
    if not value:
        return True
    if (colon_count := value.count(":")) > 1:
        # everything before @ is then considered as a username
        # this is a bad practice, but syntactically valid URL
        return _username_regex().match(unquote(value))
    if colon_count < 1:
        return _username_regex().match(value)
    username, password = value.rsplit(None, 1)
    return _username_regex().match(username) and all(
        char_to_avoid not in password for char_to_avoid in ("/", "?", "#", "@")
    )


def x__validate_auth_segment__mutmut_14(value: str):
    """Validate authentication segment."""
    if not value:
        return True
    if (colon_count := value.count(":")) > 1:
        # everything before @ is then considered as a username
        # this is a bad practice, but syntactically valid URL
        return _username_regex().match(unquote(value))
    if colon_count < 1:
        return _username_regex().match(value)
    username, password = value.rsplit(":", None)
    return _username_regex().match(username) and all(
        char_to_avoid not in password for char_to_avoid in ("/", "?", "#", "@")
    )


def x__validate_auth_segment__mutmut_15(value: str):
    """Validate authentication segment."""
    if not value:
        return True
    if (colon_count := value.count(":")) > 1:
        # everything before @ is then considered as a username
        # this is a bad practice, but syntactically valid URL
        return _username_regex().match(unquote(value))
    if colon_count < 1:
        return _username_regex().match(value)
    username, password = value.rsplit(1)
    return _username_regex().match(username) and all(
        char_to_avoid not in password for char_to_avoid in ("/", "?", "#", "@")
    )


def x__validate_auth_segment__mutmut_16(value: str):
    """Validate authentication segment."""
    if not value:
        return True
    if (colon_count := value.count(":")) > 1:
        # everything before @ is then considered as a username
        # this is a bad practice, but syntactically valid URL
        return _username_regex().match(unquote(value))
    if colon_count < 1:
        return _username_regex().match(value)
    username, password = value.rsplit(":", )
    return _username_regex().match(username) and all(
        char_to_avoid not in password for char_to_avoid in ("/", "?", "#", "@")
    )


def x__validate_auth_segment__mutmut_17(value: str):
    """Validate authentication segment."""
    if not value:
        return True
    if (colon_count := value.count(":")) > 1:
        # everything before @ is then considered as a username
        # this is a bad practice, but syntactically valid URL
        return _username_regex().match(unquote(value))
    if colon_count < 1:
        return _username_regex().match(value)
    username, password = value.split(":", 1)
    return _username_regex().match(username) and all(
        char_to_avoid not in password for char_to_avoid in ("/", "?", "#", "@")
    )


def x__validate_auth_segment__mutmut_18(value: str):
    """Validate authentication segment."""
    if not value:
        return True
    if (colon_count := value.count(":")) > 1:
        # everything before @ is then considered as a username
        # this is a bad practice, but syntactically valid URL
        return _username_regex().match(unquote(value))
    if colon_count < 1:
        return _username_regex().match(value)
    username, password = value.rsplit("XX:XX", 1)
    return _username_regex().match(username) and all(
        char_to_avoid not in password for char_to_avoid in ("/", "?", "#", "@")
    )


def x__validate_auth_segment__mutmut_19(value: str):
    """Validate authentication segment."""
    if not value:
        return True
    if (colon_count := value.count(":")) > 1:
        # everything before @ is then considered as a username
        # this is a bad practice, but syntactically valid URL
        return _username_regex().match(unquote(value))
    if colon_count < 1:
        return _username_regex().match(value)
    username, password = value.rsplit(":", 2)
    return _username_regex().match(username) and all(
        char_to_avoid not in password for char_to_avoid in ("/", "?", "#", "@")
    )


def x__validate_auth_segment__mutmut_20(value: str):
    """Validate authentication segment."""
    if not value:
        return True
    if (colon_count := value.count(":")) > 1:
        # everything before @ is then considered as a username
        # this is a bad practice, but syntactically valid URL
        return _username_regex().match(unquote(value))
    if colon_count < 1:
        return _username_regex().match(value)
    username, password = value.rsplit(":", 1)
    return _username_regex().match(username) or all(
        char_to_avoid not in password for char_to_avoid in ("/", "?", "#", "@")
    )


def x__validate_auth_segment__mutmut_21(value: str):
    """Validate authentication segment."""
    if not value:
        return True
    if (colon_count := value.count(":")) > 1:
        # everything before @ is then considered as a username
        # this is a bad practice, but syntactically valid URL
        return _username_regex().match(unquote(value))
    if colon_count < 1:
        return _username_regex().match(value)
    username, password = value.rsplit(":", 1)
    return _username_regex().match(None) and all(
        char_to_avoid not in password for char_to_avoid in ("/", "?", "#", "@")
    )


def x__validate_auth_segment__mutmut_22(value: str):
    """Validate authentication segment."""
    if not value:
        return True
    if (colon_count := value.count(":")) > 1:
        # everything before @ is then considered as a username
        # this is a bad practice, but syntactically valid URL
        return _username_regex().match(unquote(value))
    if colon_count < 1:
        return _username_regex().match(value)
    username, password = value.rsplit(":", 1)
    return _username_regex().match(username) and all(
        None
    )


def x__validate_auth_segment__mutmut_23(value: str):
    """Validate authentication segment."""
    if not value:
        return True
    if (colon_count := value.count(":")) > 1:
        # everything before @ is then considered as a username
        # this is a bad practice, but syntactically valid URL
        return _username_regex().match(unquote(value))
    if colon_count < 1:
        return _username_regex().match(value)
    username, password = value.rsplit(":", 1)
    return _username_regex().match(username) and all(
        char_to_avoid in password for char_to_avoid in ("/", "?", "#", "@")
    )


def x__validate_auth_segment__mutmut_24(value: str):
    """Validate authentication segment."""
    if not value:
        return True
    if (colon_count := value.count(":")) > 1:
        # everything before @ is then considered as a username
        # this is a bad practice, but syntactically valid URL
        return _username_regex().match(unquote(value))
    if colon_count < 1:
        return _username_regex().match(value)
    username, password = value.rsplit(":", 1)
    return _username_regex().match(username) and all(
        char_to_avoid not in password for char_to_avoid in ("XX/XX", "?", "#", "@")
    )


def x__validate_auth_segment__mutmut_25(value: str):
    """Validate authentication segment."""
    if not value:
        return True
    if (colon_count := value.count(":")) > 1:
        # everything before @ is then considered as a username
        # this is a bad practice, but syntactically valid URL
        return _username_regex().match(unquote(value))
    if colon_count < 1:
        return _username_regex().match(value)
    username, password = value.rsplit(":", 1)
    return _username_regex().match(username) and all(
        char_to_avoid not in password for char_to_avoid in ("/", "XX?XX", "#", "@")
    )


def x__validate_auth_segment__mutmut_26(value: str):
    """Validate authentication segment."""
    if not value:
        return True
    if (colon_count := value.count(":")) > 1:
        # everything before @ is then considered as a username
        # this is a bad practice, but syntactically valid URL
        return _username_regex().match(unquote(value))
    if colon_count < 1:
        return _username_regex().match(value)
    username, password = value.rsplit(":", 1)
    return _username_regex().match(username) and all(
        char_to_avoid not in password for char_to_avoid in ("/", "?", "XX#XX", "@")
    )


def x__validate_auth_segment__mutmut_27(value: str):
    """Validate authentication segment."""
    if not value:
        return True
    if (colon_count := value.count(":")) > 1:
        # everything before @ is then considered as a username
        # this is a bad practice, but syntactically valid URL
        return _username_regex().match(unquote(value))
    if colon_count < 1:
        return _username_regex().match(value)
    username, password = value.rsplit(":", 1)
    return _username_regex().match(username) and all(
        char_to_avoid not in password for char_to_avoid in ("/", "?", "#", "XX@XX")
    )

x__validate_auth_segment__mutmut_mutants : ClassVar[MutantDict] = {
'x__validate_auth_segment__mutmut_1': x__validate_auth_segment__mutmut_1, 
    'x__validate_auth_segment__mutmut_2': x__validate_auth_segment__mutmut_2, 
    'x__validate_auth_segment__mutmut_3': x__validate_auth_segment__mutmut_3, 
    'x__validate_auth_segment__mutmut_4': x__validate_auth_segment__mutmut_4, 
    'x__validate_auth_segment__mutmut_5': x__validate_auth_segment__mutmut_5, 
    'x__validate_auth_segment__mutmut_6': x__validate_auth_segment__mutmut_6, 
    'x__validate_auth_segment__mutmut_7': x__validate_auth_segment__mutmut_7, 
    'x__validate_auth_segment__mutmut_8': x__validate_auth_segment__mutmut_8, 
    'x__validate_auth_segment__mutmut_9': x__validate_auth_segment__mutmut_9, 
    'x__validate_auth_segment__mutmut_10': x__validate_auth_segment__mutmut_10, 
    'x__validate_auth_segment__mutmut_11': x__validate_auth_segment__mutmut_11, 
    'x__validate_auth_segment__mutmut_12': x__validate_auth_segment__mutmut_12, 
    'x__validate_auth_segment__mutmut_13': x__validate_auth_segment__mutmut_13, 
    'x__validate_auth_segment__mutmut_14': x__validate_auth_segment__mutmut_14, 
    'x__validate_auth_segment__mutmut_15': x__validate_auth_segment__mutmut_15, 
    'x__validate_auth_segment__mutmut_16': x__validate_auth_segment__mutmut_16, 
    'x__validate_auth_segment__mutmut_17': x__validate_auth_segment__mutmut_17, 
    'x__validate_auth_segment__mutmut_18': x__validate_auth_segment__mutmut_18, 
    'x__validate_auth_segment__mutmut_19': x__validate_auth_segment__mutmut_19, 
    'x__validate_auth_segment__mutmut_20': x__validate_auth_segment__mutmut_20, 
    'x__validate_auth_segment__mutmut_21': x__validate_auth_segment__mutmut_21, 
    'x__validate_auth_segment__mutmut_22': x__validate_auth_segment__mutmut_22, 
    'x__validate_auth_segment__mutmut_23': x__validate_auth_segment__mutmut_23, 
    'x__validate_auth_segment__mutmut_24': x__validate_auth_segment__mutmut_24, 
    'x__validate_auth_segment__mutmut_25': x__validate_auth_segment__mutmut_25, 
    'x__validate_auth_segment__mutmut_26': x__validate_auth_segment__mutmut_26, 
    'x__validate_auth_segment__mutmut_27': x__validate_auth_segment__mutmut_27
}

def _validate_auth_segment(*args, **kwargs):
    result = _mutmut_trampoline(x__validate_auth_segment__mutmut_orig, x__validate_auth_segment__mutmut_mutants, args, kwargs)
    return result 

_validate_auth_segment.__signature__ = _mutmut_signature(x__validate_auth_segment__mutmut_orig)
x__validate_auth_segment__mutmut_orig.__name__ = 'x__validate_auth_segment'


def x__validate_netloc__mutmut_orig(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_1(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value and value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_2(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_3(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count(None) > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_4(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("XX@XX") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_5(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") >= 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_6(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 2:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_7(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return True
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_8(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count(None) < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_9(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("XX@XX") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_10(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") <= 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_11(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 2:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_12(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            None,
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_13(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=None,
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_14(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=None,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_15(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=None,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_16(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=None,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_17(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=None,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_18(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=None,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_19(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=None,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_20(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=None,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_21(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_22(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_23(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_24(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_25(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_26(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_27(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_28(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_29(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_30(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) and "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_31(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(None, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_32(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, None) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_33(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_34(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, ) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_35(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "XX]:XX" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_36(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" not in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_37(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace(None, "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_38(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", None, 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_39(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", None)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_40(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_41(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_42(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", )
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_43(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip(None).replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_44(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.rstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_45(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("XX[XX").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_46(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("XX]XX", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_47(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "XXXX", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_48(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 2)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_49(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(None, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_50(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, None),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_51(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_52(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, ),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_53(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = None
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_54(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit(None, 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_55(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", None)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_56(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit(1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_57(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", )
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_58(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.split("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_59(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("XX@XX", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_60(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 2)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_61(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) or _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_62(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        None,
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_63(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=None,
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_64(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=None,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_65(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=None,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_66(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=None,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_67(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=None,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_68(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=None,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_69(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=None,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_70(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=None,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_71(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_72(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_73(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_74(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_75(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_76(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_77(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_78(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_79(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_80(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) and "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_81(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(None, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_82(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, None) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_83(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_84(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, ) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_85(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "XX]:XX" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_86(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" not in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_87(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace(None, "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_88(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", None, 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_89(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", None)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_90(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_91(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_92(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", )
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_93(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip(None).replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_94(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.rstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_95(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("XX[XX").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_96(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("XX]XX", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_97(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "XXXX", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_98(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 2)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_99(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(None, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_100(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, None),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_101(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_102(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, ),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def x__validate_netloc__mutmut_103(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(None)

x__validate_netloc__mutmut_mutants : ClassVar[MutantDict] = {
'x__validate_netloc__mutmut_1': x__validate_netloc__mutmut_1, 
    'x__validate_netloc__mutmut_2': x__validate_netloc__mutmut_2, 
    'x__validate_netloc__mutmut_3': x__validate_netloc__mutmut_3, 
    'x__validate_netloc__mutmut_4': x__validate_netloc__mutmut_4, 
    'x__validate_netloc__mutmut_5': x__validate_netloc__mutmut_5, 
    'x__validate_netloc__mutmut_6': x__validate_netloc__mutmut_6, 
    'x__validate_netloc__mutmut_7': x__validate_netloc__mutmut_7, 
    'x__validate_netloc__mutmut_8': x__validate_netloc__mutmut_8, 
    'x__validate_netloc__mutmut_9': x__validate_netloc__mutmut_9, 
    'x__validate_netloc__mutmut_10': x__validate_netloc__mutmut_10, 
    'x__validate_netloc__mutmut_11': x__validate_netloc__mutmut_11, 
    'x__validate_netloc__mutmut_12': x__validate_netloc__mutmut_12, 
    'x__validate_netloc__mutmut_13': x__validate_netloc__mutmut_13, 
    'x__validate_netloc__mutmut_14': x__validate_netloc__mutmut_14, 
    'x__validate_netloc__mutmut_15': x__validate_netloc__mutmut_15, 
    'x__validate_netloc__mutmut_16': x__validate_netloc__mutmut_16, 
    'x__validate_netloc__mutmut_17': x__validate_netloc__mutmut_17, 
    'x__validate_netloc__mutmut_18': x__validate_netloc__mutmut_18, 
    'x__validate_netloc__mutmut_19': x__validate_netloc__mutmut_19, 
    'x__validate_netloc__mutmut_20': x__validate_netloc__mutmut_20, 
    'x__validate_netloc__mutmut_21': x__validate_netloc__mutmut_21, 
    'x__validate_netloc__mutmut_22': x__validate_netloc__mutmut_22, 
    'x__validate_netloc__mutmut_23': x__validate_netloc__mutmut_23, 
    'x__validate_netloc__mutmut_24': x__validate_netloc__mutmut_24, 
    'x__validate_netloc__mutmut_25': x__validate_netloc__mutmut_25, 
    'x__validate_netloc__mutmut_26': x__validate_netloc__mutmut_26, 
    'x__validate_netloc__mutmut_27': x__validate_netloc__mutmut_27, 
    'x__validate_netloc__mutmut_28': x__validate_netloc__mutmut_28, 
    'x__validate_netloc__mutmut_29': x__validate_netloc__mutmut_29, 
    'x__validate_netloc__mutmut_30': x__validate_netloc__mutmut_30, 
    'x__validate_netloc__mutmut_31': x__validate_netloc__mutmut_31, 
    'x__validate_netloc__mutmut_32': x__validate_netloc__mutmut_32, 
    'x__validate_netloc__mutmut_33': x__validate_netloc__mutmut_33, 
    'x__validate_netloc__mutmut_34': x__validate_netloc__mutmut_34, 
    'x__validate_netloc__mutmut_35': x__validate_netloc__mutmut_35, 
    'x__validate_netloc__mutmut_36': x__validate_netloc__mutmut_36, 
    'x__validate_netloc__mutmut_37': x__validate_netloc__mutmut_37, 
    'x__validate_netloc__mutmut_38': x__validate_netloc__mutmut_38, 
    'x__validate_netloc__mutmut_39': x__validate_netloc__mutmut_39, 
    'x__validate_netloc__mutmut_40': x__validate_netloc__mutmut_40, 
    'x__validate_netloc__mutmut_41': x__validate_netloc__mutmut_41, 
    'x__validate_netloc__mutmut_42': x__validate_netloc__mutmut_42, 
    'x__validate_netloc__mutmut_43': x__validate_netloc__mutmut_43, 
    'x__validate_netloc__mutmut_44': x__validate_netloc__mutmut_44, 
    'x__validate_netloc__mutmut_45': x__validate_netloc__mutmut_45, 
    'x__validate_netloc__mutmut_46': x__validate_netloc__mutmut_46, 
    'x__validate_netloc__mutmut_47': x__validate_netloc__mutmut_47, 
    'x__validate_netloc__mutmut_48': x__validate_netloc__mutmut_48, 
    'x__validate_netloc__mutmut_49': x__validate_netloc__mutmut_49, 
    'x__validate_netloc__mutmut_50': x__validate_netloc__mutmut_50, 
    'x__validate_netloc__mutmut_51': x__validate_netloc__mutmut_51, 
    'x__validate_netloc__mutmut_52': x__validate_netloc__mutmut_52, 
    'x__validate_netloc__mutmut_53': x__validate_netloc__mutmut_53, 
    'x__validate_netloc__mutmut_54': x__validate_netloc__mutmut_54, 
    'x__validate_netloc__mutmut_55': x__validate_netloc__mutmut_55, 
    'x__validate_netloc__mutmut_56': x__validate_netloc__mutmut_56, 
    'x__validate_netloc__mutmut_57': x__validate_netloc__mutmut_57, 
    'x__validate_netloc__mutmut_58': x__validate_netloc__mutmut_58, 
    'x__validate_netloc__mutmut_59': x__validate_netloc__mutmut_59, 
    'x__validate_netloc__mutmut_60': x__validate_netloc__mutmut_60, 
    'x__validate_netloc__mutmut_61': x__validate_netloc__mutmut_61, 
    'x__validate_netloc__mutmut_62': x__validate_netloc__mutmut_62, 
    'x__validate_netloc__mutmut_63': x__validate_netloc__mutmut_63, 
    'x__validate_netloc__mutmut_64': x__validate_netloc__mutmut_64, 
    'x__validate_netloc__mutmut_65': x__validate_netloc__mutmut_65, 
    'x__validate_netloc__mutmut_66': x__validate_netloc__mutmut_66, 
    'x__validate_netloc__mutmut_67': x__validate_netloc__mutmut_67, 
    'x__validate_netloc__mutmut_68': x__validate_netloc__mutmut_68, 
    'x__validate_netloc__mutmut_69': x__validate_netloc__mutmut_69, 
    'x__validate_netloc__mutmut_70': x__validate_netloc__mutmut_70, 
    'x__validate_netloc__mutmut_71': x__validate_netloc__mutmut_71, 
    'x__validate_netloc__mutmut_72': x__validate_netloc__mutmut_72, 
    'x__validate_netloc__mutmut_73': x__validate_netloc__mutmut_73, 
    'x__validate_netloc__mutmut_74': x__validate_netloc__mutmut_74, 
    'x__validate_netloc__mutmut_75': x__validate_netloc__mutmut_75, 
    'x__validate_netloc__mutmut_76': x__validate_netloc__mutmut_76, 
    'x__validate_netloc__mutmut_77': x__validate_netloc__mutmut_77, 
    'x__validate_netloc__mutmut_78': x__validate_netloc__mutmut_78, 
    'x__validate_netloc__mutmut_79': x__validate_netloc__mutmut_79, 
    'x__validate_netloc__mutmut_80': x__validate_netloc__mutmut_80, 
    'x__validate_netloc__mutmut_81': x__validate_netloc__mutmut_81, 
    'x__validate_netloc__mutmut_82': x__validate_netloc__mutmut_82, 
    'x__validate_netloc__mutmut_83': x__validate_netloc__mutmut_83, 
    'x__validate_netloc__mutmut_84': x__validate_netloc__mutmut_84, 
    'x__validate_netloc__mutmut_85': x__validate_netloc__mutmut_85, 
    'x__validate_netloc__mutmut_86': x__validate_netloc__mutmut_86, 
    'x__validate_netloc__mutmut_87': x__validate_netloc__mutmut_87, 
    'x__validate_netloc__mutmut_88': x__validate_netloc__mutmut_88, 
    'x__validate_netloc__mutmut_89': x__validate_netloc__mutmut_89, 
    'x__validate_netloc__mutmut_90': x__validate_netloc__mutmut_90, 
    'x__validate_netloc__mutmut_91': x__validate_netloc__mutmut_91, 
    'x__validate_netloc__mutmut_92': x__validate_netloc__mutmut_92, 
    'x__validate_netloc__mutmut_93': x__validate_netloc__mutmut_93, 
    'x__validate_netloc__mutmut_94': x__validate_netloc__mutmut_94, 
    'x__validate_netloc__mutmut_95': x__validate_netloc__mutmut_95, 
    'x__validate_netloc__mutmut_96': x__validate_netloc__mutmut_96, 
    'x__validate_netloc__mutmut_97': x__validate_netloc__mutmut_97, 
    'x__validate_netloc__mutmut_98': x__validate_netloc__mutmut_98, 
    'x__validate_netloc__mutmut_99': x__validate_netloc__mutmut_99, 
    'x__validate_netloc__mutmut_100': x__validate_netloc__mutmut_100, 
    'x__validate_netloc__mutmut_101': x__validate_netloc__mutmut_101, 
    'x__validate_netloc__mutmut_102': x__validate_netloc__mutmut_102, 
    'x__validate_netloc__mutmut_103': x__validate_netloc__mutmut_103
}

def _validate_netloc(*args, **kwargs):
    result = _mutmut_trampoline(x__validate_netloc__mutmut_orig, x__validate_netloc__mutmut_mutants, args, kwargs)
    return result 

_validate_netloc.__signature__ = _mutmut_signature(x__validate_netloc__mutmut_orig)
x__validate_netloc__mutmut_orig.__name__ = 'x__validate_netloc'


def x__validate_optionals__mutmut_orig(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, separator="&")
            and parse_qs(query, strict_parsing=strict_query, separator=";")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", fragment, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_1(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = None
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, separator="&")
            and parse_qs(query, strict_parsing=strict_query, separator=";")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", fragment, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_2(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = False
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, separator="&")
            and parse_qs(query, strict_parsing=strict_query, separator=";")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", fragment, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_3(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments = bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, separator="&")
            and parse_qs(query, strict_parsing=strict_query, separator=";")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", fragment, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_4(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments |= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, separator="&")
            and parse_qs(query, strict_parsing=strict_query, separator=";")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", fragment, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_5(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(None)
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, separator="&")
            and parse_qs(query, strict_parsing=strict_query, separator=";")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", fragment, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_6(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(None))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, separator="&")
            and parse_qs(query, strict_parsing=strict_query, separator=";")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", fragment, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_7(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, separator="&") or parse_qs(query, strict_parsing=strict_query, separator=";")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", fragment, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_8(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query or parse_qs(query, strict_parsing=strict_query, separator="&")
            and parse_qs(query, strict_parsing=strict_query, separator=";")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", fragment, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_9(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(None, strict_parsing=strict_query, separator="&")
            and parse_qs(query, strict_parsing=strict_query, separator=";")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", fragment, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_10(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=None, separator="&")
            and parse_qs(query, strict_parsing=strict_query, separator=";")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", fragment, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_11(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, separator=None)
            and parse_qs(query, strict_parsing=strict_query, separator=";")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", fragment, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_12(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(strict_parsing=strict_query, separator="&")
            and parse_qs(query, strict_parsing=strict_query, separator=";")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", fragment, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_13(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, separator="&")
            and parse_qs(query, strict_parsing=strict_query, separator=";")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", fragment, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_14(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, )
            and parse_qs(query, strict_parsing=strict_query, separator=";")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", fragment, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_15(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, separator="XX&XX")
            and parse_qs(query, strict_parsing=strict_query, separator=";")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", fragment, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_16(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, separator="&")
            and parse_qs(None, strict_parsing=strict_query, separator=";")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", fragment, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_17(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, separator="&")
            and parse_qs(query, strict_parsing=None, separator=";")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", fragment, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_18(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, separator="&")
            and parse_qs(query, strict_parsing=strict_query, separator=None)
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", fragment, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_19(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, separator="&")
            and parse_qs(strict_parsing=strict_query, separator=";")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", fragment, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_20(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, separator="&")
            and parse_qs(query, separator=";")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", fragment, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_21(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, separator="&")
            and parse_qs(query, strict_parsing=strict_query, )
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", fragment, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_22(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, separator="&")
            and parse_qs(query, strict_parsing=strict_query, separator="XX;XX")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", fragment, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_23(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, separator="&")
            and parse_qs(query, strict_parsing=strict_query, separator=";")
        ):
            optional_segments = True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", fragment, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_24(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, separator="&")
            and parse_qs(query, strict_parsing=strict_query, separator=";")
        ):
            optional_segments |= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", fragment, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_25(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, separator="&")
            and parse_qs(query, strict_parsing=strict_query, separator=";")
        ):
            optional_segments &= False
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", fragment, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_26(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, separator="&")
            and parse_qs(query, strict_parsing=strict_query, separator=";")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query or parse_qs(query, strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", fragment, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_27(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, separator="&")
            and parse_qs(query, strict_parsing=strict_query, separator=";")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(None, strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", fragment, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_28(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, separator="&")
            and parse_qs(query, strict_parsing=strict_query, separator=";")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=None):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", fragment, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_29(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, separator="&")
            and parse_qs(query, strict_parsing=strict_query, separator=";")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", fragment, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_30(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, separator="&")
            and parse_qs(query, strict_parsing=strict_query, separator=";")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, ):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", fragment, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_31(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, separator="&")
            and parse_qs(query, strict_parsing=strict_query, separator=";")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments = True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", fragment, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_32(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, separator="&")
            and parse_qs(query, strict_parsing=strict_query, separator=";")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments |= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", fragment, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_33(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, separator="&")
            and parse_qs(query, strict_parsing=strict_query, separator=";")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments &= False
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", fragment, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_34(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, separator="&")
            and parse_qs(query, strict_parsing=strict_query, separator=";")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments = bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", fragment, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_35(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, separator="&")
            and parse_qs(query, strict_parsing=strict_query, separator=";")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments |= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", fragment, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_36(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, separator="&")
            and parse_qs(query, strict_parsing=strict_query, separator=";")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            None
        )
    return optional_segments


def x__validate_optionals__mutmut_37(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, separator="&")
            and parse_qs(query, strict_parsing=strict_query, separator=";")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(None, fragment, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_38(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, separator="&")
            and parse_qs(query, strict_parsing=strict_query, separator=";")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", None, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_39(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, separator="&")
            and parse_qs(query, strict_parsing=strict_query, separator=";")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", fragment, None)
        )
    return optional_segments


def x__validate_optionals__mutmut_40(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, separator="&")
            and parse_qs(query, strict_parsing=strict_query, separator=";")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(fragment, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_41(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, separator="&")
            and parse_qs(query, strict_parsing=strict_query, separator=";")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_42(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, separator="&")
            and parse_qs(query, strict_parsing=strict_query, separator=";")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", fragment, )
        )
    return optional_segments


def x__validate_optionals__mutmut_43(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, separator="&")
            and parse_qs(query, strict_parsing=strict_query, separator=";")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"XX[0-9a-z?/:@\-._~%!$&'()*+,;=#]*XX", fragment, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_44(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, separator="&")
            and parse_qs(query, strict_parsing=strict_query, separator=";")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", fragment, re.IGNORECASE)
        )
    return optional_segments


def x__validate_optionals__mutmut_45(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    try:
        if (
            query
            # ref: https://github.com/python/cpython/issues/117109
            and parse_qs(query, strict_parsing=strict_query, separator="&")
            and parse_qs(query, strict_parsing=strict_query, separator=";")
        ):
            optional_segments &= True
    except TypeError:
        # for Python < v3.9.2 (official v3.10)
        if query and parse_qs(query, strict_parsing=strict_query):
            optional_segments &= True
    if fragment:
        # See RFC3986 Section 3.5 Fragment for allowed characters
        # Adding "#", see https://github.com/python-validators/validators/issues/403
        optional_segments &= bool(
            re.fullmatch(r"[0-9A-Z?/:@\-._~%!$&'()*+,;=#]*", fragment, re.IGNORECASE)
        )
    return optional_segments

x__validate_optionals__mutmut_mutants : ClassVar[MutantDict] = {
'x__validate_optionals__mutmut_1': x__validate_optionals__mutmut_1, 
    'x__validate_optionals__mutmut_2': x__validate_optionals__mutmut_2, 
    'x__validate_optionals__mutmut_3': x__validate_optionals__mutmut_3, 
    'x__validate_optionals__mutmut_4': x__validate_optionals__mutmut_4, 
    'x__validate_optionals__mutmut_5': x__validate_optionals__mutmut_5, 
    'x__validate_optionals__mutmut_6': x__validate_optionals__mutmut_6, 
    'x__validate_optionals__mutmut_7': x__validate_optionals__mutmut_7, 
    'x__validate_optionals__mutmut_8': x__validate_optionals__mutmut_8, 
    'x__validate_optionals__mutmut_9': x__validate_optionals__mutmut_9, 
    'x__validate_optionals__mutmut_10': x__validate_optionals__mutmut_10, 
    'x__validate_optionals__mutmut_11': x__validate_optionals__mutmut_11, 
    'x__validate_optionals__mutmut_12': x__validate_optionals__mutmut_12, 
    'x__validate_optionals__mutmut_13': x__validate_optionals__mutmut_13, 
    'x__validate_optionals__mutmut_14': x__validate_optionals__mutmut_14, 
    'x__validate_optionals__mutmut_15': x__validate_optionals__mutmut_15, 
    'x__validate_optionals__mutmut_16': x__validate_optionals__mutmut_16, 
    'x__validate_optionals__mutmut_17': x__validate_optionals__mutmut_17, 
    'x__validate_optionals__mutmut_18': x__validate_optionals__mutmut_18, 
    'x__validate_optionals__mutmut_19': x__validate_optionals__mutmut_19, 
    'x__validate_optionals__mutmut_20': x__validate_optionals__mutmut_20, 
    'x__validate_optionals__mutmut_21': x__validate_optionals__mutmut_21, 
    'x__validate_optionals__mutmut_22': x__validate_optionals__mutmut_22, 
    'x__validate_optionals__mutmut_23': x__validate_optionals__mutmut_23, 
    'x__validate_optionals__mutmut_24': x__validate_optionals__mutmut_24, 
    'x__validate_optionals__mutmut_25': x__validate_optionals__mutmut_25, 
    'x__validate_optionals__mutmut_26': x__validate_optionals__mutmut_26, 
    'x__validate_optionals__mutmut_27': x__validate_optionals__mutmut_27, 
    'x__validate_optionals__mutmut_28': x__validate_optionals__mutmut_28, 
    'x__validate_optionals__mutmut_29': x__validate_optionals__mutmut_29, 
    'x__validate_optionals__mutmut_30': x__validate_optionals__mutmut_30, 
    'x__validate_optionals__mutmut_31': x__validate_optionals__mutmut_31, 
    'x__validate_optionals__mutmut_32': x__validate_optionals__mutmut_32, 
    'x__validate_optionals__mutmut_33': x__validate_optionals__mutmut_33, 
    'x__validate_optionals__mutmut_34': x__validate_optionals__mutmut_34, 
    'x__validate_optionals__mutmut_35': x__validate_optionals__mutmut_35, 
    'x__validate_optionals__mutmut_36': x__validate_optionals__mutmut_36, 
    'x__validate_optionals__mutmut_37': x__validate_optionals__mutmut_37, 
    'x__validate_optionals__mutmut_38': x__validate_optionals__mutmut_38, 
    'x__validate_optionals__mutmut_39': x__validate_optionals__mutmut_39, 
    'x__validate_optionals__mutmut_40': x__validate_optionals__mutmut_40, 
    'x__validate_optionals__mutmut_41': x__validate_optionals__mutmut_41, 
    'x__validate_optionals__mutmut_42': x__validate_optionals__mutmut_42, 
    'x__validate_optionals__mutmut_43': x__validate_optionals__mutmut_43, 
    'x__validate_optionals__mutmut_44': x__validate_optionals__mutmut_44, 
    'x__validate_optionals__mutmut_45': x__validate_optionals__mutmut_45
}

def _validate_optionals(*args, **kwargs):
    result = _mutmut_trampoline(x__validate_optionals__mutmut_orig, x__validate_optionals__mutmut_mutants, args, kwargs)
    return result 

_validate_optionals.__signature__ = _mutmut_signature(x__validate_optionals__mutmut_orig)
x__validate_optionals__mutmut_orig.__name__ = 'x__validate_optionals'


@validator
def url(
    value: str,
    /,
    *,
    skip_ipv6_addr: bool = False,
    skip_ipv4_addr: bool = False,
    may_have_port: bool = True,
    simple_host: bool = False,
    strict_query: bool = True,
    consider_tld: bool = False,
    private: Optional[bool] = None,  # only for ip-addresses
    rfc_1034: bool = False,
    rfc_2782: bool = False,
    validate_scheme: Callable[[str], bool] = _validate_scheme,
):
    r"""Return whether or not given value is a valid URL.

    This validator was originally inspired from [URL validator of dperini][1].
    The following diagram is from [urlly][2]::


            foo://admin:hunter1@example.com:8042/over/there?name=ferret#nose
            \_/   \___/ \_____/ \_________/ \__/\_________/ \_________/ \__/
             |      |       |       |        |       |          |         |
          scheme username password hostname port    path      query    fragment

    [1]: https://gist.github.com/dperini/729294
    [2]: https://github.com/treeform/urlly

    Examples:
        >>> url('http://duck.com')
        True
        >>> url('ftp://foobar.dk')
        True
        >>> url('http://10.0.0.1')
        True
        >>> url('http://example.com/">user@example.com')
        ValidationError(func=url, args={'value': 'http://example.com/">user@example.com'})

    Args:
        value:
            URL string to validate.
        skip_ipv6_addr:
            When URL string cannot contain an IPv6 address.
        skip_ipv4_addr:
            When URL string cannot contain an IPv4 address.
        may_have_port:
            URL string may contain port number.
        simple_host:
            URL string maybe only hyphens and alpha-numerals.
        strict_query:
            Fail validation on query string parsing error.
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
        validate_scheme:
            Function that validates URL scheme.

    Returns:
        (Literal[True]): If `value` is a valid url.
        (ValidationError): If `value` is an invalid url.
    """
    if not value or re.search(r"\s", value):
        # url must not contain any white
        # spaces, they must be encoded
        return False

    try:
        scheme, netloc, path, query, fragment = urlsplit(value)
    except ValueError:
        return False

    return (
        validate_scheme(scheme)
        and _validate_netloc(
            netloc,
            skip_ipv6_addr,
            skip_ipv4_addr,
            may_have_port,
            simple_host,
            consider_tld,
            private,
            rfc_1034,
            rfc_2782,
        )
        and _validate_optionals(path, query, fragment, strict_query)
    )
