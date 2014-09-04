object Main extends App {
  val source = scala.io.Source.fromFile(args(0))
  val lines = source.getLines.filter(_.length > 0)
  var max = 0
  for (l <- lines) {
      var lst = l.trim.split("\\,").map(_.toInt)
      max = lst.sum
      getMax(lst)
      println(max)
  }
  
  def getMax(arr: Array[Int]) {
      for (i<-1 to arr.length+1) {
          for(j<-0 to arr.length) {
             if(!arr.slice(j,i).isEmpty) {
                max = if(arr.slice(j,i).sum > max) arr.slice(j,i).sum else max
             }
          }
      }
  }
}
