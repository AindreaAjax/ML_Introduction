

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

## Hypothesis testing for nearly normal point estimates of a *single variable*

The main question we ask in hypothesis testing is that, if the Null Hypothesis $H_0$ is true, how extreme is the sample data? If the sample data is not extreme enough, then we accept the Null Hypothesis. If the sample data is extreme, then we reject the Null Hypothesis.

- **z-score:** It is a measure of how extreme the sample data is compared to the Null Hypothesis. It is given as, 
$$ z = \frac{\text{Sample statistic} - \text{Null Hypothesis value}}{\text{Standard error of the sample statistic}} $$ 

For example if we were testing the mean of a population, then the z-score is given as,
$$ z = \frac{\bar{x} - \mu_0}{\frac{\sigma}{\sqrt{n}}} $$

where $\bar{x}$ is the sample mean, $\mu_0$ is the Null Hypothesis value of the population mean, $\sigma$ is the population standard deviation and $n$ is the sample size.

The corresponding significance level for a z-score can be found from the z-table. The z-table gives the area under the standard normal curve to the left of a given z-score. 

- **t-score:** The t-score is used when we don't know the population standard deviation $\sigma$ (Which  is almost always). The t-score is given as,

$$ t = \frac{\text{Point estimate} - \text{Null Hypothesis value}}{\text{Standard error of the point estimate}} $$

For example if we were testing for mean of a population, then the t-score is given as,

$$ t = \frac{\bar{x} - \mu_0}{\frac{s}{\sqrt{n}}} $$

where $s$ is the sample standard deviation.

In this case we use the t-table to find the significance level corresponding to the t-score. The t-table gives the area under the t-distribution curve to the left of a given t-score. This is very similar to the z-table.

- **p-value:** A similar and complementary measure of z-score/t-score is the **p-value**. The p-value is the probability of getting a sample as extreme as ours, given the Null Hypothesis is true.

We reject the Null Hypothesis if the p-value is less than the significance level or if the z-score/t-score is greater than the z-score/t-score corresponding to the significance level.


## Hypothesis testing for comparing sample statistics across *two groups* of a variable

For comparing sample statistics across two groups of a variable, we use the **two-sample t-test**. The two-sample t-test is used to test whether the means of two populations are equal. 

The Null Hypothesis $H_0$ is that the means of the two populations are equal i.e, $H_0: \mu_1 = \mu_2$.

The Alternative Hypothesis $H_A$ is that the means of the two populations are not equal i.e, $H_A: \mu_1 \neq \mu_2$.

For comparing two different populations i.e, across two groups of a variable, we use the difference of the estimators to test the Null Hypothesis. 

$$ t = \frac{\text{Difference in sample statistics} - \text{Difference in population parameters}}{\text{Standard error of the difference in sample statistics}} $$

For example, if we were testing the difference in means of two groups of a variable, then the t-score is given as,

$$ t = \frac{(\bar{x}_1 - \bar{x}_2) - (\mu_1 - \mu_2)}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}} $$

Where: 
- $\bar{x}_1$ and $\bar{x}_2$ are the sample means of the two groups
- $\mu_1$ and $\mu_2$ are the population means of the two groups 
- $s_1$ and $s_2$ are the sample standard deviations of the two groups and $n_1$ and $n_2$ are the sample sizes of the two groups.

Assuming the Null Hypothesis is true, $H_0: \mu_1 - \mu_2 = 0$, we can reduce the above equation to,

$$ t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}} $$

The corresponding significance level for a t-score can be found from the t-table. The t-table gives the area under the t-distribution curve to the left of a given t-score.

The confidence interval for the difference in means of two groups of a variable is given as,

$$ CI = (\bar{x}_1 - \bar{x}_2) \pm t^* \sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}} $$

Where $t^*$ is the t-score corresponding to the desired confidence level. The t-score depends on the degrees of freedom. The degrees of freedom is given as, $df = min(n_1 - 1, n_2 - 1)$. Using the calculated degrees of freedom, we can find the t-score from the t-table.

