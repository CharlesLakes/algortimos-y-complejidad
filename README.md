# Ayudantías Algoritmos y Complejidad

## Estructura del Repositorio  
Los archivos PDF de las presentaciones, organizados según cápsulas y ayudantías, se encuentran en la carpeta `src/presentaciones/*`.

## Colaboración usando MARP

Esta sección está dirigida a los ayudantes del ramo, pero cualquier persona puede colaborar si encuentra un error o mejora posible.

### Instalación y Uso

#### Instalación

Asegúrate de tener **Node.js** instalado en tu sistema. Luego, instala las dependencias del proyecto ejecutando:

```sh
npm install
```

#### Uso

##### Iniciar el Servidor de Presentaciones

Para iniciar el servidor y visualizar las presentaciones en tiempo real, usa:

```sh
npm start
```

Esto iniciará un servidor en el directorio `src/`, utilizando el tema `beam.css`.

##### Generar Presentaciones

Puedes generar archivos en diferentes formatos usando los siguientes comandos:

- **HTML:**
  ```sh
  npm run html
  ```
  Genera presentaciones en formato HTML a partir de los archivos Markdown dentro de `src/`.

- **PDF:**
  ```sh
  npm run pdf
  ```
  Genera presentaciones en formato PDF.

- **PPTX:**
  ```sh
  npm run pptx
  ```
  Genera presentaciones en formato PPTX.