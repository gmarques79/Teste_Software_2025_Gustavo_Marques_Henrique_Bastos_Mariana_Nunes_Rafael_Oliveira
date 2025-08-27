"""Test Finance."""

# external
import pytest

# local
from validators import ValidationError, cusip, isin, sedol

# ==> CUSIP <== #


@pytest.mark.parametrize(
    "value",
    [
        # Casos de teste originais
        "912796X38",
        "912796X20",
        "912796x20",

        # --- NOVOS TESTES DIRECIONADOS (COM CHECKSUMS CORRIGIDOS) ---
        
        # 1. Testando as fronteiras de letras e números
        "A12345673",  # Contém 'A' (fronteira inferior de letras)
        "Z12345676",  # Contém 'Z' (fronteira superior de letras)
        "123456782",  # Usa o dígito '8'
        "123456790",  # Usa o dígito '9' (checksum é 0)

        # 2. Testando os caracteres especiais
        "*12345675",  # Contém '*' (asterisco)
        "@12345674",  # Contém '@' (arroba)
        "#12345673",  # Contém '#' (cerquilha)

        # 3. Teste para estressar a lógica de soma (um exemplo da Wikipedia)
        "037833100",

        "a12345673", # Contém 'a' (fronteira inferior de minúsculas) 
        "z12345676", # Contém 'z' (fronteira superior de minúsculas)
    ],)
def test_returns_true_on_valid_cusip(value: str):
    """Test returns true on valid cusip."""
    assert cusip(value)


@pytest.mark.parametrize(
    "value",
    [
        # Casos inválidos originais
        "912796T67",
        "912796T68",
        "XCVF",
        "00^^^1234",

        # Comprimento inválido
        "12345678",     # 8 caracteres
        "12345678901",  # 11 caracteres

        # Checksum incorreto
        "037833101",  # válido seria ...100
        "912796X39",  # válido seria ...38

        # Caracteres ilegais
        "12345$678",   # símbolo no meio
        "abcdefghi",   # letras minúsculas      
    ],
)
def test_returns_failed_validation_on_invalid_cusip(value: str):
    """Test returns failed validation on invalid cusip."""
    assert isinstance(cusip(value), ValidationError)


# ==> ISIN <== #


@pytest.mark.parametrize("value", ["US0004026250", "JP000K0VF054", "US0378331005"])
def test_returns_true_on_valid_isin(value: str):
    """Test returns true on valid isin."""
    assert isin(value)


@pytest.mark.parametrize("value", ["010378331005", "XCVF", "00^^^1234", "A000009"])
def test_returns_failed_validation_on_invalid_isin(value: str):
    """Test returns failed validation on invalid isin."""
    assert isinstance(isin(value), ValidationError)


# ==> SEDOL <== #


@pytest.mark.parametrize("value", ["0263494", "0540528", "B000009"])
def test_returns_true_on_valid_sedol(value: str):
    """Test returns true on valid sedol."""
    assert sedol(value)


@pytest.mark.parametrize("value", ["0540526", "XCVF", "00^^^1234", "A000009"])
def test_returns_failed_validation_on_invalid_sedol(value: str):
    """Test returns failed validation on invalid sedol."""
    assert isinstance(sedol(value), ValidationError)
