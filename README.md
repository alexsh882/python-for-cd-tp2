# TLP 3 - Python para Ciencia de datos
## Trabajo Práctico N° 2

El programa realiza lo siguiente:

**Agrupación y Exportación por Provincia:**
1. Agrupa las localidades por provincia.
2. Exporta cada grupo de localidades en un archivo de `.csv` separado.
3. Cada archivo CSV representa una provincia y contiene la lista de sus localidades.
4. Al final de cada lista del `.csv` contiene la cantidad total de localidades por provincia.

## Sobre el proyecto

Realizado con `python` y como persistencia `sqlite3`
- Para la estructura de carpetas se tuvo en cuenta lo descrito en el siguiente link: [Automatiza la estructura de tu proyecto de Data Science en 3 sencillos pasos](https://planetachatbot.com/automatiza-proyecto-data-science/)

### Bibliotecas standard utilizadas 
- csv
- sqlite3
- os
- time

### Requerimientos

- Archivo `localidades.csv`

**Las carpetas de exportación se crearán automáticamente.**

- Instalación de virtual env

```bash
py -m venv nombre_venv
```

No utilice librerías externas, por lo que no requiere instalación de dependencias.