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

+ **Latent space**: 

+ **Label smoothing**: 

+ **Multi-modal/Multi-modality**: The multi-modality refers to multiple different types of data that usually are analysed individually. They could be handled in parallel with multi-task learning. Here refers to distinct sequening data.

+ **Multi-task Learning**: It is a subfield of machine learning which intends to handle multiple task in parallel, and exploring the relative information across the tasks. The revealed relative information would also be shared to each single task for better performance.

+ **Regularizatioin**: It is a process that changes the result answer to be "simpler". It is often used to obtain results for ill-posed problems or to prevent overfitting - where a model memorizes training data details but can't generalize to new data—and underfitting [3].

+ **Reparameterization**:

+ **Variational autoencoder (VAE)**:

Reference
--------------
[1] S. Santurkar, D. Tsipras, A. Ilyas, and A. Madry, “How does batch normalization help optimization?,” Advances in neural information processing systems, vol. 31, 2018.

[2] N. Srivastava, “Improving neural networks with dropout,” University of Toronto, vol. 182, no. 566, p. 7, 2013.

[3]  Bühlmann, Peter; Van De Geer, Sara (2011). Statistics for High-Dimensional Data. Springer Series in Statistics. p. 9. doi:10.1007/978-3-642-20192-9. ISBN 978-3-642-20191-2.

[4]

[5]

[6]


