import tensorflow as tf
import tensorflow_datasets as tfds

(train_data, test_data), ds_info = tfds.load(
    'emnist/bymerge',
    split=['train', 'test'],
    shuffle_files=True,
    as_supervised=True,
    with_info=True,
)

def normalize_img(image, label):
    """Normalizes images: `uint8` -> `float32`."""
    return tf.cast(image, tf.float32) / 255., label

train_data = train_data.map(normalize_img)
test_data = test_data.map(normalize_img)

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28, 1)),
  tf.keras.layers.Dense(128,activation='relu'),
  tf.keras.layers.Dense(62, activation='softmax')
])
model.compile(
    loss='sparse_categorical_crossentropy',
    optimizer=tf.keras.optimizers.Adam(0.001),
    metrics=['accuracy'],
)
model.fit(
    train_data.batch(128),
    epochs=6,
    validation_data=test_data.batch(128),
)