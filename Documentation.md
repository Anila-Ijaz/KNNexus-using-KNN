# Introduction:
In this exercise, the KNN Classifier was implemented from scratch. For comparison two other
classifiers were used named “ sklearn KNN” and “sklearn Decision Tree”. From five datasets,
two were used in this practical task.
# Experiment setup:
The two datasets that were selected are following:
1. Iris Dataset
2. Wine Quality Dataset
Three classifiers are used for both datasets in order to make comparisons between them. These
classifiers are following:
1. K-Nearest Neighbor — Scratch Implementation
2. K-Nearest Neighbor — Sklearn Python Library
3. Decision Tree — Sklearn Python Library
Decision trees handle non-linear relationships, fast training time, few parameters and are
computationally efficient.
Different dataset ratios are used for training and testing in this task. The ratio varies from 70:30
to 80:20 for this particular task. As the dataset is small for the Iris dataset, I decided to split the
train and test dataset as 70:30. For the second dataset the dataset size is relatively larger than
the first, so split train and test ratio was 80:20.
Different hyperparameters of K-Nearest Neighbors were tested as follows:
k ranging from 2 to 10 was considered. The highest accuracy at k=4 for the first dataset and
remains constant almost for above k and k remains stable. For k=3 in the second dataset, the
accuracy was highest which was 80% almost . Because both the datasets are relatively small,
k=3 and k=4 were chosen as a good tradeoff to minimize model complexity while retaining high
accuracy. Besides, smaller values of k better preserve local neighborhood information and
reduce the risk of over-smoothing of the decision boundary.
# Presentation of results:
Lets see the results obtained from Iris dataset:
<img width="752" height="430" alt="image" src="https://github.com/user-attachments/assets/e7496019-47a2-4df0-9827-c2f7a7b605f2" />
# Discussion of the results:
# Dataset 1 — Iris Dataset:
The experimental results show that both the custom KNN method and the scikit-learn library's
KNN Classifier achieved the highest accuracy of around 97.78%, confirming that the custom
method works comparably to its library counterpart. Also, the accuracy achieved by the Decision
Tree Classifier was a bit low at around 95.56%, this could be due to its natural inclination toward
data overfitting with smaller datasets. In conducting computations, both the scikit-learn library's
methods finished computations earlier owing to the optimizations made with the library's internal
functions, whereas the custom's computation with the KNN method took slightly longer because
all distances were calculated using the Euclidean distance method. Once again, this experiment
verifies the correctness and reliability of the custom method with its accuracy on this dataset
proving the power of the KNN method itself. In the end, the confusion matrix helped to
understand the false positive and false negative values of the feature, the confusion matrix was
quite similar in case of sklearn KNN and sklearn Decision Tree but it was different in custom
KNN.
# Dataset 2 — Wine quality Dataset:
In the case of the Wine Quality dataset, it was observed that the highest accuracy was obtained
using the Decision Tree Classifier at approximately 94.44%, significantly outperforming both
versions of the KNN Classifier, with both versions producing an accuracy of approximately
80.56%. These results provide evidence that the Decision Tree algorithm was better equipped to learn relationships between key features inherent to this dataset. With regard to
computational time, all models performed well for this dataset; however, there was an
observable reduction for models developed using the sklearn library. Confusion matrix was also
made in order to know the false positive and false negative values for features. The confusion
matrices explain that both the custom and sklearn KNN classifiers show similar behavior in
performing well on Classes 0 and 1, while performing considerably poorly on Class 2, which
results in several misclassifications. This is in deep contrast to the Decision Tree classifier,
which showed notably better performance on all classes, especially Class 2, where it attained a
much higher number of correct predictions along with fewer misclassifications. This explains
better class-wise separation that results in a higher overall accuracy attained by a Decision Tree
model on the Wine Quality dataset.
# Conclusion:
In conclusion, although it was realized the custom-developed KNN Classifier worked as well as
its counterpart from the Scikit-learn package, its slower speed attests to its possibility for
optimization. Moreover, although not a major part, it was realized how the size of the datasets
affects the performance metrics as well as the speed through applying the Decision Tree
Classifier Algorithm over the datasets; especially how a one false positive from a smaller
dataset as Dataset 1 affects the accuracy
