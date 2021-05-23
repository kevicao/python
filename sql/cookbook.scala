val df=spark.sql(s"""
with data as (
SELECT *

FROM table
WHERE a = 0

)

select *
from data

""") 

val df = spark.sql("""
        with exploded as (
            select col1
                , explode(col2) as col2
            from snapshot
        ),

        select col1
            , LOWER(concat_ws(' ', collect_set(col2))) as col2
        from exploded
        group by col1

        """)

val sales=sc.parallelize(List(
   ("Y"),
   ("UNKNOWN")
))

val salesDf= sales.toDF("store")
salesDf.show()

val data = Seq(("", ""), ("Python", "Python"), ("Scala", "3000"))

val rdd = spark.sparkContext.parallelize(data)

val df = sc.textFile("s3://../test.txt")
df.collect().foreach(println)

df.createOrReplaceTempView("df")
//////////////////////////////////////////////////////

df.withColumn("new", "old").na.fill("", Seq("old")).
	.withColumn("new", split(col("old"), " "))
	.withColumn("new", expr("case when col1 = 1 then 0 else 1 end"))
	.withColumn("new", col("old").cast("Int"))
	.withColumn("new", regexp_replace($"old", "\\/", " ")(0))
	.withColumn("NODE_ID", expr("substr(NODE_ID, 2, length(NODE_ID))") )
	.withColumn("new", myUDF("old"))
	.withColumnRenamed("old", "new")
	.drop("col1", "col2")
	.filter(col("col")=="a").filter("col = 'a'")
	.filter(col(coll).isNull)
	.where(col(coll).isNotNull)
	.where(col("date").between("2010-08-01", "2010-08-05"))
	.withColumn(
		  "rn", row_number().over(Window.partitionBy("col1").orderBy(col("col2").desc, col("col3").desc))
		).filter(
		  $"rn" === 1
		)
	.select("col1", "col2")



df.groupBy("col1","col2").agg(
    sum("col3").alias("col3") 
    , sum("col4") / sum("col5") as "col4"
    , sum( when($"col1".isNotNull, 1).otherwise(0) ).as("num_prime")
).orderBy("col1",desc("col2")).show(100,false)


df.repartition(1).write.mode("overwrite").format("parquet").save("s3://../")
tmp.limit(500).write.format("csv").option("header", "true").csv("s3://../test.csv")
/////////////////////////////////

val gls = List("a", "b")

gls.foreach( gl => {
	val tmp = df.filter(col("col1") === gl)
	println(gl, computeAUC(tmp, "col1", "col2"))
})


df.dtypes.foreach {  f =>
      val fName = f._1
      val fType = f._2
      if (fType  == "StringType") { println(s"STRING_TYPE") }
      if (fType  == "MapType") { println(s"MAP_TYPE") }
      //else {println("....")}
      println("Name %s Type:%s - all:%s".format(fName , fType, f))

    }


//UDF
val myUDF = udf {
	(Set1: WrappedArray[String], Set2: WrappedArray[String]) => 
     (Set1.toList.intersect(Set2.toList)).size.toDouble / (Set1.toList.union(Set2.toList)).distinct.size.toDouble
}

///////
def array_contains_any(s:Seq[String]): UserDefinedFunction = {
udf((c: WrappedArray[String]) =>
  (c.toList.intersect(s).nonEmpty))
}
val safeString: String => String = s => if (s == null) "" else s
val udfSafeString = udf(safeString)
val male = List("men")
array_contains_any(male)(split(udfSafeString(col("old")), " "))




////////
def getZonedDateTime(dateStr: String): ZonedDateTime = {
    val formatter: DateTimeFormatter = DateTimeFormatter.ISO_INSTANT.withZone(ZoneId.of("UTC"))
    ZonedDateTime.parse(dateStr + "T00:00:00Z", formatter)
}

def getDateTimeString(date: ZonedDateTime, connector: String="-"): String = {
    // val formatter: DateTimeFormatter = DateTimeFormatter.ISO_INSTANT.withZone(ZoneId.of("UTC"))
    // date.format(formatter)
  List("%04d".format(date.getYear), 
    "%02d".format(date.getMonthValue),
    "%02d".format(date.getDayOfMonth)
  ).mkString(connector)
}

def getDates(start: ZonedDateTime, end: ZonedDateTime): Seq[ZonedDateTime] = {
  val days = DAYS.between(start, end)
  for(i <- 0 to days.toInt) yield start.plusDays(i)
}


def readSampleDf(root: String, date: ZonedDateTime, sampleType: String): DataFrame = {
    val (year, month, day) = ("%04d".format(date.getYear), "%02d".format(date.getMonthValue), "%02d".format(date.getDayOfMonth))
    spark.read.parquet(root + s"/year=/")
}

def readSampleDfs(root: String, dates: Seq[ZonedDateTime], sampleType: String, addDate: Boolean=false): DataFrame = {
    val firstDf = if (addDate) {
        readSampleDf(root, dates.head, sampleType).withColumn("date", lit(getDateTimeString(dates.head)))
    } else{
        readSampleDf(root, dates.head, sampleType)
    }
    dates.tail.foldLeft(firstDf){case (df, date) => {
        if (addDate) {
            df.union(readSampleDf(root, date, sampleType).withColumn("date", lit(getDateTimeString(date))))
        } else {
            df.union(readSampleDf(root, date, sampleType))
        }
    }}
}

val sampleDates = getDates(getZonedDateTime("2010-10-29"), getZonedDateTime("2010-11-09"))
