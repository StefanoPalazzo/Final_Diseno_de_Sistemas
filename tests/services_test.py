import pytest
from Services.detect_mutant import is_mutant

def test_is_mutant_with_mutant_dna():
    dna = [
        "ATGCGA",
        "CAGTGC",
        "TTATGT",
        "AGAAGG",
        "CCCCTA",
        "TCACTG"
    ]
    assert is_mutant(dna) == True

def test_is_mutant_with_mutant_dna2():
    dna = [
        "ATGCGA",
        "CAGTGC",
        "TTATGT",
        "AGAAGG",
        "CCACTA",
        "TCACTG"
    ]
    assert is_mutant(dna) == True

def test_is_mutant_with_nonmutant_dna():
    dna = [
        "ATGCGA",
        "CGGTGC",
        "TTGAGT",
        "AGATTG",
        "CCACTA",
        "TCACTG"
    ]
    assert is_mutant(dna) == False

def test_is_mutant_with_invalid_dna_length():
    dna = [
        "ATGCGA",
        "CAGTGC",
        "TTATGT",
        "AGAAGG",
        "CCCCTA"
    ]
    with pytest.raises(ValueError, match="La matriz debe ser NxN y contener solo las letras 'A', 'T', 'C', 'G'"):
        is_mutant(dna)

def test_is_mutant_with_invalid_dna_characters():
    dna = [
        "ATGCGA",
        "CAGTGC",
        "TTATGT",
        "AGAAGG",
        "CCCXTA",
        "TCACTG"
    ]
    with pytest.raises(ValueError, match="La matriz debe ser NxN y contener solo las letras 'A', 'T', 'C', 'G'"):
        is_mutant(dna)

def test_is_mutant_with_horizontal_sequence():
    dna = [
        "AAAAAA",
        "CAGTGC",
        "TTATGT",
        "AGAAGG",
        "CCCCTA",
        "TCACTG"
    ]
    assert is_mutant(dna) == True

def test_is_mutant_with_vertical_sequence():
    dna = [
        "ATGCGA",
        "ATGTGC",
        "ATGAGT",
        "ATGTTG",
        "CCACTA",
        "TCACTG"
    ]
    assert is_mutant(dna) == True

def test_is_mutant_with_diagonal_right_sequence():
    dna = [
        "ATGCAA",
        "CAGTAC",
        "TTGTAT",
        "AGGTAG",
        "CCACTA",
        "TCACTG"
    ]
    assert is_mutant(dna) == True

def test_is_mutant_with_diagonal_left_sequence():
    dna = [
        "ATGCGA",
        "CAGTGC",
        "TTATGT",
        "AGGAGG",
        "CCACTA",
        "TCACTG"
    ]
    assert is_mutant(dna) == True