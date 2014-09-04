open(INFILE, "<$ARGV[0]") or die("Cannot open file $ARGV[0] for reading: $!");
while(chomp(my $line = <INFILE>)) {
    next if($line =~ m/^s$/); # skip blank lines
    print $line % 2 == 0 ? "1\n" : "0\n";
}
close(INFILE);
