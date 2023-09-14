- [Spread](#spread)
- [Range](#range)
- [Quantiles](#quantiles)
- [Interquartile Range (IQR)](#interquartile-range-iqr)
- [Variance](#variance)
    - [Answer to 2 common questions about the Variance](#answer-to-2-common-questions-about-the-variance)
- [Standard Deviation](#standard-deviation)
- [Coefficient of Variation (CV)](#coefficient-of-variation-cv)
- [Conclusion](#conclusion)


# Spread
Spread, in statistics, refers to the extent to which the values in a data set vary or are dispersed from the central tendency (such as the mean, median, or mode). It provides information about the degree of variability or dispersion in the data. Spread is an important concept because it helps you understand how much individual data points deviate from the central value and can provide insights into the data's overall distribution.

There are several measures that are commonly used to describe spread such as, range, interquartile range, variance, standard deviation, coefficient of variation etc.

# Range
The range is the simplest measure of spread and is calculated as the difference between the maximum and minimum values in a data set. *It gives you an idea of the total spread in the data but is sensitive to outliers and often does not provide a complete picture of the distribution.*

$$ Range = Max\ val - Min\ val $$

# Quantiles
Before discussing interquartile range, let's first understand what are quantiles.

Quantiles are values that divide an ordered data set into equal-sized parts. Common quantiles include quartiles, quintiles, deciles, and percentiles, each of which divides the data into a specific number of equal parts.

Here are some commonly used quantiles:

  - **Quartiles:** Quartiles divide a data set into four equal parts, with each part containing approximately 25% of the data. There are three quartiles:
    - First Quartile (Q1): The value/observation that is one quarter or 25% of the way through the ordered dataset. It is the value below which 25% of the data falls.
    - Second Quartile (Q2): The same as the median, the value below which 50% of the data falls.
    - Third Quartile (Q3): The value below which 75% of the data falls.

- **Quintiles:** Quintiles divide a data set into five equal parts, each containing approximately 20% of the data.

- **Deciles:** Deciles divide a data set into ten equal parts, each containing approximately 10% of the data.

- **Percentiles:** Percentiles divide a data set into 100 equal parts, with each percentile representing a specific percentage of the data set.

Quantiles are useful for analyzing and summarizing data because they help you understand how values are distributed across various parts of the data set. They are particularly valuable for identifying outliers, assessing the spread of data, and making comparisons between different data sets. 

*When working with large data sets or data that has a wide range, quantiles provide a more detailed view of the distribution than just measures like the mean and standard deviation.*

# Interquartile Range (IQR)

The IQR is a robust measure of spread that is less affected by outliers. It is calculated as the difference between the third quartile (Q3) and the first quartile (Q1) of the data. The quartiles divide the data into four equal parts, and the IQR represents the spread of the middle 50% of the data.

$$ IQR = Q3 - Q1 $$

Box and whisker plots are a popular visualization technique to represent the IQR and other measures of spread. The box represents the IQR, and the whiskers extend to the minimum and maximum values in the data set. Outliers are plotted as individual points.

# Variance

Variance provides a measure of how much individual data points deviate from the mean. 
$$ Population\ Variance,\ \sigma^2 = \frac{\sum_{i=1}^{N}(x_i - \mu)^2}{N} $$

where, $\mu$ is the population mean and $N$ is the number of data points.

$$ Sample\ Variance,\ s^2 = \frac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n-1} $$

where, $\bar{x}$ is the sample mean and $n$ is the number of data points.

### Answer to 2 common questions about the Variance
1. Why do we square the distance of the data points from the mean? Since the mean is by definition sits at the middle of the dataset, if we were to just simply find out the average deviation (of the data points from the mean) then the deviations of the data points above the mean would have canceled out the deviations below the mean. Thus, if we don't square the individual deviations, the sum of the deviations will always be zero. Squaring the deviations ensures that the sum of the deviations is always positive. Now we might say why not take the absolute value of the deviations instead of squaring them? Short and simple answer is Math (Enter Math Jargon: the reason is that the absolute value function is not differentiable at zero, which makes it difficult to work with mathematically. The squared function, on the other hand, is differentiable everywhere). 

    **`Note:`** We actually use the absolute deviation to form another measure of spread called the **Mean Absolute Deviation (MAD)**.
    $$ MAD = \frac{\sum_{i=1}^{N} |x_i - \mu|}{N}$$

    Since we squared all the deviations, the variance penalizes the larger deviations more severly whereas, MAD treats all deviations equally. Thus, variance is more sensitive to outliers than MAD. Also, the variance is in squared units of the original data whereas MAD is in the same units as the original data. Thus, MAD is more interpretable than variance. Even then Standard Deviation is more commonly used than MAD.

2. Why do we divide the sum of squared deviations by $N-1$ in the population variance formula and by $n-1$ in the sample variance formula? This is done to correct for the bias in the estimation of the population variance from the sample variance. The sample variance is a biased estimator of the population variance because it tends to underestimate the population variance (since we can't exactly know the population mean thus we use sample mean to calculate the sample variance). Dividing by $n-1$ instead of $n$ corrects for this bias. This is known as Bessel's correction.


# Standard Deviation

The standard deviation is the square root of the variance and provides a more interpretable measure of spread in the same units as the data. It quantifies the average distance of data points from the mean.

$$ Population\ Standard\ Deviation,\ \sigma = \sqrt{\frac{\sum_{i=1}^{N}(x_i - \mu)^2}{N}} $$

$$ Sample\ Standard\ Deviation,\ s = \sqrt{\frac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n-1}} $$


# Coefficient of Variation (CV)

The coefficient of variation is the ratio of the standard deviation to the mean, expressed as a percentage. 

So why do we need it? The standard deviation is a measure of absolute variability. It doesn't take the scale of the data into account. But it is often useful to compare variability between two data sets that have different means. The coefficient of variation allows you to compare the spread of two data sets that have different units or scales. A practical example is explained in [this YouTube video](https://www.youtube.com/watch?v=9dwLKGoaeEs&list=PLTNMv857s9WVStKLco6ZBOsfSGXzJ1L0f&index=8). 


$$ CV = \frac{s}{\bar{x}} \times 100 \% $$


# Conclusion
These measures of spread helps us understand the distribution and variability within a data set. A large spread indicates that data points are widely dispersed, while a small spread suggests that data points are closely clustered around the central value. The choice of spread measure depends completely on the dataset (whether it's skewed or not, whether there are outliers or not etc.) and the context of the problem.
