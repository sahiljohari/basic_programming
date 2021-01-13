## Dynamic Programming

There are essentially 2 approaches to solving a dynamic programming problem:

- Memoization
- Tabulation

#### Memoization

The recipe for this approach is:

- Make it work
  - Visualize the problem as a tree structure
  - Implement the tree using a _recursive_ solution
  - Test it
- Make it efficient
  - Add a `memo` object that is shared among all recursive calls
  - Add a base case to return `memo` values
  - Store return values into the `memo`

#### Tabulation

The recipe for this approach is:

- Visualize the problem as a table which has a size based on the inputs
- Initialize the table with default values
- Seed the trivial answer into the table (this is similar to defining a base case in recursive approaches)
- Iterate through the table
- Fill further positions based on the current position using certain logic depending on the problem

### Things to remember

- Notice any overlapping subproblems
- Decide what is the trivially smallest input
- Think recursively to use Memoization
- Think iteratively to use Tabulation
- Draw a strategy first!!
