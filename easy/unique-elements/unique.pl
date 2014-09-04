open(INFILE, "<$ARGV[0]") or die("Cannot open file $ARGV[0] for reading: $!");
while(my $line = <INFILE>) {
    next if($line =~ m/^s$/); # skip blank lines
    chomp($line);
    %st = ();
    map {$st{$_}++} split(',', $line);
    print join(',', sort {$a  <=> $b} keys %st);
    print "\n";
}
close(INFILE);
