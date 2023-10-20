- [ANOVA](#anova)
  - [Overview](#overview)
  - [Mathematicall breakdown of the ANOVA test](#mathematicall-breakdown-of-the-anova-test)
    - [Hypothesis setup](#hypothesis-setup)
    - [Variability partitioning](#variability-partitioning)
    - [Mathematical equations](#mathematical-equations)
    - [F-distribution](#f-distribution)
    - [Conditions for ANOVA](#conditions-for-anova)
  - [Post-hoc tests/Pairwise comparisons for determining which groups have statistically significant differences in their means](#post-hoc-testspairwise-comparisons-for-determining-which-groups-have-statistically-significant-differences-in-their-means)



# ANOVA

## Overview
ANOVA stands for Analysis of Variance. It is a statistical test used to compare the means of three or more groups. ANOVA is used to determine if there is a significant difference between the groups, and if so, to identify which groups are different.

ANOVA works by partitioning the total variance in the data into two parts: the variance between the groups and the variance within the groups. The variance between the groups is a measure of how much the group means differ from each other. The variance within the groups is a measure of how much the individual observations within each group differ from their group mean.

ANOVA then calculates a test statistic, called the F-statistic, which is a ratio of the variance between the groups to the variance within the groups. The F-statistic is used to test the null hypothesis that there is no difference between the group means.

If the F-statistic is statistically significant, then the null hypothesis is rejected and we conclude that there is a significant difference between the group means. However, ANOVA cannot tell us which groups are different. To determine which groups are different, we need to perform post-hoc tests.

## Mathematicall breakdown of the ANOVA test

### Hypothesis setup

The Null Hypothesis is, 
$$H_0 = \mu_1 = \mu_2 = \mu_3 = ....... = \mu_k$$

The Alternative Hypothesis is, 
$$H_A: \text{at least one of the group means is different from the other group means}$$

In ANOVA, the categorical variable is the *explanatory variable* and the numerical variable is the *response variable*. The groups are the different levels of the categorical variable.

### Variability partitioning

Total variability in the sample = Variability between the groups (variability attributed to the explanatory variable) + Variability within the groups (variability attributed to the response variable)

When writing the mathematical equations for ANOVA, the following notation is used:

------ | degrees of freedom | Sum of Squares | Mean Square
--- | --- | --- | ---
Group | df<sub>g</sub> | SS<sub>g</sub> | MS<sub>g</sub>
Error | df<sub>e</sub> | SS<sub>e</sub> | MS<sub>e</sub>
Total | df<sub>t</sub> | SS<sub>t</sub> | -

### Mathematical equations

**`->`** Total Sum of Squares (SS<sub>t</sub>) = Sum of Squares between the groups (SS<sub>g</sub>) + Sum of Squares within the groups (SS<sub>e</sub>)

$$ SS_t = \sum_{i=1}^{n} (y_i - \bar{y})^2 $$

Where, 
- $y_i$: value of the response variable for each observation
- $\bar{y}$: grand mean of the response variable

**`->`** Sum of Squares between the groups, $$SS_g = \sum_{j=1}^{k} n_j (\bar{y_j} - \bar{y})^2$$

Where,
- $n_j$: number of observations in the jth group
- $\bar{y_j}$: mean of the response variable for the jth group
- $\bar{y}$: grand mean of the response variable

**`->`** Sum of Squares within the groups, $$SS_e = SS_t - SS_g$$

**`->`** Degrees of freedom associated with ANOVA are,

$$df_t= n - 1$$

$$ df_g = k - 1$$

$$ df_e = df_t - df_g = n - k$$

Where,
- n: total number of observations
- k: number of groups

**`->`** Mean Square between the groups, $$MS_g = \frac{SS_g}{df_g}$$

**`->`** Mean Square within the groups, $$MS_e = \frac{SS_e}{df_e}$$

**`->`** F-statistic, $$F = \frac{MS_g}{MS_e}$$

### F-distribution

Test statistic for ANOVA is the F-statistic. The F-statistic follows an F-distribution. The F-statistic is given as, 

$$ F = \frac{\text{Variability between the groups}}{\text{Variability within the groups}} $$

**Some properties of the F-distribution:**
- The F-distribution is always right-skewed.
- Test statistic F is always positive.

The **p-value** is the probability of observing a test statistic as extreme as the one observed, assuming the null hypothesis is true. The p-value is calculated from the calculated F-statistic and the degrees of freedom associated with the F-distribution. This p-value is then compared to the significance level to determine if the null hypothesis should be rejected or not.

### Conditions for ANOVA

1. Independence: The observations are independent within and across the groups.
2. Normality: The response variable is approximately normally distributed within each group.
3. Equal variance: The variance of the response variable is roughly the same in each group.

## Post-hoc tests/Pairwise comparisons for determining which groups have statistically significant differences in their means

If the ANOVA test yields a statistically significant result so that $H_0$ is rejected then we need to figure out which pair of the groups have statistically significant differences in their means. This is done using pairwise comparisons.

All the groups are paired with each other in a combinatory fashion and t-tests are performed on each pair of groups adjusting the significance level.

If there are k groups, then there will be $\frac{k(k-1)}{2}$ pairwise comparisons. As the number of groups increases, the number of pairwise comparisons increases quadratically. As a result using the original significance level will increase the probability of making a Type I error (rejecting $H_0$ when it is true). For example, With a significance level of point-two, if we run one test, the chance of a false positive result is point-two. With five groups and ten tests, the probability of at least one false positive is around point-seven. With twenty groups, it's almost guaranteed that we'll get at least one false positive. This is why adjusting the significance level is necessary as the post-hoc t-tests are conducted.

A popular method for adjusting the significance level is the Bonferroni correction. The Bonferroni correction is given as, $$\alpha^* = \frac{\alpha}{\frac{k(k-1)}{2}}$$

The standard error for the difference between two means in a pairwise t-test is given as, $$SE = \sqrt{\frac{MS_e}{n_1} + \frac{MS_e}{n_2}}$$

And the associated degrees of freedom for a pairwise t-test is given as, $$df = n_1 + n_2 - 2$$
