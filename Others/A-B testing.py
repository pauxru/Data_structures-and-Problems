"""
A / B  testing is used to measure the effectiveness of two options. e.g.
is a blue button better than a red button on a website

p-value: Represents the false positivity probability i.e. what is the probability
that one will see difference after the test while in reality there is no difference
between the two options being tested. if p-value < 5% the results are significant

https://www.youtube.com/watch?v=AJX4W3MwKzU&ab_channel=StanfordOnline

1) if a user has a desired false positive probability a

2) Stop the experiment when the sample mean crosses constant.sqrt(log n / n) which is an outer
boundary of the false positive probability.

3) If the truth is different from this rule is guranteed to detect it eventually since
constant.sqrt(log n / n) approaches zero as n tends to infinity.

A likely-hood ratio between the alternative and the null hypothesis is tracked instead of
calculating the p-values every time

https://www.youtube.com/watch?v=KS6KEWaoOOE&ab_channel=KhanAcademy
"""