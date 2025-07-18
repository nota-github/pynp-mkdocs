from functools import partial

import cv2
import numpy as np

IMAGENET_DEFAULT_MEAN = (0.485, 0.456, 0.406)
IMAGENET_DEFAULT_STD = (0.229, 0.224, 0.225)
INVERSE_MODES_MAPPING = {
    "bilinear": cv2.INTER_LINEAR,
    "bicubic": cv2.INTER_CUBIC,
}


def resize_img(img, size, interpolation, max_size, resize_criteria):
    assert isinstance(size, int), "Only support int type ``size`` now."
    assert resize_criteria == "long", "Only support ``long`` type ``resize_criteria`` now."
    h, w = img.shape[:2]
    long_side, short_side = max(h, w), min(h, w)
    resize_factor = size / long_side
    target_size = [size, round(resize_factor * short_side)] if h < w else [round(resize_factor * short_side), size]
    img = cv2.resize(img, dsize=target_size, interpolation=cv2.INTER_LINEAR)
    return img


def pad_img(img, size, fill):
    assert isinstance(size, int), "Only support int type ``size`` now."
    h, w = img.shape[:2]
    padded = np.full((size, size, 3), fill, dtype="uint8")
    padded[:h, :w] = img
    return padded


def normalize(img, mean, std):
    img = img.astype("float32") / 255.0
    img = img - np.array(mean).reshape(1, 1, -1).astype("float32")
    img = img / np.array(std).reshape(1, 1, -1).astype("float32")
    img = img[np.newaxis, ...]
    return img


class Preprocessor:
    DEVICE_TRANSFORM_DICT = {
        "resize": resize_img,
        "pad": pad_img,
        "normalize": normalize,
    }

    def __init__(self, preprocess_list):
        self.transforms = []
        for transform in preprocess_list:
            if transform["name"] == "totensor":
                continue
            name = transform["name"]
            augment_kwargs = list(transform.keys())
            augment_kwargs.remove("name")
            augment_kwargs = {k: transform[k] for k in augment_kwargs}
            transform = partial(self.DEVICE_TRANSFORM_DICT[name], **augment_kwargs)
            self.transforms.append(transform)

    def __call__(self, img):
        for transform in self.transforms:
            img = transform(img)
        return img
