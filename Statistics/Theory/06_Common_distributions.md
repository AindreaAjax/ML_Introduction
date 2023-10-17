- [Expected value of a distribution](#expected-value-of-a-distribution)
- [Common discrete probability distributions](#common-discrete-probability-distributions)
  - [Binomial distribution](#binomial-distribution)
  - [Poisson distribution](#poisson-distribution)
  - [Hypergeometric distribution](#hypergeometric-distribution)
- [Common continuous probability distributions](#common-continuous-probability-distributions)
  - [Exponential distribution](#exponential-distribution)
  - [Uniform distribution](#uniform-distribution)
  - [Normal distribution](#normal-distribution)


# Expected value of a distribution

The expected value of a distribution is the average of the values of the distribution, weighted by their probabilities. It is also known as the mean or average of the distribution.

The expected value (or mean) of a probability distribution is often denoted by the symbol $E(X)$ or $μ$ (mu) for a random variable $X$. 

The formula for calculating the expected value of a discrete random variable is:

$$E(X) = \sum_{x} x \cdot P(X = x)$$

And for a continuous random variable, it's calculated as an integral:

$$E(X) = \int_{-\infty}^{\infty} x \cdot f(x) \, dx$$

Where:
- $E(X)$ is the expected value of the random variable $X$.
- $x$ represents the possible values of the random variable.
- $P(X = x)$ is the probability mass function (for discrete) or $f(x)$ is the probability density function (for continuous) at $x$.



# Common discrete probability distributions

## Binomial distribution

`Prerequisites:`
1. Bernoulli trials (each trial is independent and has only 2 possible outcomes).
2. The probability of success (p) is the same across all trials.
3. The number of trials (n) is fixed.

`Formula:`

The binomial distribution is defined by two parameters:

- n: The number of trials.
- p: The probability of success on each trial.

The PMF of a binomial distribution i.e, the probability of getting $x$ successes in $n$ trials is given by the following formula:

$$P(X = x) = \binom{n}{x} \cdot p^x \cdot (1 - p)^{(n - x)}$$

Where, $\binom{n}{x}$ is called the binomial coefficient and is nothing but the number of ways to choose $x$ successes from $n$ trials. You maybe familiar with this as the combination formula $nCx$.

`Examples:`

Here are some examples of how the binomial distribution can be used:

- A marketing manager can use the binomial distribution to estimate the number of customers who will respond to a new advertising campaign.
- A quality control engineer can use the binomial distribution to estimate the number of defective products that are produced in a factory.

`Explained with example:` [Binomial distribution by zedstatistics](https://www.youtube.com/watch?v=e04_wUoscBU&list=PLTNMv857s9WVzutwxaMb0YZKW7hoveGLS&index=2)


## Poisson distribution

Poisson Distribution describes the probability of getting a certain number of events in a fixed interval of time or space, where the events occur independently and at a constant rate.

`One line summary:` *Events per single unit of time.*

`Prerequisites:`
1. The expected number of events in each time interval must be constant.
2. The events must be independent.


`Formula:`
The Poisson distribution is defined by a single parameter:

- λ: The mean rate of occurrence of events i.e, the expected number of events per time interval.

The PMF of the poisson distribution i.e, the probability of getting $x$ number of occurence/events in a fixed interval is given by the following formula:

$$P(X = x) = \frac{\lambda^x e^{-\lambda}}{x!}
$$

`Examples:`


Here are some examples of how the Poisson distribution can be used:

- A call center manager can use the Poisson distribution to estimate the number of phone calls that will be received in a given hour.
- A store manager can use the Poisson distribution to estimate the number of customers who will visit the store on a given day.
- An insurance company can use the Poisson distribution to estimate the number of accidents that will occur in a given month.

`Notes:`
- Poission distribution is bounded by 0 on the left and infinity on the right.
- In a Poisson distribution the expected value, $E(X)$ and the variance, $Var(X)$ are equal i.e, $E(X) = Var(X) = \lambda$.
- $\lambda$ doesn't necessarily have to be an integer. It can be any positive real number.
- In a poisson distribution the max probabilities are centered around the $\lambda$ i.e, the distribution mean or expected value.
- The Poisson distribution approaches a normal distribution as λ increases.
- For a poisson distribution, the expected value can be scaled along with the time interval. For example, if the expected number of events in 1 day is 48, then the expected number of events in 1 hour is 2.


`Explained with example:` [Poisson distribution by zedstatistics](https://www.youtube.com/watch?v=cPOChr_kuQs&list=PLTNMv857s9WVzutwxaMb0YZKW7hoveGLS&index=3)


## Hypergeometric distribution
It is equivalent to the binomial distribution, except that instead of sampling with replacement, the sampling is done without replacement. As a result, the probability of success changes from trial to trial.

The hypergeometric distribution is a discrete probability distribution that describes the probability of getting a certain number of successes in a fixed number of draws, without replacement, from a finite population.

`Formula:`
The hypergeometric distribution is defined by three parameters:

- N: The size of the population.
- K: The number of successes in the population.
- n: The number of draws.

The PMF of the heypergeometric distribution i.e, the probability of getting $x$ successes in $n$ draws is given by the following formula:

$$P(X = x) = \frac{\binom{K}{x} \binom{N-K}{n-x}}{\binom{N}{n}}$$

`Examples:`

Here are some examples of how the hypergeometric distribution can be used:

- A quality control engineer can use the hypergeometric distribution to estimate the probability of getting a certain number of defective products in a sample of products.
- A medical researcher can use the hypergeometric distribution to estimate the probability of getting a certain number of people with a certain disease in a population sample.

`Explained with example:` [Hypergeometric distribution by zedstatistics](https://www.youtube.com/watch?v=upVJ4YqTlC4&list=PLTNMv857s9WVzutwxaMb0YZKW7hoveGLS&index=4)


# Common continuous probability distributions

## Exponential distribution
Exponential Distribution models the time between events in a Poisson process. It is the inverse of the Poisson distribution. 

The exponential distribution describes the time between events that occur independently and at a constant rate. It is often used to model the time between customer arrivals at a store, the time between failures of a machine etc.


`One line summary:` *Time per single event.*

`Prerequisites:`
1. The events must be independent.
2. The events must occur at a constant rate.


`Formula:`
The exponential distribution is defined by a single parameter:

- λ: The rate of occurrence of events. 
- Sometimes the parameter used is, $\mu$ which denotes the expected time per each event. Also, the mean/expected time between events is the inverse of $\lambda$ i.e, $\mu = \frac{1}{\lambda}$.

The probability density function (PDF) of the exponential distribution is given by the following formula:

$$f(x) = \lambda e^{(-\lambda x)}$$

Where, $x$ is the time between events.

The cumulative distribution function (CDF) of the exponential distribution is given by the following formula:

$$F(x) = P(X \le x) =  1 - e^{(-\lambda x)}$$

`Examples:`


Here are some examples of how the exponential distribution can be used:

- A customer service manager can use the exponential distribution to estimate the average waiting time for customers at a call center.
- A maintenance engineer can use the exponential distribution to estimate the average time between failures of a machine.
- A nuclear physicist can use the exponential distribution to estimate the average time between radioactive decays.


`Notes:`

1. The mean and variance of the exponential distribution are both equal to 1/λ.

`Explained with example:` [Exponential distribution by zedstatistics](https://www.youtube.com/watch?v=2kg1O0j1J9c&list=PLTNMv857s9WVzutwxaMb0YZKW7hoveGLS&index=5)

## Uniform distribution
Uniform Distribution represents a continuous random variable that is equally likely to take any value within a specified range.

They are mainly used for random number generation, simulation modeling, and statistical sampling when there is no particular reason to favor one value over another within a given range.

## Normal distribution
The Normal Distribution, also known as the Gaussian distribution or the bell curve, is one of the most important and widely used probability distributions in statistics and probability theory. It is characterized by a symmetric, bell-shaped curve and is defined by two parameters: the mean ($μ$) and the standard deviation ($σ$).

`Prerequisites:`

1. The observations in the distribution must be independent.
2. The observations in the distribution must be random i.e, they are not the result of any known pattern or process.
3. The distribution must be based on a large sample size. This is because the normal distribution is a limiting distribution, meaning that it is the distribution that all other distributions approach (both discrete and continuous random distributions, when a sampling distribution is taken) as the sample size increases. This is also known as the **central limit theorem**. The central limit theorem applies to summary statistics such as, count, mean, median, standard deviation, proportion etc.

`Formula:`

The normal distribution is defined by two parameters:

- $μ$: The mean of the distribution.
- $σ$: The standard deviation of the distribution.

The probability density function (PDF) of the normal distribution is given by the following formula:
$$f(x) = \frac{1}{{\sigma \sqrt{2\pi}}} e^{-\frac{{(x - \mu)^2}}{{2\sigma^2}}}$$

Where $x$ is a real number. This formula gives the heights of the normal distribution's bell curve at each point $x$.

The cumulative distribution function (CDF) of the normal distribution is given by the following formula:

$$F(x) = \Phi\left(\frac{{x - \mu}}{{\sigma}}\right)$$

Where $Φ(x)$ is the *standard normal cumulative distribution function*.

`Examples:`

Here are some examples of distributions that are often assumed to be normal:

- Heights of people.
- IQ scores of students.
- Errors in measurements.
- The distribution of return on investments.

`Standard normal distribution:`

The standard normal distribution is a special type of normal distribution with a mean of, ${\mu} = 0$ and a standard deviation of, $\sigma = 1$. Note that the variance will also be equal to 1.

In this case, the PDF simplifies to:

$$f(x) = \frac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}}$$

Statistical tables are calculated for the standard normal distribution, so it is often useful to convert a normal distribution to a standard normal distribution before looking up probabilities in a statistical table.

To convert a normal distribution to a standard normal distribution, we use the following formula:

$$z = \frac{x - \mu}{\sigma}$$

Where: 
- $z$ is the standard normal random variable 
- $x$ is the normal random variable 
- $μ$ is the mean of the normal distribution 
- $σ$ is the standard deviation of the normal distribution

We can use this $z$ score to calculate PDF and CDF of usual normal distributions in a simple manner.


`Notes:`
- In a normal distribution 68-95-99.7 rule holds i.e,
  - Approximately 68% of the data falls within one standard deviation of the mean.
  - Approximately 95% falls within two standard deviations.
  - Approximately 99.7% falls within three standard deviations.

- There is only one normal distribution for a given mean and standard deviation.
