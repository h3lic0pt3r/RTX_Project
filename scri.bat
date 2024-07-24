@echo off

g++ ppmout.cpp -o ppmout.exe -I utilities/collision -I utilities/datatypes -I utilities/objtypes -I utilities/pixelhandle -I utilities/

if errorlevel 1 (
  echo Compilation failed!
  exit /b 1
)

.\ppmout.exe > imageout/image.ppm
python.exe utilities/imageview.py imageout/image.ppm

exit




