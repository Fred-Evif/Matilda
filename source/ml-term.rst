Machine Learning Terms Explanation
====================================

+ **Batch normalization**: It is a popular strategy applied to neural networks, for solving the problem of internal covariate shift (ICS) which refers to the phenomena that changes the changing distributions of layers’ input during the updating of previous layers. It would lead to an unstable gradient descent and lower training as the instability [1]. Therefore, batch normalisation is implemented before each activation layer to normalise the distribution, which improves the training efficiency.

+ **Data augmentation**: Here refers to the process of synthetically creating new data for minority based on the original data for training models, in order to offset the impacts of imbalance in data.

+ **Data simulation**: The process that simulating original data and produce new samples. Here is applied for data augmentation, achieved via VAE.

+ **Dimension reduction**: Reducing the dimension of data for efficient calculation and task implementation. 

+ **Dropout**: Dropout is a common approach to avoid model overfitting, which through randomly disables fractions of neurons with a probability commonly named as ‘p’ for short [2]. 

+ **Feature Selection**:

+ **Fully connected neural network**:

+ **Gradient Descent**:

+ **Latent space**:

+ **Label smoothing**:

+ **Multi-modal/Multi-modality**: The multi-modality refers to multiple different types of data that usually are analysed individually. They could be handled in parallel with multi-task learning. Here refers to distinct sequening data.

+ **Multi-task Learning**: It is a subfield of machine learning which intends to handle multiple task in parallel, and exploring the relative information across the tasks. The revealed relative information would also be shared to each single task for better performance.

+ **Regularizatioin**:

+ **Reparameterization**:

+ **Variational autoencoder (VAE)**:

Reference
--------------
[1] S. Santurkar, D. Tsipras, A. Ilyas, and A. Madry, “How does batch normalization help optimization?,” Advances in neural information processing systems, vol. 31, 2018.

[2] N. Srivastava, “Improving neural networks with dropout,” University of Toronto, vol. 182, no. 566, p. 7, 2013.

[3]

[4]

[5]

[6]

[7]

[8]

