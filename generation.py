import argparse
import bpy
import bmesh
import os
import sys

class GenBlender():
    def create_objects(self):
        objs = []
        for obj in self.all_objects:
            if obj.name.endswith('Body'):
                objs.append(obj)
                print(obj)
            
        return objs
    
    def __init__(self, args):
        self.blenderModel = args.blenderModel
        self.outputFolder = args.outputFolder
        self.CAMERA = args.CAMERA
        self.SETRAIN = args.SETRAIN
        self.SETFOG = args.SETFOG
        self.SETTREE = args.SETTREE
        self.SETPOLE = args.SETPOLE
        self.SETDAY = args.SETDAY
        self.options = ['Car_07','Car_03','Car_05', 'Car_08', 'Bus_03', 'Bus_04', 'Truck_04', 'Truck_02']
        print('Render configuration')
        print('Model=', self.blenderModel)
        print('Camera=', self.CAMERA)
        print('Rain=', self.SETRAIN)
        print('Fog=', self.SETFOG)
        print('Tree=', self.SETTREE)
        print('Pole=', self.SETPOLE)
        print('Day=', self.SETDAY)
        
        self.scene = bpy.data.scenes['Scene']
        self.all_objects = bpy.data.collections[self.blenderModel].all_objects[:]
        self.objects = self.create_objects()
        
   
        self.dir = str(self.blenderModel) + '_' + 'cam' + str(self.CAMERA) + '_' + 'rain' + str(self.SETRAIN) + '_' + 'fog' + str(self.SETFOG) + '_' + 'tree' + str(self.SETTREE) + '_' + 'cables' + str(self.SETPOLE) + '_' + 'day' + str(self.SETDAY)
        filepath = self.outputFolder
        self.path = os.path.join(filepath, self.dir)
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        
        

####### GENERATE VIDEO SCENE #########
    
    def define_model(self):
        for all_coll in bpy.data.collections:
            if all_coll.name.startswith(('Car', 'Bus', 'Truck')):
                all_coll.hide_render = True
        
        name = self.blenderModel
        coll = bpy.data.collections.get(name)
        if coll:
            coll.hide_render = False
                      

    def define_camera(self):        
        if self.blenderModel in self.options:
            obj_camera1 = bpy.data.objects["Camera.01"]
            self.camera = obj_camera1
            bpy.context.scene.camera = obj_camera1
            obj_camera1.hide_set(False)
            
            if self.CAMERA == 0:
                obj_camera1.location = (4.1518, -6.6965, 6)
                obj_camera1.rotation_euler = (1.0821, 0, 1.2217)
                obj_camera1.data.sensor_width = 5
                
                
            if self.CAMERA == 1:
                obj_camera1.location = (4.1518, -6.6965, 6)
                obj_camera1.rotation_euler = (1477, 0.000001, 0)
                obj_camera1.data.sensor_width = 9
                
        else:
            obj_camera2 = bpy.data.objects["Camera.02"]
            self.camera = obj_camera2
            bpy.context.scene.camera = obj_camera2
            obj_camera2.hide_set(False)
        
            if self.CAMERA == 0:
                obj_camera2.location = (-28.806, 20.332, 6)
                obj_camera2.rotation_euler = (1.0995, 0, -1.8849)
                obj_camera2.data.sensor_width = 4
            
            
            if self.CAMERA == 1:
                obj_camera2.location = (-28.806, 20.332, 6)
                obj_camera2.rotation_euler = (25.7785, -0.00342, 3.14159)
                obj_camera2.data.sensor_width = 9
            
       

    def define_rain(self):
        rain_object = bpy.data.objects["Plane"]
        rain_object.hide_set(False)
        ps = rain_object.particle_systems['ParticleSystem.001']
        
        ps.settings.count = int(self.SETRAIN)

      
    def define_fog(self):
        fog_object = bpy.data.objects["Fog"]
        fog_object.hide_set(False)
        
        bpy.data.materials['fog_material'].node_tree.nodes['ColorRamp'].color_ramp.elements[0].position = self.SETFOG


    def define_tree(self):
        if self.blenderModel in self.options:
            tree_object1 = bpy.data.objects['tree.01']
            leaves1 = bpy.data.objects['leaves']
            tree_object1.hide_set(False)
            leaves1.hide_set(False)
            
            if self.CAMERA == 0:
                tree_object1.location = (1.1063, -8.7174, 0.539)
                bpy.data.collections['Arvore'].hide_render = False
                bpy.data.collections['Arvore'].hide_viewport = False
                
                tree_object1.location.x = tree_object1.location.x * self.SETTREE
                tree_object1.location.y = tree_object1.location.y
                tree_object1.location.z = tree_object1.location.z
                
                if tree_object1.location.x == 0.0:
                    bpy.data.collections['Arvore'].hide_render = True
                    bpy.data.collections['Arvore'].hide_viewport = True
                
            if self.CAMERA == 1:
                tree_object1.location = (2.5124, -8.7174, 0.539)
                
                tree_object1.location.x = tree_object1.location.x * self.SETTREE
                tree_object1.location.y = tree_object1.location.y 
                tree_object1.location.z = tree_object1.location.z
                
                if tree_object1.location.x == 0.0:
                    bpy.data.collections['Arvore'].hide_render = True
                    bpy.data.collections['Arvore'].hide_viewport = True
                    
                    
        else:
            tree_object2 = bpy.data.objects['tree.02']
            leaves2 = bpy.data.objects['leaves']
            tree_object2.hide_set(False)
            leaves2.hide_set(False)
            
            if self.CAMERA == 0:
                tree_object2.location = (-30.933, 21.9159, 0.53900)
                bpy.data.collections['Arvore'].hide_render = False
                bpy.data.collections['Arvore'].hide_viewport = False
                
                tree_object2.location.x = tree_object2.location.x * self.SETTREE
                tree_object2.location.y = tree_object2.location.y
                tree_object2.location.z = tree_object2.location.z
                
                if tree_object2.location.x == 0.0:
                    bpy.data.collections['Arvore'].hide_render = True
                    bpy.data.collections['Arvore'].hide_viewport = True
                
            if self.CAMERA == 1:
                tree_object2.location = (-31.8863, 21.9159, 0.53900)
                
                tree_object2.location.x = tree_object2.location.x * self.SETTREE
                tree_object2.location.y = tree_object2.location.y 
                tree_object2.location.z = tree_object2.location.z
                
                if tree_object2.location.x == 0.0:
                    bpy.data.collections['Arvore'].hide_render = True
                    bpy.data.collections['Arvore'].hide_viewport = True
                        
                
    def define_cables(self):
        if self.blenderModel in self.options:
            pole_object = bpy.data.objects['cables.01']
            pole_object.hide_set(False)
        
            if self.CAMERA == 0:
                pole_object.rotation_euler = (0,0, -1.5708)
                pole_object.location = (0.8074, -7.2407, 2.1275)
                
                bpy.data.collections['Cabos'].hide_render = False
                bpy.data.collections['Cabos'].hide_viewport = False

                pole_object.location.x = pole_object.location.x
                pole_object.location.y = pole_object.location.y * self.SETPOLE
                pole_object.location.z = pole_object.location.z
                
                if pole_object.location.y == 0.0:
                    bpy.data.collections['Cabos'].hide_render = True
                    bpy.data.collections['Cabos'].hide_viewport = True
            
            
            if self.CAMERA == 1:
                pole_object.rotation_euler = (0,0, -1.5708)
                pole_object.location = (0.8074, -7.5596, 2.1275)
                bpy.data.collections['Cabos'].hide_render = False
                bpy.data.collections['Cabos'].hide_viewport = False
        
                pole_object.location.x = pole_object.location.x * self.SETPOLE
                pole_object.location.y = pole_object.location.y
                pole_object.location.z = pole_object.location.z
                
                if pole_object.location.x == 0.0:
                    bpy.data.collections['Cabos'].hide_render = True
                    bpy.data.collections['Cabos'].hide_viewport = True
                    
        else:
            pole_object = bpy.data.objects['cables.02']
            pole_object.hide_set(False)
            
            if self.CAMERA == 0:
                pole_object.rotation_euler = (0,0, -1.5707)
                pole_object.location = (-24.5529, 21.0736, 2.1275)
                
                bpy.data.collections['Cabos'].hide_render = False
                bpy.data.collections['Cabos'].hide_viewport = False

                pole_object.location.x = pole_object.location.x
                pole_object.location.y = pole_object.location.y * self.SETPOLE
                pole_object.location.z = pole_object.location.z
                
                if pole_object.location.y == 0.0:
                    bpy.data.collections['Cabos'].hide_render = True
                    bpy.data.collections['Cabos'].hide_viewport = True
            
            
            if self.CAMERA == 1:
                pole_object.rotation_euler = (0,0, -1.5707)
                pole_object.location = (-24.5529, 20.9799, 2.1275)
                bpy.data.collections['Cabos'].hide_render = False
                bpy.data.collections['Cabos'].hide_viewport = False
        
                pole_object.location.x = pole_object.location.x * self.SETPOLE
                pole_object.location.y = pole_object.location.y
                pole_object.location.z = pole_object.location.z
                
                if pole_object.location.x == 0.0:
                    bpy.data.collections['Cabos'].hide_render = True
                    bpy.data.collections['Cabos'].hide_viewport = True
               
               
    def define_daytime(self):
        light_area_01 = bpy.data.objects['Area.01']
        light_point_01 = bpy.data.objects['Point.01']
        light__area_02 = bpy.data.objects['Area.02']
        light_point_02 = bpy.data.objects['Point.02']
        scene = bpy.context.scene
        
        if self.SETDAY == 0: 
            night = scene.view_settings.view_transform = 'Raw'
            light_area_01.hide_render = False
            light_area_01.hide_viewport = False
            light_point_01.hide_render = False
            light_point_01.hide_viewport = False
            light__area_02.hide_render = False
            light__area_02.hide_viewport = False
            light_point_02.hide_render = False
            light_point_02.hide_viewport = False
        
        elif  self.SETDAY== 1: 
            day = scene.view_settings.view_transform = 'Filmic'
            light_area_01.hide_render = True
            light_area_01.hide_viewport = True
            light_point_01.hide_render = True
            light_point_01.hide_viewport = True
            light__area_02.hide_render = True
            light__area_02.hide_viewport = True
            light_point_02.hide_render = True
            light_point_02.hide_viewport = True
            
    
    
    def render(self):
        output_dir = self.outputFolder
        bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
        bpy.context.scene.render.ffmpeg.format = 'MPEG4'
        filext = bpy.context.scene.render.image_settings.file_format
    
        filename = self.dir
           
        bpy.context.scene.render.filepath = os.path.join(output_dir, filename + '.mp4')
        bpy.context.scene.frame_set(1)
        bpy.ops.render.render(animation=True)
        print('Finished!')
        


####### FIND BOUNDING BOXES #########

                
    def find_bounding_box(self, obj): #coordenadas em  relação ao enquadramento da camera
        matrix = self.camera.matrix_world.normalized().inverted()
        mesh = obj.to_mesh(preserve_all_data_layers=True)
        mesh.transform(obj.matrix_world)
        mesh.transform(matrix)


        frame = [-v for v in self.camera.data.view_frame(scene=self.scene)[:3]]

        lx = []
        ly = []

        for v in mesh.vertices:
            co_local = v.co
            z = -co_local.z

            if z <= 0.0:    
                continue
            
            else:
        
                frame = [(v / (v.z / z)) for v in frame]

            min_x, max_x = frame[1].x, frame[2].x
            min_y, max_y = frame[0].y, frame[1].y

            x = (co_local.x - min_x) / (max_x - min_x)
            y = (co_local.y - min_y) / (max_y - min_y)

            lx.append(x)
            ly.append(y)

        if not lx or not ly:
            return None

        min_x = np.clip(min(lx), 0.0, 1.0)
        min_y = np.clip(min(ly), 0.0, 1.0)
        max_x = np.clip(max(lx), 0.0, 1.0)
        max_y = np.clip(max(ly), 0.0, 1.0)

        if min_x == max_x or min_y == max_y:
            return None
            
        coord_list = [min_x, min_y, max_x, max_y]
        if min(coord_list) == 0.0:
            indexmin = coord_list.index(min(coord_list))
            coord_list[indexmin] = coord_list[indexmin] + 0.0000001
        return (min_x, min_y), (max_x, max_y)
    

    def clamp(self, x, minimum, maximum):
        return max(minimum, min(x, maximum))


    def camera_view_bounds_2d(self, scene, cam_object, mesh_object):
        matrix = cam_object.matrix_world.normalized().inverted()
        depsgraph = bpy.context.evaluated_depsgraph_get() 
        mesh_eval = mesh_object.evaluated_get(depsgraph)

        # A new mesh data block is created, using the i
        mesh = mesh_eval.to_mesh() 
        mesh.transform(mesh_object.matrix_world)
        mesh.transform(matrix)

        camera = cam_object.data

        # Get the world coordinates for the camera frame boun
        frame = [-v for v in camera.view_frame(scene=scene)[:3]] 

        #For perspective camera you need to do a transformation
        camera_persp = camera.type != 'ORTHO'

        lx = []
        ly = []

        for v in mesh.vertices: #so you loop over all the vertices of the object (for cube 8)
            co_local = v.co #Extract locations of the object in the object reference frame
            z = -co_local.z 

            if camera_persp:
                if z == 0.0:
                    lx.append(0.5)
                    ly.append(0.5)
                if z <= 0.0:
                    """ Vertex is behind the camera; ignore it. """
                    continue
                else:
                    # Perspective division - I think this makes it into homogeneous coordinates (divide by homogeneous w component)
                    frame = [(v / (v.z / z)) for v in frame] #v.z is the camera frame coordinates world, so you loop through frame (line 46) and then 
            #I think this decides on the size of the camera frame in world coordinates
            min_x, max_x = frame[1].x, frame[2].x
            min_y, max_y = frame[0].y, frame[1].y

            # max_x - min_x is the width, so you find the vertex location, minus the min location (the size of image), therefore x always positive in image reference frame.
            
            # max_y - min_y is the height of the camera frame (image) and then with origin of system in top left corner you will always have a positive y coordinate if in the image. This process is done for each vertex. This is normalized (dividing by width or height)
            x = (co_local.x - min_x) / (max_x - min_x)
            y = (co_local.y - min_y) / (max_y - min_y)
            
            #So you append the x,y location of the vertex in the image reference frame
            lx.append(x)
            ly.append(y)

        mesh_eval.to_mesh_clear()

        """ Image is not in view if all the mesh verts were ignored """
        if not lx or not ly:
            return None

        #What this does is you check all the vertices and then you calculate the image frame coordinate corresponding to it. 
        min_x = self.clamp(min(lx), 0.0, 1.0)
        max_x = self.clamp(max(lx), 0.0, 1.0)
        min_y = self.clamp(min(ly), 0.0, 1.0)
        max_y = self.clamp(max(ly), 0.0, 1.0)
        
        mesh_eval.to_mesh_clear()

        """ Figure out the rendered image size """
        r = scene.render
        fac = r.resolution_percentage * 0.01
        dim_x = r.resolution_x * fac
        dim_y = r.resolution_y * fac

        """ Image is not in view if both bounding points exist on the same side """
        if round((max_x - min_x) * dim_x) == 0 or round((max_y - min_y) * dim_y) == 0:
            return None

        
        id = mesh_object.pass_index
        #x = round(min_x * dim_x)
        y1 = round(dim_y - min_y * dim_y)
        y2 = round(dim_y - max_y * dim_y)
        y = (y1+y2)/2
        x = ((min_x + max_x)/2) * dim_x
        w = round((max_x - min_x) * dim_x)
        h = round((max_y - min_y) * dim_y)
        
        
        id = mesh_object.pass_index
        x = x/dim_x
        y = y/dim_y
        w = w/dim_x
        h = h/dim_y
                
        results = str(id) + ' ' + str(x) + ' ' + str(y) + ' ' + str(w) + ' ' + str(h)
 
        return results
                
    def get_coordinates(self):
        output_dir = self.path
        for frame in range(self.scene.frame_start, self.scene.frame_end+1):
            self.scene.frame_set(frame)
            labels = os.path.join(output_dir, str(self.blenderModel) + '_' + str(frame).zfill(4) + '.txt')
            with open(labels, 'w') as fp:
                for i, objct in enumerate(self.objects):
                    b_box = self.camera_view_bounds_2d(self.scene, self.camera, objct)
                    print(b_box)
                    if b_box:  
                        fp.write(b_box)                                                  
                    else:
                        pass
                    
                    
                    
    def render_frames(self):
        output_dir = self.path
        bpy.context.scene.render.image_settings.file_format = 'PNG'
        filext = bpy.context.scene.render.image_settings.file_format
              
        for i in range(self.scene.frame_start, self.scene.frame_end+1):
            filepath = os.path.join(output_dir, str(self.blenderModel) + '_' + str(i).zfill(4))           
            
            if os.path.isfile(filepath + filext):
                print('File exists, skipping to next...')
            else:
                self.scene.render.filepath = filepath
                self.scene.frame_set(i)
                bpy.ops.render.render(write_still=True)
                
        self.scene.render.filepath = output_dir
        print('Finished!')


def parse_args(argv=None):
    parser = argparse.ArgumentParser(prog='generate_blender')
    parser.add_argument('-c', '--CAMERA', type=int, help='defines camera angle (0:oblique, 1:parallel). Default=%(default)d', default=1)
    parser.add_argument('-r', '--SETRAIN', type=float, help='define rain intensity (number of water drops). Default=%(default).1f', default=3000)
    parser.add_argument('-f', '--SETFOG', type=float, help='define fog intensity (1: no fog, 0: complete fog ). Default=%(default).1f', default=0.7)
    parser.add_argument('-t', '--SETTREE', type=float, help='define tree occlusion percentage. Default=%(default).1f', default=0.1)
    parser.add_argument('-p', '--SETPOLE', type=float, help='define light pole occlusion percentage. Default=%(default).1f', default=0)
    parser.add_argument('-d', '--SETDAY', type=float, help='defines lighting (0:night, 1:day). Default=%(default)d', default=1)
    parser.add_argument('blenderModel', type=str, help='blender collection containing 3D model to be used')
    parser.add_argument('outputFolder', type=str, help='path to output folder')
    
    if argv == None:
        return parser.parse_args()
    else:
        return parser.parse_args(argv)

if __name__ == '__main__':

    argv = sys.argv
    try:
        index = argv.index("--") + 1
    except ValueError:
        index = len(argv)

    argv = argv[index:]
    args = parse_args(argv)

    g = GenBlender(args)

    g.define_model()
    g.define_camera()
    g.define_rain()
    g.define_fog()
    g.define_tree()
    g.define_cables()
    g.define_daytime()
    #g.render()
    
    g.get_coordinates()
    #g.render_frames()