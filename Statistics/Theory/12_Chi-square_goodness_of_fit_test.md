- [Chi-square goodness of fit test](#chi-square-goodness-of-fit-test)
  - [Conditions for the chi-square test](#conditions-for-the-chi-square-test)
  - [Hypotheses for the chi-square goodness of fit test](#hypotheses-for-the-chi-square-goodness-of-fit-test)
  - [Chi-square test statistic](#chi-square-test-statistic)


# Chi-square goodness of fit test

A one-sample chi-square test is called a chi-square goodness of fit test. It is used to determine whether sample data are consistent with a hypothesized distribution.

It is called a goodness of fit test because it measures how well the observed distribution of data fits with the distribution that is expected.

The one-sample proportion test is used to determine whether the proportion of success in a ceategorical variable (i.e, the observed distribution) is equal to some hypothesized proportion of success (i.e., the expected distribution of the population). It is an extreme case of the chi-square goodness of fit test.

In general, the idea of chi-square goodness of fit test expands on the idea of the one-sample proportion test. Instead of comparing the observed proportion of success with the hypothesized proportion of success, we compare the observed frequencies of the categories with the expected frequencies of the categories across a common categorical variable.

For a chi-square goodness of fit test, we create a table that compares the observed frequencies of the categories with the expected frequencies of the categories across a common categorical variable. It is called a contingency table. The cells/rows of the table are the categories of the variable and there is one column for the observed frequencies and one column for the expected frequencies. The expected frequencies are calculated based on the expected distribution of the categories in the general population.

An example of a chi-square goodness of fit test is testing whether the observed distribution of eye colors in a sample of 100 people is consistent with the expected distribution of eye colors in the general population. The table for this example might look like this:

| Eye color | Observed frequency | Expected frequency |
|:----------:|:------------------:|:------------------:|
| Brown      |          30        |         35         |
| Blue       |          30        |         25         |
| Green      |          25        |         20         |
| Hazel      |          15        |         20         |
| **Total**  |         **100**    |        **100**     |

**Note:** the chi-square goodness of fit test requires you to know the population distribution that you are testing the observed data against. If you do not have the population data, then you cannot use the chi-square goodness of fit test.

However, there are other statistical tests that you can use to test the goodness of fit of a categorical variable to a theoretical distribution, even if you do not have the population data. One such test is the Kolmogorov-Smirnov test.

## Conditions for the chi-square test

1. Independence:
    - Random sample/assignment
    - If sampling without replacement, the sample size should be less than 10% of the population size i.e, $n < 0.1N$.
    - Each case can contribute to only one cell in the table i.e, each observation must belong to only one category.
2. Sample size: Each category should have at least 5 expected cases/observations.


## Hypotheses for the chi-square goodness of fit test

The null hypothesis is that the observed distribution of the categorical variable is consistent with the expected distribution of the categorical variable.

The alternative hypothesis is not explicitly stated rather it is implicitly understood from the null hypothesis.

## Chi-square test statistic

When dealing with counts and investigating how far the observed counts are from the expected counts, we use a test statistic called the chi-square ($X^2$) statistic. 

The chi-square statistic for the chi-square goodness of fit test is calculated as:

$$ X^2 = \sum_{i=1}^{k} \frac{(O_i - E_i)^2}{E_i} $$

Where, 
- $k$ is the number of categories
- $O_i$ is the observed frequency of the $i^{th}$ category 
- $E_i$ is the expected frequency of the $i^{th}$ category

The degrees of freedom for the chi-square goodness of fit test is, $$df = k-1$$

The p-value for the chi-square statistic is calculated from the chi-square distribution. The chi-square distribution is a right-skewed distribution that is bounded below by 0. The shape of the chi-square distribution depends on the degrees of freedom. The higher the degrees of freedom, the more symmetric the distribution becomes. Similar to the F-statistic (in ANOVA test) and F-distribution, the chi-square statistic, $X^2$ and the chi-square distribution is always positive. The p-value is the area under the chi-square distribution to the right of the chi-square statistic.

