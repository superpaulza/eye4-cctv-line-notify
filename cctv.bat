cd "Y:\"
Del "001.jpg"
cd "%UserProfile%\Documents\Eye4\alarm\VSTJ571476UNVYU\"
FOR /F "delims=" %%i IN ('dir /b /ad-h /t:c /od') DO SET a=%%i
cd %a%
echo open %a%
FOR /F "delims=" %%i IN ('dir /b /ad-h /t:c /od') DO SET a=%%i
cd %a%
echo open %a%
COPY 001.jpg "Y:\"
COPY 001.jpg "%UserProfile%\Desktop\CCTV"
cd ..
DEL /F/Q/S *.* > NUL
cd "%UserProfile%\Desktop\CCTV"
py crop.py
py ai.py
PAUSE