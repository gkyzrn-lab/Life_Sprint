# Compatibility shim for misnamed package directory 'welbeing'
# Re-export modules from the existing 'welbeing' package so imports
# using 'wellbeing' (correct spelling) work without renaming folders.

from importlib import import_module as _import

_import('welbeing.activity_effects')
_import('welbeing.stress_burnout')
_import('welbeing.time_budget')

from welbeing.activity_effects import *
from welbeing.stress_burnout import *
from welbeing.time_budget import *
