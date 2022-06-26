from os import walk
from pydoc import describe
from ssl import OP_NO_RENEGOTIATION
from optparse import OptionParser
import shutil

# Pedir al usuario que ruta !
def get_argument():
    parser = OptionParser();
    parser.add_option("-p", "--path", dest="path", help="Path to delete 'node_modules'")
    (options, argument) = parser.parse_args()
    if not options.path or '\\' not in options.path:
        parser.error('[-] please specific an path, use --help for more info.')
    return options.path


def ls(ruta=''):
    
    # listaarchivos = []12345678a
    for (a, b, archivos) in walk(ruta):
        for c in b:
            if(c == 'node_modules'):
                shutil.rmtree('{}\{}'.format(a,c))
                print('{}\{} se ha eliminado correctamente'.format(a,c))
    print('Terminado correctamente')

# salida modificar
ls(get_argument())