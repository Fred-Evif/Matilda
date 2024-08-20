Hyperparameter Tuning
========================

In this part, we go through the basic steps for tuning the hyperparameters of  Matilda. It is an example with specified dataset. The commands below would need to be run in settled conda environment, which could be referred to the :doc:`installation` part.

Before Tuning the hyperparameter, the data should be appropriately prepared and loaded. The process could be referred to the corresponding parts in :doc:`Intro`.

Tunable hyperparameters
-------------------------------------------------------
could be viewed in the sections of :doc:`Guide`.

+----------------+-------------+------+--------------------------------------------------------+
| Tunable        | Default     | Input|      Basic                                             |
| hyperparameter | value       | type |      meaning                                           |
+================+=============+======+========================================================+
| batch_size     | 64          | int  | Batch size for learning                                |
+----------------+-------------+------+--------------------------------------------------------+
| epochs         | 30          | int  | Training epoches                                       |
+----------------+-------------+------+--------------------------------------------------------+
| hidden_rna     | 185         | int  | The number of neurons for RNA layer                    |
+----------------+-------------+------+--------------------------------------------------------+
| hidden_adt     | 30          | int  | The number of neurons for ADT layer                    |
+----------------+-------------+------+--------------------------------------------------------+
| hidden_atac    | 185         | int  | The number of neurons for ATAC layer                   |
+----------------+-------------+------+--------------------------------------------------------+
| lr             | 0.02        |float | Learning rate for optimisation                         |
+----------------+-------------+------+--------------------------------------------------------+
| simulation_num | 100         | int  | The number of cells to simulate for the specified cell |
|                |             |      | type. Only be activated when `simulation = True`.      |
+----------------+-------------+------+--------------------------------------------------------+
| z_dim          | 100         | int  | Dimension of latent space                              |
+----------------+-------------+------+--------------------------------------------------------+

Functional hyperparameters
-------------------------------------------------------
These hyperparameters are typically the switches of corresponding funtion/process. They are all Bool type.

+----------------+-------------+--------------------------------------------------------+
| Functional     | Default     |      Controlling                                       |
| hyperparameter | value       |      Function/process                                  |
+================+=============+========================================================+
| dim_reduce     | False       | Dimension reduction                                    |
+----------------+-------------+--------------------------------------------------------+
| fs             | False       | Feature selection                                      |
+----------------+-------------+--------------------------------------------------------+
| simulation     | False       | Data simulation                                        |
+----------------+-------------+--------------------------------------------------------+
| query          | False       | The number of neurons for ADT layer                    |
+----------------+-------------+--------------------------------------------------------+
| hidden_atac    | 185         | The number of neurons for ATAC layer                   |
+----------------+-------------+--------------------------------------------------------+
| lr             | 0.02        | Learning rate for optimisation                         |
+----------------+-------------+--------------------------------------------------------+
| simulation_num | 100         | The number of cells to simulate for the specified cell |
|                |             | type. Only be activated when `simulation = True`.      |
+----------------+-------------+--------------------------------------------------------+
| z_dim          | 100         | Dimension of latent space                              |
+----------------+-------------+--------------------------------------------------------+



Tuning strategies and methods
-------------------------------------------------------
You could use the validation set for performance evaluation during tuning. If the size of dataset is larger, the classic Grid Search might take a long time to find out the optimized solution since it needs to be set manually. Bayesian optimisation could be a relatively efficient method without manual operation. If you have enough prior information for datasets or models' expectation, it would be better. The metrics or benchmarks might need to be customised for multimodal sequencing data analysis for different process, such as the correlation visualisation for feature selection process or overall accuracy for classification... 



