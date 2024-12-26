@Echo Off

Set "VIRTUAL_ENV=venv"

If Not Exist "%VIRTUAL_ENV%\Scripts\activate.bat" (
    python.exe -m venv %VIRTUAL_ENV%
)

If Not Exist "%VIRTUAL_ENV%\Scripts\activate.bat" Exit /B 1

Call "%VIRTUAL_ENV%\Scripts\activate.bat"
pip.exe install -r requirements.txt
Call "%VIRTUAL_ENV%\Scripts\deactivate.bat"
Pause
Exit /B 0