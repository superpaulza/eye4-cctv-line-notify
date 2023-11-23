Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "%UserProfile%\Desktop\CCTV\cctv.bat" & Chr(34), 0
Set WshShell = Nothing