环境配置：
python3
tensorflow>=1.3
neuralgym：pip install git+https://github.com/JiahuiYu/neuralgym

因为已经将程序完全封装，所以baseline，mix，spectrum三个版本的框架运行方式完全一样。

训练：
首先修改inpaint.yml下一些参数，对跑通代码而言比较重要的有如下几个：
2行DATASET：选择'places2'
23行NUM_GPUS: N 表示用N个gpu运行
24行GPU_ID: [a, b, ...] 表示用a, b, ...号卡运行
DATA_FLIST: 路径设置

其中DATA_FLIST是一个文件，内部每行是每个图像的路径，样例如本目录下validation_static_view.flist

之后直接运行python train.py即可


测试：
val样例可以直接通过tensorboard来查看

单独对一张图片进行测试可运行：
python test.py --image image.jpg --mask mask.jpg --output output.jpg --checkpoint model_logs/your_model_dir

对批量图片处理可以运行：
python test_batch.py --img_dir imageDir --mask_dir maskDir --output_dir outputDir --checkpoint_dir model_logs/your_model_dir