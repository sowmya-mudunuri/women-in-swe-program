import os

# Paths to our main directories
DIR_BASE = "C:/Users/Sowmya Mudunuri/Downloads/archive"
DIR_TRAIN = os.path.join(DIR_BASE, 'train')
DIR_VALID = os.path.join(DIR_BASE, 'valid')
DIR_TEST = os.path.join(DIR_BASE, 'test')

# Paths to our models
PATH_OUT = "C:/Users/Sowmya Mudunuri/Downloads/archive/EfficientNetB0-525-(224 X 224)- 98.97.h5"
VGG_PATH_OUT = "C:/Users/Sowmya Mudunuri/Downloads/archive/EfficientNetB0-525-(224 X 224)- 98.97.h5"
LOCAL_MODEL = "C:/Users/Sowmya Mudunuri/Downloads/archive/EfficientNetB0-525-(224 X 224)- 98.97.h5"

# Image properties
IMAGE_SIZE = (224, 224)
INPUT_IMAGE_SIZE = (224, 224, 3)

# Batches properties
BATCH_SIZE_32 = 32
BATCH_SIZE_64 = 64

# CNN properties
KERNEL_SIZE = (3, 3)
POOL_SIZE = (3, 3)
