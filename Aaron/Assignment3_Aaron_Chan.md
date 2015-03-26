Assignment3_Aaron_Chan.md

## Assignment 3

* **What was the name of the algorithm you read about?**

I read about the Mininnum Description Length (MDL) algorithm.

* **What data problem does it solve? (listed under Technique on previous page)**

The algorithm ranks data attributes and features according to the strength of relationship with the target feature.

* **In layman's terms, what does the algorithm do? Even if you aren't sure, that's okay! Just try your best--we're not looking for perfect answers.**

Conceptually, the MDL assumes that the simplest and most compact representation of the data is the best and most probable explanation of the data.

This is achieved through the process of data compression (encoding information using fewer bits), entropy (uncertainty in a random variable) measurement and model selection, where each attribute is a simple predictive model of the target attribute. The single predictor models are then compared and ranked in terms of their MDL metric, which is the relative compression in bits or description length.

In other words, models (attributes) that result in the shortest description length and the lowest random variable entropy are seen as the most significant attributes.

* **Come up with up to three applications of this algorithm in business. Try relating it to your own job or line of work, your other data interests, or what have you.**

In stock analysis, you could look at a plethora of non-price related attributes like EPS growth rates, ROA, ROE, gross/op/profit margins, and capital expenditures and rank them according the their respective MDL description lengths relative to price.

For talent acquisition and retention, you could look at salaries, salary increases, vacation time, average weekely hours and other perks and compare them to tenure to try and understand which attributes are associated with longer tenures at the company. 

* **Concepts/Words**

* "shortest description of the data is the most probable"
* "over-fit"
* "MDL uses a communication model for solving the model selection problem"

