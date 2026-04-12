import os
import hou 

class UsdMigrationUtils: 

    def __init__(self):
        pass

    def test(self):
        print("This is a test method in UsdMigrationUtils class.")
    
    def createMainTemplate(self, dir_path):
        print(f"Creating main template in directory: {dir_path}")

        fbx_file = [file for file in os.listdir(dir_path) if file.endswith(".fbx")][0] 
        print(fbx_file)

        #sobcreat lop 
        root_path = "/stage"
        sopcreate_lop = hou.node(root_path).createNode("sopcreate", "asset01")
        sopcreate_lop.parm("enable_partitionattribs").set(0)

        #file sop
        file_sop = hou.node(sopcreate_lop.path() + "/sopnet/create").createNode("file")
        file_sop.parm("file").set(dir_path + "/" + fbx_file)

        #for loop 
        for_each_begin = file_sop.createOutputNode("block_begin", "foreach_begin1")
        for_each_begin.parm("method").set(1)
        for_each_begin.parm("blockpath").set("../foreach_end1")
        for_each_begin.parm("createmetablock").pressButton()
        meta_node = hou.node(for_each_begin.parent().path() + "/foreach_begin1_metadata1")
        meta_node.parm("blockpath").set("../foreach_end1")

        #atttribute wrangle sop
        attri_wrangele = for_each_begin.createOutputNode("attribwrangle")
        attri_wrangele.setInput(1,meta_node)
        attri_wrangele.parm("class").set(1)
        attri_wrangele.parm("snippet").set('string assets[] = {"leaves","trunk","twigs", leaves_small"}\n s@path = "/" + assets[detail(1,"iteration")];')

        #foreach end
        for_each_end = attri_wrangele.createOutputNode("block_end", "foreach_end1")
        for_each_end.parm("itermethod").set(1)
        for_each_end.parm("class").set(0)
        for_each_end.parm("method").set(1)
        for_each_end.parm("useattrib").set(1)
        for_each_end.parm("attrib").set("shop_materialpath")
        for_each_end.parm("blockpath").set("../foreach_begin1")
        for_each_end.parm("templatepath").set("../foreach_begin1")

        #attrib delete
        att_delete = for_each_end.createOutputNode("attribdelete")
        att_delete.parm("ptdel").set("fbx_rotation fbx_scale fbx_translation")
        att_delete.parm("primdel").set("shop_materialpath MaxHandle name")

        #output flag 
        output_flag = att_delete.createOutputNode("output")

        #create primitve lop 
        primitive_lop = hou.node(root_path).createNode("primitive")
        primitive_lop.parm("primpath").set("/asset01")
        primitive_lop.parm("primkind").set("component")

        #graft stages
        graft_stages_lop = primitive_lop.createOutputNode("graftstages")
        graft_stages_lop.setNextInput(sopcreate_lop)
        graft_stages_lop.parm("primkind").set("subcomponent")
        
        #materials lop
        materials = ["leaves", "leaves_small", "trunk", "twigs"]
        materiallib_lob = graft_stages_lop.createOutputNode("materiallibrary")
        materiallib_lob.parm("materials").set(len(materials))      

        for i, material in enumerate(materials):
            materiallib_lob.parm(f"matname{i+1}").set(material)
            materiallib_lob.parm(f"matpath{i+1}").set(f"/asset01/materials/{material}_mat")
            materiallib_lob.parm(f"assign{i+1}").set(1)
            materiallib_lob.parm(f"geopath{i+1}").set(f"/asset01/materials/{material}")

            #set mat network inside
            mat_network = houd.node()materiallib_lob.path()).createNode("subnet", material)

            # texture maps and nodes
            usd_uv_texture = hou.node(mat_network.path()).createNode("usduvtextrure::2.0")
            texture_dir_ref = dir_path + "/maps"

            if material == "leaves:"
                texture_map_color = [file for file in os.listdir(texture_dir_ref) if file.endswith("_01.jpg")]
            elif material =="trunk"
                texture_map_color = [file for file in os.listdir(texture_dir_ref) if file.endswith("_02.jpg")]
            elif material == "twigs":
                texture_map_color = [file for file in os.listdir(texture_dir_ref) if file.endswith("_03.jpg")]
            elif material == "leaves_small":
                texture_map_color = [file for file in os.listdir(texture_dir_ref) if file.endswith("_04.jpg")]

            usd_uv_texture.parm("file").set(texture_dir_ref + "/" + texture_map_color) 

            mtlsurface = houd.node(mat_network.path()).createNode("mtlxstandard_surface")
            output_ref = houd.node(mat_network.path()).createNode("/suboutput1")

            usd_uv_texture.output = usd_uv_texture.outputIndex("rgb")
            mtlsurgace_input = mtlsurface.inputIndex("base_color")
            mtlsurgace_output = mtlsurface.outputIndex("out")

            mtlsurface.setInput(mtlsurgace_input, usd_uv_texture, usd_uv_texture_output)   
            output_ref.setNextInput(mtlsurface, mtlsurface_output)
            break
      

        
