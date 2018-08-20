REG ADD "HKCU\Control Panel\Desktop" /v Win8DpiScaling /t REG_DWORD /d 1 /f
REG ADD "HKCU\Control Panel\Desktop" /v LogPixels /t REG_DWORD /d 120 /f
shutdown -h
