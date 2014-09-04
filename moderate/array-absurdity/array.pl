open(INFILE, "<$ARGV[0]") or die("Cannot open file $ARGV[0] for reading: $!");
while(my $line = <INFILE>) {
    next if($line =~ m/^s$/); # skip blank lines
    chomp($line);
    @vals = split(';', $line);
    @ints = split(',', $vals[1]);
    %st = ();
    $st{$_}++ for @ints;
    @vals = sort {$st{$b}<=>$st{$a}} keys %st;
    print "$vals[0]\n";
}
close(INFILE);
