# Strip EXIF Data
EXIF stands for Exchangeable Image File Format.

It’s the hidden data that your camera or phone embeds inside your photos when you take them.

I wanted to remove sensitive EXIF (location, serial numbers, capture settings) but preserve authorship (Copyright, Artist). This is an updated Windows-friendly Python script that keeps only copyright-related fields and strips everything else.

Purpose:
- Preserve Privacy: Exact home (GPS) location from where photos were shot
- Security: Camera serial can tie back to personal identity
- Clean Branding: Removes edit history before sending to clients
- Improved Performance: Smaller file sizes for web/gallery uploads

Installation Instructions:
Prerequisite: Must have [Python](http://www.python.com) installed. 

1. Save files to directory of your choosing.
2. Run "install_dependencies.bat"
3. Open "run_strip_exif_data.bat". Change the following input and output folder names to the appropriate folder names in your PC. Save.

- set INPUT_DIR=<i>.\Photos\Export_With_Metadata</i></br>
- set OUTPUT_DIR=<i>.\Photos\Export_Clean</i>

4. Place photos with metadata in the input folder location.
5. Double-click "run_strip_exif_data.bat"
6. You will see EXIF-free copies of the photos in the output folder.  Only copyright information will be preserved.
