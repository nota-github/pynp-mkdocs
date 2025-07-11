# Trainer

## Description

::: netspresso.trainer.trainer.Trainer
    handler: python
    options:
      heading_level: 3
      show_root_heading: true
      show_source: false
      show_symbol_type_toc: true

## Examples

### Training

```python
from netspresso import NetsPresso
from netspresso.enums import Task
from netspresso.trainer.augmentations import Resize
from netspresso.trainer.optimizers import AdamW
from netspresso.trainer.schedulers import CosineAnnealingWarmRestartsWithCustomWarmUp


netspresso = NetsPresso(email="YOUR_EMAIL", password="YOUR_PASSWORD")

# 1. Declare trainer
trainer = netspresso.trainer(task=Task.OBJECT_DETECTION)

# 2. Set config for training
# 2-1. Data
trainer.set_dataset_config(
   name="traffic_sign_config_example",
   root_path="/root/traffic-sign",
   train_image="images/train",
   train_label="labels/train",
   valid_image="images/valid",
   valid_label="labels/valid",
   id_mapping=["prohibitory", "danger", "mandatory", "other"],
)

# 2-2. Model
print(trainer.available_models)  # ['EfficientFormer', 'YOLOX-S', ...]
trainer.set_model_config(model_name="YOLOX-S", img_size=512)

# 2-3. Augmentation
trainer.set_augmentation_config(
   train_transforms=[Resize()],
   inference_transforms=[Resize()],
)

# 2-4. Training
optimizer = AdamW(lr=6e-3)
scheduler = CosineAnnealingWarmRestartsWithCustomWarmUp(warmup_epochs=10)
trainer.set_training_config(
   epochs=40,
   batch_size=16,
   optimizer=optimizer,
   scheduler=scheduler,
)

# 3. Train
training_result = trainer.train(gpus="0, 1", project_name="project_sample")
```

### Retraining

```python
from netspresso import NetsPresso
from netspresso.trainer.optimizers import AdamW


netspresso = NetsPresso(email="YOUR_EMAIL", password="YOUR_PASSWORD")

# 1. Declare trainer
trainer = netspresso.trainer(yaml_path="./temp/hparams.yaml")

# 2. Set config for retraining
# 2-1. FX Model
trainer.set_fx_model(fx_model_path="./temp/FX_MODEL_PATH.pt")

# 2-2. Training
trainer.set_training_config(
   epochs=30,
   batch_size=16,
   optimizer=AdamW(lr=6e-3),
)

# 3. Train
trainer.train(gpus="0, 1", project_name="project_retrain_sample")
```
