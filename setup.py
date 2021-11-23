import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

build_exe_options = {'packages': ["seaborn"],
                     'includes': ["flask_compress"],
                     'excludes': ["tkinter"],
                     'build_exe': 'C:\\Users\\pc080\\Desktop\\app\\1.0',
                     'optimize': 2
                     }

setup(
    name='ZDH-Calculation Software',
    version=1.0,
    description='EDI calculation software',
    options={'build_exe': build_exe_options},
    executables=[Executable('app.py',
                            base=base,
                            icon="resource/EDI-logo.ico"
                            )]
)

#  请执行下述操作
#  python setup.py build
#  nuitka3 --mingw64 --follow-import-to=widgets --follow-import-to=tools --plugin-enable=numpy --plugin-enable=qt-plugins --recurse-all --recurse-not-to=numpy,PySide6,matplotlib,pandas --output-dir=out app.py
#  pyinstaller --onedir -windowed -path="C:\Users\pc080\Desktop\app"
