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

## 数据预处理 √

通过ifcConvert将ifc文件转换为obj文件，通过python脚本对obj文件进行预处理

- 转换坐标系，交换y,z轴，并翻转z轴
- 将Beam与Plate的Guid转换为注释标号

输出结果obj

## 数据输入/清理

通过ting_obj载入obj模型

## 数据处理

对于单个实体，生成多个点集，每个点集存在两个基础点与基础法向量，来自点集生成时的第一个三角面片

具体实现：

将点与已存在点集相匹配，测试是否加入点集，若没有可加入的点集，则基于基础三角形生成新的点集

## 数据输出

数据以csv格式输出,输出处理后的面编号与点集各点坐标

## 模块化

- 数据读入模块 `ObjLoaderIn`
- 数据处理模块 `ObjDeal`
- 数据输出模块 `ObjWriteOut`

以动态链接库存在，通过最终通过python在主程序中调用
