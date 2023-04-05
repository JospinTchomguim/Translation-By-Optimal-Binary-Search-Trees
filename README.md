# Translation-By-Optimal-Binary-Search-Trees
Optimal Binary Search Trees: Application to the text translation from english to french


Suppose you want to write a program that translates texts from English to French. For each occurrence of each English word, search the French equivalent. One way to implement these searches is to create a binary search tree containing n English words as keys, the French equivalents that being the satellite data. As we will explore the tree for each word of the text,we want to minimize the total consultation time. We could guarantee a time of search O(lg n) by occurrence using a red-black tree, or any other species of balanced binary search tree. But the words have different frequencies of appearance; 
however, it may happen that a very common word such as “the” is far from the root and that a rare word like "mycophagist" is near the root. Such an arrangement slows down translation, since the number of nodes visited when searching for a key in a binary tree is one more than the depth of the node containing the key. We want the words that come up often to be close to the root.
Also, there may be English words for which there is no translation in French; these words therefore do not appear in the tree at all.
to modify the dictionary (English words and their meanings in French), you will just have to modify the values of the keys in the source code
