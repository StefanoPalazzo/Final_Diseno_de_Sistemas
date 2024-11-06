from repositories.mutant_repository import MutantRepository

def is_mutant(dna):
    n = len(dna)
    sequences_found = 0
    directions = [
        (0, 1),  # Horizontal
        (1, 0),  # Vertical
        (1, 1),  # Diagonal ↘
        (1, -1)  # Diagonal ↙
    ]

    # Validar que la matriz sea NxN y contenga solo caracteres válidos
    valid_chars = {'A', 'T', 'C', 'G'}
    if not all(len(row) == n and set(row).issubset(valid_chars) for row in dna):
        raise ValueError("La matriz debe ser NxN y contener solo las letras 'A', 'T', 'C', 'G'")

    for i in range(n):
        for j in range(n):
            for dx, dy in directions:
                try:
                    base = dna[i][j]
                    if all(dna[i + k * dx][j + k * dy] == base for k in range(1, 4)):
                        sequences_found += 1
                        if sequences_found > 1:
                            return True
                except IndexError:
                    continue  # Salta si se sale de los límites de la matriz

    return False


def detect_and_save(dna):
    ismutant = is_mutant(dna)
    Result = MutantRepository.save(dna, ismutant)
    return ismutant, Result