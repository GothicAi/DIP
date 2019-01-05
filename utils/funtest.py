import numpy as np
import cv2
def random_ff_mask():
    """Generate a random free form mask with configuration.

    Args:
        config: Config should have configuration including IMG_SHAPES,
            VERTICAL_MARGIN, HEIGHT, HORIZONTAL_MARGIN, WIDTH.

    Returns:
        tuple: (top, left, height, width)
    """

    h, w = 256, 256
    mask = np.zeros((h, w))
    num_v = 12 + np.random.randint(
        5)  # tf.random_uniform([], minval=0, maxval=config.MAXVERTEX, dtype=tf.int32)

    for i in range(num_v):
        start_x = np.random.randint(w)
        start_y = np.random.randint(h)
        for j in range(1 + np.random.randint(5)):
            angle = 0.01 + np.random.randint(4.0)
            if i % 2 == 0:
                angle = 2 * 3.1415926 - angle
            length = 10 + np.random.randint(40)
            brush_w = 10 + np.random.randint(10)
            end_x = (start_x + length * np.sin(angle)).astype(np.int32)
            end_y = (start_y + length * np.cos(angle)).astype(np.int32)

            cv2.line(mask, (start_y, start_x), (end_y, end_x), 1.0, brush_w)
            start_x, start_y = end_x, end_y

    return mask.reshape(mask.shape + (1,)).astype(np.float32)

mask = random_ff_mask()
print(mask.shape)
#cv2.imshow("aaa", mask)
#cv2.waitKey(0)