from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Union

from omegaconf import MISSING, MissingMandatoryValue

DEFAULT_IMG_SIZE = 256


@dataclass
class Transform:
    name: str = MISSING


@dataclass
class AugmentationConfig:
    img_size: int = DEFAULT_IMG_SIZE
    train: Optional[List] = None
    inference: Optional[List] = None


@dataclass
class CenterCrop(Transform):
    name: str = "centercrop"
    size: int = DEFAULT_IMG_SIZE


@dataclass
class ColorJitter(Transform):
    name: str = "colorjitter"
    brightness: Optional[float] = 0.25
    contrast: Optional[float] = 0.25
    saturation: Optional[float] = 0.25
    hue: Optional[float] = 0.1
    p: Optional[float] = 0.5


@dataclass
class HSVJitter(Transform):
    name: str = "hsvjitter"
    h_mag: int = 5
    s_mag: int = 30
    v_mag: int = 30


@dataclass
class Mixing(Transform):
    name: str = "mixing"
    mixup: Optional[List[float]] = field(default=None)
    cutmix: Optional[List[float]] = field(default=None)
    inplace: bool = False


@dataclass
class MosaicDetection(Transform):
    name: str = "mosaicdetection"
    size: List = field(default_factory=lambda: [DEFAULT_IMG_SIZE, DEFAULT_IMG_SIZE])
    mosaic_prob: float = 1.0
    affine_scale: List = field(default_factory=lambda: [0.5, 1.5])
    degrees: float = 10.0
    translate: float = 0.1
    shear: float = 2.0
    enable_mixup: bool = True
    mixup_prob: float = 1.0
    mixup_scale: List = field(default_factory=lambda: [0.5, 1.5])
    fill: int = 114
    mosaic_off_duration: int = 10


@dataclass
class Pad(Transform):
    name: str = "pad"
    size: List = field(default_factory=lambda: [DEFAULT_IMG_SIZE, DEFAULT_IMG_SIZE])
    fill: int = 0


@dataclass
class PoseTopDownAffine(Transform):
    name: str = "posetopdownaffine"
    scale: List = field(default_factory=lambda: [0.75, 1.25])
    scale_prob: float = 1.0
    translate: float = 0.1
    translate_prob: float = 1.0
    rotation: int = 60
    rotation_prob: float = 1.0
    size: List = field(default_factory=lambda: [DEFAULT_IMG_SIZE, DEFAULT_IMG_SIZE])


@dataclass
class RandomCrop(Transform):
    name: str = "randomcrop"
    size: int = DEFAULT_IMG_SIZE
    fill: int = 114


@dataclass
class RandomErasing(Transform):
    name: str = "randomerasing"
    p: float = 0.5
    scale: List = field(default_factory=lambda: [0.02, 0.33])
    ratio: List = field(default_factory=lambda: [0.3, 3.3])
    value: Optional[int] = 0
    inplace: bool = False


@dataclass
class RandomHorizontalFlip(Transform):
    name: str = "randomhorizontalflip"
    p: float = 0.5


@dataclass
class RandomResize(Transform):
    name: str = "randomresize"
    base_size: List = field(default_factory=lambda: [256, 256])
    stride: int = 32
    random_range: int = 4
    interpolation: str = "bilinear"


@dataclass
class RandomResize2(Transform):
    name: str = "randomresize2"
    base_size: List = field(default_factory=lambda: [512, 2048])
    random_range: List = field(default_factory=lambda: [0.5, 1.5])
    interpolation: str = "bilinear"


@dataclass
class RandomResizedCrop(Transform):
    name: str = "randomresizedcrop"
    size: int = DEFAULT_IMG_SIZE
    scale: List = field(default_factory=lambda: [0.08, 1.0])
    ratio: List = field(default_factory=lambda: [0.75, 1.33])
    interpolation: Optional[str] = "bilinear"


@dataclass
class RandomVerticalFlip(Transform):
    name: str = "randomverticalflip"
    p: float = 0.5


@dataclass
class Resize(Transform):
    name: str = "resize"
    size: List = field(default_factory=lambda: [DEFAULT_IMG_SIZE, DEFAULT_IMG_SIZE])
    interpolation: Optional[str] = "bilinear"
    max_size: Optional[int] = None
    resize_criteria: Optional[int] = None


class TrivialAugmentWide(Transform):
    name: str = "trivialaugmentwide"
    num_magnitude_bins: int = 31
    interpolation: str = "bilinear"
    fill: Optional[int] = None


@dataclass
class RandomMixup(Transform):
    name: str = "mixup"
    alpha: float = 0.2
    p: float = 1.0
    inplace: bool = False


@dataclass
class RandomCutmix(Transform):
    name: str = "cutmix"
    alpha: float = 1.0
    p: float = 1.0
    inplace: bool = False


@dataclass
class ToTensor(Transform):
    name: str = "totensor"
    pixel_range: float = 1.0


@dataclass
class Normalize(Transform):
    name: str = "normalize"
    mean: List[float] = field(default_factory=lambda: [0.485, 0.456, 0.406])
    std: List[float] = field(default_factory=lambda: [0.229, 0.224, 0.225])


@dataclass
class ClassificationAugmentationConfig(AugmentationConfig):
    img_size: int = 256
    train: Optional[List] = field(
        default_factory=lambda: [RandomResizedCrop(size=256), RandomHorizontalFlip(), Mixing(mixup=[0.25, 1.0])]
    )
    inference: Optional[List] = field(default_factory=lambda: [Resize(size=[256, 256])])


@dataclass
class SegmentationAugmentationConfig(AugmentationConfig):
    img_size: int = 512
    train: Optional[List] = field(
        default_factory=lambda: [RandomResizedCrop(size=512), RandomHorizontalFlip(), ColorJitter()]
    )
    inference: Optional[List] = field(default_factory=lambda: [Resize(size=[512, 512])])


@dataclass
class DetectionAugmentationConfig(AugmentationConfig):
    img_size: int = 512
    train: Optional[List] = field(default_factory=lambda: [Resize(size=[512, 512])])
    inference: Optional[List] = field(default_factory=lambda: [Resize(size=[512, 512])])
