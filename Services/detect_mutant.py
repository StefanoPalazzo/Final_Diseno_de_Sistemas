def is_mutant(dna):
    n = len(dna)
    
    # Validar que la matriz sea NxN y contenga solo caracteres válidos
    for row in dna:
        if len(row) != n or any(base not in "ATCG" for base in row):
            raise ValueError("La matriz debe ser NxN y contener solo las letras 'A', 'T', 'C', 'G'")
    
    def has_sequence(x, y, dx, dy):
        """
        Verifica si hay una secuencia de cuatro letras iguales comenzando
        desde la posición (x, y) en la dirección dada por (dx, dy).
        """
        base = dna[x][y]
        for i in range(1, 4):
            nx, ny = x + dx * i, y + dy * i
            if nx < 0 or ny < 0 or nx >= n or ny >= n or dna[nx][ny] != base:
                return False
        return True

    sequences_found = 0

    # Buscar secuencias de cuatro letras iguales en todas las direcciones posibles
    for i in range(n):
        for j in range(n):
            if dna[i][j] in 'ATCG':
                # Horizontal derecha
                if j + 3 < n and has_sequence(i, j, 0, 1):
                    sequences_found += 1
                # Vertical hacia abajo
                if i + 3 < n and has_sequence(i, j, 1, 0):
                    sequences_found += 1
                # Diagonal derecha hacia abajo
                if i + 3 < n and j + 3 < n and has_sequence(i, j, 1, 1):
                    sequences_found += 1
                # Diagonal izquierda hacia abajo
                if i + 3 < n and j - 3 >= 0 and has_sequence(i, j, 1, -1):
                    sequences_found += 1
                
                # Si encontramos más de una secuencia, es mutante
                if sequences_found > 1:
                    return True

    return False

