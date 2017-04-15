from keras.datasets import mnist
from utils import to_one_hot
from rnn_clf import RNNClassifier
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os, sys
import tensorflow as tf


def plot(log, dir='./log'):
    if not os.path.exists(dir):
        os.makedirs(dir)
    sns.set(style='white')
    plt.plot(log['loss'], label='train_loss')
    plt.plot(log['val_loss'], label='test_loss')
    plt.legend(loc='best')
    plt.savefig(os.path.join(dir, sys.argv[0][:-3]))
    print("Figure created !")


if __name__ == '__main__':
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    X_train /= 255.0
    X_test /= 255.0
    y_train = to_one_hot(y_train)
    y_test = to_one_hot(y_test)

    sess = tf.Session()
    clf = RNNClassifier(n_in=28, n_step=28, n_hidden=128, n_out=10, n_layer=2, sess=sess, stateful=False)
    log = clf.fit(X_train, y_train, n_epoch=10, en_exp_decay=True, keep_prob_tuple=(0.5,1.0),
                  val_data=(X_test,y_test))
    pred = clf.predict(X_test)
    tf.reset_default_graph()

    final_acc = np.equal(np.argmax(pred,1), np.argmax(y_test,1)).astype(float).mean()
    print("final testing accuracy: %.4f" % final_acc)

    plot(log)