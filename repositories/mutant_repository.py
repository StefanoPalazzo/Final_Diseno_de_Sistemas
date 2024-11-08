from model import db, Mutant

class MutantRepository:
    @staticmethod
    def get_by_dna(dna_sequence):
        return Mutant.query.filter_by(dna_sequence=dna_sequence).first()
    
    @staticmethod
    def get_all():
        return Mutant.query.all()
    
    @staticmethod
    def save(dna_sequence, is_mutant):
        # Convertir el JSON de ADN a una cadena para compararla con los registros en la base de datos
        dna_sequence_str = "{" + ",".join(dna_sequence) + "}"
    
        
        # Verificar si el ADN ya existe en la base de datos
        existing_record = Mutant.query.filter_by(dna_sequence=dna_sequence_str).first()
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