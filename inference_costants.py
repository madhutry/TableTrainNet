from dataset_costants import TABLE_DICT

PATH_TO_LABELS = '/content/TableTrainNet/data/object-detection.pbtxt'
BMP_IMAGE_TEST_TO_PATH = '/content/TableTrainNet/test'

NUM_CLASSES = 1

PATHS_TO_TEST_IMAGE = [
    'test/test1.png',
    'test/test2.png',
    'test/test3.png',
    'test/test4.png',
    'test/test5.png',
    'test/test6.png',
    'test/test7.png'
]

PATHS_TO_CKPTS = [
    '/content/ckpt/model.ckpt'
]

TEST_SCORES = [0.2, 0.4, 0.6, 0.8]

MAX_NUM_BOXES = 10
