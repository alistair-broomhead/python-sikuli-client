""" Generates manual pages """
from os import listdir

with open('sikuli_server.rst', 'w') as rst:
    rst.write("""
.. automodule:: sikuli_server
   :members:""")
for module in (x for x in listdir('../sikuli_server') if x.endswith('.py') and not '__init__' in x):
    module = module[:-3]
    with open('sikuli_server.%s.rst' % module, 'w') as rst:
        rst.write("""
:mod:`%s`
========================
.. automodule:: sikuli_server.%s
   :members:""" % (module, module))

with open('sikuli_client.rst', 'w') as rst:
    rst.write("""
.. automodule:: sikuli_client
   :members:""")
for module in (x for x in listdir('../sikuli_client') if x.endswith('.py') and not '__init__' in x):
    module = module[:-3]
    with open('sikuli_client.%s.rst' % module, 'w') as rst:
        rst.write("""
:mod:`%s`
========================
.. automodule:: sikuli_client.%s
   :members:""" % (module, module))
