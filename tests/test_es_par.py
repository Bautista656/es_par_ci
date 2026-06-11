import pytest
from es_par import es_par


def test_numero_par():
    assert es_par(8) is True


def test_numero_impar():
    assert es_par(7) is False


def test_cero_es_par():
    assert es_par(0) is True


def test_numero_negativo_par():
    assert es_par(-4) is True


def test_entrada_invalida_texto():
    with pytest.raises(TypeError):
        es_par("8")