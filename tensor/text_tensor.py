import tensorflow as tf
import tensorflow_datasets as tfds

(train_data, test_data), ds_info = tfds.load(
    'emnist/bymerge',
    split=['train', 'test'],
    shuffle_files=True,
    as_supervised=True,
    with_info=True,
)
