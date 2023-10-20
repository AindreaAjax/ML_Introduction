- [Hypothesis testing](#hypothesis-testing)
  - [One-tailed and two-tailed tests](#one-tailed-and-two-tailed-tests)
  - [Choosing the correct statistical test](#choosing-the-correct-statistical-test)
  - [Hypothesis testing for nearly normal point estimates of a *single variable*, **z-test**](#hypothesis-testing-for-nearly-normal-point-estimates-of-a-single-variable-z-test)
    - [Conditions for z-test](#conditions-for-z-test)


# Hypothesis testing
Hypothesis testing is a statistical method that is used in making statistical decisions using experimental data. Hypothesis testing is used to evaluate the plausibility of a hypothesis by using sample data. 

For a hypothesis test we have two competing hypotheses, the **Null Hypothesis** $H_0$ and the **Alternative Hypothesis** $H_1$. These two can be explained by the classical example of a court case. The Null Hypothesis $H_0$ is the statement that the defendant is innocent. The Alternative Hypothesis $H_1$ is the statement that the defendant is guilty. The alternative hypothesis $H_1$ is the statement we are seeking evidence for. The Null Hypothesis $H_0$ is the reverse of the Alternative Hypothesis.


A general statement for $H_0$ and $H_1$ is as follows:

-> $H_0$ : No effect or no difference

-> $H_1$ : Effect or difference

True situation | Sample result - Not significant | Sample result - Significant
--- | --- | ---
No effect - $H_0$ is True | True Negative, Correctly failed to reject the Null Hypothesis (1-$\alpha$) | False Positive, Type I error, Incorrectly rejected the Null Hypothesis ($\alpha$)
Effect - $H_1$ is True | False Negative, Type II error, Failed to reject the Null Hypothesis when it should've been rejected ($\beta$) | True Positive, Power, Correctly rejected the Null Hypothesis (1-$\beta$)

**Significance level:** $\alpha$ is also called the **significance level** of the test. The significance level is the probability of rejecting the Null Hypothesis when it is true. We can choose the significance level based on how strict we want to be in rejecting the Null Hypothesis.

**Convention for selecting the alternative hypothesis:** The convention is to select the alternative hypothesis $H_1$ as the statement that we want to find evidence for. 

If we had set the Null Hypothesis $H_0$ as the statement that we want to find evidence for, then just failing to reject the Null Hypothesis at a certain significance level would not be evidence enough to support our hypothesis. That's why we set the Alternative Hypothesis $H_1$ as the statement that we want to find evidence for. If we find enough evidence to reject the Null Hypothesis at a certain significance level (say 5%), then it is far more convincing to reject the Null Hypothesis in favor of the Alternative Hypothesis. 

**Caution:** We can never accept the Null Hypothesis. We can only reject the Null Hypothesis or fail to reject the Null Hypothesis.

## One-tailed and two-tailed tests

The **one-tailed test** is used when we are interested in only one direction of the Alternative Hypothesis. For example, if we are interested in only the positive direction of the Alternative Hypothesis, then we use the one-tailed test. A common pattern is that the Alternative Hypothesis contains the phrase "greater than" or "less than".

The **two-tailed test** is used when we are interested in both directions of the Alternative Hypothesis. For example, if we are interested in both the positive and negative directions of the Alternative Hypothesis, then we use the two-tailed test. A common pattern is that the Alternative Hypothesis contains the phrase "not equal to".

For a two-tailed test, the significance level is split into two equal parts. For example, if the significance level is 5%, then the significance level for each tail is 2.5%. 

## Choosing the correct statistical test
It is important to choose the correct statistical test for your data and your research question. Using the wrong statistical test can lead to inaccurate results.

Here are some examples of statistical tests that can be used to compare different the mean:
    
    Mean: t-test, ANOVA, z-test, Welch's t-test
    Proportion: Chi-squared test, z-test, Fisher's exact test
    Standard deviation: F-test, Levene's test, Bartlett's test
    Median: Wilcoxon rank-sum test, Mann-Whitney U test
    Mode: Chi-squared test
    Variance: F-test, Bartlett's test, Levene's test, z-test
    

## Hypothesis testing for nearly normal point estimates of a *single variable*, **z-test**

The main question we ask in hypothesis testing is that, if the Null Hypothesis $H_0$ is true, how extreme is the sample data? If the sample data is not extreme enough, then we accept the Null Hypothesis. If the sample data is extreme, then we reject the Null Hypothesis.

- **z-score:** It is a measure of how extreme the sample data is compared to the Null Hypothesis. It is given as, 
$$ z = \frac{\text{Sample statistic} - \text{Null Hypothesis value}}{\text{Standard error of the sample statistic}} $$ 

For example if we were testing the mean of a population, then the z-score is given as,
$$ z = \frac{\bar{x} - \mu_0}{\frac{\sigma}{\sqrt{n}}} $$

where $\bar{x}$ is the sample mean, $\mu_0$ is the Null Hypothesis value of the population mean, $\sigma$ is the population standard deviation and $n$ is the sample size.

The corresponding significance level for a z-score can be found from the z-table. The z-table gives the area under the standard normal curve to the left of a given z-score. 

- **p-value:** A similar and complementary measure of z-score is the **p-value**. The p-value is the probability of getting a sample as extreme as ours, given the Null Hypothesis is true.

We reject the Null Hypothesis if the p-value is less than the significance level or if the z-score is greater than the z-score corresponding to the significance level.


### Conditions for z-test

**The z-test** can be used to test the null hypothesis that a population parameter is equal to a certain value, *for any population parameter that is normally distributed*. This includes parameters such as the *population mean, the population variance, and the population proportion*.

The *z-score* is calculated as,

$$ z = \frac{\text{Sample statistic} - \text{Null Hypothesis value}}{\text{Standard error of the sample statistic i.e, population standard deviation of the sample statistic}} $$ 

It should be noted that we often don't know the population standard deviation. As a result direct calculation of the standard error i.e, the population standard deviation (of the sample statistic) is not possible. 

In such cases we usually create a **bootstrap distribution** of the sample statistic and use the standard deviation of the bootstrap distribution as the standard error of the sample statistic i.e, the bootstrap distribution is used as an estimate of the population distribution.

But creating a bootstrap distribution is not always possible. As a result we have to use the sample standard deviation as an estimate of the population standard deviation. But this introduces a new order of uncertainty in our calculations (since we use the sample to calculate the sample statistic in the numerator instead of using the population parameter). If this is the case, then we can't use the z-test. Instead we have to use the **t-test**.
