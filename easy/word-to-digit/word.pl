open(INFILE, "<$ARGV[0]") or die("Cannot open file $ARGC[0] for reading: $!");
%hs = ('zero',0,'one',1,'two',2,'three',3,'four',4,'five',5,'six',6,'seven',7,'eight',8,'nine',9);
while(my $line = <INFILE>) {
    next if($line =~ m/^s$/); # skip blank lines
    chomp($line);
    print join('', map {$hs{$_}} split(';', $line)); print "\n";
}
close(INFILE);
