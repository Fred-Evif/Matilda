Installation
========================================

Matilda is developed using PyTorch 1.9.1 and requires >=1 GPU to run. We recommend using conda enviroment to install and run Matilda. Note the following installation code snippets were tested on a Ubuntu system (v20.04) with NVIDIA GeForce 3090 GPU. The installation process needs about 5 minutes.

Install via conda
------------------
We assume conda is installed. You can use the provided environment or install the environment by yourself accoring to your hardware settings. 

I: Installation using provided environment
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

Step 1: Create and activate the conda environment for matilda using our provided file ::

   conda env create -f environment_matilda.yaml
   conda activate environment_matilda

Step 2:
Otain Matilda by clonning the github repository: ::

   git clone https://github.com/liuchunlei0430/Matilda.git


II: Installation by youself
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

Step 1:
Create and activate the conda environment for matilda ::

   conda create -n environment_matilda python=3.7
   conda activate environment_matilda

Step 2:
Otain Matilda by clonning the github repository: ::

   git clone https://github.com/liuchunlei0430/Matilda.git


Install via pip 
-----------------
Install Matilda directly via Command Prompt in your activated environment with the following codes: ::

   pip install Matilda


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



