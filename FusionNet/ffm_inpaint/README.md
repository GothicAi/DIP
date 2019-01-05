环境配置：
python3
tensorflow=1.3.0
pytorch=0.4.1

训练：
因为已经将程序完全封装，所以baseline，mixinpaint，addmask三个版本的框架运行方式几乎完全一样，只有addmask需要多加一步处理被添加的mask。

首先修改config/inpaint_places2_sagan.yml下一些参数，对跑通代码而言比较重要的有如下几个：
2行DATASET：选择'places2'
32行NUM_GPUS: N 表示用N个gpu运行
33行GPU_ID: [a, b, ...] 表示用a, b, ...号卡运行
DATA_FLIST: 路径设置

构建train和val的filelist，对于train_filelist下是每个图片的路径，对于test_filelist下是每个mask对应pkl文件的路径，如flist_sample.flist文件所示
对addmask需要进行额外一步操作，data/inpaint_dataset.py 100-117行，指定maskdir以及选择mask的策略，这里maskdir下放置的是mask图片而非pkl文件

运行run_inpaint_sa.sh

测试：
val的结果可以在result_logs下看到

对于测试，需要在test文件夹下进行操作
首先配置config/test_places2_sagan.yml，配置过程与train类似
需要注意这里需要将第9行MODEL_RESTORE设置为当前所用model路径，GPU_IDS需要为一个有两个元素的list
之后生成与train类似的flist
运行test_inpaint.sh