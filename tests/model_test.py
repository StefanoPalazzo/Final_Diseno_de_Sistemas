import unittest
from model import db, Mutant
from flask import Flask

def test_to_json():
    mutant = Mutant(1, ["ABC"])
    mutant.id = 1
    mutant.dna_sequence = ["ABC"]
    mutant.is_mutant = True
    assert mutant.to_dict() == {"id": 1, "dna_sequence": ["ABC"], "is_mutant": True}