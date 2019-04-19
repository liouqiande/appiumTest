# -*- coding: utf-8 -*-
import yaml


class OperYaml(object):
    # 获得 yaml 文件数据
    def get_yaml_data(self,file_path):
        with open(file_path,'rb') as f:
            data = f.read()
            yaml_data = yaml.load(data)
        return yaml_data

    # 获取元素定位方式及定位值
    def get_ele_info(self, ele_name, file_path):
        yaml_data = self.get_yaml_data(file_path)
        ele_by = yaml_data.get(ele_name).get("by")
        ele_value = yaml_data.get(ele_name).get("value")
        return ele_by, ele_value