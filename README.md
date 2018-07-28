# Election Simulation Scripts

Scripts to simulate election outcome using polling average.  

Designed with the 2016 polling errors in mind for more reliable results.  

Run from the command line or add them to a Jupyter Notebook.

### The Core Concepts

- Clearing 50% of votes is an undisputed victory as it is mathematically impossible to lose.  
- A plurality win (a win with less than 50% of votes) should not have a high probability of victory if both candidates are tied within the margin of error.  
- Third-party candidates behind the two leading candidates by 20% are unlikely to win adding to the probability of a last-minute support change not captured in polling.  

### Election.py

Simulates 10,000 elections. Both candidates are simulated as having a polling error.

![electionsim](https://github.com/ahoaglandnu/election/blob/master/electionsim.png)  

### Electionbias.py

Simulates 20,000 elections. One candidate is the subject of polling bias while the other remains within the margin of error.

![electionbias](https://github.com/ahoaglandnu/election/blob/master/electionbias.png)  

### Requirements

Pure Python. Only uses Random.  

Print statements in Python 3 if you are still using Python 2.
