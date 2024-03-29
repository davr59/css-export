# export css to png image | exportar css a png imagen

Python3 Method to consume HCTI API that converts HTML/CSS to Image.

Método en Python 3 para consumir HCTI API que convierte HTML/CSS a Imagen.

## References | Referencias

- [HTML/CSS to Image API](https://htmlcsstoimage.com/)

## Quickstart | Inicio rápido

### Install dependencies | Instalar dependencias

```
pip3 install requests
pip3 install Pillow
```

### Set API Key | Establecer API Key

Set your API Key information in config.ini:

Establecer tu información API Key en config.ini:

```
[DEFAULT]
HCTI_API_ENDPOINT = https://hcti.io/v1/image
HCTI_API_USER_ID =
HCTI_API_KEY =
```

### Initialize image information | Inicializar image information

Set image width and height, body html code, style code, destination file path and if it is a RGBA image.

Establecer el ancho y alto de la imagen, el código html del cuerpo (body), el código del estilo (style), la ruta del archivo destino y si la imagen es RGBA.

```image_info = ImageInfo(1024, 768, body_text, css_text, './result.png', False)```

In case you have the html and style code in a html file, there is a static method that extracts both texts:

Si tienes el código de html y estilo en un archivo html, hay un método estático que extrae ambos textos:

```
body_text, css_text = ImageInfo.read_html_body_css(html_file_path)
image_info = ImageInfo(1024, 768, body_text, css_text, './result.png', False)
```

### Export | Exportar

Call export method with the image_info and image will be created in the destination file path:

Llamar el método de exportar con image_info y la imagen se creará en la ruta del archivo destino:

```
exporter = Exporter()
exporter.export_image(image_info)
```

## Want to help? | ¿Quiere ayudar?

Want to file a bug, contribute some code, or improve documentation? Thanks! Feel free to contact me at [@davidvives](https://twitter.com/davidvives) or at davr59@outlook.com.

¿Quiere reportar un error o una pulga, contribuir con código o mejorar la documentación? ¡Muchas gracias! Puede contactarme a [@davidvives](https://twitter.com/davidvives) o a davr59@outlook.com.

