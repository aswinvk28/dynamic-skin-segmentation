# Image segmentation and Optical Flow

```bash

python execute.py --image concert.jpg && python calculate_optical_flow.py --image concert.jpg && python execute.py --image group.jpg && python calculate_optical_flow.py --image group.jpg && python execute.py --image trooper.jpg && python calculate_optical_flow.py --image trooper.jpg && python deterministic_stochastic.py --det_coeff 0.6 --stoc_coeff 0.4

```

**Image Segmentation as a deterministic problem and Optical Flow as a stochastic problem**

Image Segmentation
------------------

**Segmentation of Image using Region Growing (Erosion/Dilation), and using OpenCV.**

![./images/concert.jpg](./images/concert.jpg)

![./images/group.jpg](./images/group.jpg)

![./images/trooper.jpg](./images/trooper.jpg)

Optical Flow
------------

**Calculating Optical Flow Derivatives of the Images given**

![./output/concert.jpg](./output/concert.jpg)

![./output/group.jpg](./output/group.jpg)

![./output/trooper.jpg](./output/trooper.jpg)

Final Image after Interpolation
-------------------------------

**Final Interpolated Image from Optical Flow Model and Image Segmentation Model in OpenCV**

![./net/concert.jpg](./net/concert.jpg)

![./net/group.jpg](./net/group.jpg)

![./net/trooper.jpg](./net/trooper.jpg)

Original Images
---------------

**These are the original images from which models were run**

![./concert.jpg](./concert.jpg)

![./group.jpg](./group.jpg)

![./trooper.jpg](./trooper.jpg)
