# Assignment 3
_ODM algorithm write up_

## Naive Bayes

Naive Bayes is a classification algorithm that is an example of supervised learning.

The idea of the algorithm is to use Bayesian approach that has the following key components:
- Likelihood: the distribution is specified for feature variables assuming different parameters for each target category.
- Prior: prior distribution is specified for marginal probability of belonging to a target category 
in the absense of any other information.
- Posterior distribution: based on Bayes theorem it is proportional to likelihood times prior.

Further "naive" assumption is made that featuers are pairwise independent, 
which simplifies etimation of the posterior distribution. 
Odds of belonging to a particular class are then estimated using maximum aposteriori estimation.

The examples of using Naive Bayes would be various types of classification problems:
- classifying e-mail as spam or not spam, with features corresponding to occurence of each word in an e-mail;
- classifying presence or absense of disorder based on a given set of measurements.
