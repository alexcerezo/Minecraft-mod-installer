import urllib.request 
import shutil
import tkinter
import tkinter.messagebox
import os


USER = os.getlogin()

urlmods = "https://www.dropbox.com/sh/z01q4kqljpmatkm/AAC58qAgEDuEXibGr78T2vhMa?dl=1"

urlshaders = "https://www.dropbox.com/s/9ge1r9q3tzlk6cs/shaders.zip?dl=1"

rutacarpetamods = "/Users/" + USER + "/AppData/Roaming/.minecraft/mods"

rutacarpetashaders = "/Users/" + USER + "/AppData/Roaming/.minecraft/shaderpacks"

rutamods = "/Users/" + USER + "/AppData/Roaming/.minecraft/mods/mods.zip"

rutashaders = "/Users/" + USER + "/AppData/Roaming/.minecraft/shaderpacks/shaders.zip"

mirarcarpetamods = os.path.exists(rutacarpetamods)

mirarcarpetashaders = os.path.exists(rutacarpetashaders)


if tkinter.messagebox.askyesno(message="¿Quieres instalar los shaders recomendados?", title="Mods Installer"):
    if not mirarcarpetashaders:
        os.mkdir(rutacarpetashaders)
    urllib.request.urlretrieve(urlshaders, rutashaders)
    if not mirarcarpetamods:
        os.mkdir(rutacarpetamods)

    urllib.request.urlretrieve(urlmods, rutamods)

    shutil.unpack_archive(rutamods, rutacarpetamods)

    os.remove(rutamods)

    tkinter.messagebox.showinfo("Peruanos Mods Installer","Mods y shaders instalados correctamente.")
else:

    if not mirarcarpetamods:
        os.mkdir(rutacarpetamods)

    urllib.request.urlretrieve(urlmods, rutamods)

    shutil.unpack_archive(rutamods, rutacarpetamods)

    os.remove(rutamods)

    tkinter.messagebox.showinfo("Peruanos Installer","Mods instalados correctamente.")



