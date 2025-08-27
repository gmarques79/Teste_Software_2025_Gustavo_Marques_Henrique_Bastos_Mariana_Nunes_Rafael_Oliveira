"""Utils."""

# standard
from functools import wraps
from inspect import getfullargspec
from itertools import chain
from os import environ
from typing import Any, Callable, Dict
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


class ValidationError(Exception):
    """Exception class when validation failure occurs."""

    def xǁValidationErrorǁ__init____mutmut_orig(self, function: Callable[..., Any], arg_dict: Dict[str, Any], message: str = ""):
        """Initialize Validation Failure."""
        if message:
            self.reason = message
        self.func = function
        self.__dict__.update(arg_dict)

    def xǁValidationErrorǁ__init____mutmut_1(self, function: Callable[..., Any], arg_dict: Dict[str, Any], message: str = "XXXX"):
        """Initialize Validation Failure."""
        if message:
            self.reason = message
        self.func = function
        self.__dict__.update(arg_dict)

    def xǁValidationErrorǁ__init____mutmut_2(self, function: Callable[..., Any], arg_dict: Dict[str, Any], message: str = ""):
        """Initialize Validation Failure."""
        if message:
            self.reason = None
        self.func = function
        self.__dict__.update(arg_dict)

    def xǁValidationErrorǁ__init____mutmut_3(self, function: Callable[..., Any], arg_dict: Dict[str, Any], message: str = ""):
        """Initialize Validation Failure."""
        if message:
            self.reason = message
        self.func = None
        self.__dict__.update(arg_dict)

    def xǁValidationErrorǁ__init____mutmut_4(self, function: Callable[..., Any], arg_dict: Dict[str, Any], message: str = ""):
        """Initialize Validation Failure."""
        if message:
            self.reason = message
        self.func = function
        self.__dict__.update(None)
    
    xǁValidationErrorǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁValidationErrorǁ__init____mutmut_1': xǁValidationErrorǁ__init____mutmut_1, 
        'xǁValidationErrorǁ__init____mutmut_2': xǁValidationErrorǁ__init____mutmut_2, 
        'xǁValidationErrorǁ__init____mutmut_3': xǁValidationErrorǁ__init____mutmut_3, 
        'xǁValidationErrorǁ__init____mutmut_4': xǁValidationErrorǁ__init____mutmut_4
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁValidationErrorǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁValidationErrorǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁValidationErrorǁ__init____mutmut_orig)
    xǁValidationErrorǁ__init____mutmut_orig.__name__ = 'xǁValidationErrorǁ__init__'

    def xǁValidationErrorǁ__repr____mutmut_orig(self):
        """Repr Validation Failure."""
        return (
            f"ValidationError(func={self.func.__name__}, "
            + f"args={ ({k: v for (k, v) in self.__dict__.items() if k != 'func'}) })"
        )

    def xǁValidationErrorǁ__repr____mutmut_1(self):
        """Repr Validation Failure."""
        return (
            f"ValidationError(func={self.func.__name__}, " - f"args={ ({k: v for (k, v) in self.__dict__.items() if k != 'func'}) })"
        )

    def xǁValidationErrorǁ__repr____mutmut_2(self):
        """Repr Validation Failure."""
        return (
            f"ValidationError(func={self.func.__name__}, "
            + f"args={ ({k: v for (k, v) in self.__dict__.items() if k == 'func'}) })"
        )

    def xǁValidationErrorǁ__repr____mutmut_3(self):
        """Repr Validation Failure."""
        return (
            f"ValidationError(func={self.func.__name__}, "
            + f"args={ ({k: v for (k, v) in self.__dict__.items() if k != 'XXfuncXX'}) })"
        )

    def xǁValidationErrorǁ__repr____mutmut_4(self):
        """Repr Validation Failure."""
        return (
            f"ValidationError(func={self.func.__name__}, "
            + f"args={ ({k: v for (k, v) in self.__dict__.items() if k != 'FUNC'}) })"
        )
    
    xǁValidationErrorǁ__repr____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁValidationErrorǁ__repr____mutmut_1': xǁValidationErrorǁ__repr____mutmut_1, 
        'xǁValidationErrorǁ__repr____mutmut_2': xǁValidationErrorǁ__repr____mutmut_2, 
        'xǁValidationErrorǁ__repr____mutmut_3': xǁValidationErrorǁ__repr____mutmut_3, 
        'xǁValidationErrorǁ__repr____mutmut_4': xǁValidationErrorǁ__repr____mutmut_4
    }
    
    def __repr__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁValidationErrorǁ__repr____mutmut_orig"), object.__getattribute__(self, "xǁValidationErrorǁ__repr____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __repr__.__signature__ = _mutmut_signature(xǁValidationErrorǁ__repr____mutmut_orig)
    xǁValidationErrorǁ__repr____mutmut_orig.__name__ = 'xǁValidationErrorǁ__repr__'

    def xǁValidationErrorǁ__str____mutmut_orig(self):
        """Str Validation Failure."""
        return repr(self)

    def xǁValidationErrorǁ__str____mutmut_1(self):
        """Str Validation Failure."""
        return repr(None)
    
    xǁValidationErrorǁ__str____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁValidationErrorǁ__str____mutmut_1': xǁValidationErrorǁ__str____mutmut_1
    }
    
    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁValidationErrorǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁValidationErrorǁ__str____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __str__.__signature__ = _mutmut_signature(xǁValidationErrorǁ__str____mutmut_orig)
    xǁValidationErrorǁ__str____mutmut_orig.__name__ = 'xǁValidationErrorǁ__str__'

    def xǁValidationErrorǁ__bool____mutmut_orig(self):
        """Bool Validation Failure."""
        return False

    def xǁValidationErrorǁ__bool____mutmut_1(self):
        """Bool Validation Failure."""
        return True
    
    xǁValidationErrorǁ__bool____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁValidationErrorǁ__bool____mutmut_1': xǁValidationErrorǁ__bool____mutmut_1
    }
    
    def __bool__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁValidationErrorǁ__bool____mutmut_orig"), object.__getattribute__(self, "xǁValidationErrorǁ__bool____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __bool__.__signature__ = _mutmut_signature(xǁValidationErrorǁ__bool____mutmut_orig)
    xǁValidationErrorǁ__bool____mutmut_orig.__name__ = 'xǁValidationErrorǁ__bool__'


def x__func_args_as_dict__mutmut_orig(func: Callable[..., Any], *args: Any, **kwargs: Any):
    """Return function's positional and key value arguments as an ordered dictionary."""
    return dict(
        list(zip(dict.fromkeys(chain(getfullargspec(func)[0], kwargs.keys())), args))
        + list(kwargs.items())
    )


def x__func_args_as_dict__mutmut_1(func: Callable[..., Any], *args: Any, **kwargs: Any):
    """Return function's positional and key value arguments as an ordered dictionary."""
    return dict(
        None
    )


def x__func_args_as_dict__mutmut_2(func: Callable[..., Any], *args: Any, **kwargs: Any):
    """Return function's positional and key value arguments as an ordered dictionary."""
    return dict(
        list(zip(dict.fromkeys(chain(getfullargspec(func)[0], kwargs.keys())), args)) - list(kwargs.items())
    )


def x__func_args_as_dict__mutmut_3(func: Callable[..., Any], *args: Any, **kwargs: Any):
    """Return function's positional and key value arguments as an ordered dictionary."""
    return dict(
        list(None)
        + list(kwargs.items())
    )


def x__func_args_as_dict__mutmut_4(func: Callable[..., Any], *args: Any, **kwargs: Any):
    """Return function's positional and key value arguments as an ordered dictionary."""
    return dict(
        list(zip(None, args))
        + list(kwargs.items())
    )


def x__func_args_as_dict__mutmut_5(func: Callable[..., Any], *args: Any, **kwargs: Any):
    """Return function's positional and key value arguments as an ordered dictionary."""
    return dict(
        list(zip(dict.fromkeys(chain(getfullargspec(func)[0], kwargs.keys())), None))
        + list(kwargs.items())
    )


def x__func_args_as_dict__mutmut_6(func: Callable[..., Any], *args: Any, **kwargs: Any):
    """Return function's positional and key value arguments as an ordered dictionary."""
    return dict(
        list(zip(args))
        + list(kwargs.items())
    )


def x__func_args_as_dict__mutmut_7(func: Callable[..., Any], *args: Any, **kwargs: Any):
    """Return function's positional and key value arguments as an ordered dictionary."""
    return dict(
        list(zip(dict.fromkeys(chain(getfullargspec(func)[0], kwargs.keys())), ))
        + list(kwargs.items())
    )


def x__func_args_as_dict__mutmut_8(func: Callable[..., Any], *args: Any, **kwargs: Any):
    """Return function's positional and key value arguments as an ordered dictionary."""
    return dict(
        list(zip(dict.fromkeys(None), args))
        + list(kwargs.items())
    )


def x__func_args_as_dict__mutmut_9(func: Callable[..., Any], *args: Any, **kwargs: Any):
    """Return function's positional and key value arguments as an ordered dictionary."""
    return dict(
        list(zip(dict.fromkeys(chain(None, kwargs.keys())), args))
        + list(kwargs.items())
    )


def x__func_args_as_dict__mutmut_10(func: Callable[..., Any], *args: Any, **kwargs: Any):
    """Return function's positional and key value arguments as an ordered dictionary."""
    return dict(
        list(zip(dict.fromkeys(chain(getfullargspec(func)[0], None)), args))
        + list(kwargs.items())
    )


def x__func_args_as_dict__mutmut_11(func: Callable[..., Any], *args: Any, **kwargs: Any):
    """Return function's positional and key value arguments as an ordered dictionary."""
    return dict(
        list(zip(dict.fromkeys(chain(kwargs.keys())), args))
        + list(kwargs.items())
    )


def x__func_args_as_dict__mutmut_12(func: Callable[..., Any], *args: Any, **kwargs: Any):
    """Return function's positional and key value arguments as an ordered dictionary."""
    return dict(
        list(zip(dict.fromkeys(chain(getfullargspec(func)[0], )), args))
        + list(kwargs.items())
    )


def x__func_args_as_dict__mutmut_13(func: Callable[..., Any], *args: Any, **kwargs: Any):
    """Return function's positional and key value arguments as an ordered dictionary."""
    return dict(
        list(zip(dict.fromkeys(chain(getfullargspec(None)[0], kwargs.keys())), args))
        + list(kwargs.items())
    )


def x__func_args_as_dict__mutmut_14(func: Callable[..., Any], *args: Any, **kwargs: Any):
    """Return function's positional and key value arguments as an ordered dictionary."""
    return dict(
        list(zip(dict.fromkeys(chain(getfullargspec(func)[1], kwargs.keys())), args))
        + list(kwargs.items())
    )


def x__func_args_as_dict__mutmut_15(func: Callable[..., Any], *args: Any, **kwargs: Any):
    """Return function's positional and key value arguments as an ordered dictionary."""
    return dict(
        list(zip(dict.fromkeys(chain(getfullargspec(func)[0], kwargs.keys())), args))
        + list(None)
    )

x__func_args_as_dict__mutmut_mutants : ClassVar[MutantDict] = {
'x__func_args_as_dict__mutmut_1': x__func_args_as_dict__mutmut_1, 
    'x__func_args_as_dict__mutmut_2': x__func_args_as_dict__mutmut_2, 
    'x__func_args_as_dict__mutmut_3': x__func_args_as_dict__mutmut_3, 
    'x__func_args_as_dict__mutmut_4': x__func_args_as_dict__mutmut_4, 
    'x__func_args_as_dict__mutmut_5': x__func_args_as_dict__mutmut_5, 
    'x__func_args_as_dict__mutmut_6': x__func_args_as_dict__mutmut_6, 
    'x__func_args_as_dict__mutmut_7': x__func_args_as_dict__mutmut_7, 
    'x__func_args_as_dict__mutmut_8': x__func_args_as_dict__mutmut_8, 
    'x__func_args_as_dict__mutmut_9': x__func_args_as_dict__mutmut_9, 
    'x__func_args_as_dict__mutmut_10': x__func_args_as_dict__mutmut_10, 
    'x__func_args_as_dict__mutmut_11': x__func_args_as_dict__mutmut_11, 
    'x__func_args_as_dict__mutmut_12': x__func_args_as_dict__mutmut_12, 
    'x__func_args_as_dict__mutmut_13': x__func_args_as_dict__mutmut_13, 
    'x__func_args_as_dict__mutmut_14': x__func_args_as_dict__mutmut_14, 
    'x__func_args_as_dict__mutmut_15': x__func_args_as_dict__mutmut_15
}

def _func_args_as_dict(*args, **kwargs):
    result = _mutmut_trampoline(x__func_args_as_dict__mutmut_orig, x__func_args_as_dict__mutmut_mutants, args, kwargs)
    return result 

_func_args_as_dict.__signature__ = _mutmut_signature(x__func_args_as_dict__mutmut_orig)
x__func_args_as_dict__mutmut_orig.__name__ = 'x__func_args_as_dict'


def validator(func: Callable[..., Any]):
    """A decorator that makes given function validator.

    Whenever the given `func` returns `False` this
    decorator returns `ValidationError` object.

    Examples:
        >>> @validator
        ... def even(value):
        ...     return not (value % 2)
        >>> even(4)
        True
        >>> even(5)
        ValidationError(func=even, args={'value': 5})

    Args:
        func:
            Function which is to be decorated.

    Returns:
        (Callable[..., ValidationError | Literal[True]]):
            A decorator which returns either `ValidationError`
            or `Literal[True]`.

    Raises:
        (ValidationError): If `r_ve` or `RAISE_VALIDATION_ERROR` is `True`
    """

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any):
        raise_validation_error = False
        if "r_ve" in kwargs:
            raise_validation_error = True
            del kwargs["r_ve"]
        if environ.get("RAISE_VALIDATION_ERROR", "False") == "True":
            raise_validation_error = True

        try:
            if raise_validation_error:
                if func(*args, **kwargs):
                    return True
                else:
                    raise ValidationError(func, _func_args_as_dict(func, *args, **kwargs))
            else:
                return (
                    True
                    if func(*args, **kwargs)
                    else ValidationError(func, _func_args_as_dict(func, *args, **kwargs))
                )
        except (ValueError, TypeError, UnicodeError) as exp:
            if raise_validation_error:
                raise ValidationError(
                    func, _func_args_as_dict(func, *args, **kwargs), str(exp)
                ) from exp
            else:
                return ValidationError(func, _func_args_as_dict(func, *args, **kwargs), str(exp))

    return wrapper
