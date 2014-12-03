from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
import sys
sys.path.append('./gui')


incs = ['atexit', 'sys', 'PyQt4.QtCore', 'PyQt4.QtGui', 'utils', 'gui']
buildOptions = dict(packages=[], excludes=[], includes=incs)
import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('geniusbar.py', base=base, targetName = 'GeniusBar.exe')
]

setup(name='xx',
      version = '1.0',
      description = '',
      options = dict(build_exe = buildOptions),
      executables = executables)
