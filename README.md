# Ayudantías Algoritmos y Complejidad

## Instalación y Uso

### Instalación

Asegúrate de tener **Node.js** instalado en tu sistema. Luego, instala las dependencias del proyecto ejecutando:

```sh
npm install
```

### Uso

#### Iniciar el Servidor de Presentaciones

Para iniciar el servidor y visualizar las presentaciones en tiempo real, usa:

```sh
npm start
```

Esto iniciará un servidor en el directorio `src/`, utilizando el tema `beam.css`.

#### Generar Presentaciones

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
  Genera presentaciones en formato PDF con edición habilitada en PPTX.

- **PPTX:**
  ```sh
  npm run pptx
  ```
  Genera presentaciones en formato PPTX.