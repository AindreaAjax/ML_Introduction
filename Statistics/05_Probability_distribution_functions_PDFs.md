- [Discrete and Continuous random variables](#discrete-and-continuous-random-variables)
  - [Discrete random variables](#discrete-random-variables)
  - [Continuous random variables](#continuous-random-variables)
- [Probability distribution function (PDFs)](#probability-distribution-function-pdfs)
  - [Cuminative distribution function (CDF)](#cuminative-distribution-function-cdf)
- [Probability mass function (PMF)](#probability-mass-function-pmf)
  - [Cumulative distribution function (CDF) for discrete random variables](#cumulative-distribution-function-cdf-for-discrete-random-variables)
- [Probability density function (PDF)](#probability-density-function-pdf)
  - [Cumilitive distribution function (CDF) for continuous random variables](#cumilitive-distribution-function-cdf-for-continuous-random-variables)


# Discrete and Continuous random variables

## Discrete random variables

A discrete random variable is a random variable that can only take on a finite or countable number of distinct values. These values are often represented by integers or whole numbers. For example, the number of children in a family can take on the values 0, 1, 2, 3, 4, and so on. It can never be 2.5 children.

Discrete random variables are often used to model real-world phenomena, such as the number of children in a family, the number of defective products in a production line, or the number of cars that pass through an intersection in a certain amount of time.

## Continuous random variables

The set of possible values for a continuous random variable is an interval of real numbers and a continuous random variable can take on any value in that particular range. 

In other words, a continuous random variable represents a quantity that can take on an infinite number of possible values within a specified range. 

Unlike discrete random variables, which can only take on a countable number of distinct values, continuous random variables can assume any value within their defined range. Continuous random variables are usually measurements, such as height, weight, the amount of sugar in an orange, or the time required to run a mile. 


# Probability distribution function (PDFs)

**Probability Distribution Functions (PDFs), often referred to as simply "distributions," describe the set of all possible values a random variable can take and the probability associated with each value.**

PDFs can be used to model a wide variety of real-world phenomena, such as the number of customers in a store on a given day, the height of students in a class, or the amount of rainfall in a month.

PDFs can be used for both discrete and continuous random variables. For discrete random variables, PDFs provide the probability mass function (PMF), which assigns probabilities to specific values. For continuous random variables, PDFs provide the probability density function (PDF), which assigns probabilities to intervals or ranges of values.

The notation for PDFs varies depending on whether it's for a discrete or continuous random variable. For discrete, it's often denoted as $P(X=x)$, and for continuous, it's denoted as $f(x)$.


## Cuminative distribution function (CDF)

**The cumulative distribution function (CDF) provides the cumulative probability that a random variable X takes on a value less than or equal to a specific value x.**

The CDF of a random variable can be used to calculate a number of important probabilities, such as the probability that a random variable will fall within a certain range of values.

Similar to PDFs (probability distribution function), CDF can be calculated for both discrete and continuous random variables.

The CDF of a random variable has a number of important properties. For example, 
1. The CDF is always non-decreasing 
2. The CDF of a continuous random variable is always continuous.
3. The CDF of a random variable is always equal to 1 at the point where the random variable takes on its largest possible value.


# Probability mass function (PMF)

Probability mass function (PMF) describes the probability that a discrete random variable will take on a particular value. In other words, a probability mass function is a function that gives the probability that a discrete random variable is exactly equal to some value.

For example, if we were to toss a fair coin 3 times then the PMF for X = 'head' would be,

x = Number of heads | 0 | 1 | 2 | 3
--- | --- | --- | --- | ---
P(X = x) | 1/8 | 3/8 | 3/8 | 1/8

So the probability that we will get 3 heads in 3 tosses is 1/8 which is equal to the probability that we will get no heads in those 3 tosses.


## Cumulative distribution function (CDF) for discrete random variables

The CDF of a discrete random variable, X can be calculated by summing the probabilities of all the values of X that are less than or equal to x. Where x denotes the discrete values that X can take on.

Expanding on our previous example of tossing a fair coin 3 times, the CDF for 'head' (X) would be,

x = Number of heads | 0 | 1 | 2 | 3
--- | --- | --- | --- | ---
P(X ≤ x) | 1/8 | 4/8 | 7/8 | 1

At first glance this may seem ridiculuos to some, that the probability of getting 3 or less heads in 3 tosses is 1. But this is because in that x <= 3, the probability of x = 0 i.e, getting 0 heads is also included. 

Remember, the CDF is the probability that X will take a value less than or equal to x and the PMF is the probability that X will take a particular value. So the probability that we will get 3 heads in 3 tosses is 1/8 (as obtained from the PMF).

This would be less confusing if we asked what is the probability that in 3 fair coin tosses at least 1 head is obtained. This would be, 
$$P(X >= 1) = 1 - P(X < 1)$$ 
$$ = 1 - P(X = 0)$$ 
$$ = 1 - 1/8 = 7/8.$$


# Probability density function (PDF)

The Probability density function (PDF), denoted as f(x), describes how the probability is distributed across the possible values of a continuous random variable X. It provides the density of probabilities over a small interval/range of values.

Due to the nature of continuous random variables, the probability that a continuous random variable will take on a particular value is zero. This is because there are an infinite number of possible values, and the probability of any one value occurring is infinitesimally small. This is why PDF is defined as the probability density rather than the probability itself.

**Note:** Probability density function (PDF) should not be confused with probability distribution function (PDFs).  "Probability Distribution Functions" is a broader term that encompasses the concept of probability distributions for both discrete and continuous random variables, while "Probability Density Function" is a specific term used only for continuous random variables to describe the probability distribution in terms of densities over intervals.

Example: If X represents the height of individuals in a population, the PDF tells you how likely it is for an individual's height to be within a specific range (e.g., between 5 feet and 6 feet).

To find the probability that a continuous random variable falls within a specific interval [a, b], you integrate the PDF over that interval:

$$P(a \leq X \leq b) = \int_{a}^{b} f(x) \, dx
$$

**Note:** 

The total area under the PDF curve, over its entire possible range, is always equal to 1.

$$\int_{-\infty}^{\infty} f(x) \, dx = 1
$$



## Cumilitive distribution function (CDF) for continuous random variables

The CDF of a continuous random variable tells us how much of the distribution is to the left of a certain value. The CDF of a continuous random variable is the integral of its PDF.

Example: Using the same height example, the CDF tells you what is the probability that an individual's height is less than or equal to 6 feet.

The CDF of a continuous random variable can be calculated by integrating the probability density function (PDF) of X from 0 to x.

$$F(x) = \int_{-\infty}^{x} f(x) \, dx $$


**Note:** 
1. $0≤F(x)≤1$: The CDF is always between 0 and 1.
2. $F(−∞)=0$ and $F(∞)=1$: The CDF approaches 0 as x approaches negative infinity and approaches 1 as x approaches positive infinity.

