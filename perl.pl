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



# open file read only with the operator : '<'
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