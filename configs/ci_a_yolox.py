# 这个新的配置文件继承自一个原始配置文件，只需要突出必要的修改部分即可
_base_ = '/home/cv_user1/Desktop/mmdetection/configs/yolox/yolox_l_8x8_300e_coco.py'

# 我们需要对头中的类别数量进行修改来匹配数据集的标注
model = dict(
        bbox_head=dict(num_classes=12))

# 修改数据集相关设置
dataset_type = 'CocoDataset'
classes = ("FD", "RS", "JCRF", "JM1", "JM2", "JHS1", "JHS2", "FS", "BSRF", "JDY", "HBS", "NLS", )
data_root = '/home/cv_user1/Desktop/mmdetection/'
train_dataset = dict(
    type='MultiImageMixDataset',
    dataset=dict(
        type=dataset_type,
        ann_file=data_root + 'dataset/train_a.json',
        img_prefix=data_root + 'dataset/train_img/',
        pipeline=[
            dict(type='LoadImageFromFile'),
            dict(type='LoadAnnotations', with_bbox=True)
        ],
        filter_empty_gt=False,
    ))


data = dict(
    samples_per_gpu=12,
    workers_per_gpu=4,
    persistent_workers=True,
    train=train_dataset,
    val=dict(
        type=dataset_type,
        ann_file=data_root + 'dataset/valid_a.json',
        img_prefix=data_root + 'dataset/val_img/'),
    test=dict(
        type=dataset_type,
        ann_file=data_root + 'dataset/test_a.json',
        img_prefix=data_root + 'dataset/test_img/'))
optimizer = dict(
    type='SGD',
    lr=0.001,
    momentum=0.9,
    weight_decay=5e-4,
    nesterov=True,
    paramwise_cfg=dict(norm_decay_mult=0., bias_decay_mult=0.))
# 我们可以使用预训练的 Mask R-CNN 来获取更好的性能
load_from = data_root + 'checkpoints/yolox_l_8x8_300e_coco_20211126_140236-d3bd2b23.pth'