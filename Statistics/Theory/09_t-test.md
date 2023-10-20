- [Hypothesis testing for comparing the mean across *two groups* of a variable, **t-test**](#hypothesis-testing-for-comparing-the-mean-across-two-groups-of-a-variable-t-test)
  - [Why do we use t-test?](#why-do-we-use-t-test)
  - [Independent t-test](#independent-t-test)
  - [Paired t-test](#paired-t-test)
    - [**Some examples of paired t-tests are,**](#some-examples-of-paired-t-tests-are)


# Hypothesis testing for comparing the mean across *two groups* of a variable, **t-test**

## Why do we use t-test?

We could've also used the z-test for comparing the mean across two groups of a variable. So why don't we? 

Well we do in some cases and in most cases we can't even if we want to.

**The z-test** can be used to test the null hypothesis that a population parameter is equal to a certain value, *for any population parameter that is normally distributed*. This includes parameters such as the *population mean, the population variance, and the population proportion*.

The *z-score* is calculated as, 

$$ z = \frac{\text{Sample statistic} - \text{Null Hypothesis value}}{\text{Standard error of the sample statistic i.e, population standard deviation of the sample statistic}} $$ 

$$i.e, z = \frac{\text{Sample statistic} - \text{Null Hypothesis value}}{\sigma/\sqrt{n}}$$

But the problem is that we often don't know the population standard deviation. As a result direct calculation of the standard error i.e, the population standard deviation (of the sample statistic) is not possible. 

In such cases if we want to use the *z-test* what we can do is we can create a **bootstrap distribution** of the sample statistic. Then we can use the standard deviation of the bootstrap distribution as the standard error of the sample statistic i.e, the bootstrap distribution is used as an estimate of the population distribution.

But creating a bootstrap distribution is not always possible. As a result we have to use the sample standard deviation as our best estimate of the population standard deviation. But this introduces a new order of uncertainty in our calculations (since we use the sample to calculate the sample statistic in the numerator instead of using the population parameter). If this is the case, then we can't use the z-test. Instead we have to use the **t-test**.


**`Note:`** t-tests can only be used to compare the means of two groups of a variable and no other sample statistics.

## Independent t-test
In an independent t-test, we are comparing the means of two independent groups of a variable. Here the term independent means that the two groups are not directly related to each other i.e, there are no inherent relationships between the two groups.

For comparing the mean across two independent groups of a variable, we use the **two-sample t-test**. 

The Null Hypothesis $H_0$ is that the means of the two populations are equal i.e, $H_0: \mu_1 = \mu_2$.

The Alternative Hypothesis $H_A$ is that the means of the two populations are not equal i.e, $H_A: \mu_1 \neq \mu_2$.

For comparing two different populations i.e, across two groups of a variable, we use the difference of the estimators to test the Null Hypothesis. 

The t-score is given as,

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

Where $t^*$ is the t-score corresponding to the desired confidence level. The t-distribution depends on the degrees of freedom. The degrees of freedom is given as, $df = min(n_1 - 1, n_2 - 1)$. Using the calculated degrees of freedom, we can find the **p-value** from the t-table. This p-value is then used to decide whether to reject the Null Hypothesis or not.

## Paired t-test
A paired t-test is a statistical test used *to compare the means* of **two related groups**. 

It is a type of paired-samples t-test, which means that each subject or entity is usually measured twice, resulting in pairs of observations. The two groups are usually related inherently or by design.

Paired t-tests are often used in before-and-after studies or in studies where two different treatments are applied to the same group of subjects.

The Null Hypothesis $H_0$ is that the means of the two related groups are equal i.e, $H_0: \mu_1 = \mu_2$.

The Alternative Hypothesis $H_A$ is that the means of the two related groups are not equal i.e, $H_A: \mu_1 \neq \mu_2$.

For comparing two related groups, we use the difference of the observations to calculate the sample statistic and then use this statistic to test the Null Hypothesis.

The t-score is given as,

$$ t = \frac{\bar{x}_d - \bar{\mu}_d}{\frac{s_d}{\sqrt{n}}} $$

Assuming the Null Hypothesis is true the above equation can be reduced to,

$$ t = \frac{\bar{x}_d}{\frac{s_d}{\sqrt{n}}} $$

Where:
- $\bar{x}_d = \overline{(x_1 - x_2)}$
- $s_d$ is the sample standard deviation of the difference between the two related groups and $n$ is the sample size of the two related groups.

Degrees of freedom is given as, $df = n - 1$ where $n$ is the sample size of the two related groups.

The t-score and the degrees of freedom are used to find the p-value from the t-table. The t-table gives the area under the t-distribution curve to the left of a given t-score. This p-value is then used to decide whether to reject the Null Hypothesis or not.

### **Some examples of paired t-tests are,**

- To test the effectiveness of a new elementary school study technique, *pre and post-tests* are given *to the same random sample of students*.
- Scientists wish to understand whether older children like sugar less than younger children, sibiling pairs were surveyed on their sugar preferences.
- A researcher wants to test the hypothesis that a new drug is more effective than a standard treatment for a certain disease. The researcher randomly assigns patients to either the new drug or the standard treatment. After a certain period of time, the researcher measures the improvement in each patient's condition. The researcher uses a paired t-test to compare the improvement scores of the two groups.The researcher used a paired t-test instead of other tests because the data was collected from the same group of subjects before and after receiving the new drug.

