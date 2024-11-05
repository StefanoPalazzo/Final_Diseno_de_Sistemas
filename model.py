from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

class Mutant(db.Model):
    __tablename__ = 'mutants'
    
    id = db.Column(db.Integer, primary_key=True)
    dna_sequence = db.Column(db.String, unique=True, nullable=False)
    is_mutant = db.Column(db.Boolean, nullable=False)

    def __init__(self, dna_sequence, is_mutant):
        self.dna_sequence = dna_sequence
        self.is_mutant = is_mutant
