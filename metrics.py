
def accuracy(y_true, y_pred):
    correct = 0
    for a, b in zip(y_true, y_pred):
        if a == b:
            correct += 1
    return correct / len(y_true)


def precision(y_true, y_pred):
    true_positive = 0
    predicted_positive = 0

    for a, b in zip(y_true, y_pred):
        if b == 1:
            predicted_positive += 1
            if a == 1:
                true_positive += 1

    if predicted_positive == 0:
        return 0

    return true_positive / predicted_positive


def recall(y_true, y_pred):
    true_positive = 0
    actual_positive = 0

    for a, b in zip(y_true, y_pred):
        if a == 1:
            actual_positive += 1
            if b == 1:
                true_positive += 1

    if actual_positive == 0:
        return 0

    return true_positive / actual_positive
