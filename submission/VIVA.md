# Viva Questions and Answers

1. Q: What is Hadoop? A: Hadoop is an open-source framework for distributed storage and processing of large datasets.
2. Q: What is Docker? A: Docker packages applications and dependencies into containers that run consistently.
3. Q: What is HDFS? A: HDFS is the Hadoop Distributed File System used to store large data across machines.
4. Q: What is the NameNode? A: NameNode manages the metadata and namespace of HDFS.
5. Q: What is the DataNode? A: DataNode stores actual blocks of data and serves read/write requests.
6. Q: What is YARN? A: YARN is Hadoop's resource management and job scheduling layer.
7. Q: What is the ResourceManager? A: ResourceManager manages cluster resources and scheduling across applications.
8. Q: What is the NodeManager? A: NodeManager monitors resource usage and launches containers on each node.
9. Q: What is MapReduce? A: MapReduce is a programming model for processing data in parallel across distributed clusters.
10. Q: What is a Mapper? A: A Mapper reads input records and emits intermediate key-value pairs.
11. Q: What is a Reducer? A: A Reducer aggregates intermediate values by key and writes final results.
12. Q: What is Shuffle and Sort? A: It is the phase where map outputs are partitioned, sorted, and sent to reducers.
13. Q: What is a key-value pair? A: It is a pair of data structured as key and value, such as word and count.
14. Q: What is Hadoop Streaming? A: It allows MapReduce jobs to run using external programs like Python scripts.
15. Q: What is Word Count? A: It counts how many times each word appears in the dataset.
16. Q: Why normalize case? A: To ensure Hadoop, hadoop, and HADOOP are treated as the same word.
17. Q: Why remove punctuation? A: To avoid counting punctuation as part of words like Hadoop! and hello, as separate tokens.
18. Q: What is HDFS input/output? A: HDFS input is the source data directory and output is the path where job results are written.
19. Q: How do we compute the top 10 words? A: Sort the final frequency list by count descending and then by word ascending.
20. Q: Why is MapReduce suitable for text analysis? A: It distributes the work and processes large datasets in parallel.
21. Q: Can Hadoop Streaming work with Python? A: Yes, with mapper.py and reducer.py as executable scripts.
22. Q: What happens if a word appears with uppercase variations? A: The mapper lowercases it so all variants become one normalized word.
