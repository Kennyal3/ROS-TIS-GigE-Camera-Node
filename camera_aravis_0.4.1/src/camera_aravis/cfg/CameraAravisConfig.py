## *********************************************************
## 
## File autogenerated for the camera_aravis package 
## by the dynamic_reconfigure package.
## Please do not edit.
## 
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 245, 'name': 'Default', 'parent': 0, 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [], 'parameters': [{'srcline': 273, 'description': 'Acquire', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'Acquire', 'edit_method': '', 'default': True, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 273, 'description': 'Automatic exposure', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'ExposureAuto', 'edit_method': "{'enum_description': 'Automatic Settings', 'enum': [{'srcline': 14, 'description': 'Use Manual Settings', 'srcfile': '/home/auto3/catkin_ws/src/camera_aravis/cfg/CameraAravisConfig.cfg', 'cconsttype': 'const char * const', 'value': 'Off', 'ctype': 'std::string', 'type': 'str', 'name': 'Off_'}, {'srcline': 15, 'description': 'Recalc Once', 'srcfile': '/home/auto3/catkin_ws/src/camera_aravis/cfg/CameraAravisConfig.cfg', 'cconsttype': 'const char * const', 'value': 'Once', 'ctype': 'std::string', 'type': 'str', 'name': 'Once'}, {'srcline': 16, 'description': 'Recalc Continually', 'srcfile': '/home/auto3/catkin_ws/src/camera_aravis/cfg/CameraAravisConfig.cfg', 'cconsttype': 'const char * const', 'value': 'Continuous', 'ctype': 'std::string', 'type': 'str', 'name': 'Continuous'}]}", 'default': 'Off', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 273, 'description': 'Automatic gain', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'GainAuto', 'edit_method': "{'enum_description': 'Automatic Settings', 'enum': [{'srcline': 14, 'description': 'Use Manual Settings', 'srcfile': '/home/auto3/catkin_ws/src/camera_aravis/cfg/CameraAravisConfig.cfg', 'cconsttype': 'const char * const', 'value': 'Off', 'ctype': 'std::string', 'type': 'str', 'name': 'Off_'}, {'srcline': 15, 'description': 'Recalc Once', 'srcfile': '/home/auto3/catkin_ws/src/camera_aravis/cfg/CameraAravisConfig.cfg', 'cconsttype': 'const char * const', 'value': 'Once', 'ctype': 'std::string', 'type': 'str', 'name': 'Once'}, {'srcline': 16, 'description': 'Recalc Continually', 'srcfile': '/home/auto3/catkin_ws/src/camera_aravis/cfg/CameraAravisConfig.cfg', 'cconsttype': 'const char * const', 'value': 'Continuous', 'ctype': 'std::string', 'type': 'str', 'name': 'Continuous'}]}", 'default': 'Off', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 273, 'description': 'Exposure time (us)', 'max': 1000000.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'ExposureTimeAbs', 'edit_method': '', 'default': 2000.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 273, 'description': 'Gain (%)', 'max': 10000.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'Gain', 'edit_method': '', 'default': 1.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 273, 'description': 'Acquisition Mode', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'AcquisitionMode', 'edit_method': "{'enum_description': 'AcquisitionMode', 'enum': [{'srcline': 18, 'description': 'Capture continuously upon trigger.', 'srcfile': '/home/auto3/catkin_ws/src/camera_aravis/cfg/CameraAravisConfig.cfg', 'cconsttype': 'const char * const', 'value': 'Continuous', 'ctype': 'std::string', 'type': 'str', 'name': 'Continuous_'}, {'srcline': 19, 'description': 'Capture one frame upon trigger.', 'srcfile': '/home/auto3/catkin_ws/src/camera_aravis/cfg/CameraAravisConfig.cfg', 'cconsttype': 'const char * const', 'value': 'SingleFrame', 'ctype': 'std::string', 'type': 'str', 'name': 'SingleFrame'}, {'srcline': 20, 'description': 'Capture multiple frames upon trigger.', 'srcfile': '/home/auto3/catkin_ws/src/camera_aravis/cfg/CameraAravisConfig.cfg', 'cconsttype': 'const char * const', 'value': 'MultiFrame', 'ctype': 'std::string', 'type': 'str', 'name': 'MultiFrame'}]}", 'default': 'Continuous', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 273, 'description': 'Framerate (fps)', 'max': 1000.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'AcquisitionFrameRate', 'edit_method': '', 'default': 100.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 273, 'description': 'TriggerMode', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'TriggerMode', 'edit_method': "{'enum_description': 'On or Off', 'enum': [{'srcline': 11, 'description': 'Off', 'srcfile': '/home/auto3/catkin_ws/src/camera_aravis/cfg/CameraAravisConfig.cfg', 'cconsttype': 'const char * const', 'value': 'Off', 'ctype': 'std::string', 'type': 'str', 'name': 'Off'}, {'srcline': 12, 'description': 'On', 'srcfile': '/home/auto3/catkin_ws/src/camera_aravis/cfg/CameraAravisConfig.cfg', 'cconsttype': 'const char * const', 'value': 'On', 'ctype': 'std::string', 'type': 'str', 'name': 'On'}]}", 'default': 'Off', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 273, 'description': 'Trigger Source', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'TriggerSource', 'edit_method': "{'enum_description': 'TriggerSource', 'enum': [{'srcline': 22, 'description': 'FrameStart triggered via software', 'srcfile': '/home/auto3/catkin_ws/src/camera_aravis/cfg/CameraAravisConfig.cfg', 'cconsttype': 'const char * const', 'value': 'Software', 'ctype': 'std::string', 'type': 'str', 'name': 'Software'}, {'srcline': 23, 'description': 'FrameStart triggered via hardware input 1', 'srcfile': '/home/auto3/catkin_ws/src/camera_aravis/cfg/CameraAravisConfig.cfg', 'cconsttype': 'const char * const', 'value': 'Line1', 'ctype': 'std::string', 'type': 'str', 'name': 'Line1'}, {'srcline': 24, 'description': 'FrameStart triggered via hardware input 2', 'srcfile': '/home/auto3/catkin_ws/src/camera_aravis/cfg/CameraAravisConfig.cfg', 'cconsttype': 'const char * const', 'value': 'Line2', 'ctype': 'std::string', 'type': 'str', 'name': 'Line2'}]}", 'default': 'Line1', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 273, 'description': 'Software Trigger Rate (hz)', 'max': 200.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'softwaretriggerrate', 'edit_method': '', 'default': 100.0, 'level': 0, 'min': 0.01, 'type': 'double'}, {'srcline': 273, 'description': 'FocusPos', 'max': 65535, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'FocusPos', 'edit_method': '', 'default': 32767, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 273, 'description': 'ROS camera frame', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'frame_id', 'edit_method': '', 'default': 'camera', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 273, 'description': 'mtu', 'max': 9000, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'mtu', 'edit_method': '', 'default': 1500, 'level': 0, 'min': 576, 'type': 'int'}], 'type': '', 'id': 0}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])    
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

CameraAravis_Off = 'Off'
CameraAravis_On = 'On'
CameraAravis_Off_ = 'Off'
CameraAravis_Once = 'Once'
CameraAravis_Continuous = 'Continuous'
CameraAravis_Continuous_ = 'Continuous'
CameraAravis_SingleFrame = 'SingleFrame'
CameraAravis_MultiFrame = 'MultiFrame'
CameraAravis_Software = 'Software'
CameraAravis_Line1 = 'Line1'
CameraAravis_Line2 = 'Line2'
