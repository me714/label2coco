import json


# 根据all_points_x|all_points_y求坐标和宽高
def extremum_value(all_points):
    max_num = max(all_points)
    min_num = min(all_points)
    return min_num, max_num - min_num


# 将label_me的json文件中异形框转化成矩形框
def read_json(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    via_img_data = json_data['_via_img_metadata']
    for photo in via_img_data:
        img_regions = via_img_data[photo]['regions']
        for reg in img_regions:
            model = reg['shape_attributes']
            if model['name'] == 'polyline':
                model['name'] = 'rect'
                all_points_x = model['all_points_x']
                all_points_y = model['all_points_y']

                if all_points_x == []:
                    print(photo)
                    continue
                if all_points_y == []:
                    print(photo)
                    continue
                x, width = extremum_value(all_points_x)
                y, height = extremum_value(all_points_y)
                model['x'] = x
                model['y'] = y
                model['width'] = width
                model['height'] = height
    json_data['_via_img_metadata'] = via_img_data
    # 在这里填写输出json路径
    with open('D:/2.json', 'w', encoding='utf-8') as f:
        json.dump(json_data, f)
        print('------json内容格式整理完毕')


if __name__ == '__main__':
    # 需要处理的json
    read_json(r'D:/1.json')
