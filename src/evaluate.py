import tensorflow as tf

data_dir = '../data/raw/PetImages'
report_path = '../output/report-5.txt'
model_path = '../models/my_model'


def evaluate():
    _, val_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir,
        validation_split=0.2,
        subset="both",
        seed=1337,
        image_size=(180, 180),
        batch_size=10,
    )
    model = tf.keras.models.load_model(model_path)
    metrics = [
        tf.metrics.BinaryAccuracy(),
        tf.metrics.Precision(),
        tf.metrics.Recall()
    ]
    model.compile(metrics=metrics)
    result = model.evaluate(val_ds)
    _, acc, precision, recall = result

    result_lines = [
        f'Test data len: {len(val_ds)}\n'
        f'Accuracy: {acc:.3f}, Precision: {precision:.3f}, Recall: {recall:.3f}'
    ]
    with open(report_path, 'w', encoding='utf-8') as f:
        f.writelines(result_lines)


if __name__ == '__main__':
    evaluate()
