# Heap Data Structures

##  What is Heap:

MaxHeap is a complete binary tree where none of the child nodes are greater than the root(In case of Min heap the vice versa). Heap is implemented uing list. 

For the binary tree inlist format to be called as heap, it must be complete ie, All the nodes which are not leaf nodes should have both child. For Heap to be represented in a list of **contiguous** values, the left leaves must be populated first. 

How the trees are represented in a list format. The tree is traversed in a **Breadth first** traversal. The incoming Nodes are appended in list as per the traversal order.

---------------------------------------------------------

## Representation of Heap

### Valid Max Heap

1. **Binary representation**

    ```mermaid
        
    graph TD;
        subgraph "Max Heap"
            A[10] --> B[9];
            A --> C[8];
            B --> D[7];
            B --> E[6];
            C --> F[5];
            C --> G[4];
        end
        
    ```

2. **List Representation**

    ```mermaid
    graph
        subgraph "List Representation";
            A[10] --> B[9] --> C[8] --> D[7] --> E[6] --> F[5] --> G[4];
        end
    ```
    -------------------------------------------------------

### Invalid Max Heap

 - **NOTE:** In below example the node 11 does not adhre to idea of max heap, Parent value is smaller than child


    ```mermaid
    graph TD;
        subgraph "Invalid Max Heap"
            A[10] --> B[9];
            A --> C[8];
            B --> D[7];
            B --> E[6];
            C --> F[5];
            C --> G[11];
        end
    ```



---------------------------------------------------------

### Incomplete Binary Tree 

All the examples stated above were complete trees, but what if tree is not complete. Even if tree is not complete it can still be called as a heap, provided it adhres to the principle of no child value exceeding the value of parent for max heap.

1. **Right Sided incomplete tree**

    ```mermaid
    graph TD;
        subgraph "R Incomplete Tree"
            A[10] --> B[9];
            A --> C[8];
            B --> D[7];
            B --> E[6];
            C --> F[5];
        end
    ```

2. **Left sided incomplete tree.**

    ```mermaid
    graph TD;
        subgraph "L Incomplete Tree"
            A[10] --> B[9];
            A --> C[8];
            C --> F[5];
        end
    ```

**Question** : Which one of the above is valid heap? 

**Hint** Think of the List Representation of both.

If your answer was 1st then you are right. Let look at the the list representaion of both graphs to see why.

1. **Right Sided incomplete Tree**

    ```mermaid
    graph 
        subgraph "List Reprensation of R Tree"
            a[10]-->b[9]-->c[8]-->d[7]-->e[6]-->f[5];
        end

    ```

    The values in the tree can be listed in a contiguos manner. Thats why the Right Sided incomplete tree is a valid max heap.

2. **Left Sided Incomplete Tree**

    ```mermaid
    graph 
        subgraph "List Reprensation of L Tree"
            a[10]-->b[9]-->g["empty"]-->e["empty"]-->c[8]-->f[5]
        end
    ```

    As shown, there are empty places in the list, so the left sided incomplete cant be called as a valid heap.


---------------------------------------------------------

## Internals of Heap

- ### Node Representation:

    Nodes are represented in Breadth first order from left to right in a list. Given the index of the element in list, how do we find its position in a heap. Below is the example.

    - `Left Node of i = 2*i+1`

    - `Right node of i = 2*i+1` 

    - `Parent of i = i//2`

- ### Heapify

    Heapify is operation to heapify any unsorted array.

    - **Code**:
    ```python
    #insert code here

    ```

    - **Time Complexity**: `log(n)`

    - **Space Complexity**: `1`

Mention 



1. heapify, 
heappop
heappush
2. shiftdown
3. shift up
4. heapsort
5. time complexity of all these things. 
6. space complexity as well

## Python Implemenation

1. mention >> 1 trick 
2. Limitations
3. Maxheap or absence of it.