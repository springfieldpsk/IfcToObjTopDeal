import os
import sys
import subprocess
import zipfile

try:
    import ifcopenshell
except ImportError:
    try:
        with zipfile.ZipFile("ifcopenshell-python-39-v0.6.0-517b819-win64.zip",'r') as zf:
            zf.extractall(sys.path[5])
        import ifcopenshell
    except ImportError:
        raise Exception("Import Error")
# 导入ifcopenshell库

in_file_path = 'newPro.obj'
out_file_path = 'res.obj'
ifc_file_path = 'newPro.ifc'


def swap(t1,t2):
    return t2,t1


def guid_to_def(ifc_guid):
    product = ifc_file.by_guid(ifc_guid)
    if product.is_a('IfcBeam') or product.is_a('IfcPlate'):
        for definition in product.IsDefinedBy:
            if definition.is_a('IfcRelDefinesByProperties'):
                property_set = definition.RelatingPropertyDefinition
                if property_set.is_a('IfcPropertySet'):
                    for pro_perty in property_set.HasProperties:
                        if pro_perty.is_a('IfcPropertySingleValue'):
                            if pro_perty.NominalValue is not None:
                                if pro_perty.NominalValue.is_a('IfcIdentifier'):
                                    return pro_perty.NominalValue.wrappedValue
        return "!cal_error"
    else:
        return "!type_error"
# 通过ifc_guid获取定义标号

def convert_ifc_to_obj(file_path):
    subprocess.run(".\\IfcConvert.exe --use-element-guids " + ".\\" + file_path + " .\\" + in_file_path)
# ifc转换至obj文件

# 待修改 添加URL下载类库与IfcConvert
if __name__ == '__main__':

    if os.path.exists(ifc_file_path) == False:
        raise Exception("ifc 文件不存在")

    convert_ifc_to_obj(ifc_file_path)

    if os.path.exists(in_file_path) == False:
        raise Exception("文件转换失败")

    try:
        read_file = open(in_file_path, 'r')
        res_file = open(out_file_path, 'w')
        ifc_file = ifcopenshell.open(ifc_file_path)
    except Exception as e:
        raise Exception("IO 错误")

    for line in read_file.readlines():
        line = line.strip('\n')
        v = line.split(' ')
        if v[0] == 'v' or v[0] == 'vt':
            v[2] = -1 * float(v[2]) 
            v[2],v[3] = swap(v[2],v[3])
            v[3] = str(v[3])
            # 调整坐标系结果至正确值
        elif v[0] == 'g':
            ifc_guid = v[1]
            # print(guid_to_def(ifc_guid))
            v[1] = guid_to_def(ifc_guid)
            # 解析目标物体
        out_line = ""
        for t in v:
            out_line += t + ' '
        out_line = out_line[:-1] + '\n'

        res_file.write(out_line)

    read_file.close()
    res_file.close()
    

