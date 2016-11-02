# Used successfully in Python2.5 with matplotlib 0.91.2 and PyQt4 (and Qt 4.3.3)
from distutils.core import setup
import py2exe,pygame
import winsound

# We need to import the glob module to search for all files.
import glob

# We need to exclude matplotlib backends not being used by this executable.  You may find
# that you need different excludes to create a working executable with your chosen backend.
# We also need to include include various numerix libraries that the other functions call.

opts = {
    'py2exe': { "includes" : [ "matplotlib.backends",  "matplotlib.backends.backend_qt4agg",
                               "matplotlib.figure","pylab", "numpy", "matplotlib.backends.backend_tkagg"],
                'excludes': ['_gtkagg', '_tkagg', '_agg2', '_cairo', '_cocoaagg',
                             '_fltkagg', '_gtk', '_gtkcairo', ],
                'dll_excludes': ['libgdk-win32-2.0-0.dll',
                                 'libgobject-2.0-0.dll']
              }
       }

# Save matplotlib-data to mpl-data ( It is located in the matplotlib\mpl-data
# folder and the compiled programs will look for it in \mpl-data
# note: using matplotlib.get_mpldata_info
data_files = [(r'mpl-data', glob.glob(r'C:\Python27\Lib\site-packages\matplotlib\mpl-data\*.*')),
                    # Because matplotlibrc does not have an extension, glob does not find it (at least I think that's why)
                    # So add it manually here:
                  (r'mpl-data', [r'C:\Python27\Lib\site-packages\matplotlib\mpl-data\matplotlibrc']),
                  (r'mpl-data\images',glob.glob(r'C:\Python27\Lib\site-packages\matplotlib\mpl-data\images\*.*')),
                  (r'mpl-data\fonts',glob.glob(r'C:\Python27\Lib\site-packages\matplotlib\mpl-data\fonts\*.*')),"1.wav","2.wav","3.wav",
              "Simulacion.s3db","turbulence3.tga","wood.tga","random.tga","earth.tga","BlueMarble.tga","brickbump.tga","msvcp90.dll","msvcr90.dll","12.png","Contactanos.png","Contactanos1.png","Inicio_sesion.gif","9152064-boton-de-nombre-de-usuario-y-contrasena-ademas-de-inicio-de-sesion-en-un-candado-para-acceso-seguro-.jpg","anterior.png","Banner.png","Banner1.png","Banner2.png","Banner3.png","buscar.png","cancelar.png","eliminar.png","engranaje.png","engranaje1.png","guardar.png","icono_telefono.png",
              "icono_telefono1.png","Info.png","infoAdmin.png","infoAdmin1.png","informacion.png","informacion1.png","nuevo.png","primero.png","salir.png","salir1.png","siguiente.png","soporte_tecnico_icono.png","soporte_tecnico_icono1.png","ultimo.png","usuarios.png","usuarios1.png","manual1.png"]

# for console program use 'console = [{"script" : "scriptname.py"}]
setup(name="Sistema de Cimulacion de Cinematica",
      version="0.1",
      licence="license",
      windows=[{
          "script" : "Entrada.py",
          "icon_resources":[(0,"12.ico")]
          }],
      options=opts,   data_files=data_files)
