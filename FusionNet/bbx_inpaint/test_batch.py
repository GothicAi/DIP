import argparse

import cv2
import numpy as np
import tensorflow as tf
import neuralgym as ng

from inpaint_model import InpaintCAModel

import sys
import os
import time
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('--img_dir', default='', type=str,
                    help='The filename of image to be completed.')
parser.add_argument('--mask_dir', default='', type=str,
                    help='The filename of mask, value 255 indicates mask.')
parser.add_argument('--output_dir', default='', type=str,
                    help='Where to write output.')
parser.add_argument('--checkpoint_dir', default='', type=str,
                    help='The directory of tensorflow checkpoint.')


if __name__ == "__main__":
    #ng.get_gpus(4)
    args = parser.parse_args()

    args.image_height = 400
    args.image_width = 400

    #load model
    sess_config = tf.ConfigProto()
    sess_config.gpu_options.allow_growth = True
    sess = tf.Session(config=sess_config)

    model = InpaintCAModel()
    input_image_ph = tf.placeholder(
        tf.float32, shape=(1, args.image_height, args.image_width * 2, 3))
    output = model.build_server_graph(input_image_ph)
    output = (output + 1.) * 127.5
    output = tf.reverse(output, [-1])
    output = tf.saturate_cast(output, tf.uint8)
    vars_list = tf.get_collection(tf.GraphKeys.GLOBAL_VARIABLES)
    assign_ops = []
    for var in vars_list:
        vname = var.name
        from_name = vname
        var_value = tf.contrib.framework.load_variable(
            args.checkpoint_dir, from_name)
        assign_ops.append(tf.assign(var, var_value))
    sess.run(assign_ops)
    print('Model loaded.')

    inp_img_list = os.listdir(args.img_dir)

    t = time.time()
    for image_name in tqdm(inp_img_list, file=sys.stdout, desc='processing', unit='img'):
        image = os.path.join(args.img_dir,image_name)
        mask = os.path.join(args.mask_dir,image_name)
        out = os.path.join(args.output_dir, image_name)

        image = cv2.imread(image)
        mask = cv2.imread(mask)
        ori_width = image.shape[1]
        ori_height = image.shape[0]
        image = cv2.resize(image, (args.image_width, args.image_height))
        mask = cv2.resize(mask, (args.image_width, args.image_height))
        # cv2.imwrite(out, image*(1-mask/255.) + mask)
        # # continue
        # image = np.zeros((128, 256, 3))
        # mask = np.zeros((128, 256, 3))

        assert image.shape == mask.shape

        h, w, _ = image.shape
        grid = 4
        image = image[:h // grid * grid, :w // grid * grid, :]
        mask = mask[:h // grid * grid, :w // grid * grid, :]
        print('Shape of image: {}'.format(image.shape))

        image = np.expand_dims(image, 0)
        mask = np.expand_dims(mask, 0)
        input_image = np.concatenate([image, mask], axis=2)

        # load pretrained model
        result = sess.run(output, feed_dict={input_image_ph: input_image})
        print('Processed: {}'.format(out))
        outimg = cv2.resize(result[0][:, :, ::-1], (ori_width,ori_height))
        cv2.imwrite(out, outimg)

    print('Time total: {}'.format(time.time() - t))


