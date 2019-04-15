### Section E

1)

p = 1/50 (Success : ball falls in a bin)
Poisson probability is: P(x; μ) = (e-μ) (μx) / x!
μ = 100*(1/50)=2 (expected mean of balls in a bin = np)
x = 0 (for the case when 0 balls fall in a bin)
=> P(x; μ) = (e<sup>-2</sup>) (20) / 0! = e-2 = 0.135
Therefore, for 50 bins, total no. of empty bins = 50 * 0.135 = 6.75 ~ 6

2)
i)
The expectation value of the PER is denoted packet error probability pp, which for a data packet length of N bits can be expressed as:
Pp = 1- ( 1-Pe )N
Since, that the bit errors are independent of each other. For small bit error probabilities and large data packets, this is approximately:
Pp=Pe*N= 10<sup>-10*</sup> .1000= 10<sup>-7</sup>
 
ii)

By Markov inequality:
Upper bound for the probability of a random variable is greater than or equal to 10 : 
P{N≥10}  ≤ E(N)/10 = 10<sup>-7</sup> / 10 = 10<sup>-8</sup>


3)

p1 (winning $4) = 17/52 (13/52 for spades + 4/52 for queens)
p2 (losing $1)= 35/52 (= 1 - 17/52)
Expected win in 1 night = (4*17/52) + (-1*35/52) = 33/52 = $0.635
Expected win after 30 nights = (33/52) *30 = $ 19.04
 
