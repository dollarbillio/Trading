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

Using theplot()function
# Create a vector of numbers x and plot them
x <- c(1, 2, 3.2, 4, 3, 2.1, 9, 19)
plot(x)

# Convert the graph into a line plot
plot(x, type = "l")

?plotreveals a few more useful plot types:
• ''p'' for points
• ''l'' for lines
• ''b'' for both
• ''c'' for the lines part alone of ''b''
• ''o'' for both overplotted
• ''h'' for histogram like (or high-density) vertical lines
• ''s'' for stair steps
• ''S'' for other steps
• ''n'' for no plotting

The following example demonstrates the creation of a plot with a main title, axis-labels,
and a basic grid. A vertical and a horizontal line are also placed on the graph after
the initial points have been rendered byplot():

# Set up the canvas
plot(rnorm(1000), main = "Some returns", cex.main = 0.9,
xlab = "Time", ylab = "Returns")
# Superimpose a basic grid
grid()
# Create a few vertical and horizontal lines
abline(v = 400, lwd = 2, lty = 1)
abline(h = 2, lwd = 3, lty = 3)

Further information onv, h, lwd, lty, and other arguments of abline()
can be found by calling?abline.Thelwdargument defines the line-width, and
theltyargument defines the line-type.

Thepar()command is used to query or set up global graphical parameters that can be used by all subsequent calls toplot(). The following code splits the view-ing window into a rectangular format with two rows and two columns. Aplot() command can then be issued for each one of the child windows. Lines and text can subsequently be added to each unique child plot:

# Create a 2-row, 2-column format
par(mfrow = c(2, 2))
# First plot (points).
plot(rnorm(100), main = "Graph 1")
# Second plot (lines).
plot(rnorm(100), main = "Graph 2", type = "l")
# Third plot (steps) with a vertical line
plot(rnorm(100), main = "Graph 3", type = "s")
abline(v = 50, lwd = 4)
# Fourth plot
plot(rnorm(100), type = "h", main = "Graph 4")
# Reset the plot window
par(mfrow = c(1, 1))

Here’s how to add some text and a legend to the plot:
plot(rnorm(100), main = "A line plot",
cex.main = 0.8,
xlab = "x-axis",
ylab = "y-axis",
type = "l")
# Extra text
mtext("Some text at the top", side = 3)
#Atx=40andy= -1coordinates
legend(40, -1, "A legend")

Entering
?plot.default in the console will list what these are. Alternatively, the
formals()function can be used to extract the arguments of the function:
formals(plot.default)
```
---
```R
# Greate 100 standard normals
x <- rnorm(100, mean = 0, sd = 1)
# Find the length of the vector x.
length(x)
# Compute the mean of x
mean(x)
# Compute the standard deviation of x
sd(x)
# Compute the median value of the vector x
median(x)
# Compute the range (min, max) of a variable
range(x)
# Find the sum of all the numbers in x
sum(x)
# Do a cumulative sum of the values in x
cumsum(x)
# Display the first 3 elements of x
head(x, 3)
# Display summary statistics on x
summary(x)
# Sort x from largest to smallest.
sort(x, decreasing = TRUE)
# Compute the successive difference in x
diff(x)
# Create an integer sequence from 1 to 10
1:10
# A sequence from 1 to 10 in steps of 0.1
seq(1, 10, 0.1)

# Define a boolean variable
my_boolean <- 1 == 2
if (my_boolean) {
print("not correct")
} else {
print("XYZ")
}

The commandsifelse()andswitch()are also used for controlling the flow
of execution. For the repetitive execution of code, thefor(), while(),and
repeat()commands should be used. Thefor()loop is used to execute certain
functionality multiple times in a row. According to the help("for")documen-tation, the syntax of the for loop is of the form:for(var in seq) expr,where var is a variable,in is a reserved keyword, and seq is an expression evaluating to a
vector.Hereare two examples:
for(i in 1:5) {
cat(i, "\n")
}
## 1
## 2
## 3
## 4
## 5
some_list <- list()
for(z in c("hello", "goodbye")) {
some_list[[z]] <- z
}
some_list
## $hello
## [1] "hello"
## $goodbye
## [1] "goodbye"

## Helper Function and Regular Expression
filter_and_sort_symbols <- function(symbols) {
# Name: filter_symbols
# Purpose: Convert to upper case if not
# and remove any non valid symbols
# Input: symbols = vector of stock tickers
# Output: filtered_symbols = filtered symbols
# Convert symbols to uppercase
symbols <- toupper(symbols)
# Validate the symbol names
valid <- regexpr("^[A-Z]{2,4}$", symbols)
# Return only the valid ones
return(sort(symbols[valid == 1]))
}

The regular expression pattern used in the previous example
(^[A-Z]{2,4}$) specifies that the string to bematched should start with an upper-case letter and end with an uppercase letter. It also requires that there be exactly
two, three, or four letters present. Anything else will not be considered as a valid
stock symbol. Theregexpr()function returns a vector of equal length to that of
thesymbolsvector. An entry of 1 is used to denote the valid names, and an entry
of−1, the invalid ones. Thetopper()function is used to convert all the letters into
uppercase prior to applying the regular expression.

extract_prices <- function(filtered_symbols, file_path) {
# Name: extract_prices
# Purpose: Read price data from specified file
# Inputs: filtered_symbols = vector of symbols,
# file_path = location of price data
# Output: prices = data.frame of prices per symbol
# Read in the .csv price file
all_prices <- read.csv(file = file_path, header = TRUE,
stringsAsFactors = FALSE)
# Make the dates row names
rownames(all_prices) <- all_prices$Date
# Remove the original Date column
all_prices$Date <- NULL
# Extract only the relevant data columns
valid_columns <- colnames(all_prices) %in% filtered_symbols
return(all_prices[, valid_columns])
}
By assigning a column name of a data frame to NULL, we effectively remove that
column from the data frame. This operation can also be used to remove elements
from a list. The %in%command asks the following question: which elements of
vector A are also in vector B?

Now that we have the prices of the filtered stocks in a data frame, we can perform
some basic filtering. For now, we will take a look at the data and identify the rows
withmissing values. At this stage, we will not use this information to filter the data.
We just care about the mechanics of identifying bad entries.
filter_prices <- function(prices) {
# Name: filter_prices
# Purpose: Identify the rows with missing values
# Inputs: prices = data.frame of prices
# Output: missing_rows = vector of indexes where
# data is missing in any of the columns
# Returns a boolean vector of good or bad rows
valid_rows <- complete.cases(prices)
# Identify the index of the missing rows
missing_rows <- which(valid_rows == FALSE)
return(missing_rows)
}

compute_pairwise_correlations <- function(prices) {
# Name: compute_pairwise_correlations
# Purpose: Calculates pairwise correlations of returns
# and plots the pairwise relationships
# Inputs: prices = data.frame of prices
# Output: correlation_matrix = A correlation matrix
# Convert prices to returns
returns <- apply(prices, 2, function(x) diff(log(x)))
# Plot all the pairwise relationships
pairs(returns, main = "Pairwise return scatter plot")
# Compute the pairwise correlations
correlation_matrix <- cor(returns, use = "complete.obs")
return(correlation_matrix)
}

# Stock tickers entered by user
symbols <- c("IBM", "XOM", "2SG", "TEva",
"G0og", "CVX", "AAPL", "BA")
# Location of our database of prices
file_path <- "path/prices.csv"
# Filter and sort the symbols
filtered_symbols <- filter_and_sort_symbols(symbols)
filtered_symbols
## [1] "AAPL" "BA" "CVX" "IBM" "TEVA" "XOM"
# Extract prices
prices <- extract_prices(filtered_symbols, file_path)
# Filter prices
missing_rows <- filter_prices(prices)
missing_rows
## integer(0)
# Compute correlations
correlation_matrix <- compute_pairwise_correlations(prices)
correlation_matrix
```
---
```R
# Load the .csv file
aapl_2 <- read.csv(file = "path/aapl.csv", header = TRUE,
stringsAsFactors = FALSE)
# Reverse the entries
aapl_2 <- aapl_2[rev(rownames(aapl_2)), ]
This time around, we specified that headers are present in the input file. R knows
to call the columns by their correct names, and if we want to extract the closing-price, the following command suffices:
aapl_close <- aapl_2[, "Close"]
To get some quick summary statistics in tabular format, we can utilize the
summary()function.
summary(aapl_close)
## Min. 1st Qu. Median Mean 3rd Qu. Max.
## 11.00 25.50 40.50 96.29 77.00 702.10

install.packages("quantmod")
install.packages(pkgs, lib, repos = getOption("repos"),
contriburl = contrib.url(repos, type),
method, available = NULL, destdir = NULL,
dependencies = NA, type = getOption("pkgType"),
configure.args = getOption("configure.args"),
configure.vars = getOption("configure.vars"),
clean = FALSE, Ncpus = getOption("Ncpus", 1L),
verbose = getOption("verbose"),
libs_only = FALSE, INSTALL_opts, quiet = FALSE,
keep_outputs = FALSE, ...)

# Write to csv?
write.csv(aapl_2, file = "path/aapl_2.csv")
This file registers as 455 KB on disk.
save(aapl_2, file = "path/aapl_2.rdata")

aapl_old <- aapl_2
rm(aapl_2)
load(file = "path/aapl_2.rdata")

identical(aapl_old, aapl_2)
## [1] TRUE

library(XLConnect)
# Create a workbook object
book <- loadWorkbook("path/strategy.xlsx")
# Convert it into a data frame
signals = readWorksheet(book, sheet = "signals", header
= TRUE)

strength = readWorksheet(book, sheet = "strength", header
= TRUE)

It is also possible to create a workbook and populate it with data from R.
# Setup a new spreadsheet
book <- loadWorkbook("demo_sheet.xlsx", create = TRUE)
# Create a sheet called stock1
createSheet(book, name = "stock1")
# Creating a sheet called stock2
createSheet(book, name = "stock2")
# Load data into workbook
df <- data.frame(a = c(1, 2, 3), b = c(4, 5, 6))
writeWorksheet (book, data=df, sheet="stock1", header = TRUE)
# Save the workbook
saveWorkbook(book, file = "path/demo_sheet.xlsx")
```
---
```R
# Load the RODBC package
require(RODBC)
# Establish a connection to MySQL
con <- odbcConnect("rfortraders")
# Choose the database name and table name
database_name <- "OptionsData"
table_name <- "ATMVolatilities"
symbol <- "SPY"
sql_command <- paste0("SELECT Symbol, Date, Maturity,Delta, CallPut, ImpliedVolatility FROM ",
database_name, ".", table_name,
" WHERE Maturity = 91
AND Symbol IN ('", symbol, "');")
iv <- sqlQuery(con, sql_command)
# disconnect from database
odbcClose(con)

The above SQL-query extracts the implied volatilities of a 91-daymaturity option
for the SPY ETF for an arbitrary number of days.

TheRMySQLpackage provides similar functionality to theRODBCone. It is
custom tailored to MySQL, and many practitioners who work with such databases
prefer to use this package instead. Here is some code that establishes a connection
to the local instance, extracts the data in the form of a data frame, and then, closes
the connection:
# Load the necessary package
require(RMySQL)
# Establish a connection
con <- dbConnect(MySQL(), user="your_login",
password="your_password",
dbname="OptionsData",
host="location_of_database")
# List the tables and fields
dbListTables(con)
# Define the command and extract a data frame
sql_command <- paste0("SELECT Symbol, Date, Maturity,
Delta, CallPut, ImpliedVolatility FROM ",database_name, ".", table_name,
" WHERE Maturity = 91
AND Symbol IN ('", symbol, "');")
result <- dbGetQuery(con, sql_command)
# Close the connection
dbDisconnect(con)
It is also possible to extract the tabular data in chunks if the data is voluminous.
results <- dbSendQuery(con, sql_command)
partial_results <- fetch(results, n = 100)

Thedplyrpackage
# Get the CRAN version
install.packages("dplyr")
require(dplyr)
# Or, first load devtools
install.packages("devtools")
require(devtools)
# Get the github version
devtools::install_github("hadley/dplyr")
require(dplyr)

Here are some important commands to be aware of when dealing withdplyr:
• tbl()
• groupby()
• summarise()
• do()
• %>%

core functionality and will utilize a
data set that is part of thedplyrinstallation
# Load the flight database that comes with dplyr
library(hflights)
# Look at number of rows and columns
dim(hflights)
## [1] 227496 21

We could have easily coerced the data into a data frame instead.
# First, coerce the data into a data.table
flights_dt <- tbl_dt(hflights)
# What type of object is this?
class(flights_dt)
## [1] "tbl_dt" "tbl" "data.table" "data.frame"

To find the median arrival delay time for all carriers, we begin by grouping the
data by carrier:
# Create a grouping by carrier
carrier_group <- group_by(flights_dt, UniqueCarrier)
# Now compute the summary statistics
summarise(carrier_group, avg_delay = mean(ArrDelay, na.rm = TRUE))

The execution time for the aggregate summary is on the order ten milliseconds.
This is pretty fast indeed. Here is what the summary looks like in Table 3.2.
Thedo()function allows one to apply an arbitrary function to a group of data.
The%>%operator can be used to chain the results together. An example of this can
be seen by typing?doin the R console.

# load the library xts
library(xts)

# Load a small dataset that comes along with xts.
# We could have used our original .csv file as well.

data(sample_matrix)
# Look at the data
head(sample_matrix)
## [1] "matrix"
# What is the type of this object?
class(sample_matrix)
## [1] "matrix"
# Use the str() command to get more details about this object.
str(sample_matrix)
## num [1:180, 1:4] 50 50.2 50.4 50.4 50.2 ...
## - attr(*, "dimnames")=List of 2
## ..$ : chr [1:180] "2007-01-02" "2007-01-03"
## "2007-01-04" "2007-01-05" ...
## ..$ : chr [1:4] "Open" "High" "Low" "Close"

The output fromstr()can be somewhat daunting. It is telling us that thematrix
has 180 rows and 4 columns. It is also displaying that the row names equal the dates
and that the column names equal the strings: "Open", "High", "Low", and "Close".
We can take this data and convert it into anxtsobject.Totheuser,everythingwill
look the same as before. Underneath the hood, though, R will be doing some pretty
neat indexing.

xts_matrix<-as.xts(sample_matrix, descr ='my new xts object')

str(xts_matrix}
## An 'xts' object on 2007-01-02/2007-06-30 containing:
## Data: num [1:180, 1:4] 50 50.2 50.4 50.4 50.2 ...
## - attr(*, "dimnames")=List of 2
## ..$ : NULL
## ..$ : chr [1:4] "Open" "High" "Low" "Close"
## Indexed by objects of class: [POSIXct,POSIXt] TZ:
## xts Attributes:
## List of 3
## $ tclass: chr [1:2] "POSIXct" "POSIXt"
## $ tzone : chr ""
## $ descr : chr "my new xts object"

Theplot()function knows that it is now dealing
with anxtsinput object and, as such, will produce a different graphical layout. This
is polymorphic
11
behavior in action.
# Simple plot
plot(xts_matrix[,1], main = "Our first xts plot",
cex.main = 0.8)
# Or we can try something fancier.
plot(xts_matrix, main = "Candle plot on xts object",
cex.main = 0.8, type = "candles")

Given that we
want to plot the price of a stock between two dates, how can this be accomplished?
Here are some examples:
plot(xts_matrix["2007-01-01::2007-02-12"],
main = "An xts candle plot with subsetting",
cex.main = 0.8, type = "candles")

Notice the single string argument that is passed to the price matrix. This
time-based formatting makes it easy to work with human readable dates as time
boundaries.
range <- "2007-03-15::2007-06-15"
plot(xts_matrix(range))

Thepaste()function is useful for concatenating strings together. It takes the
input arguments and pastes them together. By default, it will separate the strings
with a space, unless one specifiessep = "".
start_date <- "2007-05-05"
end_date <- "2007-12-31"
plot(xts_matrix[paste(start_date, "::",
end_date, sep = "")])
# Defaults to space separator
paste("Hello", "World", "in R")
## [1] "Hello World in R"
paste("Hello", "Again", sep = "**")
## [1] "Hello**Again"

A vector of strings can be pasted together with a specified separator between the
elements of the vector as follows:
paste(c(1,2,3,4,5), collapse = "oooo")
## [1] "1oooo2oooo3oooo4oooo5"

In most
cases, the user has to specify what format the time index is in.
Here is an example that illustrates this point:

# Create a vector of 10 fictitious stock prices along with
# a time index in microsecond resolution.
price_vector <- c(101.02, 101.03, 101.03, 101.04, 101.05,
101.03, 101.02, 101.01, 101.00, 100.99)
dates <- c("03/12/2013 08:00:00.532123",
"03/12/2013 08:00:01.982333",
"03/12/2013 08:00:01.650321",
"03/12/2013 08:00:02.402321",
"03/12/2013 08:00:02.540432",
"03/12/2013 08:00:03.004554",
"03/12/2013 08:00:03.900213",
"03/12/2013 08:00:04.050323",
"03/12/2013 08:00:04.430345",
"03/12/2013 08:00:05.700123")

# Allow the R console to display the microsecond field
options(digits.secs = 6)
# Create the time index with the correct format
time_index <- strptime(dates, format = "%d/%m/%Y %H:%M:%OS")

# Pass the time index into the its object
xts_price_vector <- xts(price_vector, time_index)

Theoptions(digits.secs)command controls themaximumnumber of dig-its to print on the screen when formatting time values in seconds. This will ensure
that the microseconds in the time stamp show up when the xtspricevector
is referenced in the console.

 The strptime()function takes a string or a vector
of strings as an input and converts them into the specified format. One important
thing to keep in mind is that the specified time stamp has microsecond resolution.
Therefore, a %OS symbol, and not %S (seconds), is required at the end of the time
format. The documentation on?strptimeincludes specific formatting details.

Given a perfectly validxtstime series object, we can plot it and also add some
vertical and horizontal lines as we have done before. The vertical line can now be
indexed by the time stamp. The only tricky part with the vertical line is that we have
to define what format the time stamp is in. This can be done via theas.POSIXct()
function.

# Plot the price of the fictitious stock
plot(xts_price_vector, main = "Fictitious price series",
cex.main = 0.8)
# Add a horizontal line where the mean value is
abline(h = mean(xts_price_vector), lwd = 2)
# Add a vertical blue line at a specified time stamp
my_time <- as.POSIXct("03/12/2013 08:00:03.004554",
format = "%d/%m/%Y %H:%M:%OS")
abline(v = my_time, lwd = 2, lty = 2)

To extract the data component of the price vector, we can use thecoredata()
command. The following example looks at manipulating the time index directly.
To motivate this example, we will create a nonhomogeneous time series. Nonho-mogeneity in time is something that is encountered a lot in practice. Important
events tend to arrive at irregular time intervals. Take, for example, a subset of trades
on the S&P 500 E-mini (ES) futures contract within a specified time interval. It
might look something like this:
es_price <- c(1700.00, 1700.25, 1700.50, 1700.00, 1700.75,
1701.25, 1701.25, 1701.25, 1700.75, 1700.50)
es_time <- c("09/12/2013 08:00:00.532123",
"09/12/2013 08:00:01.982333",
"09/12/2013 08:00:05.650321",
"09/12/2013 08:10:02.402321",
"09/12/2013 08:12:02.540432",
"09/12/2013 08:12:03.004554",
"09/12/2013 08:14:03.900213",
"09/12/2013 08:15:07.090323",
"09/12/2013 08:16:04.430345",
"09/12/2013 08:18:05.700123")
# create an xts time series object
xts_es <- xts(es_price, as.POSIXct(es_time,
format = "%d/%m/%Y %H:%M:%OS"))
names(xts_es) <- c("price")

Onemetric of interest that comes up in high-frequency trading is the trade order-arrival rate. We can explore this metric by looking at the successive differences in
time stamps between trades. Thedifftime()function computes the time differ-ence between two date-time objects. This example sets the time unit explicitly to
seconds. The default setting also happens to be the same.
time_diff <- difftime(index(xts_es)[2], index(xts_es)[1],
units = "secs")
time_diff
## Time difference of 1.45021 secs

We can create a loop that will go through all the pairs and then store the results
in a vector.
diffs <- c()

for(i in 2:length(index(xts_es))) {
diffs[i] <- difftime(index(xts_es)[i], index(xts_es)[i - 1],
units = "secs")
}
This will certainly work, but it is not the optimal way to obtain the answer. Here
is a vectorized solution:
diffs <- index(xts_es)[-1] - index(xts_es)[-length(index(xts_es))]
diffs
## Time differences in secs
## [1] 1.4502099 3.6679881 596.7520001
## [4] 120.1381109 0.4641221 120.8956590
## [7] 63.1901100 57.3400221 121.2697780
## attr(,"tzone")

class(diffs)
## [1] "difftime"

The above line of code can further be optimized by calling theindex()function
once instead of three times.
es_times <- index(xts_es)
diffs <- es_times[-1] - es_times[-length(es_times)]
diffs
## Time differences in secs
## [1] 1.4502099 3.6679881 596.7520001
## [4] 120.1381109 0.4641221 120.8956590
## [7] 63.1901100 57.3400221 121.2697780
## attr(,"tzone")
We can also generate a graphical representation of the the time differences
between consecutive trades for our fictitious ES future time series.
par(mfrow = c(2, 1))
diffs <- as.numeric(diffs)
plot(diffs, main = "Time difference in seconds for ES trades",
xlab = "", ylab = "Time differences",
cex.lab = 0.8,
cex.main = 0.8)
grid()
hist(diffs, main = "Time difference in seconds for ES trades",

xlab = "Time difference (secs)", ylab = "Observations",
breaks = 20,
cex.lab = 0.8,
cex.main = 0.8)
grid()
```
---
Using the quantmod package
```R
Thequantmodpackage provides online and offline access to financial data inxts
format. It also provides facilities for creating intricate graphs tailored to financial
data.
Here is howwe can extract some Apple stock data from Yahoo.
# Load the quantmod packages after installing it locally.
library(quantmod)
AAPL <- getSymbols("AAPL", auto.assign=FALSE)
head(AAPL)

Theauto.assignparameter allows for the returned object to be stored in a local
variable rather than the R session’s.GlobalEnv. Some of the other arguments to
getSymbols()are:src,time,andverbose.
Thesrcargument specifies the source of the input data. It can be set to extract
information from sources such as:
• Yahoo
• Google
• Fred
• Oanda
• mysql
• .csv files
The time argument can be of the form ''2011/'' or ''2010-08-09::2010-08-12''.

Charting withquantmod
ThechartSeriesfunction can be directly applied to anxtsobject with open, high,
low, and close data. There are many arguments to chartSeriesthat can assist in
the further customization of a chart. As usual, we can reference ?chartSeries
for more information. Using our previously created AAPL object, this is what the
function outputs:
# Adding some technical indicators on top of the original plot
chartSeries(AAPL, subset='2010::2010-04',
theme = chartTheme('white'),
TA = "addVo(); addBBands()")
ThereChart()function can be used to update the original chart without
specifying the full set of arguments:
reChart(subset='2009-01-01::2009-03-03')
Thequantmodpackage exposes a range of technical indicators that can seam-lessly be added on top of any chart. These technical indicators reside within theTTR
package that was authored by Josh Ulrich [59].TTRis one of those dependencies
that is automatically loaded during thequantmodinstallation process.
chartSeries(AAPL, subset='2011::2012',
theme = chartTheme('white'),
TA = "addBBands(); addDEMA()")

Technical indicators can also be invoked after the chart has been drawn by using
addVo()
addDPO()

Two more functions that are definitely worth exploring are addTA()and
newTA(). These allow the creation of custom indicators that can be rendered in
a subchart or overlaid onto the main plot.
In this next example, we will plot the price of AAPL without any technical indica-tors, and thenwe will create a custom indicator that uses the close price of the stock.
The custom indicator simply adds 90 to the existing price. One can, of course, use
this method to create arbitrarily complex indicators.
# Initial chart plot with no indicators
chartSeries(AAPL, theme = chartTheme('white'), TA = NULL)
# Custom function creation
my_indicator <- function(x) {
return(x + 90)
}

add_my_indicator <- newTA(FUN = my_indicator, preFUN=Cl,
legend.name = "My Fancy Indicator", on = 1)
add_my_indicator()
```
---
ggplot2
```R
In order to illustrate some of the functionality ofggplot2, we will create a plot of
the volume distribution of AAPL for varying levels of percentage returns:
# Create a matrix with price and volume
df <- AAPL[, c("AAPL.Adjusted", "AAPL.Volume")]
names(df) <- c("price", "volume")

# Create
df$return <- diff(log(df[, 1]))
df <- df[-1, ]
Next, we will use thecut()function to create buckets of returns. We are specifi-cally interested in themagnitude of the returns. A total of three buckets will be used
for this demonstration:
df$cuts <- cut(abs(df$return),
breaks = c(0, 0.02, 0.04, 0.25),
include.lowest = TRUE)
# Create another column for the mean
df$means <- NA
for(i in 1:3) {
group <- which(df$cuts == i)
if(length(group) > 0) {
df$means[group] <- mean(df$volume[group])
}
}

Figure 4.13 displays the contents of our objectdf.
Buckets labeled as 1, group together the lowest returns, whereas buckets with the
value of 3, include the highest returns. All other returns fall somewhere in-between.
We want to graph the distribution of the volume for each of these buckets.
# Load ggplot2
library(ggplot2)
ggplot(df) +
geom_histogram(aes(x=volume)) +
facet_grid(cuts ~ .) +
geom_vline(aes(xintercept=means), linetype="dashed", size=1)
Upon initial inspection,ggplot2syntax can appear somewhat confusing. The
aes()attribute specifies the aesthetics of how the data will be rendered on the x or
yaxis. Thegeomidiom defines the type of plot to be displayed. The + operator is
used to concatenate the layers together into a coherent graph.
```
---
```R
# Set the seed
set.seed(100)
X <- rnorm(1000000, mean = 2.33, sd = 0.5)
mu <- mean(X)
sd <- sd(X)
hist(X, breaks = 100)
abline(v = mu, lwd = 3, lty = 2)

set.seed(12)
rnorm(5)
## [1] -1.4805676 1.5771695 -0.9567445 -0.9200052 -1.9976421
Runningrnorm(5)againwithout preceding it withset.seed(12)will produce
a different set of numbers:
rnorm(5)
## [1] -0.2722960 -0.3153487 -0.6282552 -0.1064639 0.4280148
We will create three vectors of size 5, 10, and 50 from X:

sample5 <- sample(X, 5, replace = TRUE)
sample10 <- sample(X, 10, replace = TRUE)
sample50 <- sample(X, 50, replace = TRUE)
sample5
## [1] 2.497921 2.635927 2.291848 2.127974 2.268268
sample10
## [1] 2.064451 2.274464 2.468938 1.800007 2.557669
## [6] 2.535241 1.331020 1.159151 1.661762 2.285889
sample50
## [1] 2.581844 2.138331 3.003670 1.864148 2.049141
## [6] 2.808971 1.400057 2.527640 3.639216 3.311873
mean(sample5)
## [1] 2.364388
mean(sample10)
## 2.013859
mean(sample50)
## 2.447003
mean(sample(X, 1000, replace = TRUE))
## 2.323124
mean(sample(X, 10000, replace = TRUE))
## [1] 2.334109

This example will build on the previous one. This time, we will take repeated
measurements from X, but we will keep the sample size the same:
mean_list <- list()
for(i in 1:10000) {
mean_list[[i]] <- mean(sample(X, 10, replace = TRUE))
}
hist(unlist(mean_list), breaks = 500,xlab = "Mean of 10 samples from X",
main = "Convergence of sample distribution",
cex.main = 0.8)
abline(v = mu, lwd = 3, col = "white", lty = 2)

The distribution of the sample averages converges to a normal-looking distribu-tion! To see how powerful theCentral Limit Theoremis, consider a population
that is highly nonnormal. We can create such a population by repeatedly picking
eithera0or a1with a50percentprobability:
population <- sample(c(0, 1), 100000, replace = TRUE)
hist(population, main = "Non-normal", cex.main = 0.8)
abline(v = mean(population), lwd = 3, lty = 3)
By repeatedly extracting samples of size 10 from this highly nonnormal distribu-tion, we still obtain a normal-looking distribution for the sample means:
mean_list <- list()
for(i in 1:10000) {
mean_list[[i]] <- mean(sample(population, 10, replace = TRUE))
}
hist(unlist(mean_list), main = "Distribution of averages",
cex.main = 0.8,
xlab = "Average of 10 samples")
abline(v = 0.5, lwd = 3)

```
---
```R
# Set the seed
set.seed(100)
X <- rnorm(1000000, mean = 2.33, sd = 0.5)
mu <- mean(X)
sd <- sd(X)
hist(X, breaks = 100)
abline(v = mu, lwd = 3, lty = 2)

set.seed(12)
rnorm(5)
## [1] -1.4805676 1.5771695 -0.9567445 -0.9200052 -1.9976421

Runningrnorm(5)againwithout preceding it withset.seed(12)will produce
a different set of numbers:
rnorm(5)
## [1] -0.2722960 -0.3153487 -0.6282552 -0.1064639 0.4280148

sample5 <- sample(X, 5, replace = TRUE)
sample10 <- sample(X, 10, replace = TRUE)
sample50 <- sample(X, 50, replace = TRUE)
sample5
## [1] 2.497921 2.635927 2.291848 2.127974 2.268268
sample10
## [1] 2.064451 2.274464 2.468938 1.800007 2.557669
## [6] 2.535241 1.331020 1.159151 1.661762 2.285889
sample50
## [1] 2.581844 2.138331 3.003670 1.864148 2.049141
## [6] 2.808971 1.400057 2.527640 3.639216 3.311873
mean(sample5)
## [1] 2.364388
mean(sample10)
## 2.013859
mean(sample50)
## 2.447003
mean(sample(X, 1000, replace = TRUE))
## 2.323124
mean(sample(X, 10000, replace = TRUE))
## [1] 2.334109

mean_list <- list()
for(i in 1:10000) {
mean_list[[i]] <- mean(sample(X, 10, replace = TRUE))
}
hist(unlist(mean_list), breaks = 500,
     xlab = "Mean of 10 samples from X",
     main = "Convergence of sample distribution",
     cex.main = 0.8)
abline(v = mu, lwd = 3, col = "white", lty = 2)

#We can create such a population by repeatedly picking either a 0 or a 1 with a 50 percent probability
population <- sample(c(0, 1), 100000, replace = TRUE)
hist(population, main = "Non-normal", cex.main = 0.8)
abline(v = mean(population), lwd = 3, lty = 3)

extracting samples of size 10 from this highly nonnormal distribu-tion, we still obtain a normal-looking distribution for the sample means:
mean_list <- list()
for(i in 1:10000) {
mean_list[[i]] <- mean(sample(population, 10, replace = TRUE))
}
hist(unlist(mean_list), main = "Distribution of averages",
cex.main = 0.8,
xlab = "Average of 10 samples")
abline(v = 0.5, lwd = 3)

The one with the larger variance is
unbiased and inefficient. The one with a lower variance is unbiased and efficient.
Similarly, the other two displayed distributions are both biased (since their averages
do not fall on the true parameter)

This next function computes the variance:
# Formula for population variance
population_variance <- function(x) {
mean <- sum(x) / length(x)
return(sum((x - mean) ^ 2) / length(x))
}
# Create a population
population <- as.numeric(1:100000)
variance <- population_variance(population)
variance
## [1] 833333333

What happens when we use the same formula on repeated samples from this
population? We will call thepopulationvariance()function repeatedly with a
sample size set to 100.
output <- list()
for(i in 1:1000) {
output[[i]] <- population_variance(sample(population,
10, replace = TRUE))
}
variance_estimates <- unlist(output)
hist(variance_estimates, breaks = 100, cex.main = 0.9)
average_variance <- mean(variance_estimates)
abline(v = average_variance, , lty = 2, lwd = 2)
abline(v = variance, lwd = 2)

# Formula for unbiased variance estimator
sample_variance <- function(x) {
mean <- sum(x) / length(x)
return(sum((x - mean) ^ 2) / (length(x) - 1))
}
output <- list()
for( i in 1:1000 ) {
output[[i]] <- sample_variance(sample(population,
10, replace = TRUE))
}
sample_variance_estimates <- unlist(output)
average_sample_variance <- mean(sample_variance_estimates)
average_sample_variance
## [1] 836184961

# Draw the graph
plot(c(-1, 1), c(0.5, 0.5), type = "h", lwd = 3,
xlim = c(-2, 2), main = "Probability mass function of coin
toss",
ylab = "Probability",
xlab = "Random Variable",
cex.main = 0.9)
```
---
```R
outcomes <- sample(c(0, 1), 1000, replace = TRUE)

set.seed(101)
biased_outcomes <- sample(c(0, 1), 1000,
replace = TRUE, prob = c(0.4, 0.6))

# Extract prices and compute statistics
prices <- SPY$SPY.Adjusted
mean_prices <- round(mean(prices), 2)
sd_prices <- round(sd(prices), 2)
# Plot the histogram along with a legend
hist(prices, breaks = 100, prob=T, cex.main = 0.9)
abline(v = mean_prices, lwd = 2)
legend("topright", cex = 0.8, border = NULL, bty = "n",
paste("mean=", mean_prices, "; sd=", sd_prices))
```
---
```R
We can take a look at a similar price distribution, but this time, over a different
time range.
plot_4_ranges <- function(data, start_date, end_date, title){
# Set the plot window to be 2 rows and 2 columns
par(mfrow = c(2, 2))
for(i in 1:4) {
# Create a string with the appropriate date range
range <- paste(start_date[i], "::", end_date[i], sep = "")
# Create the price vector and necessary statistics
time_series <- data[range]
mean_data <- round(mean(time_series, na.rm = TRUE), 3)
sd_data <- round(sd(time_series, na.rm = TRUE), 3)
# Plot the histogram along with a legend
hist_title <- paste(title, range)
hist(time_series, breaks = 100, prob=TRUE,
xlab = "", main = hist_title, cex.main = 0.8)
legend("topright", cex = 0.7, bty = 'n',
paste("mean=", mean_data, "; sd=", sd_data))
}
# Reset the plot window
par(mfrow = c(1, 1))
}
Having defined the function, we can now use it as follows:
# Define start and end dates of interest
begin_dates <- c("2007-01-01", "2008-06-06",
"2009-10-10", "2011-03-03")
end_dates <- c("2008-06-05", "2009-09-09",
"2010-12-30", "2013-01-06")
# Create plots
plot_4_ranges(prices, begin_dates,
end_dates, "SPY prices for:")

# Compute log returns
returns <- diff(log(prices))
# Use the same function as before to plot returns rather
than prices
plot_4_ranges(returns, begin_dates, end_dates, "SPY log
prices for:")
```
---
Stationary test
```R
# Get SPY data and let's confirm that it is non-stationary
require(quantmod)
getSymbols("SPY")
spy <- SPY$SPY.Adjusted
# Use the default settings
require(urca)
test <- ur.kpss(as.numeric(spy))
# The output is an S4 object
class(test)

spy_returns <- diff(log(spy))
# Test on the returns
test_returns <- ur.kpss(as.numeric(spy_returns))
test_returns@teststat
## [1] 0.336143
test_returns@cval
## 10pct 5pct 2.5pct 1pct
## critical values 0.347 0.463 0.574 0.739

--> doesn't reject null --> Here we cannot reject the null hypothesis that we have a stationary time series.

We can try to superimpose such a normal distribution onto our empirical daily
return data and see what that looks like.We start by generating random numbers
that are normally distributed with the same mean and standard deviation as that
of our stock returns. The two plots can then be superimposed via the following R
code:
# Plot histogram and density
mu <- mean(returns, na.rm = TRUE)
sigma <- sd(returns, na.rm = TRUE)
x <- seq(-5 * sigma, 5 * sigma, length = nrow(returns))
hist(returns, breaks = 100,
main = "Histogram of returns for SPY",
cex.main = 0.8, prob=TRUE)
lines(x, dnorm(x, mu, sigma), col = "red", lwd = 2)

Thednorm()function creates a normal distribution given a range of x values, a
mean, and a standard deviation. Thelines()function creates a line plot on top of
the existing histogram plot.

Another way to visualize the difference between the empirical data at hand and
a theoretical normal distribution is via theqqnorm()andqqline()functions.
Using the same data as before
# Set plotting window
par(mfrow = c(1, 2))
# SPY data
qqnorm(as.numeric(returns),
main = "SPY empirical returns qqplot()",
cex.main = 0.8)
qqline(as.numeric(returns), lwd = 2)
grid()
# Normal random data
normal_data <- rnorm(nrow(returns), mean = mu, sd = sigma)
qqnorm(normal_data, main = "Normal returns", cex.main = 0.8)
qqline(normal_data, lwd = 2)
grid()
```
---
```R
The Shapiro test, for example, is run by providing the raw returns to the
shapiro.test()function as an argument. The resulting p-value
4
is a proba-bility of sorts that specifies the likelihood of the data originating from a normal
distribution.
answer <- shapiro.test(as.numeric(returns))
answer[[2]]
## [1] 5.118396e-34

# Correlation
sv <- as.xts(returns_matrix[, c(1, 6)])
head(sv)
## SPY.Close VXX.Close
## 2009-02-02 -0.003022794 -0.003160468
## 2009-02-03 0.013949240 -0.047941603
## 2009-02-04 -0.004908132 0.003716543
## 2009-02-05 0.014770965 -0.006134680
```
---
```R
# Find the outliers
outliers <- which(sv[, 2] > 1.0)
# If any outliers exist, remove them
if(length(outliers) > 0) {
sv <- sv[-outliers, ]
}
```
