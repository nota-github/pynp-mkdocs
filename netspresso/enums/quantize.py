from netspresso.enums.base import StrEnum


class QuantizationPrecision(StrEnum):
    INT8 = "int8"
    FLOAT16 = "float16"
    FLOAT32 = "float32"


class QuantizationMode(StrEnum):
    AUTOMATIC_QUANTIZATION = "automatic_quantization"
    UNIFORM_PRECISION_QUANTIZATION = "uniform_precision_quantization"
    CUSTOM_PRECISION_QUANTIZATION = "custom_precision_quantization"
    ADVANCED_QUANTIZATION = "advanced_quantization"
    RECOMMEND_QUANTIZATION = "recommend_quantization"


class SimilarityMetric(StrEnum):
    SNR = "SNR"


class OnnxOperator(StrEnum):
    Adagrad = "Adagrad"
    Momentum = "Momentum"
    ZipMap = "ZipMap"
    TreeEnsembleClassifier = "TreeEnsembleClassifier"
    SVMRegressor = "SVMRegressor"
    LinearClassifier = "LinearClassifier"
    DictVectorizer = "DictVectorizer"
    CategoryMapper = "CategoryMapper"
    CastMap = "CastMap"
    StringSplit = "StringSplit"
    Adam = "Adam"
    Gelu = "Gelu"
    Scaler = "Scaler"
    AffineGrid = "AffineGrid"
    BitwiseOr = "BitwiseOr"
    BitwiseAnd = "BitwiseAnd"
    Mish = "Mish"
    MelWeightMatrix = "MelWeightMatrix"
    BlackmanWindow = "BlackmanWindow"
    Gradient = "Gradient"
    HammingWindow = "HammingWindow"
    HannWindow = "HannWindow"
    SequenceMap = "SequenceMap"
    LayerNormalization = "LayerNormalization"
    GridSample = "GridSample"
    CastLike = "CastLike"
    OptionalHasElement = "OptionalHasElement"
    Optional = "Optional"
    SoftmaxCrossEntropyLoss = "SoftmaxCrossEntropyLoss"
    GreaterOrEqual = "GreaterOrEqual"
    LessOrEqual = "LessOrEqual"
    Celu = "Celu"
    Imputer = "Imputer"
    SequenceLength = "SequenceLength"
    OptionalGetElement = "OptionalGetElement"
    SequenceAt = "SequenceAt"
    SequenceConstruct = "SequenceConstruct"
    GatherND = "GatherND"
    ScatterND = "ScatterND"
    GatherElements = "GatherElements"
    CumSum = "CumSum"
    RoiAlign = "RoiAlign"
    NonMaxSuppression = "NonMaxSuppression"
    DequantizeLinear = "DequantizeLinear"
    DFT = "DFT"
    QuantizeLinear = "QuantizeLinear"
    QLinearConv = "QLinearConv"
    ConvInteger = "ConvInteger"
    Det = "Det"
    QLinearMatMul = "QLinearMatMul"
    MatMulInteger = "MatMulInteger"
    Normalizer = "Normalizer"
    RandomNormal = "RandomNormal"
    IsInf = "IsInf"
    Or = "Or"
    ConcatFromSequence = "ConcatFromSequence"
    Constant = "Constant"
    FeatureVectorizer = "FeatureVectorizer"
    Mul = "Mul"
    Max = "Max"
    GRU = "GRU"
    GroupNormalization = "GroupNormalization"
    Mod = "Mod"
    Log = "Log"
    ArgMax = "ArgMax"
    ReduceMax = "ReduceMax"
    Split = "Split"
    If = "If"
    ReduceMin = "ReduceMin"
    DeformConv = "DeformConv"
    MaxPool = "MaxPool"
    Sign = "Sign"
    Min = "Min"
    Range = "Range"
    Cast = "Cast"
    PRelu = "PRelu"
    RandomUniform = "RandomUniform"
    Pad = "Pad"
    NonZero = "NonZero"
    Ceil = "Ceil"
    Tan = "Tan"
    Not = "Not"
    Clip = "Clip"
    ReduceL2 = "ReduceL2"
    Neg = "Neg"
    LinearRegressor = "LinearRegressor"
    BitwiseXor = "BitwiseXor"
    Conv = "Conv"
    StringConcat = "StringConcat"
    Abs = "Abs"
    Softplus = "Softplus"
    MaxUnpool = "MaxUnpool"
    TfIdfVectorizer = "TfIdfVectorizer"
    ConvTranspose = "ConvTranspose"
    SequenceEmpty = "SequenceEmpty"
    And = "And"
    Flatten = "Flatten"
    ReduceLogSum = "ReduceLogSum"
    Einsum = "Einsum"
    ReduceLogSumExp = "ReduceLogSumExp"
    Sub = "Sub"
    Floor = "Floor"
    RandomUniformLike = "RandomUniformLike"
    MaxRoiPool = "MaxRoiPool"
    Concat = "Concat"
    Sigmoid = "Sigmoid"
    SequenceInsert = "SequenceInsert"
    Less = "Less"
    Softmax = "Softmax"
    Add = "Add"
    DynamicQuantizeLinear = "DynamicQuantizeLinear"
    InstanceNormalization = "InstanceNormalization"
    Loop = "Loop"
    LpPool = "LpPool"
    ArgMin = "ArgMin"
    Equal = "Equal"
    LabelEncoder = "LabelEncoder"
    SplitToSequence = "SplitToSequence"
    Round = "Round"
    Unique = "Unique"
    BitShift = "BitShift"
    AveragePool = "AveragePool"
    Slice = "Slice"
    Dropout = "Dropout"
    Exp = "Exp"
    EyeLike = "EyeLike"
    LSTM = "LSTM"
    ArrayFeatureExtractor = "ArrayFeatureExtractor"
    MatMul = "MatMul"
    LeakyRelu = "LeakyRelu"
    ReduceMean = "ReduceMean"
    ReverseSequence = "ReverseSequence"
    BatchNormalization = "BatchNormalization"
    LpNormalization = "LpNormalization"
    Gemm = "Gemm"
    OneHot = "OneHot"
    Bernoulli = "Bernoulli"
    NegativeLogLikelihoodLoss = "NegativeLogLikelihoodLoss"
    Greater = "Greater"
    RNN = "RNN"
    GlobalLpPool = "GlobalLpPool"
    Gather = "Gather"
    HardSwish = "HardSwish"
    Mean = "Mean"
    IsNaN = "IsNaN"
    RegexFullMatch = "RegexFullMatch"
    Asin = "Asin"
    OneHotEncoder = "OneHotEncoder"
    DepthToSpace = "DepthToSpace"
    Div = "Div"
    Softsign = "Softsign"
    GlobalMaxPool = "GlobalMaxPool"
    Reciprocal = "Reciprocal"
    MeanVarianceNormalization = "MeanVarianceNormalization"
    ReduceL1 = "ReduceL1"
    Relu = "Relu"
    ScatterElements = "ScatterElements"
    ReduceSum = "ReduceSum"
    Elu = "Elu"
    Reshape = "Reshape"
    ImageDecoder = "ImageDecoder"
    Shape = "Shape"
    Selu = "Selu"
    ConstantOfShape = "ConstantOfShape"
    GlobalAveragePool = "GlobalAveragePool"
    Size = "Size"
    HardSigmoid = "HardSigmoid"
    LogSoftmax = "LogSoftmax"
    SpaceToDepth = "SpaceToDepth"
    TreeEnsembleRegressor = "TreeEnsembleRegressor"
    BitwiseNot = "BitwiseNot"
    ReduceSumSquare = "ReduceSumSquare"
    Sqrt = "Sqrt"
    Col2Im = "Col2Im"
    RandomNormalLike = "RandomNormalLike"
    Multinomial = "Multinomial"
    Identity = "Identity"
    Expand = "Expand"
    Squeeze = "Squeeze"
    STFT = "STFT"
    Sum = "Sum"
    Upsample = "Upsample"
    Tanh = "Tanh"
    Tile = "Tile"
    TopK = "TopK"
    LRN = "LRN"
    Unsqueeze = "Unsqueeze"
    ThresholdedRelu = "ThresholdedRelu"
    SequenceErase = "SequenceErase"
    Xor = "Xor"
    Acos = "Acos"
    Pow = "Pow"
    Atan = "Atan"
    SVMClassifier = "SVMClassifier"
    Cos = "Cos"
    Sin = "Sin"
    Transpose = "Transpose"
    ReduceProd = "ReduceProd"
    Scan = "Scan"
    Compress = "Compress"
    Scatter = "Scatter"
    CenterCropPad = "CenterCropPad"
    Sinh = "Sinh"
    Asinh = "Asinh"
    Binarizer = "Binarizer"
    Trilu = "Trilu"
    Acosh = "Acosh"
    Cosh = "Cosh"
    StringNormalizer = "StringNormalizer"
    Atanh = "Atanh"
    Shrink = "Shrink"
    Hardmax = "Hardmax"
    ERF = "Erf"
    Where = "Where"
    Resize = "Resize"
