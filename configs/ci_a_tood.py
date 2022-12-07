# 这个新的配置文件继承自一个原始配置文件，只需要突出必要的修改部分即可
_base_ = '/home/cv_user1/Desktop/mmdetection/configs/tood/tood_x101_64x4d_fpn_mstrain_2x_coco.py'

# 我们需要对头中的类别数量进行修改来匹配数据集的标注
model = dict(
    bbox_head=dict(num_classes=12))

# 修改数据集相关设置
dataset_type = 'CocoDataset'
classes = ("FD", "RS", "JCRF", "JM1", "JM2", "JHS1", "JHS2", "FS", "BSRF", "JDY", "HBS", "NLS", )
root_path = '/home/cv_user1/Desktop/mmdetection/'
data = dict(
    samples_per_gpu=4,
    workers_per_gpu=4,
    train=dict(
        img_prefix=root_path + 'dataset/train_img/',
        classes=classes,
        ann_file=root_path + 'dataset/train_a.json'),
    val=dict(
        img_prefix=root_path + 'dataset/val_img/',
        classes=classes,
        ann_file=root_path + 'dataset/valid_a.json'),
    test=dict(
        img_prefix=root_path + 'dataset/test_img/',
        classes=classes,
        ann_file=root_path + 'dataset/test_a.json'))

lr_config = dict(
    policy='step',
    warmup='linear',
    warmup_iters=500,
    warmup_ratio=0.001,
    step=[16, 22])
runner = dict(type='EpochBasedRunner', max_epochs=200)

# 我们可以使用预训练的 Mask R-CNN 来获取更好的性能
load_from = root_path + 'checkpoints/tood_x101_64x4d_fpn_mstrain_2x_coco_20211211_003519-a4f36113.pth'