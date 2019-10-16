# Test 1

Bespoke neural network performing task of identifying which square on a 3x3 grid is "empty". Performed with random validation set of size 100000 (for future tests such a large validation set is probably not neccessary). The two main takeaways that I've gathered from interpreting these results: 
### 1. Number of training data examples is siginifcantly more important than number of iterations 
### 2. Adding additional nodes to the hidden layer siginificantly improved performance
 
examples, iterations, accuracy

num_hidden == 9
- 250, 250, 31.659%
- 250, 500, 33.968%
- 250, 1000, 32.562%
- 500, 250, 75.717%
- 500, 500, 69.302%
- 500, 1000, 73.081%
- 1000, 250, 79.550%
- 1000, 500, 78.227%
- 1000, 1000, 82.677%

num_hidden == 18
- 250, 250, 63.462%
- 250, 500, 68.778%
- 250, 1000, 40.422%
- 500, 250, 97.495%
- 500, 500, 92.409%
- 500, 1000, 89.909%
- 1000, 250, 97.126%
- 1000, 500, 100%
- 1000, 1000, 100%