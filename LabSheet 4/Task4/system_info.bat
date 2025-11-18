@echo off
echo Kernel Version:
ver

echo Current User:
whoami

echo Hardware / Virtualization Info:
systeminfo | find "Hyper-V"
wmic computersystem get model
