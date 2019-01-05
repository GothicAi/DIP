import numpy as np
import pycocotools.mask as cocomask
def cocoseg_to_binary(seg, height, width):
    """
    COCO style segmentation to binary mask
    :param seg: coco-style segmentation
    :param height: image height
    :param width: image width
    :return: binary mask
    """
    if type(seg) == list:
        rle = cocomask.frPyObjects(seg, height, width)
        rle = cocomask.merge(rle)
        mask = cocomask.decode([rle])
    elif type(seg['counts']) == list:
        rle = cocomask.frPyObjects(seg, height, width)
        mask = cocomask.decode([rle])
    else:
        rle = cocomask.merge(seg)
        mask = cocomask.decode([rle])
    assert mask.shape[2] == 1
    return mask[:, :, 0]

def get_coco_masks(anns: list, height: int, width: int):
    """
    Get coco masks from annotations.
    :param anns: list of coco-style annotation
    :param height: image height
    :param width: image width
    :return: masks, hxw numpy array
    """
    mask = np.zeros((height, width), dtype=np.int32)
    
    for inst_idx, ann in enumerate(anns):
        cat_id = ann['category_id']

        m = cocoseg_to_binary(ann['segmentation'], height, width)  # zero one mask
        m = m.astype(np.int32) * (inst_idx + 1)
        mask[m > 0] = m[m > 0]

    return mask

if __name__ == '__main__':
    from pycocotools.coco import COCO
    import cv2
    annFile = 'instances_val2017.json'
    coco=COCO(annFile)
    imgIds = coco.getImgIds()[:20]
    for img_id in imgIds:
        img = coco.loadImgs(img_id)[0]
        ann_ids = coco.getAnnIds(imgIds=img_id)
        anns = coco.loadAnns(ann_ids)
        mask = get_coco_masks(anns, img['height'], img['width'])
        #mask = cv2.resize(mask, (255, 255), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(img['file_name'], mask*255)