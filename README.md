#Algorithms in Python

这是学习笔记[Algorithms](https://github.com/hahastudio/Algorithms)，欢迎访问。

这个项目的教材基于Algorithms by Sanjoy Dasgupta & Christos Papadimitriou & Umesh Vazirani，可以[从这里翻阅](http://www.cs.berkeley.edu/~vazirani/algorithms.html)。

所有的算法实现语言均为`Python`，在`Python2.6.6`的环境下均能测试通过。

##关于实现

基本上所有的实现方案都是照抄书上的伪代码_ (:3」∠)_ 让人感觉Python真是简单易懂，写出来的代码跟书上的伪代码没差嘛！所以，嗯，也就是说， **这些实现都只是玩具，不要用到实际环境中** 。

比如说，关于求`(x**y) % z`，在 `modular_arithmetic.py` 中有函数 `modexp(x, y, z)` ，但我觉得你不用想都知道，肯定还是 `pow(x, y[, z])` 来得更快。再比如UniHashing类，肯定也没有dict类高效且经得起碰撞。

所以，这些都是玩具= =

##目前进度：

* Chapter 0: Prologue
    * Fibonacci numbers    `fibonacci.py`
* Chapter 1: Algorithms with numbers
    * Basic arithmetic     `basic_arithmetic.py`
    * modular arithmetic   `modular_arithmetic.py`
    * Euclid's algorithm   `euclid.py`
    * Primality test       `primality.py`
    * Generating primes    `primality.py`
    * RSA                  `rsa.py`
    * Universal hashing    `hashing.py`
* Chapter 2: Divide-and-conquer algorithms
    * divide-and-conquer multiplication `basic_arithmetic.py`
    * Mergesort                         `mergesort.py`
    * the fast Fourier transform        `fft.py`
    * Polynomial multiplication         `fft.py`
* Chapter 3: Decompositions of graphs
    * Depth-first search                `dfs.py`
* Chapter 4: Paths in graphs
    * Breadth-first search              `bfs.py`
    * Dijkstra's shortest-path algorithm `shortest_path.py`
    * Bellman-Ford algorithm for single-source shortest path `shortest_path.py`
* Chapter 5: Greedy algorithms
    * Kruskal's mininum spanning tree algorithm
    
