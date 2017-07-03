![ucl-logo](http://static.ucl.ac.uk/img/ucl-logo.svg)

## Contents
* [机器学习](https://github.com/zhedongzheng/finch/blob/master/README-CH.md#机器学习)
    * [线性模型](https://github.com/zhedongzheng/finch/blob/master/README-CH.md#线性模型)
    * [支持向量机](https://github.com/zhedongzheng/finch/blob/master/README-CH.md#支持向量机)
    * [集成](https://github.com/zhedongzheng/finch/blob/master/README-CH.md#集成)
    * [分解](https://github.com/zhedongzheng/finch/blob/master/README-CH.md#分解)
* [深度学习](https://github.com/zhedongzheng/finch/blob/master/README-CH.md#深度学习)
    * [多层感知](https://github.com/zhedongzheng/finch/blob/master/README-CH.md#多层感知)
    * [卷积网络](https://github.com/zhedongzheng/finch/blob/master/README-CH.md#卷积网络)
    * [循环网络](https://github.com/zhedongzheng/finch/blob/master/README-CH.md#循环网络)
    * [自动解码](https://github.com/zhedongzheng/finch/blob/master/README-CH.md#自动解码)
    * [高速公路网络](https://github.com/zhedongzheng/finch/blob/master/README-CH.md#高速公路网络)
    * [生成对抗网络](https://github.com/zhedongzheng/finch/blob/master/README-CH.md#生成对抗网络)
* [自然语言处理](https://github.com/zhedongzheng/finch/blob/master/README-CH.md#自然语言处理)
    * [预处理](https://github.com/zhedongzheng/finch/blob/master/README-CH.md#预处理)
    * [语言模型](https://github.com/zhedongzheng/finch/blob/master/README-CH.md#语言模型)
    * [文本分类](https://github.com/zhedongzheng/finch/blob/master/README-CH.md#文本分类)
    * [文本生成](https://github.com/zhedongzheng/finch/blob/master/README-CH.md#文本生成)
    * [词性标记](https://github.com/zhedongzheng/finch/blob/master/README-CH.md#词性标记)
    * [分词](https://github.com/zhedongzheng/finch/blob/master/README-CH.md#分词)
* [计算机视觉](https://github.com/zhedongzheng/finch/blob/master/README-CH.md#计算机视觉)
    * [OpenCV](https://github.com/zhedongzheng/finch/blob/master/README-CH.md#opencv)

## 机器学习
#### 线性模型
* TensorFlow &nbsp; | &nbsp; 线性回归 &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/tensorflow-models/linear_model/linear_regr.py) &nbsp; &nbsp; [测试](https://github.com/zhedongzheng/finch/blob/master/tensorflow-models/linear_model/linear_regr_test.py) &nbsp; | &nbsp;

* TensorFlow &nbsp; | &nbsp; 逻辑回归 &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/tensorflow-models/linear_model/logistic.py) &nbsp; &nbsp; [测试](https://github.com/zhedongzheng/finch/blob/master/tensorflow-models/linear_model/logistic_test.py) &nbsp; | &nbsp;

* Java &nbsp; | &nbsp; 逻辑回归 &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/java-models/LogisticRegression.java) &nbsp; &nbsp; [测试](https://github.com/zhedongzheng/finch/blob/master/java-models/LogisticRegressionTest.java) &nbsp; | &nbsp;
#### 支持向量机
* TensorFlow &nbsp; | &nbsp; 线性 支持向量机 分类器 &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/tensorflow-models/svm/svm_linear_clf.py) &nbsp; &nbsp; [测试](https://github.com/zhedongzheng/finch/blob/master/tensorflow-models/svm/svm_linear_clf_test.py) &nbsp; | &nbsp;

* Java &nbsp; | &nbsp; 线性 支持向量机 分类器 &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/java-models/LinearSVM.java) &nbsp; &nbsp; [测试](https://github.com/zhedongzheng/finch/blob/master/java-models/LinearSVMTest.java) &nbsp; | &nbsp;

* Libsvm &nbsp; | &nbsp; 非线性 支持向量机 分类器 &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/classic-models/libsvm_clf.py) &nbsp; &nbsp; [测试](https://github.com/zhedongzheng/finch/blob/master/classic-models/libsvm_clf_test.py) &nbsp; | &nbsp;
#### 集成
* NumPy &nbsp; | &nbsp; Bagging 分类器 &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/classic-models/bagging_clf.py) &nbsp; &nbsp; [测试](https://github.com/zhedongzheng/finch/blob/master/classic-models/bagging_clf_test.py) &nbsp; | &nbsp;

* NumPy &nbsp; | &nbsp; Adaboost 分类器 &nbsp; &nbsp; [伪代码](https://github.com/zhedongzheng/finch/blob/master/classic-models/adaboost_clf.md) &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/classic-models/adaboost_clf.py) &nbsp; &nbsp; [测试](https://github.com/zhedongzheng/finch/blob/master/classic-models/adaboost_clf_test.py) &nbsp; | &nbsp;

* NumPy &nbsp; | &nbsp; 随机森林 分类器 &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/classic-models/random_forest_clf.py) &nbsp; &nbsp; [测试](https://github.com/zhedongzheng/finch/blob/master/classic-models/random_forest_clf_test.py) &nbsp; | &nbsp;
#### 分解
* TensorFlow &nbsp; | &nbsp; 非负矩阵分解 &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/tensorflow-models/decomposition/nmf.py) &nbsp; &nbsp; [MovieLens数据集测试](https://github.com/zhedongzheng/finch/blob/master/tensorflow-models/decomposition/nmf_movielens_test.py) &nbsp; | &nbsp;
## 深度学习
#### 多层感知
* TensorFlow &nbsp; | &nbsp; 多层感知 分类器 &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/tensorflow-models/mlp/mlp_clf.py) &nbsp; &nbsp; [MNIST数据集测试](https://github.com/zhedongzheng/finch/blob/master/tensorflow-models/mlp/mlp_clf_mnist_test.py) &nbsp; &nbsp; [CIFAR10数据集测试](https://github.com/zhedongzheng/finch/blob/master/tensorflow-models/mlp/mlp_clf_cifar10_test.py) &nbsp; | &nbsp;

* PyTorch &nbsp; | &nbsp; 多层感知 分类器 &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/pytorch-models/mlp/mlp_clf.py) &nbsp; &nbsp; [MNIST数据集测试](https://github.com/zhedongzheng/finch/blob/master/pytorch-models/mlp/mlp_clf_mnist_test.py) &nbsp; &nbsp; [CIFAR10数据集测试](https://github.com/zhedongzheng/finch/blob/master/pytorch-models/mlp/mlp_clf_cifar10_test.py) &nbsp; | &nbsp; 
#### 卷积网络
* TensorFlow &nbsp; | &nbsp; 二维卷积 分类器 &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/tensorflow-models/cnn/conv_2d_clf.py) &nbsp; &nbsp; [MNIST数据集测试](https://github.com/zhedongzheng/finch/blob/master/tensorflow-models/cnn/conv_2d_clf_mnist_test.py) &nbsp; &nbsp; [CIFAR10数据集测试](https://github.com/zhedongzheng/finch/blob/master/tensorflow-models/cnn/conv_2d_clf_cifar10_keras_idg_test.py) &nbsp; | &nbsp;

* PyTorch &nbsp; | &nbsp; 二维卷积 分类器 &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/pytorch-models/cnn/cnn_clf.py) &nbsp; &nbsp; [MNIST数据集测试](https://github.com/zhedongzheng/finch/blob/master/pytorch-models/cnn/cnn_clf_mnist_test.py) &nbsp; &nbsp; [CIFAR10数据集测试](https://github.com/zhedongzheng/finch/blob/master/pytorch-models/cnn/cnn_clf_cifar10_test.py) &nbsp; | &nbsp;
#### 循环网络
* TensorFlow &nbsp; | &nbsp; LSTM 分类器 &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/tensorflow-models/rnn/rnn_clf.py) &nbsp; &nbsp; [MNIST数据集测试](https://github.com/zhedongzheng/finch/blob/master/tensorflow-models/rnn/rnn_clf_mnist_test.py) &nbsp; &nbsp; [CIFAR10数据集测试](https://github.com/zhedongzheng/finch/blob/master/tensorflow-models/rnn/rnn_clf_cifar10_test.py) &nbsp; | &nbsp;

* TensorFlow &nbsp; | &nbsp; LSTM 回归器 &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/tensorflow-models/rnn/rnn_regr.py) &nbsp; &nbsp; [测试](https://github.com/zhedongzheng/finch/blob/master/tensorflow-models/rnn/rnn_regr_plot.py) &nbsp; &nbsp; [预览](https://github.com/zhedongzheng/finch/blob/master/assets/rnn_regr_plot.gif) &nbsp; | &nbsp;

* PyTorch &nbsp; | &nbsp; LSTM 分类器 &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/pytorch-models/rnn/rnn_clf.py) &nbsp; &nbsp; [MNIST数据集测试](https://github.com/zhedongzheng/finch/blob/master/pytorch-models/rnn/rnn_clf_mnist_test.py) &nbsp; &nbsp; [CIFAR10数据集测试](https://github.com/zhedongzheng/finch/blob/master/pytorch-models/rnn/rnn_clf_cifar10_test.py) &nbsp; | &nbsp;

* PyTorch &nbsp; | &nbsp; GRU 回归器 &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/pytorch-models/rnn/rnn_regr.py) &nbsp; &nbsp; [测试](https://github.com/zhedongzheng/finch/blob/master/pytorch-models/rnn/rnn_regr_plot.py) &nbsp; | &nbsp;

#### 自动解码
* TensorFlow &nbsp; | &nbsp; 多层感知 自动解码 &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/tensorflow-models/autoencoder/mlp_ae.py) &nbsp; | &nbsp; [MNIST数据集测试](https://github.com/zhedongzheng/finch/blob/master/tensorflow-models/autoencoder/mlp_ae_mnist_test.py) &nbsp; | &nbsp;

* TensorFlow &nbsp; | &nbsp; 二维卷积 自动解码 &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/tensorflow-models/autoencoder/conv_ae.py) &nbsp; &nbsp; [MNIST数据集测试](https://github.com/zhedongzheng/finch/blob/master/tensorflow-models/autoencoder/conv_ae_mnist_test.py) &nbsp; &nbsp; [CIFAR10数据集测试](https://github.com/zhedongzheng/finch/blob/master/tensorflow-models/autoencoder/conv_ae_cifar10_test.py) &nbsp; | &nbsp;
#### 高速公路网络
* TensorFlow &nbsp; | &nbsp; 基于高速公路的 多层感知 分类器 &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/tensorflow-models/highway/mlp_hn_clf.py) &nbsp; &nbsp; [MNIST数据集测试](https://github.com/zhedongzheng/finch/blob/master/tensorflow-models/highway/mlp_hn_clf_mnist_test.py) &nbsp; | &nbsp;

* TensorFlow &nbsp; | &nbsp; 基于高速公路的 一维卷积 分类器 &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/conv_1d_hn_text_clf.py) &nbsp; &nbsp; [IMDB数据集测试](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/conv_1d_hn_text_clf_imdb_test.py) &nbsp; | &nbsp;

#### 对抗生成网络
* TensorFlow &nbsp; | &nbsp; 基于多层感知的 对抗生成网络 &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/tensorflow-models/gan/mlp_gan.py) &nbsp; &nbsp; [测试](https://github.com/zhedongzheng/finch/blob/master/tensorflow-models/gan/mlp_gan_test.py) &nbsp; | &nbsp; 有条件限制的 对抗生成网络 &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/tensorflow-models/gan/mlp_cond_gan.py) &nbsp; &nbsp; [测试](https://github.com/zhedongzheng/finch/blob/master/tensorflow-models/gan/mlp_cond_gan_test.py) &nbsp; | &nbsp;

* TensorFlow &nbsp; | &nbsp; 基于卷积网络的 对抗生成网络 &nbsp; &nbsp; MNIST &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/tensorflow-models/gan/conv_gan_mnist.py) &nbsp; &nbsp; [测试](https://github.com/zhedongzheng/finch/blob/master/tensorflow-models/gan/conv_gan_mnist_test.py) &nbsp; | &nbsp;

## 自然语言处理
#### 预处理
* Python &nbsp; | &nbsp; [文本格式化](https://github.com/zhedongzheng/finch/blob/master/nlp-models/text-cleaning.ipynb)

* Python &nbsp; | &nbsp; [词语索引](https://github.com/zhedongzheng/finch/blob/master/nlp-models/word-indexing.ipynb)

#### 语言模型
* Sklearn &nbsp; | &nbsp; 隐含语义分析 &nbsp; &nbsp; [书名测试](https://github.com/zhedongzheng/finch/blob/master/nlp-models/python/lsa_test.py) &nbsp; | &nbsp;

* Python &nbsp; | &nbsp; 三元模型 &nbsp; &nbsp; [Amazon客户评价测试](https://github.com/zhedongzheng/finch/blob/master/nlp-models/python/trigram_test.py) &nbsp; | &nbsp;

* Sklearn &nbsp; | &nbsp; TF-IDF &nbsp; &nbsp; [Brown文集测试](https://github.com/zhedongzheng/finch/blob/master/nlp-models/python/tfidf_brown_test.py) &nbsp; | &nbsp;

* TensorFlow &nbsp; | &nbsp; Skip-Gram &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/word2vec_skipgram.py) &nbsp; &nbsp; [Text8文集测试](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/word2vec_skipgram_text8_test.py) &nbsp; | &nbsp;

#### 文本分类
* Sklearn &nbsp; | &nbsp; TF-IDF + 逻辑回归 &nbsp; &nbsp; [IMDB数据集测试](https://github.com/zhedongzheng/finch/blob/master/nlp-models/python/tfidf_imdb_test.py) &nbsp; | &nbsp;

* TensorFlow &nbsp; | &nbsp; 一维卷积 &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/conv_1d_text_clf.py) &nbsp; &nbsp; [IMDB数据集测试](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/conv_1d_text_clf_imdb_test.py) &nbsp; | &nbsp; 多通道 一维卷积 &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/concat_conv_1d_text_clf.py) &nbsp; &nbsp; [IMDB数据集测试](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/concat_conv_1d_text_clf_imdb_test.py) &nbsp; | &nbsp;

* TensorFlow &nbsp; | &nbsp; 循环网络 &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/rnn_text_clf.py) &nbsp; &nbsp; [IMDB数据集测试](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/rnn_text_clf_imdb_test.py) &nbsp; | &nbsp;

* TensorFlow &nbsp; | &nbsp; 一维卷积+循环网络 &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/conv_rnn_text_clf.py) &nbsp; &nbsp; [IMDB数据集测试](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/conv_rnn_text_clf_imdb_test.py) &nbsp; | &nbsp;

* PyTorch &nbsp; | &nbsp; 一维卷积 &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/nlp-models/pytorch/cnn_text_clf.py) &nbsp; &nbsp; [IMDB数据集测试](https://github.com/zhedongzheng/finch/blob/master/nlp-models/pytorch/cnn_text_clf_imdb_test.py) &nbsp; | &nbsp;

* PyTorch &nbsp; | &nbsp; 循环网络 &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/nlp-models/pytorch/rnn_text_clf.py) &nbsp; &nbsp; [IMDB数据集测试](https://github.com/zhedongzheng/finch/blob/master/nlp-models/pytorch/rnn_text_clf_imdb_test.py) &nbsp; | &nbsp;

* PyTorch &nbsp; | &nbsp; 一维卷积+循环网络 &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/nlp-models/pytorch/cnn_rnn_text_clf.py) &nbsp; &nbsp; [IMDB数据集测试](https://github.com/zhedongzheng/finch/blob/master/nlp-models/pytorch/cnn_rnn_text_clf_imdb_test.py) &nbsp; | &nbsp;

#### 文本生成
* Python &nbsp; | &nbsp; 二阶马尔可夫模型 &nbsp; &nbsp; [Robert Frost 文集测试](https://github.com/zhedongzheng/finch/blob/master/nlp-models/python/markov_text_gen.py) &nbsp; | &nbsp;

* TensorFlow &nbsp; | &nbsp; Char-LSTM &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/rnn_text_gen.py) &nbsp; &nbsp; [Anna Karenina 文集测试](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/rnn_text_gen_anna_test.py) &nbsp; | &nbsp;

#### 词性标记
* TensorFlow &nbsp; | &nbsp; 循环网络 &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/rnn_seq2seq_clf.py) &nbsp; &nbsp; [CoNLL-2000 数据集测试](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/pos_rnn_test.py) &nbsp; | &nbsp; 双向循环网络 &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/birnn_seq2seq_clf.py) &nbsp; &nbsp; [CoNLL-2000 数据集测试](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/pos_birnn_test.py) &nbsp; | &nbsp;

* PyTorch &nbsp; | &nbsp; 循环网络 &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/nlp-models/pytorch/rnn_seq_clf.py) &nbsp; &nbsp; [CoNLL-2000 数据集测试](https://github.com/zhedongzheng/finch/blob/master/nlp-models/pytorch/rnn_tagging_test.py) &nbsp; | &nbsp; 双向循环网络 &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/nlp-models/pytorch/birnn_seq_clf.py) &nbsp; &nbsp; [CoNLL-2000 数据集测试](https://github.com/zhedongzheng/finch/blob/master/nlp-models/pytorch/birnn_tagging_test.py) &nbsp; | &nbsp;

#### 分词
* TensorFlow &nbsp; | &nbsp; 循环网络 &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/rnn_seq2seq_clf.py) &nbsp; &nbsp; [ICWB2数据集测试](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/chseg_rnn_test.py) &nbsp; | &nbsp; 双向循环网络 &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/birnn_seq2seq_clf.py) &nbsp; &nbsp; [ICWB2数据集测试](https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/chseg_birnn_test.py) &nbsp; | &nbsp;

* PyTorch &nbsp; | &nbsp; 循环网络 &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/nlp-models/pytorch/rnn_seq_clf.py) &nbsp; &nbsp; [ICWB2数据集测试](https://github.com/zhedongzheng/finch/blob/master/nlp-models/pytorch/rnn_chseg_test.py) &nbsp; | &nbsp; 双向循环网络 &nbsp; &nbsp; [模型](https://github.com/zhedongzheng/finch/blob/master/nlp-models/pytorch/birnn_seq_clf.py) &nbsp; &nbsp; [ICWB2数据集测试](https://github.com/zhedongzheng/finch/blob/master/nlp-models/pytorch/birnn_chseg_test.py) &nbsp; | &nbsp;

## 计算机视觉
#### OpenCV
* 基本操作 &nbsp; | &nbsp; [调整大小](https://github.com/zhedongzheng/finch/blob/master/cv-models/resize.ipynb)

* 基本操作 &nbsp; | &nbsp; [旋转](https://github.com/zhedongzheng/finch/blob/master/cv-models/rotations.ipynb)

* 分割 &nbsp; | &nbsp; [轮廓](https://github.com/zhedongzheng/finch/blob/master/cv-models/contours.ipynb)

* 分割 &nbsp; | &nbsp; [轮廓排序](https://github.com/zhedongzheng/finch/blob/master/cv-models/sorting-contours.ipynb)

* 探测 &nbsp; | &nbsp; [Face & Eye Detection Using Cascade Classifier](https://github.com/zhedongzheng/finch/blob/master/cv-models/face-eye-detection.ipynb)

* 探测 &nbsp; | &nbsp; [Walker & Car Detection Using Cascade Classifier](https://github.com/zhedongzheng/finch/blob/master/cv-models/car-walker-detection.ipynb)