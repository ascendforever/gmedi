

PYXIMPORT_INSTALLED:bool = False
from glite import *
try:
    from ._Ccomp import *
    from ._Cencoding import *
    from ._memorize import *
except ImportError:
    from platform import system as ____system
    if True:
        from pyximport import install as ____pyximport_install
        from warnings import warn as ____warn
        ____warn("Pyximport has been installed because this is the first time the package is running", ImportWarning)
        # you cannot redirect pyximport compilation messages # seem to only appear on Windows
        ____pyximport_install(language_level=3, inplace=True)
        PYXIMPORT_INSTALLED = True
        from . import _Ccomp as _
        from . import _Cencoding as _
        from . import _memorize as _
    from ._Ccomp import *
    from ._Cencoding import *
    from ._memorize import *


__version__ = '1.0.0'
