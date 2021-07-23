import os
import hashlib
import sys
import shutil

suffix = './'

path = suffix + sys.argv[1]

replaced = sys.argv[1].replace('.', '')
replaced = replaced.replace('/', '')
replaced = replaced.replace('\\', '')
doublonsPath = suffix + '__DOUBLONS__' + replaced + '__'

_checksums = []
_files = []
_doublons = []

print('[=============================================]')
print('Analyse des fichiers dans le dossier courant')

for root, directories, files in os.walk(replaced, topdown=False):
    for name in files:
        rootFile = os.path.join(root, name)
        checksum = hashlib.md5(open(rootFile, 'rb').read()).hexdigest()

        if checksum in _checksums:
            if not os.path.exists(doublonsPath):
                os.makedirs(doublonsPath)
                
            _doublons.append(rootFile)
            newpath = os.path.join(doublonsPath, root)

            if not os.path.exists(newpath):    
                os.makedirs(newpath)

            shutil.move(rootFile, os.path.join(newpath, name))
        else:
            _files.append(os.path.join(root, name))
            _checksums.append(checksum)

print('[=============================================]')
print('Fichiers trouvés: ' + str(len(_checksums)))
print('Doublons:')
for entry in _doublons:
    print(entry)
print('[=============================================]')