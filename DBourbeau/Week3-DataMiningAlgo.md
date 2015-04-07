#Assignment 3 - Data Mining Algorithms Readthru


1.  What was the name of the algorithm you read about?

		Non-Negative Matrix Factorization(NMF)

2.  What data problem does it solve? (listed under Technique on previous page)
		
		This algorithm is used for Feature Selection, which will tell the modeller what attributes are the most relevant, and Feature extraction, combining attributes into a new set of data.
		Unstructured data can have numerous junk attributes that slow down the model processing or inserts noise. 

3.  In layman's terms, what does the algorithm do?

		The algorithm breaks down the data set into two pieces, the matrix W, contains all the data the model is based on. The second matrix H, contains weighting values used to iterate.
		The algorithm iterates both W and H until it converges on on a value. Matrices must be given a initial conditions, which can be set manually or default. The initial conditions are important, a bad seed can skew the results.
		The output matrix M, is produced as a new feature.  During Feature Selection, the algorithm tweaks the variables and tracks which variables make the largest difference to M. 
		NMF has a scoring feature that displays something similar to the covariance a set of variables.

4.  Come up with up to three applications of this algorithm in business.

		I am interested in using environmental data to push behaviour change. One way I think this algorithm and a large data set of personal resource consumption patterns, you could find what actions to promote that provide the best environmental impact per dollar spent. 
		In my work life, I work in property management. The feature selection, algorithm could be used to provide a weighted analysis of which expenses most need to be investigated further.

		
[Oracle Resource-Non-Negative Maxtrix Factorization](http://docs.oracle.com/database/121/DMCON/algo_nmf.htm#DMCON058)