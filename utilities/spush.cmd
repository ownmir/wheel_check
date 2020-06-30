@setlocal
@set do=c
@set quit=q
c:
cd c:\users\%username%\wheel_check
@set /p v1=Input c to run command 'git add .' or any key to quit 
@if %v1%==%do% (@goto m1
) else (
@goto exit)
:m1
@echo m1...
git add .
@set /p v2=Input c to run command 'git commit -m'%1'' or any key to quit 
@if %v2%==%do% (@goto m2
) else (
@goto exit)
:m2
@echo m2...
git commit -m"%1"
@set /p v3=Input c to run command 'git push origin master' or any key to quit 
@if %v3%==%do% (@goto m3
) else (
@goto exit)
:m3
@echo m3...
git push origin master
:exit
git status
pause
@endlocal