## 1. Updating Formulas for Sample Mean and Variance

### (a) Updating formula for the sample mean

\[
\mu_{n+1} = \frac{n \mu_n + x_{n+1}}{n+1}
\]

**Proof:**
\[
\mu_{n+1} = \frac{1}{n+1} \sum_{i=1}^{n+1} x_i = \frac{1}{n+1} \left( \sum_{i=1}^{n} x_i + x_{n+1} \right)
\]

Using \( \mu_n = \frac{1}{n} \sum_{i=1}^{n} x_i \):

\[
\mu_{n+1} = \frac{n \mu_n + x_{n+1}}{n+1}
\]


### (b) Updating formula for the sum of squared deviations

\[
\sum_{i=1}^{n+1} (x_i - \mu_{n+1})^2 = \sum_{i=1}^{n} (x_i - \mu_n)^2 + \frac{n}{n+1} (x_{n+1} - \mu_n)^2
\]

**Proof:**
Expanding the squared deviations:

\[
(x_i - \mu_{n+1})^2 = (x_i - \mu_n + \mu_n - \mu_{n+1})^2
\]

Expanding and summing:

\[
\sum_{i=1}^{n} (x_i - \mu_{n+1})^2 = \sum_{i=1}^{n} (x_i - \mu_n)^2 + 2(\mu_n - \mu_{n+1}) \sum_{i=1}^{n} (x_i - \mu_n) + n (\mu_n - \mu_{n+1})^2
\]

Since \( \sum_{i=1}^{n} (x_i - \mu_n) = 0 \), the middle term vanishes:

\[
\sum_{i=1}^{n+1} (x_i - \mu_{n+1})^2 = \sum_{i=1}^{n} (x_i - \mu_n)^2 + \frac{n}{n+1} (x_{n+1} - \mu_n)^2
\]


### (c) Updating formula for the sample variance
\[
(n+1) s_{n+1}^2 = n s_n^2 + \frac{1}{n+1} (x_{n+1} - \mu_n)^2
\]

**Proof:**
Sample variance:

\[
s_n^2 = \frac{1}{n} \sum_{i=1}^{n} (x_i - \mu_n)^2
\]

Using the result from (b):

\[
\sum_{i=1}^{n+1} (x_i - \mu_{n+1})^2 = \sum_{i=1}^{n} (x_i - \mu_n)^2 + \frac{n}{n+1} (x_{n+1} - \mu_n)^2
\]

Dividing by \( n+1 \):

\[
s_{n+1}^2 = \frac{1}{n+1} \left( \sum_{i=1}^{n} (x_i - \mu_n)^2 + \frac{n}{n+1} (x_{n+1} - \mu_n)^2 \right)
\]

Since \( s_n^2 = \frac{1}{n} \sum_{i=1}^{n} (x_i - \mu_n)^2 \), we rewrite:

\[
s_{n+1}^2 = \frac{n}{(n+1)n} s_n^2 + \frac{1}{(n+1)^2} (x_{n+1} - \mu_n)^2
\]

Multiplying both sides by \( n+1 \):

\[
(n+1) s_{n+1}^2 = n s_n^2 + \frac{1}{n+1} (x_{n+1} - \mu_n)^2
\]


## 2. You can find a dataset recording a variety of properties of secondary school students in Portugal [here](http://archive.ics.uci.edu/ml/datasets/STUDENT+ALCOHOL+CONSUMPTION). This dataset was collected by P. Cortez and A. Silva, and is hosted by the UC Irvine Machine Learning Repository. There are two datasets; one for students in a math course, and another for students in a Portuguese language course.
### (a) Use plots of conditional histograms to investigate whether math students drink more alcohol during the week than Portuguese language students.
![Stacked Histogram](homework2/conditional-histogram-stacked.png)
### (b) Use plots of conditional histograms to investigate whether students from small families drink more alcohol at the weekend than those from large families.
### (c) Each of the variables school, sex, famsize and romantic has two possible values. This means that if we characterize students by the values of these variables, there are sixteen possible types of student. Use box plots to investigate which of these types drinks more alcohol in total.
## 3. You can find a dataset recording some properties of Taiwanese credit card holders [here](http://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients). This dataset was collected by I-Cheng Yeh, and is hosted by the UC Irvine Machine Learning Repository. There is a variable indicating whether a holder defaulted or not, and a variety of other variables.
### (a) Use plots of conditional histograms to investigate whether people who default have more debt (use the variable X1 for debt) than those who don’t default.
### (b) Use box plots to investigate whether gender, education or marital status has any effect on the amount of debt (again, use X1 for debt).
