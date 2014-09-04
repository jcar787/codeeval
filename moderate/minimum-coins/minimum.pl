open(INFILE, "<$ARGV[0]") or die("Cannot open file $ARGV[0] for reading: $!");
while(chomp(my $line = <INFILE>)) {
    $coins = 0;
    while($line) {
        if ($line > 4) { $coins++; $line -= 5;}
        elsif ($line > 2) { $coins++; $line -= 3;}
        else { $coins++; $line--;}
    }
    print "$coins\n";
}
close(INFILE);
