# 1 LRU Cache
The implementation of LRU Cache was mostly based on the class OrderedDict. 
It is characterized by very high efficiency, which manifests itself in the 
implementation of basic operations. Both get and set operations are performed 
with the use of a dictionary, therefore their computational complexity remains 
at the level of O (1). In the case of a get operation, not the entire data 
structure. Knowing the hahs functions, I know where the key we are looking 
for is. The same applies to the set operation. Hash tables are indispensable 
when it comes to building efficient software. With their O(1) reads and 
insertions, it’s a difficult data structure to beat.

# 2 File Recursion
The computational complexity of recursive algorithms is a bit more complicated 
to evaluate. In this task, we look through each file within the given directory.
If the file is itself a subdirectory (and isn’t a single or double period, which 
represent the current and previous directories, respectively), we print the 
subdirectory name. The computational complexity of recursive functions can be 
considered as a tree.  Where the parent nodes are the directories and the leaf 
nodes are the files themselves. We have visited each node once, then it 
acknowledge that the time complexity of your operation is O(n) where 
N = number of files + number of directories.

# 3 Huffman Encoding
As the basic data structure, I queue to implement the tree. 
From the perspective of the outer loop, we can conclude that the complexity of 
the outer loop is O(n). The Priority_Queue operations: Specifically this 
operation self.priority_queue.put(parent). Removing items from a priority queue 
using the function get() is a constant time operation, however, putting items 
back into the queue is not a constant-time operation. Instead, it has a 
complexity of O(log(n)). Hence given that the second operation is nested within 
the first, then we can conclude that the time complexity of this operation 
is O(n(log(n))). Priority queues are at an equally advanced level of 
implementation - to keep track of the letters and counts - O(n) worst case for 
access and searching, O(1) inserting. During encoding, every iteration of the 
tree node solution adds the computed particular element one element to the 
queue, thus increasing the number of coded elements plus the size of the coding 
string that is related to the depth or number of levels. Decoding requires 
rebuilding the output string to the same size (n) as the original data 
supplied: O(n).

# 4 Active Directory
In order to assess the complexity of the algorithm, one should search for the 
most nested operation which, in this case, will take a linear traversal of all 
groups. Operations, types, comparison, condition check, we can assume that are 
constant and equal 1. The is_user_in_group function will be determined by the 
computation complexity of O(n)

# 5 Blockchain
This task flew to the implementation of basic functionality dictionary.
This implementation is necessarily unequivocally equivalent to pure Python 
and basic functionality. In order to preserve O(1) performance for node removal 
(finding nodes), we must do better than just looping through the linked-list.
The current implementation stores a pointer to the associated key only.
Our dict is a hashmap, its worst case is therefore O(n) if the hash 
function is bad and results in a lot of collisions. 
However that is a very rare case where every item added has the same hash 
and so is added to the same chain which for an our implementation would be 
extremely unlikely. The average time complexity is of course O(1).

# 6 Union and Intersection
This code contains the base implementation of linked list and two functions 
union and intersection based on the implemented structures. Both functions have 
a very similar structure. The only difference is in how the data is traversed.
The first one has two while loops in succession and the final iterations through
the list. The loop loop in this case has a complexity of log(n), we do it twice 
additionally remembering about the final iteration. The whole algorithm should 
have O(n log(n)) complexity.
The Intersect function also passes through one list item at a time, O(n). 
Instead, the structure is nested - checks values in the second list - worst
case O (n^2). The space complexity for both may require adding all the items in
the list either to the sum or to the intersection, worst case O (n^2).
