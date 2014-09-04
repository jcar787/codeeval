object Main extends App {
  val source = scala.io.Source.fromFile(args(0))
  val lines = source.getLines.filter(_.length > 0)
  for (l <- lines) {
    var arr = l.split(" ").map(_.toInt)
    for(i <-1 to arr(2)) {
        var res = ""
        if (i%arr(0) == 0) {
            res += "F" 
        }
        if (i%arr(1) == 0) {
            res += "B" 
        }
        if(res == "") {
            print(i)
        }
        else {
            print(res)
        }
        if(i!=arr(2)) {
            print(" ");
        }        
    }
    println()
  }
}
