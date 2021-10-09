# SASEhack 2021 - Crowd-sourced hate detection
### Team Members


## Initial Setup
First, the Execution Policy for PowerShell needs to be changed. The following command needs to be run in PowerShell (admin).

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
```

Verification can be done with the following, ensure RemoteSigned is returned.

```
Get-ExecutionPolicy
```

Now the virtual environment needs to be setup (we will be using virtualenv as the name).

```
python -m venv virtualenv
```

Virtual environment needs to be activated. For PowerShell, remove the .bat extension.

```
virtualenv\Scripts\activate.bat
```

Verify `(virtualenv)` is present in the beginning of the line for terminal. Now in the virtual environment, install the requirements via pip.

```
pip install -r requirements.txt
```

Now we can run the Flask application.

```
python app.py
```

Application should now be running and accessible via localhost. Default is `127.0.0.15000`
