import copy
import json

from hw5.mingfei.utils.documents import dot


class PerceptronClassifier:
    def __init__(self, weights):
        # string to int                                         1
        self.weights = weights

    @classmethod
    def from_file(cls, filename):
        """
        Load model file and construct PerceptronClassifier.
        """
        # TODO: Open and read form file at "filename"
        with open(filename) as modelfile:
            weights = json.load(modelfile)
        return cls(weights)

    @classmethod
    def from_dataset(cls, dataset):  # TODO  check data.py in utils   dataset(instanz_list,feature_set)
        """
        Initialize PerceptronClassifier for dataset. A classifier that
        is constructed with this method still needs to be trained..
        """
        weights = {word : 0 for word in dataset.feature_set}
        return cls(weights)  # TODO: Exercise 1

    def prediction(self, counts):  # TODO
        """
        Return True if prediction for counts is ham, False if prediction is spam
        counts: Bag of words representation of email
        representation : {words, freq}
        """
        score = 0
        for word, freq in counts.items():
            score = self.weights[word]*freq + score

        if score > 0:
            return 1
        else:
            return -1  # TODO: Exercise 2

    def update(self, instance):  # TODO
        """
        Perform perceptron update, if the wrong label is predicted.
        Return a boolean value indicating whether an update was performed.
        """

        """
        Error Falls:
        1. Spam-> Ham  (-1->1) gespeichert
        2. Ham -> Spam  (1->-1) gespeichert
        Kein Error, neutral(0) speichern
        """
        predicted_output = self.prediction(instance.feature_counts)  #DataInstance.feature_counts
        actual_label = instance.label
        if predicted_output == actual_label:
            error = 0  # TODO: Exercise 3: Replace with correct calculation of error
        elif predicted_output == -1:
            error = 1
        elif predicted_output == 1:
            error = -1

        do_update = error != 0
        if do_update:
            for feature, count in instance.feature_counts.items():
                #pass # TODO: Exercise 3: Replace pass with update of feature weights
                self.weights[feature] = self.weights[feature] + error * count
        return do_update

    def training_iteration(self, dataset):
        """
        Iterate over each instance of dataset and perform perceptron update.
        Return number of updates that were performed (number of train errors).
        """
        dataset.shuffle()
        for instance in dataset.instance_list:
            self.update(instance)

    def train(self, training_set, development_set, iterations):
        """
        Train classifier and return best development accuracy.
        """
        best_dev_accuracy = 0.0
        best_weights = self.weights
        for i in range(iterations):
            self.training_iteration(training_set)
            train_accuracy = self.test_accuracy(training_set)
            development_accuracy = self.test_accuracy(development_set)
            if development_accuracy > best_dev_accuracy:
                best_dev_accuracy = development_accuracy
                best_weights = self.weights.copy()
            print("Iteration: %d \t Train Accuracy: %.4f \t Dev Accuracy: %.4f \t Best Dev Accuracy: %.4f" % (
                i, train_accuracy, development_accuracy, best_dev_accuracy))
        self.weights = best_weights
        return best_dev_accuracy

    def test_accuracy(self, dataset):
        """
        Caclculate accuracy of classifier on labelled dataset.
        """
        num_errors = 0
        for instance in dataset.instance_list:
            if self.prediction(instance.feature_counts) != instance.label:
                num_errors += 1
        return 1 - num_errors / len(dataset.instance_list)

    def copy(self):
        """
        Return a copy of weights.
        """
        return PerceptronClassifier(copy.copy(self.weights))

    def features_for_class(self, is_positive_class, topn=10):
        """
        Determine the topn best features for a label (True or False).
        is_positive_class: can be True or False
        """
        high_to_low = True if is_positive_class else False
        return sorted(self.weights.items(), key=lambda x: x[1], reverse=high_to_low)[:topn]

    def save(self, filename):
        """
        Save model weights as JSON file.
        """
        with open(filename, 'w') as modelfile:
            json.dump(self.weights, modelfile)
