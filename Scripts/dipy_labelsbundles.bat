@echo off
REM wrapper to use shebang first line of dipy_labelsbundles
set mypath=%~dp0
set pyscript="%mypath%dipy_labelsbundles"
set /p line1=<%pyscript%
if "%line1:~0,2%" == "#!" (goto :goodstart)
echo First line of %pyscript% does not start with "#!"
exit /b 1
:goodstart
set py_exe=%line1:~2%
REM quote exe in case of spaces in path name
set py_exe="%py_exe%"
call %py_exe% %pyscript% %*
