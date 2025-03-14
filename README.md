# EHgallerizer

Some useful tools for people want to download large amounts of art from one website and upload them to a certain site.  
All .py files obviously require you to have [python](https://www.python.org) installed, and to atleast have a very basic understanding of how to run them.  
Same goes for the .ps1 (PowerShell) files, which require you to [change your execution policy](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-7.5) if you haven't already (atleast for the current session).  
  
Don't blame me if you, somehow, fuck something up.  
  
<br>
  
### Download.py
**Requires gallery-dlp**
<br>
<br>
Download from sites with seperate [galleries](https://github.com/mikf/gallery-dl) (like kemono) while adding the counter without resetting between galleries.  
  
```Filename: {number in own gallery} {total number across galleries}.{extension}```  
  
If you use gallery-dl on your own like I do, it uses your own config files.  
Be aware of the fact that some sites (like pixiv) require you to have your login details in the aforementioned [config file](https://github.com/mikf/gallery-dl?tab=readme-ov-file#authentication).
<br>
<br>
### Archive.py

Creates (a) zip file(s) that contains all .jpg, .jpeg, .png, .webp and .gif files in the folder it is ran in.  
**Make sure you first convert any files that are [above the limit](https://ehwiki.org/wiki/Making_Galleries#Limits).**

The program makes sure all created zip files are below the single upload limit of 500MB.
Images are stored in order of current folder sorting method so if you use numeral sorting (which you should) and sort your folder by name, it should go 001 -> 002 -> 003 etc.
<br>
<br>
### Compress.ps1
**Requires FFMPEG**  
**Requires basic PowerShell knowledge**  
**FFMPEG knowledge if you want to mess with options**

Run in current folder to compress any gifs to <=targetsize using FFMPEG. Optimized to be quick, not to get the closest to <targetsize.

**Program deletes original files after creating a file with size < targetsize so be careful**

Open the program to change any values like targetsize (default [10MB](https://ehwiki.org/wiki/Making_Galleries#Limits)), framerate (default 15fps), scale factor (default 0.8) and FFMPEG options.  
