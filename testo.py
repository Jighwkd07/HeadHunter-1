import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


from tensorflow.python.client import device_lib
device_lib.list_local_devices()