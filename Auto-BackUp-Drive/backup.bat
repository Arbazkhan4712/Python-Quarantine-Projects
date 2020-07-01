@echo off
:a
if exist E:\ (goto Yes) else(goto a)
:Yes
E:
start backup_v1.0.exe
goto end

:end
exit