# 这个新的配置文件继承自一个原始配置文件，只需要突出必要的修改部分即可
_base_ = '/home/cv_user1/Desktop/mmdetection/configs/mask2former/mask2former_r50_lsj_8x2_50e_coco.py'
num_things_classes = 12
num_stuff_classes = 0
num_classes = num_things_classes + num_stuff_classes
model = dict(
    panoptic_head=dict(
        num_things_classes=num_things_classes,
        num_stuff_classes=num_stuff_classes,
        loss_cls=dict(class_weight=[1.0] * num_classes + [0.1])),
    panoptic_fusion_head=dict(
        num_things_classes=num_things_classes,
        num_stuff_classes=num_stuff_classes),
    test_cfg=dict(panoptic_on=False))
# 我们需要对头中的类别数量进行修改来匹配数据集的标注

# 修改数据集相关设置
dataset_type = 'CocoDataset'
classes = ("FD", "RS", "JCRF", "JM1", "JM2", "JHS1", "JHS2", "FS", "BSRF", "JDY", "HBS", "NLS", )
root_path = '/home/cv_user1/Desktop/mmdetection/'
data = dict(
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

# 我们可以使用预训练的 Mask R-CNN 来获取更好的性能
load_from = root_path + 'checkpoints/mask2former_r50_lsj_8x2_50e_coco_20220506_191028-8e96e88b.pth'