

# Assumptions in hypothesis testing

Some of the fundamental assumptions in hypothesis testing are:

1. **Randomness:** Whether it uses one or multiple samples, every hypothesis test assumes that each sample is randomly sourced from its population. If we don't have a random sample, then it won't be representative of the population. To check this assumption, we need to know where our data came from. There are no statistical or coding tests we can perform to check this. If in doubt, ask the people involved in data collection, or a domain expert that understands the population being sampled. 
2. **Independence of observations:** Tests also assume that each observation is independent. There are some special cases like paired t-tests where dependencies between two samples are allowed, but these change the calculations, so we need to understand where such dependencies occur. As we saw with the paired t-test, not accounting for dependencies results in an increased chance of false negative and false positive errors. Not accounting for dependencies is a difficult problem to diagnose during analysis. Ideally, it needs to be discussed before data collection. 
3. **Large sample size:** Hypothesis tests also assume that our sample is large enough that the Central Limit Theorem applies, and the sample distribution can be assumed to be normally distributed. Smaller samples incur greater uncertainty, which may mean that the Central Limit Theorem does not apply and the sampling distribution might not be normally distributed. The increased uncertainty of a small sample means we get wider confidence intervals on the parameter we are trying to estimate. If the Central Limit Theorem does not apply, the calculations on the sample, and any conclusions drawn from them, could be nonsense, which increases the chance of false negative and false positive errors. How big our sample needs to be to be "big enough" depends on the test. 

***Sanity check:*** To check if the assumptions for hypothesis testing holds we can perform a sanity check. We calculate a bootstrap distribution and visualize it with a histogram. If we don't see a bell-shaped normal curve, then one of the assumptions hasn't been met. In that case, we should revisit the data collection process, and see if any of the three assumptions of randomness, independence, and sample size do not hold. 

# Nonparametric tests

Nonparametric tests are statistical tests that do not make assumptions about the distribution of the population from which the sample is drawn. This is in contrast to parametric tests, which do make assumptions about the distribution of the population.

Nonparametric tests are often used when the data is not normally distributed, or when the sample size is too small to make reliable assumptions about the distribution of the population.

**Here are some examples of nonparametric tests:**

- Mann-Whitney U test: This test is used to compare two independent groups on a continuous variable. This can be thought of as the nonparametric version of the independent t-test.
- Wilcoxon signed-rank test: This test is used to compare two paired groups on a continuous variable. This can be thought of as the nonparametric version of the paired t-test.
- Kruskal-Wallis test: This test is used to compare three or more independent groups on a continuous variable. This can be thought of as the nonparametric version of the one-way ANOVA.
- Spearman's rank correlation coefficient: This test is used to measure the strength and direction of the linear relationship between two ordinal variables. This can be thought of as the nonparametric version of the Pearson correlation coefficient.


**Here are some examples of how nonparametric tests can be used in exploratory data analysis:**

- A researcher might use the Wilcoxon signed-rank test to compare the pre-test and post-test scores of a group of participants in a study.
- A researcher might use the Mann-Whitney U test to compare the scores of two groups of participants on a cognitive test.
- A researcher might use the Kruskal-Wallis test to compare the scores of three or more groups of participants on a personality test.
- A researcher might use Spearman's rank correlation coefficient to measure the relationship between the scores of two participants on a test of anxiety and a test of depression.

