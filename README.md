# API con Python y Flask para detección de Gen Mutante

Este proyecto implementa una API REST con Python y Flask para la detección de genes mutantes dada una matriz de ADN.



## Tabla de Contenidos

- [Instalación Local (Opcional)](#instalación)
- [Uso](#uso)
- [Testing](#testing)


## Instalación Local (Opcional):

1. Clonar el repositorio:

```bash
git clone
```
2. Crear un entorno virtual:

```bash
python3 -m venv venv
```
3. Activar el entorno virtual:

```bash
# En Linux
source venv/bin/activate
# En Windows
venv\Scripts\activate
```
4. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

5. Ejecutar la aplicación:

```bash
python -m Controllers.mutant_controller
```

## Uso

### En local

Para probar la API en local, se puede utilizar la siguiente URL con Postman o cualquier otra herramienta de pruebas de APIs:

```bash
http://127.0.0.1:5000
```

### En render

Para probar la API en render, se debe utilizar la siguiente URL:

```bash
https://final-diseno-de-sistemas.onrender.com/
```

### Endpoints

#### GET /mutantes/

Retorna la base de DNA de los mutantes y humanos detectados.

#### POST /mutant/

Debe enviarse un DNA en formato JSON con la siguiente estructura:

```json
{
    "dna": ["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]
}
```
El endpoint retornará un código de estado 200 si el DNA es mutante, y un código de estado 403 si el DNA es humano.

#### GET /stats/

Retorna las estadísticas de los DNA analizados.



## Testing

Para ejecutar las pruebas unitarias, se debe correr el siguiente comando:

```bash
coverage run -m pytest ; coverage report 
```