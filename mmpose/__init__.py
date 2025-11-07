# Copyright (c) OpenMMLab. All rights reserved.
from importlib.metadata import version

import mmcv
import mmengine
from mmengine.utils import digit_version

mmcv_minimum_version = '2.0.0rc4'
mmcv_maximum_version = '3.0.0'
mmcv_version = digit_version(version("mmcv"))

mmengine_minimum_version = '0.6.0'
mmengine_maximum_version = '1.0.0'
mmengine_version = digit_version(version("mmengine"))

assert (mmcv_version >= digit_version(mmcv_minimum_version)
        and mmcv_version <= digit_version(mmcv_maximum_version)), \
    f'MMCV=={version("mmcv")} is used but incompatible. ' \
    f'Please install mmcv>={mmcv_minimum_version}, <={mmcv_maximum_version}.'

assert (mmengine_version >= digit_version(mmengine_minimum_version)
        and mmengine_version <= digit_version(mmengine_maximum_version)), \
    f'MMEngine=={version("mmengine")} is used but incompatible. ' \
    f'Please install mmengine>={mmengine_minimum_version}, ' \
    f'<={mmengine_maximum_version}.'
