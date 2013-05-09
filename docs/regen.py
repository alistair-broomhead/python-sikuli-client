""" Generates manual pages """
from os import listdir

with open('docs/python_sikuli_client.rst', 'w') as rst:
    rst.write(""".. automodule:: python_sikuli_client
   :members:""")
for module in (x for x in listdir('src/python_sikuli_client') if x.endswith('.py') and not '__init__' in x):
    module = module[:-3]
    with open('docs/python_sikuli_client.%s.rst' % module, 'w') as rst:
        rst.write(""":mod:`%s`
========================
.. automodule:: python_sikuli_client.%s
   :members:""" % (module, module))
