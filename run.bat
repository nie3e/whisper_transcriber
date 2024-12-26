@Echo Off

Set "VIRTUAL_ENV=venv"

If Not Exist "%VIRTUAL_ENV%\Scripts\activate.bat" (
    echo Run install.bat first
    Exit /B 0
)

Call "%VIRTUAL_ENV%\Scripts\activate.bat"

python.exe app/main.py
Call "%VIRTUAL_ENV%\Scripts\deactivate.bat"
Pause
Exit /B 0