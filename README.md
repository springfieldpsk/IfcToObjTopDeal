# 思路

## 库使用

### C/C++

- obj模型库 tiny_obj_loader
- 数学库 glm

### python

- ifcOpenShell ifc数据解释库
- os
- sys
- subprocess
- zipfile

## 数据预处理

通过ifcConvert将ifc文件转换为obj文件，通过python脚本对obj文件进行预处理

- 转换坐标系，交换y,z轴，并翻转z轴
- 将Beam与Plate的Guid转换为注释标号

输出结果obj

## 数据输入/清理

通过ting_obj载入obj模型，对于单个实体，整合所有法向量相同的三角面并合并为一个面，利用包围盒确定面的长和宽，通过长宽阈值剔除多余面

## 数据输出

数据以csv格式输出,输出处理后的面编号与点坐标

## 模块化

- 数据读入模块 `ObjLoaderIn`
- 数据处理模块 `ObjDeal`
- 数据输出模块 `ObjWriteOut`

以动态链接库存在，通过最终通过python在主程序中调用
