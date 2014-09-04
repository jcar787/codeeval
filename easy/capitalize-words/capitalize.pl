open(INFILE, "<$ARGV[0]") or die("Cannot open file $ARGV[0] for reading: $!");
while(my $line = <INFILE>) {
    next if($line =~ m/^s$/); # skip blank lines
    print join(' ', map {ucfirst $_} split(' ', $line));
    print "\n";
}
close(INFILE);
