# 这个新的配置文件继承自一个原始配置文件，只需要突出必要的修改部分即可
_base_ = '/home/cv_user1/Desktop/mmdetection/configs/mask_rcnn/mask_rcnn_r50_caffe_fpn_1x_coco.py'

# 我们需要对头中的类别数量进行修改来匹配数据集的标注
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=12),
        mask_head=dict(num_classes=12)))

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

lr_config = dict(step=[28, 34])
runner = dict(type='EpochBasedRunner', max_epochs=36)

# 我们可以使用预训练的 Mask R-CNN 来获取更好的性能
load_from = root_path + 'checkpoints/mask_rcnn_r50_caffe_fpn_1x_coco_bbox_mAP-0.38__segm_mAP-0.344_20200504_231812-0ebd1859.pth'