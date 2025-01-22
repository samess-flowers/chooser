# I JUST WANT TO WATCH MOVIES
Go to releases in the sidebar ->

# Building
## Create Venv
```python3 -m venv .venv```

## Activate Venv
### Windows
```Powershell
#needed for unsigned PS1 activation script
Set-ExecutionPolicy Unrestricted
#activate the venv
.\.venv\Scripts\Activate.ps1
```

### macOS
```bash
#oh wow this is easier than on windows thats craaaaaaaaaaazy
source .venv/bin/activate
```

### Linux
Make a pull request when you've got it working

## Install requirements
```pip install -r requirements.txt```

## Actually build it
This incantation seems to make the beast happy:
```pyinstaller --clean -i icon.ico --onefile chooser.py```
