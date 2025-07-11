# Pruning Options

## Policy

The policy of the NetsPresso Model Compressor allows for pruning connected filters or neurons identically using the given pruning criteria while preserving the information.

To calculate the importance score of the connected neurons or filters, "Sum", "Average" can be used as policies (for more details, please refer to the following documents).

### Sum

- The "Sum" policy calculates its importance score as the summation value of the connected filters' importance scores.

<div align="center">
<img src="../../../../../_static/compression/options/sum.png" width="500" />
</div>

### Average

- The "Average" policy calculates its importance score as the average value of the connected filters' importance scores.

<div align="center">
<img src="../../../../../_static/compression/options/average.png" width="500" />
</div>

## Layer Norm

The normalization process is necessary to compare the importance score of different layer's filters or neurons.

### Standard Score

<div align="center">
<img src="../../../../../_static/compression/options/standard_score.png" width="500" />
</div>

### TSS Norm (Total sum scaling normalization)

<div align="center">
<img src="../../../../../_static/compression/options/tss_norm.png" width="250" />
</div>

### Linear Scaling

<div align="center">
<img src="../../../../../_static/compression/options/linear_scaling.png" width="500" />
</div>

### Softmax Norm

<div align="center">
<img src="../../../../../_static/compression/options/softmax_norm.png" width="300" />
</div>

### None

- Normalization will not be used to compare the importance of the different layer.

## Group Policy

The reshape and group convolutional operator should prune the same number of filters for each group to preserve the shape of the weight or arguments.

For this reason, the group policy is used to ensure that the same number of filters are pruned for each group.

### Sum

- The group policy "sum" calculates its importance score as the summation value of the corresponding filter index of all groups.

### Average

- The group policy "Average" calculates its importance score as the average value of the corresponding filter index of all groups.

### Count

- The importance score of each groups' filter will be measured independently, and the minimum number of filters for the given group will be removed identically for given groups.

### None

- The group policy "None" will prune same amount of the filters to preserve the shape of the weight. None of the policy will be used to represent the filter index of group.

## Reshape Channel Axis

Reshape channel axis represents which axis of the reshape operator will be pruned.

- Ex. Consider the input of the given reshape operator is `batch, 768, 197` and the output of the reshape operator is `batch, 12, 64, 197`

    - If the `reshape_channel_axis` is `-1` or `1` when the given pruning ratio is 50%, the output model will contain `32 (64*0.5)` channels of the given reshape operator.

    - If the `reshape_channel_axis` is `-2` or `0` when the given pruning ratio is 50%, the output model will contain `6 (12*0.5)` channels of the given reshape operator.

## Step operator

Step operator is the method of rounding applied to ensure that the amount remaining after pruning aligns with the step_size.

Options include Round, Round Up, Round Down, or None.

### Round

- Rounds to the nearest step size, adjusting the remaining count of filters.

### Round Up

- Always rounds up to the next step size, directly affecting the remaining filters.

### Round Down

- Always rounds down to the closest lower step size, impacting the remaining filters.

### None

- No rounding operation is applied; the exact amount is used for pruning.
