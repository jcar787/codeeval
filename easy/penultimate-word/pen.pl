#!/usr/bin/perl 
open(INFILE, "<$ARGV[0]") or die ("Cannot open file: $!");

while($line = <INFILE>) {
    next if($line =~ m/^s$/);
    $line =~ s/(^s|s*$)//g;
    @arr = split(' ', $line);
    print "$arr[-2]\n";
}
close INFILE;
