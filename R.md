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

The$operator extracts data columns by name
symbols <- df$symbol
symbols
## [1] MOT AAPL IBM
## Levels: AAPL IBM MOT

class(symbols)
## [1] "factor"

Thesymbolscolumn fromthedf3data frame, however, yields a character vector
instead:
symbols <- df3$symbol
symbols
## [1] "MOT" "AAPL" "IBM"

my_list <- list(a = c(1, 2, 3, 4, 5),
b = matrix(1:10, nrow = 2, ncol = 5),
c = data.frame(price = c(89.3, 98.2, 21.2),
stock = c("MOT", "IBM", "CSCO")))

my_list
## $a
##[1]1 2345
## $b
## [,1] [,2] [,3] [,4] [,5]
## [1,] 13579 ## [2,] 246810
## $c
## price stock
## 1 89.3 MOT
## 2 98.2 IBM
## 3 21.2 CSCO

Lists can be indexed by passing a number (the index of the list element) or by
passing the element name into the double bracket operator[[]]:
first_element <- my_list[[1]]

first_element
##[1]1 2345
class(first_element)
## [1] "numeric"

An alternate extraction method is the following:
second_element <- my_list[["b"]]
second_element
## [,1] [,2] [,3] [,4] [,5]
## [1,] 13579 ## [2,] 246810
class(second_element)
## [1] "matrix"

Thesinglebracketoperator[]is used to extract a section of a list. This is a source
of confusion for many novice R programmers. As a reminder, double brackets[[]]
return list elements, whereas single brackets return lists
part_of_list <- my_list[c(1, 3)]
part_of_list
## $a
##[1]1 2345
## $c
## price stock
## 1 89.3 MOT
## 2 98.2 IBM
## 3 21.2 CSCO
class(part_of_list)
## [1] "list"

The size of the list can be determined by calling thelength()function.
size_of_list <- length(my_list)
size_of_list
## [1] 3

Thenew.env()object
A new environment can be created with thenew.env()command:
env <- new.env()
env[["first"]] <- 5
env[["second"]] <- 6
env$third <- 7

To obtain the names, we have to
use thelscommand:
ls(env)
## [1] "first" "second" "third"
To obtain the values associated with those names, we can use the get()
command:
get("first", envir = env)
## 5

Removing elements from an environment is accomplished via therm()com-mand:
rm("second", envir = env)
ls(env)
## [1] "first" "third"


```
