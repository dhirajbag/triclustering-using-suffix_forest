# triclustering-using-suffix_forest
UG Final Year Project based on Suffix Forest Based Tri-clustering

We introduce a novel data structure called a suffix-forest to design a tri-clustering algorithm. Tri-clustering is a method of unsupervised data analysis used to find patterns of interest in three-dimensional data.

This is a new approach for association rule mining and bi-clustering using formal concept analysis. The approach is called FIST and is based on the frequent closed itemsets framework, requiring a unique scan of the database. FIST uses a new suffix tree-based data structure to reduce memory usage and improve extraction efficiency, allowing for parallel processing of tree branches. Experiments show that FIST's memory requirements and execution times are in most cases equivalent to frequent closed itemsets-based algorithms and lower than frequent itemsets-based algorithms.


## Already existing techniques for finding frequent closed patterns:
There are several techniques for finding frequent closed patterns in a dataset. Some common techniques include:
1.	Apriori algorithm: This is a popular and well-known algorithm for finding frequent itemsets in a dataset. It uses a bottom-up approach, starting with individual items and gradually combining them into larger itemsets, while pruning any infrequent itemsets.
2.	FP-growth algorithm: This is an efficient and scalable algorithm for finding frequent itemsets in large datasets. It uses a tree-based structure (called an FP-tree) to compactly represent the frequent itemsets, and uses a pattern growth approach to generate the frequent itemsets.
3.	Closed pattern mining: This is a variant of frequent pattern mining that focuses on finding "closed" patterns, which are patterns that are frequent and cannot be extended to include any other frequent items without losing their support. This can be useful for avoiding redundant patterns and reducing the size of the pattern set.
4.	Association rule mining: This is a related technique that focuses on finding associations or relationships between items in a dataset. For example, given a dataset of transactions at a grocery store, association rule mining can be used to find rules of the form "if a customer buys item A, they are likely to also buy item B". This can be used to identify potential correlations or patterns in the data.
Overall, the choice of technique for finding frequent closed patterns in a dataset will depend on the specific requirements of the problem and the characteristics of the dataset, such as its size and complexity.

## How is Suffix Tree based approach better than FP Growth and FP Tree based approach for finding Frequent Patterns ? 
It is not necessarily the case that a suffix tree-based approach is better than an FP-growth or FP-tree-based approach for finding frequent patterns. The relative merits of different algorithms for frequent pattern mining can depend on a variety of factors, such as the size and characteristics of the dataset being analyzed, the specific parameters and settings used by the algorithms, and the desired properties of the frequent patterns being sought. In general, suffix trees can be useful for efficiently storing and processing sequences of items, such as the items in a transaction database, but they may not always be the best choice for finding frequent patterns.

