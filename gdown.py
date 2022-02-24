import gdown
url='https://drive.google.com/file/d/1aGLstfgFbBMZih_OaBaiuB40ZI8DxLpK/view?usp=sharing'
output = 'trainingDataset_mrcnn.zip'
gdown.download(url, output, quiet=False)
# md5 = 'fa837a88f0c40c513d975104edf3dal7'
# gdown. cached_download(url, output, md5=md5, postprocess=gdown. extractall)