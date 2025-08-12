@echo off
SETLOCAL
ECHO Script iniciado.
SET "PAD_PATH=E:\POWERA~1\dotnet\PAD.Console.Host.exe"
ECHO DEBUG: PAD_PATH es [%PAD_PATH%]
IF NOT EXIST "%PAD_PATH%" (
    ECHO ERROR DENTRO DEL IF: PAD_PATH no encontrado segun el IF.
    PAUSE
    GOTO :EOF
)
ECHO PASO EL IF NOT EXIST PARA PAD_PATH. El archivo deberia existir.

SET "PYTHON_SCRIPT=wait_and_sendkeys.py"
SET "READY_IMAGE=pad_ready_indicator.png"
ECHO DEBUG: PYTHON_SCRIPT es [%PYTHON_SCRIPT%]
ECHO DEBUG: READY_IMAGE es [%READY_IMAGE%]

SET "PYTHON_EXE=E:\Python\Python38-32\python.exe"
SET "INITIAL_WAIT=5"
ECHO DEBUG: PYTHON_EXE es [%PYTHON_EXE%]
ECHO DEBUG: INITIAL_WAIT es [%INITIAL_WAIT%]

IF NOT EXIST "%PYTHON_SCRIPT%" (
    ECHO ERROR: No se encontro el script de Python: %PYTHON_SCRIPT%
    PAUSE
    GOTO :EOF
)
ECHO Python script encontrado: [%PYTHON_SCRIPT%]

IF NOT EXIST "%READY_IMAGE%" (
    ECHO ERROR: No se encontro la imagen de referencia: %READY_IMAGE%
    PAUSE
    GOTO :EOF
)
ECHO Imagen de referencia encontrada: [%READY_IMAGE%]

ECHO Iniciando Power Automate Desktop...
START "" "%PAD_PATH%"

ECHO Esperando %INITIAL_WAIT% segundos iniciales...
TIMEOUT /T %INITIAL_WAIT% /NOBREAK > NUL

ECHO Iniciando script Python...
%PYTHON_EXE% "%PYTHON_SCRIPT%"

SET "PY_EXIT_CODE=%ERRORLEVEL%"

IF NOT %PY_EXIT_CODE% EQU 0 (
    ECHO ERROR: El script Python fallo (ERRORLEVEL=%PY_EXIT_CODE%).
    PAUSE
) ELSE (
    ECHO El script Python termino bien (ERRORLEVEL=%PY_EXIT_CODE%).
)


ECHO Script .bat completado.
PAUSE
ENDLOCAL