#!python3

import tempfile
from tkinter.filedialog import askopenfilename


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
        filename = askopenfilename()
        print(filename)
        print(dir)
    ...


if __name__ == "__main__":
    main()