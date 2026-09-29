# Hadoop Word Count Project

## Project title
Hadoop MapReduce Word Frequency and Top 10 Analysis

## Problem statement
Count word frequencies from library input files, ignore punctuation, normalize case, and display the top 10 most frequent words.

## Architecture
- HDFS stores the input and output directories.
- Mapper reads each line, converts to lowercase, strips punctuation, and emits word + 1.
- Shuffle and Sort groups identical keys.
- Reducer sums counts and writes final word frequencies.

## Folder structure
submission/
  README.md
  AIM_PROCEDURE.md
  VIVA.md
  mapper.py
  reducer.py
  book1.txt
  book2.txt
  book3.txt
  testcase_case.txt
  testcase_punctuation.txt
  testcase_words.txt
  word_frequency_output.txt
  top10_output.txt
  execution_log.txt
  hadoop_commands.txt

## Setup commands
docker ps -a
docker exec hadoop hadoop version
docker exec -u 0 hadoop hdfs dfsadmin -report
docker exec -u 0 hadoop yarn node -list

## HDFS commands
docker exec -u 0 hadoop hdfs dfs -ls /
docker exec -u 0 hadoop hdfs dfs -ls /library
docker exec -u 0 hadoop hdfs dfs -ls /library/input
docker exec -u 0 hadoop hdfs dfs -put -f /root/books/book1.txt /library/input/book1.txt

## MapReduce command
export HADOOP_MAPRED_HOME=/opt/hadoop
hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar -files /root/mapper.py,/root/reducer.py -mapper mapper.py -reducer reducer.py -input /library/input -output /library/output

## Top 10 command
Sort the final output by frequency descending and word ascending, then display the first 10 rows.

## Test commands
hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar -files /root/mapper.py,/root/reducer.py -mapper mapper.py -reducer reducer.py -input /library/testcase_case -output /library/testcase_case_output

## Actual results
Word frequency output was successfully generated under /library/output/part-00000. The top 10 words are:

data    11
hadoop    7
is    4
mapreduce    4
processing    4
big    3
for    3
library    3
a    2
books    2
