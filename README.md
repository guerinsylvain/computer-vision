# Some useful computer vision resources  
## Long term objective is to build a tool to detect personalities in videos  
![](https://github.com/guerinsylvain/computer-vision/blob/master/readme01.JPG)  

[References](#references)  
[Setup](#setup)  
&nbsp;&nbsp;&nbsp;[Get the sources](#get-sources)  
&nbsp;&nbsp;&nbsp;[Install Visual C++ Tools for Cmake](#setup-vstools)  
&nbsp;&nbsp;&nbsp;[Install the CUDA Toolkit 10.1](#setup-cudatoolkit)  
&nbsp;&nbsp;&nbsp;[Install the NVIDIA CUDA Deep Neural Network library (cuDNN v7.6.5 (November 5th, 2019), for CUDA 10.1)](#setup-cudnn)  
&nbsp;&nbsp;&nbsp;[Install and configure Python](#setup-python)  

<a id="references"></a>
## References
Here are some references that helped me to build this experiment:
* [Hands-On Computer Vision with TensorFlow 2: Leverage deep learning to create powerful image processing apps with TensorFlow 2.0 and Keras](https://www.amazon.fr/Hands-Computer-Vision-TensorFlow-processing/dp/1788830644) by Benjamin Planche and Eliot Andres   
* [YoloV3 Implemented in TensorFlow 2.0](https://github.com/zzh8829/yolov3-tf2) by Zihao Zhang  
* [Face Recognition](https://github.com/ageitgey/face_recognition) 

<a id="setup"></a>
## Setup
<a id="get-sources"></a>
### Get the sources
You may
* clone this github repository 
* or download a zip containing the latest version or a given release of the code
<a id="setup-vstools"></a>
### Install Visual C++ Tools for Cmake
1. Install Visual Studio build tools from [here](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community&rel=15#).  
2. In Visual Studio 2017 go to the Individual Components tab, Visual C++ Tools for Cmake, and check the checkbox under the "Compilers, build tools and runtimes" section.
<a id="setup-cudatoolkit"></a>
### Install the CUDA Toolkit 10.1
1. Please install from the following [link](https://developer.nvidia.com/cuda-10.1-download-archive-update2)  
Note that you can uncheck "Install Visual Studio Extensions" in the options.
<a id="setup-cudnn"></a>
### Install the [NVIDIA CUDA Deep Neural Network library (cuDNN v7.6.5 (November 5th, 2019), for CUDA 10.1)](https://developer.nvidia.com/cudnn)
1. Follow the instructions detailed [here](https://docs.nvidia.com/deeplearning/sdk/cudnn-install/)  
Make sure to install the version  v7.6.5 (November 5th, 2019), for CUDA 10.1
<a id="setup-python"></a>
### Install and configure Python 
1.  Install [Python 3.7 or later](https://www.python.org/downloads/).
2.	From the root folder of the project, type 
    ```
    pip install virtualenv
    ```
3.	Then type
    ```
    virtualenv --python="C:\Users\[YOUR USER NAME]\AppData\Local\Programs\Python\Python37\python.exe" venv      
    ```
    This will create a venv subfolder.   
    Note that the path to the python.exe (v3.7) may vary on your machine.
    If python has been installed with visual studio, you may have something similar to this:
    ```
    virtualenv --python="C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\python.exe" venv
    ```
4.	From the root folder of the project, activate the virtual environment by typing:
    ```
    .\venv\Scripts\activate.bat
    ```
5. Install packages:
    ```
    pip install -r requirements.txt   
    ```
