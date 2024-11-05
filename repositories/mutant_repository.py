from model import db, Mutant

class MutantRepository:
    @staticmethod
    def get_by_dna(dna_sequence):
        return Mutant.query.filter_by(dna_sequence=dna_sequence).first()
    
    @staticmethod
    def save(dna_sequence, is_mutant):
        # Verificar si ya existe el ADN en la base de datos
        existing_record = Mutant.query.filter_by(dna_sequence=dna_sequence).first()
        if existing_record:
            return False  # ADN ya registrado
        
        new_dna = Mutant(dna_sequence=dna_sequence, is_mutant=is_mutant)
        db.session.add(new_dna)
        db.session.commit()
        return True
    
    @staticmethod
    def get_stats():
        count_mutant_dna = Mutant.query.filter_by(is_mutant=True).count()
        count_human_dna = Mutant.query.filter_by(is_mutant=False).count()
        ratio = count_mutant_dna / (count_human_dna or 1)
        return {
            "count_mutant_dna": count_mutant_dna,
            "count_human_dna": count_human_dna,
            "ratio": round(ratio, 2)
        }