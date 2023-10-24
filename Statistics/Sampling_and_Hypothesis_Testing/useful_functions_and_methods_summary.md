

# Plotting functions

- `sns.boxplot()` is a great way to visualize the distribution of a common numerical variable across the levels of a categorical variable. It is also a great way to visualize any outliers in the data.

- `sns.barplot()` is a great way to visualize categorical data with certain central tendency statistics (mean, median, etc.) and confidence intervals.

- `sns.countplot()` is a barplot where the dependent variable is the number of instances of each instance of the independent variable.

- `sns.histplot()` is a great way to visualize the distribution of a single numerical variable. It is very useful for confirming the distribution of the data and checking for skewness.

- `sns.scatterplot()` is a great way to visualize if there is a relationship between two numerical variables. It is also a great way to visualize outliers. Plotting the index of the data on the x-axis and the data itself on the y-axis is very useful for visualizing if there is any underlying structure in the data.


# Hypothesis Testing Workflow in Python

![Alt text](<Hypothesis testing workflow Python.png>)


# z-test

**The z-test** can be used to test the null hypothesis that a population parameter is equal to a certain value, *for any population parameter that is normally distributed*. This includes parameters such as the *population mean, the population variance, and the population proportion*.

$$ z = \frac{\text{Sample statistic} - \text{Null Hypothesis value}}{\text{Standard error of the sample statistic}} $$

$$ z = \frac{\text{Sample statistic} - \text{Null Hypothesis value}}{\sigma / \sqrt{n}} $$

- For finding the population standard deviation, `np.std(population_parameter, ddof=0)` is used.

- For finding the sample standard deviation, `np.std(sample_parameter, ddof=1)` is used.

- After finding the *z-score* the **p-value** is found using the `stats.norm.cdf(z_score)` function. This will give the area under the normal curve to the left of the z-score. To find the area to the right of the z-score, `1 - stats.norm.cdf(z_score)` is used. For a two tailed test, `2 * (1 - stats.norm.cdf(z_score))` is used. But keep in mind that for two tailed tests the significance level is split in half for each side.

- For finding the **confidence interval** for the population parameter, either use `<series>.quantile([zl, zr])` method or the `stats.norm.interval(alpha, loc, scale)` function. The `loc` parameter is the sample statistic and the `scale` parameter is the standard error of the sample statistic.



