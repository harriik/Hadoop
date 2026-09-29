# AIM and Procedure

## TITLE
Hadoop MapReduce Word Frequency and Top 10 Analysis

## AIM
To count the frequency of each word in text files, normalize case, ignore punctuation, and identify the top 10 most frequent words using Hadoop Streaming with Python.

## OBJECTIVES
1. Create input text files representing digital library books.
2. Upload input files to HDFS.
3. Implement mapper.py to emit word and 1 pairs.
4. Implement reducer.py to aggregate counts per word.
5. Run Hadoop Streaming job.
6. Capture the word frequency output.
7. Sort by frequency descending and word ascending to find the top 10.
8. Verify test cases.

## SOFTWARE REQUIREMENTS
- Hadoop 3.3.6
- Docker
- Python 2.7 (available in container)
- HDFS and YARN services

## HADOOP DOCKER SETUP
docker ps -a
docker exec hadoop hadoop version
docker exec -u 0 hadoop hdfs dfsadmin -report
docker exec -u 0 hadoop yarn node -list

## HDFS CONFIGURATION
The environment already contained a working HDFS and YARN setup. The library directory and input folder were retained without deleting or formatting NameNode data.

## YARN CONFIGURATION
The required MapReduce environment variable was set to HADOOP_MAPRED_HOME=/opt/hadoop and mapred-site.xml was corrected so YARN could launch the application master.

## INPUT FILE CREATION
Three files were created: book1.txt, book2.txt, and book3.txt with the required digital-library content.

## HDFS UPLOAD
docker exec -u 0 hadoop hdfs dfs -mkdir -p /library/input
docker exec -u 0 hadoop hdfs dfs -put -f /root/books/book1.txt /library/input/book1.txt
docker exec -u 0 hadoop hdfs dfs -put -f /root/books/book2.txt /library/input/book2.txt
docker exec -u 0 hadoop hdfs dfs -put -f /root/books/book3.txt /library/input/book3.txt

## MAPREDUCE ARCHITECTURE
Mapper reads each line from HDFS input and emits <word,1>.
Shuffle and Sort groups all identical words together.
Reducer sums all values for each key and writes final frequencies.

## MAPPER
The mapper lowercases the text, removes punctuation, splits on whitespace, and emits each word with count 1.

## SHUFFLE AND SORT
Hadoop sorts by key before reducer execution so repeated words are processed together.

## REDUCER
The reducer groups keys and adds counts: total = total + count.

## EXECUTION
docker exec -u 0 hadoop bash -lc 'export HADOOP_MAPRED_HOME=/opt/hadoop; hdfs dfs -rm -r -f /library/output; hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar -files /root/mapper.py,/root/reducer.py -mapper mapper.py -reducer reducer.py -input /library/input -output /library/output'

## WORD FREQUENCY OUTPUT
The actual output file was:
/library/output/part-00000

## TOP 10 OUTPUT
TOP 10 MOST FREQUENTLY OCCURRING WORDS

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

## TEST CASES
1. Case normalization: Hadoop hadoop HADOOP Hadoop! => hadoop    4
2. Punctuation removal: Hello, hello! HELLO. => hello    3
3. Mixed words: MapReduce is powerful. MapReduce is scalable. => is 2, mapreduce 2, powerful 1, scalable 1

## RESULT
The Hadoop Streaming job completed successfully and the actual outputs were written to /library/output/part-00000 and saved to the submission folder.
