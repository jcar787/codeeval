#!/usr/bin/perl
open(INFILE, "<$ARGV[0]") or die("Cannot open file $ARGV[0] for reading: $!");
while(my $line = <INFILE>) {
    next if($line =~ m/^s$/); # skip blank lines
    chomp($line);
    $t = 0;
    foreach(split('', $line)) { $t += $_;}
    print "$t\n";
}
close(INFILE);
