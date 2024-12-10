import os
import glob
import importlib

# Automatically import all modules in this package
module_names = [os.path.basename(f)[:-3] for f in glob.glob(os.path.join(os.path.dirname(__file__), "*.py")) if f.endswith('.py') and not f.endswith('__init__.py')]

for module_name in module_names:
    importlib.import_module(f'.{module_name}', package=__name__)
   
