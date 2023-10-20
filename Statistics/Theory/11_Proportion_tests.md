

# Proportion tests

The idea of proportion is used exclusively for categorical variables.

Proportion tests are statistical tests used to compare two or more proportions. There are two main types of proportion tests:

- One-sample proportion test: This test is used to compare the proportion of a sample to a known population proportion, or to test the null hypothesis that the population proportion is equal to a certain value.
- Two-sample proportion test: This test is used to compare the proportions of two independent samples.

Both of these tests are based on the normal distribution.

## Central limit theorem for proportions

The distribution of sample proportions is nearly normal, centered at the population proportion ($p$) and with a standard error proportional to the sample size.

$$\hat{p} \sim N\left(\text{mean of sample proportion} = p, \text{SE} = \sqrt{\frac{p(1-p)}{n}}\right)$$

Where, 
- $\hat{p}$ is the sample proportion
- $p$ is the population proportion
- $n$ is the sample size

**Note:** Mean of a sampling distribution of sample proportion ($\hat{p}$) is equal to the population proportion ($p$).

## Conditions for proportion tests

1. Random sample
2. Independence:
   - With replacement: independence is ensured
   - Without replacement: sample size must be less than 10% of the population size i.e, $n < 0.1N$.
3. Sample size: $n > 30$ or $np > 10$ and $n(1-p) > 10$ where, $n$ is the sample size and $p$ is the population proportion for success (Null hypothesis value).

## One-sample proportion test

The one-sample proportion test is used to compare the proportion of a sample to a known population proportion, or to test the null hypothesis that the population proportion is equal to a certain value.

The null hypothesis for the one-sample proportion test is written as, $H_0: p = p_0$ 

And the alternative hypothesis is written as, $H_A: p \neq p_0$


**Common denotions:**
- $p$ is the population proportion
- $\hat{p}$ is the sample proportion (sample statistic)
- $p_0$ is the hypothesized population proportion (null hypothesis value)

The **z-score** for the one-sample proportion test:

$$ z = \frac{\hat{p} - mean(\hat{p})}{SE(\hat{p})} = \frac{\hat{p} - p}{SE(\hat{p})}$$

Assuming the null hypothesis is true, $H_0: p = p_0$ the above equation can be simplified as:

$$ z = \frac{\hat{p} - p_0}{SE(\hat{p})}$$

And, the standard error of the sample statistic $\hat{p}$ is calculated as:

$$ SE(\hat{p}) = \sqrt{\frac{p_0(1-p_0)}{n}}$$

Thus, the **z-score** for the one-sample proportion test is calculated as:

$$ z = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}}$$


