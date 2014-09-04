open(INFILE, "<$ARGV[0]") or die("Cannot open file $ARGV[0] for reading: $!");
while(chomp(my $line = <INFILE>)) {
    next if($line =~ m/^s$/); # skip blank lines
    printf "%d\n", hex($line);
}
close(INFILE);
