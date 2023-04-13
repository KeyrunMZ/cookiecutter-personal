# Cookiecuter Personal

## Requiremientos

- [Anaconda](https://www.anaconda.com/download/) >= 4.x
- [git](https://git-scm.com/) >= 2.x
- [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0:
    Esto puede ser instalado con `pip` o `conda` dependiendo cómo tú manejas tus paquetes de Python:

``` bash
pip install cookiecutter
```

o

``` bash
conda install -c conda-forge cookiecutter
```

## Crear un nuevo proyecto

En el directorio en el que quieras guardar tu proyecto generado:

```bash
cookiecutter https://github.com/platzi/curso-entorno-avanzado-ds --checkout cookiecutter-personal-platzi
```

## Estructura de directorios y archivos resultantes    

---

    {{ cookiecutter.project_slug }}
        ├── data
        │   ├── processed      
        │   └── raw            
        │
        ├── notebooks          
        ├── .gitignore         
        │
        ├── environment.yml    
        │
        └── README.md          

---