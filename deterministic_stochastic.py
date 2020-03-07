import cv2
import argparse
from time import time
import numpy as np
import os
import sys

def parse_args():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-detc', '--det_coeff',
        help='deterministic_coefficient',
        type=float,
        default=False,
        required=True
    )
    parser.add_argument(
        '-stocc', '--stoc_coeff',
        help='stochastic_coefficient',
        type=float,
        default=False,
        required=True
    )
    parser.add_argument(
        '-in1', '--input1',
        help='input 1',
        type=str,
        default=False,
        required=True
    )
    parser.add_argument(
        '-in2', '--input2',
        help='input 2',
        type=str,
        default=False,
        required=True
    )
    parser.add_argument(
        '-in3', '--input3',
        help='input 3',
        type=str,
        default=False,
        required=True
    )

    return parser.parse_args()

if __name__ == "__main__":

    args = parse_args()

    images = ['concert.jpg', 'group.jpg', 'trooper.jpg']
    inputs = [args.input1, args.input2, args.input3]

    for ii,image in enumerate(images):
        opt_flow_img = cv2.imread("output/" + image)
        segmented_img = cv2.imread("images/" + image)
        segmented_img = cv2.resize(segmented_img,(320,240))
        total_img = ((args.stoc_coeff * opt_flow_img/opt_flow_img.max() + args.det_coeff * segmented_img/segmented_img.max())*255).astype(np.uint8)
        org = (10, 10)
        font = cv2.FONT_HERSHEY_SIMPLEX
        # fontScale 
        fontScale = 0.4
        # Blue color in BGR 
        color = (255, 0, 0)
        thickness = 1
        cv2.putText(total_img, inputs[ii], org, font,  
                   fontScale, color, thickness, cv2.LINE_AA)
        cv2.imwrite("net/" + image, total_img)