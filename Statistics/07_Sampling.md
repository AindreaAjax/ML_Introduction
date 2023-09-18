
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
