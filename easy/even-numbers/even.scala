object Main extends App {
  val source = scala.io.Source.fromFile(args(0))
  val lines = source.getLines.filter(_.length > 0)
  for (l <- lines) {
    if(l.toInt % 2 == 0) {
        println(1)
    }
    else {
        println(0)
    }
  }
}
