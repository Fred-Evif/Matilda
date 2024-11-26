Installation
========================================

Matilda is developed using PyTorch 1.9.1 and requires >=1 GPU to run. We recommend using conda enviroment to install and run Matilda. Note the following installation code snippets were tested on a Ubuntu system (v20.04) with NVIDIA GeForce 3090 GPU. The installation process needs about 5 minutes.

We offer two kinds of installation, install by clonning the github repository & install via 'pip install' command. The implementing codes of Matilda would be slightly different between two kinds of installation. We have offered tutorials for both version in section 'Tutorials- :doc:`Intro` '. If you want to apply Matilda directly via any Python explainer on the scripts (via package import), especially the jupyter notebook. we recommand you to install via 'pip install' in your activated environment.

Environment setting
------------------------
We assume conda is installed. You can use the provided environment or install the environment by yourself accoring to your hardware settings. 

I: Create and activate the conda environment for matilda ::

   conda create -n environment_matilda python=3.7
   conda activate environment_matilda

II: If you have download the document "environment_matilda.yaml" from Github_, you could create and activate the conda environment with it 

.. _Github: https://github.com/PYangLab/Matilda/tree/main

::

   conda env create -f environment_matilda.yaml
   conda activate environment_matilda

Install Matilda via clonning/pip
----------------------------------

.. note:: 

   Remeber, the implementing codes is different from two kinds of installation. We recommand 'pip' If you want to directly apply Matilda via any Python explainer on the scripts (via package import).

I: Otain Matilda by clonning the github repository: ::

   git clone https://github.com/liuchunlei0430/Matilda.git


II: Install Matilda directly via Command Prompt in your activated environment with the following codes: ::

   pip install matilda-sc


Install required packages
--------------------------
The following python packages are required for running Matilda: h5py, numpy, pandas, captum. They can be installed in the conda environment as below: ::

   pip install h5py
   pip install numpy
   pip install pandas
   pip install captum
   pip install tqdm
   pip install scipy
   pip install scanpy


Check your GPU and Install correct Pytorch
-------------------------------------------
Step 1:
Check the environment including GPU settings and the highest CUDA version allowed by the GPU.::
   nvidia-smi

Step 2:
Install pytorch and cuda version based on your GPU settings. ::

   # Example code for installing CUDA 11.3
   conda install pytorch==1.9.1 torchvision==0.10.1 torchaudio==0.9.1 cudatoolkit=11.3 -c pytorch -c conda-forge



