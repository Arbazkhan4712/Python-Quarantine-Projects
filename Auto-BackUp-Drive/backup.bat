@echo off
:a
if exist E:\ (goto Yes) else(goto a)
:Yes
E:
start backup.exe
goto end

:end
exit