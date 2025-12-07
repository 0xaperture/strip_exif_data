@echo off
set INPUT_DIR=.\Photos\Export_With_Metadata
set OUTPUT_DIR=.\Photos\Export_Clean

python ".\Photos\strip_exif.py" "%INPUT_DIR%" "%OUTPUT_DIR%" --keep-copyright

echo Done. Files cleaned and copyright preserved.
pause
