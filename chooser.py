#!python3

import shutil
import subprocess
import sys
import tempfile
try:
    from tkinter.filedialog import askopenfilename
except ModuleNotFoundError:
    print("ERROR: MISSING TKINTER")
    sys.exit(10)

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
        print(sys.platform)
        if sys.platform == "darwin":
            subprocess.run(["vlc", local_file])
        elif sys.platform == "win32":
            subprocess.run(["C:\\Program Files\\VideoLAN\\VLC\\vlc.exe", local_file])
        else:
            print("ERROR: UNKNOWN OS")
            sys.exit(20)
    print("temp deleted")
    ...


if __name__ == "__main__":
    main()