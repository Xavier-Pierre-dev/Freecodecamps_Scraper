# 🚀 Freecodecamps : scrapper 🚀

![Alt text](./logo.jpg "logo perl")

## __Stacks :__
* python
* perl
* call perl from python
* selenium

_____________________________
_____________________________

## Quick Started :
* Download the chrome driver like explained here : 
https://www.selenium.dev/documentation/fr/webdriver/driver_requirements/
* You need to update the path for access to the chromedriver executable inside main.py
```python
    Web_browser = webdriver.Chrome(executable_path="Your Path")
```
* You need to install Selenium and BeautifulSoup for python using pip install ...

Now you can run the script main.py

__Note :__ for perl if you are on windows you need to install first [strawberries](https://strawberryperl.com/) 

___
___

## __Why this project :__
I create this project because i want start freecodecamps certification and I want to keep a trace of my code when I'm practicing on freecodecamps and for maybe push the code on github. 

But I'm lazy to create every file and folder for each certification so i find interesting for this case to create a scraper for save the structure inside a .json but also for automate the folders and files creation. 

For scraping data from web in this cases i use selenium in python but for create folder and file i use 2 method :
* python 
* call perl subroutines with python (Just for practice after start to learn pearl : https://github.com/Xavier-Pierre-dev/Perl-practice)

For choose perl or python :
```python
switch_perl = False # if True the program will call perl subroutines passing argument 
```

Also : 
```python
    lien = "https://www.freecodecamp.org/learn/responsive-web-design/" # url with the formation
```

And :
```python
    # You need to put the path for access to the chromedriver executable 
    # https://www.selenium.dev/documentation/fr/webdriver/driver_requirements/
    Web_browser = webdriver.Chrome(executable_path="C:\selenium browser drivers\chromedriver.exe")
```
___
___
## __How it's work ?__
In perl i use : 
```perl
#!/usr/bin/perl -s
```
whose allow me to pass argument when i execute a `script.pl` in this cases __-s__ allow me for pass argument like this :
```bash
perl .\perl.pl -file=argument1 -folder=argument2
```
<br></br>
And inside perl.pl :
```perl
#!/usr/bin/perl -s

use strict;
use warnings;
use diagnostics;
use v5.32.1;

our $folder;
our $file;

sub create(){
    if(defined($folder)){
    # This creates perl directory in /tmp directory.
    mkdir( $folder ) or die "Couldn't create $folder directory, $!";
    print "Directory created successfully\n";

    }
    if(defined($file)){
    #  open file read only with the operator : '<'
    unless(open FILE, '>'.$file) {
        # Die with error message
        # if we can't open it.
        die "\nUnable to create $file\n";
    }

    # close file
    close FILE;

    }
}

create();
```
I check if ```$folder``` and ```$file``` are defined then i can use __mkdir__ for create a folder and open File with operator `>` for create a file.
<br></br>
Inside Python i'm calling perl with the line :
```python
import os
import shlex, subprocess
        # file
        pipe = subprocess.Popen(["perl", "perl.pl", "-file=" + repertoire, "output.xml"], stdout=subprocess.PIPE)

        # folder
        pipe = subprocess.Popen(["perl", "perl.pl", "-folder=" + repertoire, "output.xml"], stdout=subprocess.PIPE)
```
So i have a function for create a file using perl and one method for create a folder.

