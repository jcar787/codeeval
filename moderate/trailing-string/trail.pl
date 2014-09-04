open(INFILE, "<$ARGV[0]") or die("Cannot open file $ARGV[0] for reading: $!");
while(chomp(my $line = <INFILE>)) {
    next if($line =~ m/^s$/); # skip blank lines
    ($word, $search) = split(',', $line, 2);
    if($word =~ /$search$/){
        print "1\n";    
    }
    else {
        print "0\n";
    }
}
close(INFILE);
