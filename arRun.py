# import fastai
from deoldify.visualize import *
import warnings
import cv2
import torch

import time

from deoldify import device
from deoldify.device_id import DeviceId
#choices:  CPU, GPU0...GPU7
# device.set(device=DeviceId.GPU0)
#
#
# if not torch.cuda.is_available():
#     print('GPU not available.')
#
# warnings.filterwarnings("ignore", category=UserWarning, message=".*?Your .*? set is empty.*?")



start_time = time.time()




colorizer = get_image_colorizer(artistic=False)

source_url = 'test_images/image.png'
render_factor = 35
watermarked = False

savepath = Path("result_images")

if source_url is not None and source_url !='':

    image_path = colorizer.plot_transformed_image(path=source_url,results_dir=None, render_factor=35, watermarked=False)
    end_time = time.time()
    server_process_time = end_time - start_time
    print("total time = ", server_process_time)
        # plot_transformed_image_from_url(url=source_url, render_factor=render_factor, compare=True, watermarked=watermarked)
    # show_image_in_notebook(image_path)
else:
    print('Provide an image url and try again.')


# psTest8Core#23a
