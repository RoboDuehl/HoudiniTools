import hou 
import sys 

hip_file = sys.argv[1]
input_file = sys.argv[2]

hou.hipFile.load(hip_file)

file_node = hou.node("/obj/file1/file1")
file_node.parm("file").set(input_file) 

# change_node = hou.node("/obj/topnet1/ropgeometry1/s/s/python1")
# change_node.parm("maintainstate").set(1) r

name_node = hou.node("/obj/file1/setname")
name_node.parm("name").set(input_file + "remeshed.test.bgeo.sc")



export_node = hou.node("/obj/file1/filecache1")
export_node.parm("file").set(input_file + "remeshed.test.sc")
export_node.parm("execute").pressButton()