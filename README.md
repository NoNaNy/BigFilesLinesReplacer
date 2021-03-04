# BigFilesLinesReplacer

Es una aplicación escrita en python con una interface gráfica simple que sirve para editar líneas de archivos grandes usualmente de GB sin necesidad de abrirlos.

Esto gracias a los comandos SED y GREP, facilitando la búsqueda y reemplazo.

![](/img/screen01.png)

## Interface gráfica
Para la creación de interface gráfica se uso el programa [PAGE](https://sourceforge.net/projects/page/) (https://sourceforge.net/projects/page/)

[Project site](http://page.sourceforge.net/)

![](/img/screen_page.png)

## Creación del ejecutable
Para crear y empaquetar el ejecutable se usó el paquete [pyintaller](https://www.pyinstaller.org/)

`pyinstaller.exe -F -c --add-binary editor.ico;. --add-binary bin\\*;bin -i editor.ico EditorWindow_support.py`

`pyinstaller.exe -F -c -n ReportFilesLinesEditor --add-binary editor.ico;. --add-binary bin\\*;bin -i editor.ico EditorWindow_support.py`