# Compressor(Manual Compression)

## Upload Model

::: netspresso.compressor.v2.compressor.CompressorV2.upload_model
    handler: python
    options:
      members:
        - automatic_quantization
      heading_level: 3
      show_root_heading: true
      show_source: false
      show_symbol_type_toc: true

### Details of Parameters

#### Framework

##### Available Framework

| Name             | Description          |
|------------------|----------------------|
| TENSORFLOW_KERAS | TensorFlow-Keras     |
| PYTORCH          | PyTorch GraphModule  |
| ONNX             | ONNX                 |

##### Example

```python
from netspresso.enums import Framework

FRAMEWORK = Framework.PYTORCH
```

!!! note
    - **ONNX (.onnx)**
        - Supported version: PyTorch >= 1.11.x, ONNX >= 1.10.x.
        - If a model is defined in PyTorch, it should be converted into the ONNX format before being uploaded.
        - [How-to-guide for the conversion of PyTorch into ONNX](https://github.com/Nota-NetsPresso/NetsPresso-Model-Compressor-ModelZoo/tree/main/models/torch#conversion-of-pytorch-into-onnx)

    - **PyTorch GraphModule (.pt)**
        - Supported version: PyTorch >= 1.11.x.
        - If a model is defined in PyTorch, it should be converted into the GraphModule before being uploaded.
        - The model must contain not only the status dictionary but also the structure of the model (do not use state_dict).
        - [How-to-guide for the conversion of PyTorch into GraphModule](https://github.com/Nota-NetsPresso/NetsPresso-Model-Compressor-ModelZoo/tree/main/models/torch#conversion-of-pytorch-into-graphmodule-torchfxgraphmodule)

    - **TensorFlow-Keras (.h5, .zip)**
        - Supported version: TensorFlow 2.3.x ~ 2.8.x.
        - Custom layer must not be included in Keras H5 (.h5) format.
        - The model must contain not only weights but also the structure of the model (do not use save_weights).
        - If there is a custom layer in the model, please upload TensorFlow SavedModel format (.zip).

        <div align="center">
        <img src="../../../../../_static/tf-keras.png" width="250" />
        </div>

#### Input Shapes

!!! note
    - For input shapes, use the same values that you used to train the model.

        - If the input shapes of the model is **dynamic**, input shapes is **required**.
        - If the input shapes of the model is **static**, input shapes is **not required**.

    - For example, batch=1, channel=3, **height=768, width=1024**.

        ```python
        input_shapes = [{"batch": 1, "channel": 3, "dimension": [768, 1024]}]
        ```

    - Currently, **only single input models** are supported.

### Example

```python
from netspresso import NetsPresso


netspresso = NetsPresso(email="YOUR_EMAIL", password="YOUR_PASSWORD")

compressor = netspresso.compressor_v2()
model = compressor.upload_model(
    input_model_path="./examples/sample_models/mobilenetv1.h5",
    input_shapes=[{"batch": 1, "channel": 3, "dimension": [224, 224]}],
)
```

## Select Compression Method

::: netspresso.compressor.v2.compressor.CompressorV2.select_compression_method
    handler: python
    options:
      members:
        - automatic_quantization
      heading_level: 3
      show_root_heading: true
      show_source: false
      show_symbol_type_toc: true

### Details of Parameters

#### Compression Method

##### Available Compression Method

| Name   | Description                      |
|--------|----------------------------------|
| PR_L2  | L2 Norm Pruning                  |
| PR_GM  | GM Pruning                       |
| PR_NN  | Nuclear Norm Pruning             |
| PR_SNP | Structured Neuron-level Pruning  |
| PR_ID  | Pruning By Index                 |
| FD_TK  | Tucker Decomposition             |
| FD_SVD | Singular Value Decomposition     |
| FD_CP  | CP Decomposition                 |

##### Example

```python
from netspresso.enums import CompressionMethod

COMPRESSION_METHOD = CompressionMethod.PR_L2
```

!!! warning
    - Nuclear Norm is only supported in the Tensorflow-Keras framework.
    - Structured Neuron-level is only supported in the PyTorch and ONNX frameworks.

!!! note
    - Click on the link to learn more about the information. ([Compression Method](compression_method.md))

#### Options

- `netspresso.enums.Policy` - Policy for handling connected filters
- `netspresso.enums.LayerNorm` - Layer normalization method
- `netspresso.enums.GroupPolicy` - Group policy for group convolutions
- `netspresso.enums.StepOp` - Step operator for rounding

##### Example

```python
from netspresso.enums import Policy, LayerNorm, GroupPolicy
from netspresso.clients.compressor.v2.schemas import Options

OPTIONS = Options(
    policy=Policy.AVERAGE,
    layer_norm=LayerNorm.TSS_NORM,
    group_policy=GroupPolicy.COUNT,
    reshape_channel_axis=-1
)
```

!!! note
    - Click the link for more information. ([Pruning Options](pruning_options.md))

!!! note
    - This parameter applies only to the Pruning Method (PR_L2, PR_GM, PR_NN, PR_SNP).

### Details of Returns

#### Example

```python
from netspresso import NetsPresso
from netspresso.enums import CompressionMethod, Policy, LayerNorm, GroupPolicy
from netspresso.clients.compressor.v2.schemas import Options


netspresso = NetsPresso(email="YOUR_EMAIL", password="YOUR_PASSWORD")

compressor = netspresso.compressor_v2()
compression_info = compressor.select_compression_method(
    model_id="YOUR_UPLOADED_MODEL_ID",
    compression_method=CompressionMethod.PR_L2,
    options=Options(
        policy=Policy.AVERAGE,
        layer_norm=LayerNorm.STANDARD_SCORE,
        group_policy=GroupPolicy.AVERAGE,
        reshape_channel_axis=-1,
    ),
)
```

#### Output

```bash
>>> compression_info
CompressionInfo(
    compression_method="PR_L2", 
    available_layers=[
        AvailableLayer(name='conv1', values=[""], channels=[32]), 
        AvailableLayer(name='layers.0.conv2', values=[""], channels=[64]), 
        AvailableLayer(name='layers.1.conv2', values=[""], channels=[128]), 
        AvailableLayer(name='layers.2.conv2', values=[""], channels=[128]), 
        AvailableLayer(name='layers.3.conv2', values=[""], channels=[256]), 
        AvailableLayer(name='layers.4.conv2', values=[""], channels=[256]), 
        AvailableLayer(name='layers.5.conv2', values=[""], channels=[512]), 
        AvailableLayer(name='layers.6.conv2', values=[""], channels=[512]), 
        AvailableLayer(name='layers.7.conv2', values=[""], channels=[512]), 
        AvailableLayer(name='layers.8.conv2', values=[""], channels=[512]), 
        AvailableLayer(name='layers.9.conv2', values=[""], channels=[512]), 
        AvailableLayer(name='layers.10.conv2', values=[""], channels=[512]), 
        AvailableLayer(name='layers.11.conv2', values=[""], channels=[1024]), 
        AvailableLayer(name='layers.12.conv2', values=[""], channels=[1024])
    ], 
    options={'reshape_channel_axis': -1, 'policy': 'average', 'layer_norm': 'tss_norm', 'group_policy': 'average'}
    original_model_id="YOUR_UPLOADED_MODEL_ID",
    compressed_model_id="", 
    compression_id="", 
)
```

## Set Compression Params

### Details of Parameters

#### Values of available layer

| Compression Method | Number of Values | Type  | Range                                 |
|--------------------|------------------|-------|---------------------------------------|
| PR_L2              | 1                | Float | 0.0 < ratio < 1.0                     |
| PR_GM              | 1                | Float | 0.0 < ratio < 1.0                     |
| PR_NN              | 1                | Float | 0.0 < ratio < 1.0                     |
| PR_SNP             | 1                | Float | 0.0 < ratio < 1.0                     |
| PR_ID              | (Num of Out Channels - 1) | Int | 0 ≤ channels < Num of Out Channels |
| FD_TK              | 2                | Int   | 0 < rank ≤ (Num of In Channels or Num of Out Channels) |
| FD_CP              | 1                | Int   | 0 < rank ≤ min(Num of In Channels or Num of Out Channels) |
| FD_SVD             | 1                | Int   | 0 < rank ≤ min(Num of In Channels or Num of Out Channels) |

#### Example

```python
for available_layer in compression_info.available_layers:
   available_layer.values = [0.2]
```

#### Output

```bash
>>> compression_info
CompressionInfo(
   compression_method="PR_L2", 
   available_layers=[
      AvailableLayer(name='conv1', values=[0.2], channels=[32]), 
      AvailableLayer(name='layers.0.conv2', values=[0.2], channels=[64]), 
      AvailableLayer(name='layers.1.conv2', values=[0.2], channels=[128]), 
      AvailableLayer(name='layers.2.conv2', values=[0.2], channels=[128]), 
      AvailableLayer(name='layers.3.conv2', values=[0.2], channels=[256]), 
      AvailableLayer(name='layers.4.conv2', values=[0.2], channels=[256]), 
      AvailableLayer(name='layers.5.conv2', values=[0.2], channels=[512]), 
      AvailableLayer(name='layers.6.conv2', values=[0.2], channels=[512]), 
      AvailableLayer(name='layers.7.conv2', values=[0.2], channels=[512]), 
      AvailableLayer(name='layers.8.conv2', values=[0.2], channels=[512]), 
      AvailableLayer(name='layers.9.conv2', values=[0.2], channels=[512]), 
      AvailableLayer(name='layers.10.conv2', values=[0.2], channels=[512]), 
      AvailableLayer(name='layers.11.conv2', values=[0.2], channels=[1024]), 
      AvailableLayer(name='layers.12.conv2', values=[0.2], channels=[1024])
   ], 
   options={'reshape_channel_axis': -1, 'policy': 'average', 'layer_norm': 'tss_norm', 'group_policy': 'average'}
   original_model_id="YOUR_UPLOADED_MODEL_ID",
   compressed_model_id="", 
   compression_id="", 
)
```

## Compress Model

::: netspresso.compressor.v2.compressor.CompressorV2.compress_model
    handler: python
    options:
      members:
        - automatic_quantization
      heading_level: 3
      show_root_heading: true
      show_source: false
      show_symbol_type_toc: true

### Example

```python
compressed_model = compressor.compress_model(
    compression=compression_info,
    output_dir="./outputs/compressed/graphmodule_manual",
)
```

## Full Example

```python
from netspresso import NetsPresso
from netspresso.enums import CompressionMethod, GroupPolicy, LayerNorm, Policy
from netspresso.clients.compressor.v2.schemas import Options


netspresso = NetsPresso(email="YOUR_EMAIL", password="YOUR_PASSWORD")

# 1. Declare compressor
compressor = netspresso.compressor_v2()

# 2. Upload model
model = compressor.upload_model(
    input_model_path="./examples/sample_models/graphmodule.pt",
    input_shapes=[{"batch": 1, "channel": 3, "dimension": [224, 224]}],
)

# 3. Select compression method
compression_info = compressor.select_compression_method(
    model_id=model.ai_model_id,
    compression_method=CompressionMethod.PR_L2,
    options=Options(
        policy=Policy.AVERAGE,
        layer_norm=LayerNorm.STANDARD_SCORE,
        group_policy=GroupPolicy.AVERAGE,
        reshape_channel_axis=-1,
    ),
)

# 4. Set params for compression(ratio or rank)
for available_layer in compression_info.available_layers[:5]:
    available_layer.values = [0.2]

# 5. Compress model
compressed_model = compressor.compress_model(
    compression=compression_info,
    output_dir="./outputs/compressed/graphmodule_manual",
)
```
