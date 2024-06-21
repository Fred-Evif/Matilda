Machine Learning Terms Explanation
====================================

+ **Batch normalization**: It is a popular strategy applied to neural networks, for solving the problem of internal covariate shift (ICS) which refers to the phenomena that changes the changing distributions of layers’ input during the updating of previous layers. It would lead to an unstable gradient descent and lower training as the instability [1]. Therefore, batch normalisation is implemented before each activation layer to normalise the distribution, which improves the training efficiency.

+ **Data augmentation**: Here refers to the process of synthetically creating new data for minority based on the original data for training models, in order to offset the impacts of imbalance in data.

+ **Data simulation**: The process that simulating original data and produce new samples. Here is applied for data augmentation, achieved via VAE.

+ **Dimension reduction**: Reducing the dimension of data for efficient calculation and task implementation. 

+ **Dropout**: Dropout is a common approach to avoid model overfitting, which through randomly disables fractions of neurons with a probability commonly named as ‘p’ for short [2]. 

+ **Feature Selection**: Not all the features in data are significant. To improve the efficiency, selecting key features is important. It is usually the key to dimension reduction.

+ **Fully connected neural network**: It is the most basic learning structures in deep learning, which inspired by the thingking process of huamans. It is usually the basic components of deep learning models.

+ **Gradient Descent**: Here refers to the iterative principle of the parameters adapting in deep learning network. It is the key to models' learning (optimisation).

+ **Latent space**: also known as a latent feature space or embedding space, is an embedding of a set of items within a manifold in which items resembling each other are positioned closer to one another. Position within the latent space can be viewed as being defined by a set of latent variables that emerge from the resemblances from the objects [3].

+ **Label smoothing**: It could also be considered as a regularization method which prevents over-fitting and imporves generalization. It refers to the process that transform the hard labels into softer labels. For example, transforming the classes from one-hot into probabilities produced by softmax function. 

+ **Multi-modal/Multi-modality**: The multi-modality refers to multiple different types of data that usually are analysed individually. They could be handled in parallel with multi-task learning. Here refers to distinct sequening data.

+ **Multi-task Learning**: It is a subfield of machine learning which intends to handle multiple task in parallel, and exploring the relative information across the tasks. The revealed relative information would also be shared to each single task for better performance.

+ **Regularizatioin**: It is a process that changes the result answer to be "simpler". It is often used to obtain results for ill-posed problems or to prevent overfitting - where a model memorizes training data details but can't generalize to new data—and underfitting [4].

+ **Reparameterization**: In VAE, when we try to optimize the parameters with gradient descent method, due to the randomness of the sampling operation, we cannot directly take its derivative. The reparameterization technique solves this problem by transforming the random sampling process into deterministic operations (via typical differentiable objection). 

+ **Variational autoencoder (VAE)**:  It is part of the families of probabilistic graphical models and variational Bayesian methods. It can be studied within the mathematical formulation of variational Bayesian methods, connecting a neural encoder network to its decoder through a probabilistic latent space that corresponds to the parameters of a variational distribution [5]. Its encoder maps each point (such as an image) from a large complex dataset into a distribution within the latent space, rather than to a single point in that space. Its decoder is to map from the latent space to the input space, again according to a distribution [6].

Reference
--------------
[1] S. Santurkar, D. Tsipras, A. Ilyas, and A. Madry, “How does batch normalization help optimization?,” Advances in neural information processing systems, vol. 31, 2018.

[2] N. Srivastava, “Improving neural networks with dropout,” University of Toronto, vol. 182, no. 566, p. 7, 2013.

[3] Latent Space, Wikipedia, https://en.wikipedia.org/wiki/Latent_space

[4] Bühlmann, Peter; Van De Geer, Sara (2011). Statistics for High-Dimensional Data. Springer Series in Statistics. p. 9. doi:10.1007/978-3-642-20192-9. ISBN 978-3-642-20191-2.

[5] Pinheiro Cinelli, Lucas; et al. (2021). "Variational Autoencoder". Variational Methods for Machine Learning with Applications to Deep Networks. Springer. pp. 111–149. doi:10.1007/978-3-030-70679-1_5. ISBN 978-3-030-70681-4. S2CID 240802776.

[6] Variational encoder, Wikipedia, https://en.wikipedia.org/wiki/Variational_autoencoder


