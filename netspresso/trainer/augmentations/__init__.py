from netspresso.trainer.augmentations.augmentation import (
    AugmentationConfig,
    CenterCrop,
    ClassificationAugmentationConfig,
    ColorJitter,
    DetectionAugmentationConfig,
    HSVJitter,
    Mixing,
    MosaicDetection,
    Normalize,
    Pad,
    PoseTopDownAffine,
    RandomCrop,
    RandomCutmix,
    RandomErasing,
    RandomHorizontalFlip,
    RandomMixup,
    RandomResize,
    RandomResize2,
    RandomResizedCrop,
    RandomVerticalFlip,
    Resize,
    SegmentationAugmentationConfig,
    ToTensor,
    Transform,
    TrivialAugmentWide,
)

AUGMENTATION_CONFIG_TYPE = {
    "classification": ClassificationAugmentationConfig,
    "detection": DetectionAugmentationConfig,
    "segmentation": SegmentationAugmentationConfig,
}


__all__ = [
    "CenterCrop",
    "HSVJitter",
    "Mixing",
    "MosaicDetection",
    "PoseTopDownAffine",
    "RandomErasing",
    "RandomResize",
    "RandomResize2",
    "ColorJitter",
    "Pad",
    "RandomCrop",
    "RandomResizedCrop",
    "RandomHorizontalFlip",
    "RandomVerticalFlip",
    "Resize",
    "TrivialAugmentWide",
    "RandomMixup",
    "RandomCutmix",
    "Transform",
    "AugmentationConfig",
    "AUGMENTATION_CONFIG_TYPE",
    "ToTensor",
    "Normalize",
]
