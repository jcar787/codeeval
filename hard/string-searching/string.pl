open(INFILE, "<$ARGV[0]") or die("Cannot open file $ARGV[0] for reading: $!");
while(chomp(my $line = <INFILE>)) {
    next if($line =~ m/^s$/); # skip blank lines
    ($word, $search) = split(',', $line);
    unless($search =~ m/\\\*/) {
        $search =~ s/\*/.*/;
    }
    
    if($word =~ m/$search/) {
        print "true\n";    
    }
    else {
        print "false\n";
    }
}
close(INFILE);
