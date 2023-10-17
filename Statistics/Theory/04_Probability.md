- [Probability](#probability)
  - [Four basic rules of probability](#four-basic-rules-of-probability)
    - [Complement rule](#complement-rule)
    - [Rule for equally likely outcomes](#rule-for-equally-likely-outcomes)
    - [Addition rule for mutually exclusive events](#addition-rule-for-mutually-exclusive-events)
    - [Multiplication rule for independent events](#multiplication-rule-for-independent-events)
  - [Conditional probability](#conditional-probability)
    - [Bayes' rule](#bayes-rule)

# Probability

In simple terms, probability involves predicting the relative likelihood that a particular event will occur, expressed as a number between 0 and 1. The higher the probability of an event, the more likely it is that the event will occur.

The probability of an event is defined as the proportion of times this event occurs in many repetitions. For example, in 2015 there were about 4 million babies born in the US, and 48.8% of the newborns were girls. So we write, $P(newborn\ is\ a\ girl)= 48.8\%$.

## Four basic rules of probability

### Complement rule
If probability of event $A$ is $P(A)$, then the probability of event $A$ not occurring is,

$$P(A\ does\ not\ occur) = 1-P(A)$$.

### Rule for equally likely outcomes
If there are $n$ equally likely outcomes, and $m$ of them correspond to event $A$, then the probability of event $A$ is, 
$$P(A) = \frac{m}{n}$$ 

For example, if you roll a fair die, the probability of getting a 6 is $P(6) = \frac{1}{6}$.

### Addition rule for mutually exclusive events
If events $A$ and $B$ are mutually exclusive, then the probability of either event occurring is, 

$$P(A\ \cup B) = P(A) + P(B)$$

So what does it mean for two events to be mutually exclusive? It means that the two events cannot occur at the same time. For example, if you roll a fair die, the events getting a 6 and getting a 5 on the same roll are mutually exclusive. But, getting a 5 and getting an odd number are not mutually exclusive, because you can get a 5 and an odd number on the same roll.

For mutually exclusive events, 

$$P(A \cap B) = 0$$ 

### Multiplication rule for independent events
If events $A$ and $B$ are independent, then the probability of both events occurring is, 

$$P(A\ \cap B) = P(A) \times P(B)$$

So what does it mean for two events to be independent of each other? Two events are independent if knowing that one occurs doesn't change the probability that the other one occurs. For example, getting a 6 on the second roll is independent of whatever you got on the first roll.

There will always be some intersection between two independent events. And for independent events $A$ and $B$, $$P(A\ |\ B) = P(A)$$

Two events are dependent if knowing that one occurs changes the probability that the other one occurs. For example, getting a 6 on the first roll completely eliminates the possibility of getting a 3 on that same roll.

Mutually exclusive events are the most extreme example of dependent events.


## Conditional probability

Conditional probability is the probability of an event occurring given that another event has already occurred. 

The conditional probability of event $B$ that occurs given that event $A$ has occurred is defined as, 

$$P(B|A) = \frac{P(A\ and\ B)}{P(A)}$$

For example, if we said what is the probability of getting two sixes in two rolls. Then the events are independent and the probability would be calculated using the multiplication rule as, $P(6\ and\ 6) = P(6) \times P(6) = \frac{1}{6} \times \frac{1}{6} = \frac{1}{36}$. 

But if we asked, what is the probability of getting two sixes in two rolls given that the first roll was a six. Then the events are dependent and the probability would be calculated using the conditional probability formula as, $P(6|6) = \frac{P(6\ and\ 6)}{P(6)} = \frac{\frac{1}{36}}{\frac{1}{6}} = \frac{1}{6}$. 

We can arrive at this result intuitively without using the formula.

- <u>A more realistic example</u>

Spam emails has a higher chance of containing the word money. Let's say that, 8% of the spam emails contains the word "money" whereas, only 1% of the ham (not spam) emails contains the word "money". So, if a new email has 20% chance of being spam, what is the probability that it contains the word "money"?

Let's go step by step.

$$P(the\ email\ contains\ money) = P(the\ email\ is\ spam\ and\ contains\ money) + P(the\ email\ is\ ham\ and\ contains\ money)$$ 

$$=P(money\ |\ spam) * P(spam) + P(money\ |\ ham) * P(ham)$$

$$=0.08 * 0.2 + 0.01 * (1-0.2) = 0.024 = 2.4\%$$

### Bayes' rule

Bayes' rule is a way to calculate conditional probabilities. It is defined as, 

$$P(A|B) = \frac{P(B|A) \times P(A)}{P(B)}$$.

To expand on our previous example about spam emails, let's say that we want to calculate the probability that an email is spam given that it contains the word "money". We can use Bayes' rule to calculate this probability as,

$$P(spam\ |\ money) = \frac{P(money\ |\ spam) \times P(spam)}{P(money)}$$

$$=\frac{0.08 \times 0.2}{0.024} = 66.7\%$$


The spam filter classifies e-mail as spam via a Bayesian analysis:

1. Before examining the e-mail, there is a prior probability of 20% that it is spam.
 
2. After examining the e-mail for certain keywords such as ‘money’, the filter updates this prior probability using Bayes’ rule to arrive at the posterior probability that the
e-mail is spam.

This is an example of how the Bayes' rule is used in real life.

