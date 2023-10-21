- [Chi-square test of independence](#chi-square-test-of-independence)
  - [Conditions for the chi-square test](#conditions-for-the-chi-square-test)
  - [Hypotheses for the chi-square test of independence](#hypotheses-for-the-chi-square-test-of-independence)
  - [Chi-square test statistic](#chi-square-test-statistic)


# Chi-square test of independence

A chi-square test of independence is used to determine whether there is a significant association between two different categorical variables. 

It is called a test of independence because it measures whether the two variables are independent of each other. Two categorical variables are considered to be statistically independent if the proportion of success in the response variable is the same across all categories of the explanatory variable.

A two-sample proportion test is used to determine whether the proportion of success in a ceategorical response variable is equal across two groups/categories of an explanatory variable. The chi-square test of independence expands on this idea and allows us to test whether there is a significant association between two categorical variables (across all the categories of the response variable and the explanatory variable).

One example of the chi-square test of independence would be a survey that investigates the relationship between gender and favorite genres of music. Gender is a binary categorical variable (Male or Female), while favorite music genres have several categories. The contingency table for the observed frequencies might look like this:

 ------      | Rock  | Pop  | Hip-Hop | Jazz  | *Total*
-------------|-------|------|---------|-------|------------
Male         | 30    | 20   | 25      | 25    | *100*
Female       | 15    | 35   | 20      | 30    | *100*
***Total***  | *45*  | *55* | *45*    | *55*  | *200*

**Note:** 
1. The chi-square test of independence can only be used to compare two categorical variables in a particular sample. It cannot be used to compare across multiple samples.
2. The chi-square test of independence can only be used to compare two categorical variables.

## Conditions for the chi-square test

1. Independence:
    - Random sample/assignment
    - If sampling without replacement, the sample size should be less than 10% of the population size i.e, $n < 0.1N$.
    - Each case can contribute to only one cell in the table.
2. Sample size: Each cell should have at least 5 expected cases/observations.

## Hypotheses for the chi-square test of independence

The null hypothesis is that there is no association between the two categorical variables. The alternative hypothesis is not explicitly stated rather implicitly understood from the null hypothesis.

## Chi-square test statistic

The chi-square ($X^2$) statistic is used to measure how far the observed counts are from the expected counts assuming the null hypothesis is true.

The expected counts are calculated based on the assumption that the null hypothesis is true. The calculation of the expected counts follows the same intuition as the calculation of $P(A \cap B)$ for two independent events $A$ and $B$ i.e, $P(A \cap B) = P(A)P(B)$. The expected count for a cell is calculated as:

$$ E_{ij} = \frac{R_i \times C_j}{n} $$

Where,
- $E_{ij}$ is the expected count for the $i^{th}$ row and $j^{th}$ column
- $R_i$ is the total count for the $i^{th}$ row
- $C_j$ is the total count for the $j^{th}$ column
- $n$ is the total number of observations i.e, the table total

For the example above, the expected counts would be calculated as:

 ------      | Rock  | Pop  | Hip-Hop | Jazz  | *Total*
-------------|-------|------|---------|-------|------------
Male         | 22.5 | 27.5| 22.5    | 27.5 | *100*
Female       | 22.5 | 27.5| 22.5    | 27.5 | *100*
***Total***  | *45*  | *55* | *45*    | *55*  | *200*


The chi-square statistic for the chi-square test of independence is calculated as:

$$ X^2 = \sum_{m=1}^{k} \frac{(O_{m} - E_{m})^2}{E_{m}} $$

Where,
- $k$ is the number of cells in the table i.e, $k = \text{number of rows} \times \text{number of columns}$.

The degrees of freedom for the chi-square test of independence is calculated as:

$$ df = (r-1)(c-1) $$

Where,
- $r$ is the number of rows in the table
- $c$ is the number of columns in the table

The p-value for the chi-square statistic is calculated from the chi-square distribution. The chi-square distribution is a right-skewed distribution that is bounded below by 0. The shape of the chi-square distribution depends on the degrees of freedom. The higher the degrees of freedom, the more symmetric the distribution becomes. Similar to the F-statistic (in ANOVA test) and F-distribution, the chi-square statistic, $X^2$ and the chi-square distribution is always positive. The p-value is the area under the chi-square distribution to the right of the chi-square statistic.

