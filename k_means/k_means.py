import numpy as np
import random
import pandas as pd

class k_means():
    def __init__(self, k, tolerance, iter):
        # Initialize the parameters
        # k: The number of clusters; tolerance: Difference between two iterations; iter: max number of iterations
        self.k = k
        self.tolerance = tolerance
        self.iter = iter

    def Cluster(self):
        dataSet = np.array(pd.read_csv('dataSet.csv'))
        dataSet = list(dataSet)
        random_centroid = random.sample(dataSet, self.k)
        # Read data and create random centroids

        iteration = 0
        previous_evaluation = 0

        while iteration < self.iter:
            all_candidates = []
            evaluation = 0

            for i in range(self.k):
                all_candidates.append([])

            for item in dataSet:
                for i in range(self.k):
                    current_candidate = item
                    if iteration == 0:
                        centroid = random_centroid[i]
                    else:
                        centroid = new_centroid[i]
                    current_distance = np.sqrt(np.sum(np.square(current_candidate - centroid)))
                    # Calculate the distance between current candidate and current centroid
                    evaluation += current_distance
                    # Total distance
                    if i == 0:
                        judgement = current_distance
                        group_number = i
                    elif judgement > current_distance:
                        judgement = current_distance
                        group_number = i
                    else:
                        continue

                for i in range(self.k):
                    if group_number == i:
                        all_candidates[i].append(current_candidate)
                        # Classify all candidates into different groups
                    else:
                        continue

            new_centroid = []
            for i in range(self.k):
                current_centroid = np.mean(all_candidates[i], axis=0)
                new_centroid.append(current_centroid)
                # Calculate new centroids

            if abs(evaluation - previous_evaluation) < self.tolerance:
                break
                # If the difference of total difference between two iterations is less than tolerance then stop
            else:
                previous_evaluation = evaluation

            iteration += 1
        return new_centroid

example = k_means(4, 0.0000001, 20000000)
final_result = example.Cluster()
print(final_result)