- [Central tendency](#central-tendency)
- [The mean](#the-mean)
    - [Weighted mean](#weighted-mean)
    - [When to use?](#when-to-use)
    - [Note: Here we've only discussed the arithmatic mean. There are also geometric and harmonic means. Get an introduction to geometric and harmonic means from this YouTube video by zedstatistics.](#note-here-weve-only-discussed-the-arithmatic-mean-there-are-also-geometric-and-harmonic-means-get-an-introduction-to-geometric-and-harmonic-means-from-this-youtube-video-by-zedstatistics)
- [The median](#the-median)
    - [When to use?](#when-to-use-1)
- [The mode](#the-mode)
    - [When to use?](#when-to-use-2)


# Central tendency
Central tendency is a measure of the value around which a set of data tends to cluster or concentrate. It is a way to describe the center or typical value of a data set. There are three common measures of central tendency: The mean, median and mode.

# The mean
The mean, also called the average, is calculated by adding up all the values in a data set and dividing by the number of observations.

- **Population mean**
$$ \mu = {\sum x \over N} $$ 
Where, `N` is the population size.

- **Sample mean**
$$ \bar x  = {\sum x \over n} $$
Where, `n` is the sample size.

### Weighted mean
If the freqency of each value is known, the mean can be calculated as,
$$ \mu = {\sum f x \over \sum f} $$

Where, `f` is the frequency of each value.

### When to use?
- It is a good measure of central tendency when the data is numeric, not skewed (such as uniform, normal or bimodal distribution) and does not have extreme outliers.

### Note: Here we've only discussed the arithmatic mean. There are also geometric and harmonic means. Get an introduction to geometric and harmonic means from [this YouTube video](https://www.youtube.com/watch?v=jXKYI7wyqp0&list=PLTNMv857s9WVStKLco6ZBOsfSGXzJ1L0f&index=2) by zedstatistics.

# The median

The median is the middle value in a data set when the values are arranged in ascending or descending order. In other words, the median is the value where 50% of the data is lower than it, and 50% of the data is higher. 

If there's an odd number of observations then the median is simply the middle value after the sorting is done. But if there is an even number of values then the median is the average of the two middle values i.e.,
$$ median = {Val_{n/2} + Val_{(n/2 + 1)} \over 2}$$

### When to use?
- The median is less affected by extreme values (outliers) compared to the mean, making it useful for skewed data sets. For example, it is often the case that the median house price is quoted instead of the average price since house prices are usually right skewed (most of the data are fairly close to each other but there are a good number of values that are way above the rest).

# The mode

The mode is the value that occurs most frequently in a data set i.e, it is the observation with the highest frequency. A data set can have one mode (unimodal), multiple modes (multimodal), or no mode at all. *The mode is often used with categorical or nominal data but can also be applied to numeric data.*

### When to use?
- The mode is useful when the data is categorical or when you want to know which option is most popular.
- The mode is not affected by extreme values (outliers) and can therefore be useful for skewed data sets.
- Try to avoid using mode when you don't have a large enough dataset. The mode sucks for small samples. 
