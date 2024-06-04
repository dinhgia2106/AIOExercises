def classification_model_f1score():
    values = {}
    for var in ['tp', 'fp', 'fn']:
        try:            
            values[var] = int(input(f"{var} = "))
            
            if values[var] <= 0:
                raise ValueError
        except ValueError:
            print(f"{var} must be a positive integer")
            return

    tp = values['tp']
    fp = values['fp']
    fn = values['fn']

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)

    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1-score: {f1_score:.2f}")

if __name__ == "__main__":
    classification_model_f1score()