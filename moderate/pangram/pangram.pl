#!/usr/bin/env perl
open(INFILE, "<$ARGV[0]") or die("Cannot open file $ARGV[0] for reading: $!");
@abc = (a..z);
while(chomp(my $line = <INFILE>)) {
    next if($line =~ m/^s$/); # skip blank lines
    $line = lc($line); @tmp = ();
    foreach(@abc) {
        unless($line =~ m/$_/) { push(@tmp, $_); }
    }
    if($#tmp == -1) { print "$line ->NULL\n"; }
    else { print "$line -> "; print join('', @tmp); print "\n"; }
}
close(INFILE);
