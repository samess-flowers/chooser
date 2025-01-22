#!python3

import shutil
import subprocess
import os
import tempfile
try:
    from tkinter.filedialog import askopenfilename
except ModuleNotFoundError:
    print("You need to install pytk")
    os.exit(10)
from rich.traceback import install
install(show_locals=True)

def main():
    '''
    get the filename from the picker
    download it
    open vlc
    enjoy film
    vlc is closed
    clean up tempdir
    '''
    with tempfile.TemporaryDirectory() as dir:
        print(dir)
        remote_file = askopenfilename()    
        local_file = shutil.copy(remote_file, dir)
        print(local_file)
        subprocess.run(["vlc", local_file])
    print("temp deleted")
    ...


if __name__ == "__main__":
    main()