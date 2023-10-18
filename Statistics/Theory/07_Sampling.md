- [Sampling](#sampling)
  - [Types of sampling on the basis of how the sample is selected](#types-of-sampling-on-the-basis-of-how-the-sample-is-selected)
    - [Probability sampling](#probability-sampling)
    - [Non-probability sampling](#non-probability-sampling)
  - [Types of sampling on the basis of the nature of the population being sampled](#types-of-sampling-on-the-basis-of-the-nature-of-the-population-being-sampled)
    - [Sampling from an infinite population](#sampling-from-an-infinite-population)
    - [Sampling from a finite population](#sampling-from-a-finite-population)
    - [Sampling from the whole population](#sampling-from-the-whole-population)
- [Sampling distribution](#sampling-distribution)
    - [How to create a sampling distribution?](#how-to-create-a-sampling-distribution)
    - [Properties of sampling distributions](#properties-of-sampling-distributions)
    - [Exact and approximate sampling distributions](#exact-and-approximate-sampling-distributions)
- [Bootsrapping](#bootsrapping)
- [Confidence interval](#confidence-interval)

# Sampling
Sampling is the process of selecting a subset of a population to study the characteristics of the whole population.

The main purpose of sampling is to make inference on the statistical characteristics of the population from the calculated characteristics of the sample. When we take a sample we are interested in answering 3 main questions.

1. What is the best estimate of the population mean i.e, what's the sample mean, $\bar x$ ? 
2. How confident are we about the estimate? Since we use a small sample we can't be 100% sure that the sample mean is equal to the population mean. So we need to measure the uncertainty in the sample mean. To do this we use a measure called the Standard Error of the sample mean, $SE ({\bar x})$. The larger the sample size, the smaller the SE becomes i.e, we are more confident about the estimate representing the true population mean.
3. What is the best estimate of the population standard deviation i.e, what's the sample standard deviation, $s$ ?


## Types of sampling on the basis of how the sample is selected

There are two main types of sampling: probability sampling and non-probability sampling.

### Probability sampling

**Probability sampling** is a type of sampling where each member of the population has a known and equal chance of being selected. This is the most common type of sampling and is used when it is important to obtain a representative sample of the population.

There are a number of different probability sampling methods, such as:

* **Simple random sampling:** This is the simplest type of probability sampling, where each member of the sample is selected independently and randomly from a population.
* **Stratified sampling:** This type of sampling divides the population into strata, or subgroups, and then selects a random sample from each stratum. This method is used to ensure that all subgroups of the population are represented in the sample.
* **Cluster sampling:** This type of sampling divides the population into clusters and then selects a random sample of clusters, followed by a sample of individuals within the selected clusters. This method is often used when it is difficult to identify and list all members of the population.


### Non-probability sampling

**Non-probability sampling** is a type of sampling where each member of the population does not have a known or equal chance of being selected. This type of sampling is often used when it is not important to obtain a representative sample of the population, or when it is difficult or costly to use probability sampling methods.

There are a number of different non-probability sampling methods, such as:

* **Convenience sampling:** This type of sampling selects members of the population who are easily accessible to the researcher. This is the most common type of non-probability sampling, but it can lead to biased results.
* **Judgment sampling:** This type of sampling selects members of the population who the researcher believes are representative of the population. This method can be effective if the researcher has good knowledge of the population, but it is subjective and can lead to biased results.
* **Quota sampling:** This type of sampling selects members of the population based on certain quotas, such as age, gender, or income. This method can be used to ensure that certain subgroups of the population are represented in the sample, but it can be difficult to find members of the population who meet all of the quotas.

Here are some examples of how sampling is used in the real world:

* A market researcher might use sampling to survey a group of consumers about their preferences for a new product.
* An economist might use sampling to collect data on the incomes and spending habits of a group of households.
* A political scientist might use sampling to poll a group of voters about their opinions on a candidate or issue.

By carefully selecting a representative sample, researchers can get insights into the population without having to study every member of the population.


## Types of sampling on the basis of the nature of the population being sampled

Sampling techniques can be categorized based on the nature of the population being sampled from as, infinite population, finite population, and the whole population.

`Explained with example:` [Sampling by zedstatistics](https://www.youtube.com/watch?v=0Jh77k0Rxsk)

### Sampling from an infinite population
In this scenario, the population is theoretically infinite, meaning it's so large that it cannot be feasibly enumerated or sampled in its entirety. For example, if we want to study the heights of all adult humans on Earth, the population is effectively infinite.

Simple random sampling, systematic sampling, and stratified sampling are common techniques for sampling from an infinite population.

The mean of the sample is our best estimate of the population mean and the standard deviation of the sample is our best estimate of the population standard deviation. To measure the uncertainty in our estimate of population mean we use the standard error of the sample mean, $SE({\bar x})$.

`Formula:`

Sample mean, 
$$\bar x = \frac{\sum_{i=1}^{n} x_i}{n}$$

Standard error of the sample mean, 
$$SE({\bar x}) = \frac{s}{\sqrt{n}}$$

Standard deviation of the sample, 
$$s = \sqrt{\frac{\sum_{i=1}^{n} (x_i - \bar x)^2}{n-1}}$$

Where, $n$ is the sample size.


### Sampling from a finite population

In this case, the population is finite, meaning it consists of a known and limited number of individuals or items. This is a rare case since you will most likely have access to the whole population. For example if we want to study the heights of all the NBA players in a particular season, the population is finite.

Sampling from a finite population is also termed as, sampling without replacement. This is because if we sampled with replacement, the population would be effectively infinite.

`Formula:`

Sample mean, 
$$ \bar x = \frac{\sum_{i=1}^{n} x_i}{n}$$

Standard error of the sample mean, 
$$SE({\bar x}) = \frac{s}{\sqrt{n}} \times \sqrt{\frac{N - n}{N - 1}}$$

Standard deviation of the sample,
$$s = \sqrt{\frac{\sum_{i=1}^{n} (x_i - \bar x)^2}{n-1}}$$

Where, $n$ is the sample size and $N$ is the population size.

### Sampling from the whole population
Sampling the whole population is a type of sampling where all members of the population are included in the sample. This is only possible when the population is small. Sampling the whole population is the most accurate way to estimate the population parameters, such as the mean and variance. For example, a company might conduct a census of all of its employees to collect data on their demographics and salaries. The population of employees is small, so the company can sample the whole population.

`Formula:`

Population mean,
$$\mu = \frac{\sum_{i=1}^{N} x_i}{N}$$

Population standard deviation,
$$\sigma = \sqrt{\frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N}}$$

Where, $N$ is the population size.

And the standard error of the population mean,
$$SE(\mu) = 0$$

This is because the population mean is the true mean of the population and there is no uncertainty in the estimate.


# Sampling distribution

**The distribution of a sample statistic is called a sampling distribution.**

A sampling distribution is a probability distribution of a statistic obtained from a larger number of samples drawn from a specific population. It describes a range of possible outcomes for a statistic, such as the mean or mode of some variable, of a population.

### How to create a sampling distribution?
To create a sampling distribution, we would need to repeatedly draw random samples from a population and calculate a statistic for each sample. The sampling distribution would then be the distribution of the values of the statistic across all of the samples.

Sampling distributions are important because they allow us to make inferences about populations based on samples. For example, we can use the sampling distribution of the mean to estimate the population mean with a certain degree of confidence.

Here is an example of a sampling distribution:

Suppose we have a population of 1000 students with a mean height of 67 inches. We draw 100 random samples of 10 students each and calculate the mean height of each sample. The sampling distribution of the mean would then be the distribution of the 100 sample means.

Sampling distributions are used in a variety of statistical methods, including hypothesis testing, confidence intervals, and regression analysis.

### Properties of sampling distributions
Here are some of the key properties of sampling distributions:

1. The shape of a sampling distribution depends on the shape of the population distribution, the statistic being considered, and the sample size.
2. The central limit theorem states that the sampling distribution of the mean will be approximately normally distributed, regardless of the shape of the population distribution, as long as the sample size is sufficiently large.

These two statements may seem contradictory at first glance, but they are actually complementary. The first statement is a general statement about the shape of sampling distributions, while the second statement is a specific statement about the sampling distribution of the mean.

The first statement is true for all sampling distributions, regardless of the statistic being considered. The shape of a sampling distribution will always depend on the shape of the population distribution and the sample size.

However, the central limit theorem tells us that the sampling distribution of the mean will be approximately normally distributed, regardless of the shape of the population distribution, as long as the sample size is sufficiently large. This is because the central limit theorem is a specific statement about the sampling distribution of the mean, and it takes into account the fact that the sample size is sufficiently large.

In other words, the first statement is a general rule, while the second statement is a specific exception to that rule. The central limit theorem is a powerful tool that allows us to make inferences about populations based on samples, even when the population distribution is not normally distributed.

3. The mean of a sampling distribution is our best estimate to the parameter of the population that the statistic is estimating.
4. The standard deviation of a sampling distribution is called the standard error of the statistic. The standard error decreases as the sample size increases. The standard error is a measure of the uncertainty in the estimate of the parameter of the population that the statistic is estimating. It is related to the standard deviation of the population distribution and the sample size by the following formula:
  $$Population\ Standard\ Deviation = \frac{Standard\ Error}{\sqrt{Sample\ Size}}$$ (Best estimate)

### Exact and approximate sampling distributions
An exact sampling distribution is a probability distribution of a statistic obtained from all possible samples of a fixed size drawn from a population. An approximate sampling distribution is a probability distribution of a statistic obtained from a sample of a fixed size drawn from a population. 

The original concept of sampling distributions refers to the exact sampling distribution.

To calculate the exact sampling distribution of a statistic, we would need to calculate the statistic for all possible samples of a fixed size drawn from the population. However, in practice, it is often difficult or impossible to compute the exact sampling distribution, especially for large populations. Therefore, we often use approximate sampling distributions to make inferences about populations based on samples.

To calculate an approximate sampling distribution of a statistic, we would take a sample from the population and then calculate the statistic for a large number of subsamples of the original sample. The distribution of the statistic for the subsamples would be the approximate sampling distribution of the statistic.

What enables us to use approximate sampling distribution instead of an exact sampling distribution is the central limit theorem. The central limit theorem states that the sampling distribution of the mean will be approximately normally distributed, regardless of the shape of the population distribution, as long as the sample size is sufficiently large. This means that we can use the normal distribution to calculate confidence intervals for the mean, even if the population distribution is not normally distributed.

Approximate sampling distributions are often used to make inferences about population parameters because they are easier to calculate than exact sampling distributions. However, it is important to note that approximate sampling distributions are only approximations, and the accuracy of the approximation depends on the sample size and the shape of the population distribution.


# Bootsrapping

Bootstrapping is a statistical method that can be used to estimate the sampling distribution of almost any statistic. It is a non-parametric method, which means that it does not make any assumptions about the shape of the population distribution.

`One line summary:` sampling with replacement.

**To create a bootstrap distribution, we follow these steps:**

1. Take a random sample from the population.
2. Create a bootstrap sample by resampling with replacement from the original sample.
3. Calculate the statistic of interest for the bootstrap sample.
4. Repeat steps 2 and 3 a large number of times (e.g., 1000 times).
5. The **bootstrap distribution** is the distribution of the statistic of interest across all of the bootstrap samples.

Bootstrapping is also known as resampling. For bootstrapping each row in the dataset should have an equal probability of being selected. 

Bootstrapping is, in some sense, the opposite of sampling from a population. Sampling treats your dataset as the population, and you generate a random subset. Bootstrapping treats your dataset as a sample and uses it to build up a theoretical population. 

The key to deciding whether to sample with replacement (bootstrapping) or without replacement (simple sampling) is whether or not your dataset is best thought of as being the whole population or not.

The bootstrap distribution can be used to estimate a variety of things, such as: The standard error of a statistic, Confidence intervals for a statistic, P-values for hypothesis tests, Power curves for statistical tests etc.

**Bootstrapping differs from the traditional approach to sampling distributions in the following ways:**

- Bootstrapping does not require us to know the population distribution.
- Bootstrapping can be used to estimate the sampling distribution of almost any statistic, including complex statistics such as the median or the correlation coefficient.


**Caution:** If the sample is not closely representative of the population, then the mean of the bootstrap distribution will not be representative of the population mean. This is less of a problem for standard errors.


# Confidence interval

A confidence interval is a range of values that we are confident contains the true population parameter. It is calculated using a sample statistic and a margin of error.

The confidence interval for a sampling distribution is given by,
$$ CI = \bar x \pm z \times SE(\bar x)$$

The confidence interval for a bootstrap distribution is given by,
$$ CI = \bar x \pm t \times SE(\bar x)$$

Where, 

- $\bar x$ is the sampling/bootstrap distribution mean (our best estimate of population statistic)
- $z$ is the z-score and depends on the confidence level
- $t$ is the t-score and depends on the confidence level and the degrees of freedom
- $SE(\bar x)$ is the standard error of the sampling/bootstrap distribution

The standard error $SE(\bar x)$ is given as, $SE(\bar x) = \frac{s}{\sqrt{n}}$ where $s$ is the standard deviation of the sampling/bootstrap distribution and $n$ is the sample size.