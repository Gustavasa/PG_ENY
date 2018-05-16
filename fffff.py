size = 200
vocab_size = 10000
layers = 2
 # input_.input_data is a 2D tensor [batch_size, num_steps] of
 #    word ids, from 1 to 10000

cell = tf.contrib.rnn.MultiRNNCell(
    [tf.contrib.rnn.BasicLSTMCell(size) for _ in range(2)]
    )

embedding = tf.get_variable(
      "embedding", [vocab_size, size], dtype=tf.float32)
inputs = tf.nn.embedding_lookup(embedding, input_.input_data)

inputs = tf.unstack(inputs, num=num_steps, axis=1)
outputs, state = tf.contrib.rnn.static_rnn(
    cell, inputs, initial_state=self._initial_state)

output = tf.reshape(tf.stack(axis=1, values=outputs), [-1, size])
softmax_w = tf.get_variable(
    "softmax_w", [size, vocab_size], dtype=data_type())
softmax_b = tf.get_variable("softmax_b", [vocab_size], dtype=data_type())
logits = tf.matmul(output, softmax_w) + softmax_b

# Then calculate loss, do gradient descent, etc.
