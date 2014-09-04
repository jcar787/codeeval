open(INFILE, "<$ARGV[0]") or die("Cannot open file $ARGV[0] for reading: $!");
$t = 0;
while(my $line = <INFILE>) {
    next if($line =~ m/^s$/); # skip blank lines
    chomp($line);
    $t+=$line;
}
print $t;
close(INFILE);
