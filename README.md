说明文档：
--byproductCode
    --colorStyleTransfer    颜色模式转换相关程序
    --watermark             去除水印相关程序
--FusionNet
    --bbx_inpaint           mask为矩形的inpainting框架
        --baseline          原始框架
        --mix               FusionNet框架
        --specturm          加了spectral normalization之后的框架
        --test_batch        批量inpainting程序，生成bbx_inpainting的结果
    --ffm_inpaint           mask为任意形状的inpainting框架
        --addmask           附加额外mask的框架
        --baseline          原始框架
        --mixinpaint        FusionNet框架
        --test              测试框架，生成ffm_inpainting的结果
--mask_generator
        --char              生成ICDAR mask dataset所用程序
        --coco              生成COCO mask dataset所用程序
--utils                     内部是一些过程中使用的功能函数，用来处理数据等等，不是主要程序
--result                    一些结果样例



实验数据：
inpainting所用数据集：
Places2：http://places2.csail.mit.edu/；在此网站上可以下载，用small images训练会快一些，共24G

生成mask所用数据集：
COCO：http://cocodataset.org/#home  
VOC：https://pjreddie.com/projects/pascal-voc-dataset-mirror/   
ICDAR：http://www.iapr-tc11.org/mediawiki/index.php/ICDAR_2003_Robust_Reading_Competitions



实验结果：在result文件夹下
搭建环境：见每个文件目录下的README
使用方式：见每个文件目录下的README


注1：搭载环境和使用方式仅针对byproductCode，FusionNet和mask_generator；对于utils，内部代码为一些过程代码，比较散，所以也不详细介绍搭建环境和使用方式
注2：因为python一些库如tensorflow与CUDA和CUDNN版本相关，所以搭载环境内的库版本号可能在不同环境下是不同的