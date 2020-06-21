@setlocal
@set do=c
@set quit=q
c:
cd c:\users\fominvv\wheel_check
@set /p v1=Input c to run command 'git pull origin master' or any key to quit 
@if %v1%==%do% (@goto m1
) else (
@goto exit)
:m1
@echo m1...
git pull origin master
:exit
pause
@endlocal
