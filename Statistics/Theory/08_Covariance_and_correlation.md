- [Covariance and correlation](#covariance-and-correlation)
  - [Covariance](#covariance)
  - [Correlation](#correlation)
  - [Miscellaneous](#miscellaneous)
  - [Correlation doesn't mean causation.](#correlation-doesnt-mean-causation)

# Covariance and correlation

Both covariance and correlation describes the relationship between two numerical variables.

One type of relationship where the change for both variables is unidirectional is called positive covariance/positive correlation. For example, in hot weather both ice cream sales and sunglasses sales might go up.

Another type of relationship is when the variables moves in opposite directions. For example, in hot weather ice cream sales might go up, but tea sales might go down. This is called negative covariance/negative correlation.

Also, there may not even be any realation between two variables. For example, the amount of ice cream sold and the number of car accidents in a city are probably not related.

But, this is all theory and our guess. We can't just decide whether two variables are related or not without any data. We need to collect data and analyse it to find out the relationship between two variables. Covariance and correlation are just some measures that can helps us to take a decision.

`Explained with example:` [Covariance and correlation by zedstatistics](https://www.youtube.com/watch?v=mG__Wpp9dns&list=PLTNMv857s9WVStKLco6ZBOsfSGXzJ1L0f&index=13)

## Covariance
Covariance is a measure of how much two random variables vary together. It’s similar to variance, but where variance tells you how a single variable varies, covariance tells you how two variables vary together. 


`Formula:`

To calculate covariance between two numerical variables X and Y we can use the following formula:

$$cov(X,Y) = \sigma_{xy} = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{n-1}$$

Where, 
- $\bar{x}$ and $\bar{y}$ are the means of X and Y respectively
- n is the sample size

`Example:`
x | y | x - $\bar x$ | y - $\bar y$ | (x - $\bar x$)(y - $\bar y$)
--- | --- | --- | ---| ---
10 | 2 | -10 | -2 | 20
20 | 4 | 0 | 0 | 0
20 | 5 | 0 | 1 | 0
30 | 5 | 10 | 1 | 10
$\sum$ |  |  | | 30

Thus, covariance between x and y is:
$$cov(x,y) = \frac{30}{4-1} = 10$$

Since the sign of the calculated $\sigma_{xy}$ is positive we can say that the two variables are positively related i.e, when x increases, y also increases. But we don't know how strongly are those variables related. For that we need to calculate correlation.

## Correlation

The correlation is a dimensionless quantity and is denoted by $\rho_{xy}$. It is a normalized measure of covariance. It is used for quantitative measurement of the statistical dependence between two random variables.

The correlation between two numerical variables is calculated by the following formula:
$$\rho_{xy} = \frac{\sigma_{xy}}{\sigma_x \sigma_y}$$

Where, 
- $\sigma_{xy}$ is the covariance of x and y
- $\sigma_x$ and $\sigma_y$ are the standard deviations of x and y respectively

`Example:`
x | y | x - $\bar x$ | y - $\bar y$ | $(x - \bar x)^2$ | $(y - \bar y)^2$ | (x - $\bar x$)(y - $\bar y$)
--- | --- | --- | ---| --- | --- | ---
10 | 2 | -10 | -2 | 100 | 4 | 20
20 | 4 | 0 | 0 | 0 | 0 | 0
20 | 5 | 0 | 1 | 0 | 1 | 0
30 | 5 | 10 | 1 | 100 | 1 | 10
$\sum$ |  |  |  | 200 | 6 | 30

Now,
$$cov(x,y) = \sigma_{xy} = \frac{30}{4-1} = 10$$
$$ \sigma_x = \sqrt{\frac{200}{4-1}} = 6.32$$
$$ \sigma_y = \sqrt{\frac{6}{4-1}} = 2.45$$

So, the correlation between x and y is:
$$\rho_{xy} = \frac{10}{6.32 \times 2.45} = 0.64$$

The value of $\rho_{xy} = 0.64$ is quite high and this tells us that the two variables are strongly positively related.

`Notes:`
- Covariance and correlation are only defined for numerical variables.
- **Covariance and correlation are only defined for linear relationships.**
- Correlation is always between -1 and 1.

## Miscellaneous
If the data is given as a probability distribution, then the covariance is calculated as:
$$cov(X,Y) = \sum_{i=1}^{n} (x_i - E_x)(y_i - E_y) \times P(x_i,y_i)$$
Where, 
- P(x,y) is the joint probability distribution of X and Y. If the data is given as a frequency distribution, then we use, $f(x_i,y_i)$ instead of $P(x_i,y_i)$.
- $E_x$ and $E_y$ are the expected values of X and Y respectively.

And the correlation is calculated same as before:
$$\rho_{xy} = \frac{cov(X,Y)}{\sigma_x \sigma_y}$$

$$ \sigma_x = \sqrt{\sum_{i=1}^{n} (x_i - E_x)^2 \times P(x_i)}$$
$$ \sigma_y = \sqrt{\sum_{i=1}^{n} (y_i - E_y)^2 \times P(y_i)}$$


## Correlation doesn't mean causation.
Correlation is a measure of the strength of the relationship between two variables. It does not imply causation. For example, there is a strong correlation between ice cream sales and sunglasses sales. But, that doesn't mean that sunglasses sales causes ice cream sales or vice versa. The reason behind this correlation is that both of these variables are related to the weather. When the weather is hot, both ice cream sales and sunglasses sales go up. So, the weather is the actual cause of this correlation.

Such correlations are called spurious correlations and the hidden causes of these correlations are called lurking or confounding variables.
