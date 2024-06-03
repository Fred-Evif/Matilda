Introduction to the Matilda (Designment)
======================================================

In this introductory tutorial, we go through the different parts of Matilda's designment.


.. image:: main.jpg
   :alt: The framework of Matilda
   :scale: 25%
   :align: center

Multi-task learning architecture
--------------------------------------
The multi-task neural networks in Matilda consist of multimodality-specific en coders and decoders in a variational autoencoder (VAE) componentfordatasimulationandafully-connectedclassi f ication network for cell type classification. The encoders in the VAEcomponent are shareable for both data simulation and classification tasks, and consist of one learnable point wise parameter layer and one fully-connected layer to the input layer. Because ADT modality has significantly fewer features than RNA and ATAC modalities, we set empiri cally, based on model selection, the numbers of neurons for encoders of RNA, ADT, and ATAC modalities to be 185, 30, and 185, respectively. To learn a latent space that inte grates the information from across modalities, we concate nated the output from the encoder trained from each data modality to perform joint learning using a fully-connected layer with 100 neurons, followed by a VAE reparameteri zation process (11). Next, the fully-connected layer of the latent space is split into two branches with one branch fed into the decoders and the other branch fed into the fully connectedclassification network.Forthedecoderbranch,it consists of multiple decoders each corresponds to an input datamodality.Eachdecoderconsistsofonefully-connected layer to the output layer that has the same number of neu rons as the features in the corresponding data modality. For each fully-connected layer in the VAE component, batch normalization (18), shortcut (19) were utilized in the model. ReLU activation was used in all fully-connected layers ex cept in the reparameterization process. Dropout (r = 0.2) was utilized only for fully-connected layers in encoders. For the classification branch, it consists of the latent space as input to a fully-connected layer with a dimension equal to the number of cell types in the training data. The fully connected layer outputs a probability vector for cell type prediction through a SoftMax function.

Loss function 
------------------
Let X be the single-cell multimodal omic data from N modalities, the VAE component of Matilda contains two procedures: (i) the encoders encode each modality in the data X individually, and concatenate them for joint learning. This process projected the high dimensional X into a low-dimensional latent space. We de note the posterior distribution of this process as qθ(z|X), where θ is the learnable parameter of the neural network in this procedure; (ii) the decoders reconstruct the low dimensional latent space to the high-dimensional original data space. We denotethe posterior distribution of this pro cess as pϕ(X|z), where ϕ is the learnable parameter of the neural network in this procedure. The loss function of the data simulation component can be represented as the nega tive log-likelihood with a regularizer:



The first term is the reconstruction loss using the expec tation of negative log-likelihood. This term encourages the decoder to learn to reconstruct the original data Xusingthe low-dimensional representation z. The second term is the Kullback-Leibler (KL) divergence between the encoder’s distribution qθ(z|X)andp(z), where p(z) is specified as a standard Normal distribution as p(z) ∼ N(0,1). This divergence measures the information loss when using qθ(z|X) to represent p(z). The encoder network parameters are in turn optimized using stochastic gradient descent via back propagation, which is made possible by the reparameteriza tion trick (11).
For the loss function of the classification component, we use cross-entropy loss with label smoothing (20). Label smoothing is a regularizer technique, which replaces one hot real label vector yreal with a mixture of yreal and the uniform distribution:



where K is the number of label classes, and α is a hyperpa rameter that determines the amount of smoothing. Then, the classification loss can be represented as:



where yi output is the predicted label for the ith cell. To learn Matilda, we combined the simulation loss and classification loss to give the following overall loss function:



where λ is a weighting coefficient that determines the importance of the classification term against the data simulation term from Matilda.
Data augmentation and balancing strategy. During the model training process, Matilda performs data augmentation and balancing using simulated data from the VAE component. Specifically, Matilda first ranks the cell types in the training dataset by the number of cells in each type. The cell type corresponding to the median number is used as the reference and those that have smaller numbers of cells are augmented to have the same number of cells as the me dian using VAE simulated single-cell multimodal data for each cell type. Cell types that have larger numbers of cells than the median number are randomly down-sampled to match the median number of cells as well. This strategy helps Matilda to mitigate imbalanced cell type distribution in the data (21) and better learn the molecular features of under-represented and rare cell types.

Joint feature selection from multiple modalities 
------------------------------------------------------
Leveraging its neural network architecture, Matilda implements two approaches, i.e. integrated gradient (IG) (22) descent and saliency (23) based procedures, to detect the most informative features simultaneously from each of all data modalities. Specifically, for the IG method, to assess the importance of each feature, the trained model was used for back propagation of the partial derivatives from the output units of the classification network to the input units of the encoders, where each input unit represents an individual feature from a given modality in the input data X. The importance score of each input feature of each cell is determined by approximating the integral gradients of the model’s output to its input:








