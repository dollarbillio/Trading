```R
x1 <- c(1, 2, 3) // vector


my_matrix <- matrix(c(1, 2, 3, 4, 5, 6),
nrow = 2, ncol = 3, byrow = TRUE)

my_matrix
## [,1] [,2] [,3]
## [1,] 1 2 3
## [2,] 4 5 6

// Change column and row names
dimnames(my_matrix) <- list(c("one", "hello"),
c("column1", "column2", "c3"))

attributes(my_matrix)
## $dim
## [1] 2 3
## $dimnames
## $dimnames[[1]]
## [1] "one" "hello"
## $dimnames[[2]]
## [1] "column1" "column2" "c3"

The extraction of elements from a matrix can be accomplished via the use of the
[,]operator. To extract the element located in row 1 and column 3, we need to
issue the following command:
ans <- my_matrix[1, 3]
ans
## [1] 3

Here are some examples that utilize vectorization and single element operations
mat1 <- matrix(rnorm(1000), nrow = 100)
round(mat1[1:5, 2:6], 3)

// Another example
mat2 <- mat1[1:25, ] ^ 2
head(round(mat2, 0), 9)[,1:7]

// Data frame
df <- data.frame(price = c(89.2, 23.2, 21.2),
symbol = c("MOT", "AAPL", "IBM"),
action = c("Buy", "Sell", "Buy"))
df
## price symbol action
## 1 89.2 MOT Buy
## 2 23.2 AAPL Sell
## 3 21.2 IBM Buy

In order to disable the conversion of any character vector into a factor, we can use the
stringsAsFactors = FALSEargument within thedata.frame()call:

```
