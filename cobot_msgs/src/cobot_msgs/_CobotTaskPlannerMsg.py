# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from cobot_msgs/CobotTaskPlannerMsg.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import cobot_msgs.msg

class CobotTaskPlannerMsg(genpy.Message):
  _md5sum = "869409f2737487bdff4734cc77b19d86"
  _type = "cobot_msgs/CobotTaskPlannerMsg"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int32 mission_id
string currentTask
string currentSubTask
string currentNavigationSubTask
float32 timeBlocked
float32 taskDuration
float32 subTaskDuration
float32 navigationSubTaskDuration
float32 navigationTimeRemaining
float32 timeToDeadline

CobotLocalizationMsg currentDestination
string fromLocation
string toLocation
string objectToFind

bool carryingObject
bool navigating
bool taskCompleted
int32 successValue

bool paused
string owner

================================================================================
MSG: cobot_msgs/CobotLocalizationMsg
float64 timeStamp
float32 x
float32 y
float32 angle
float32 angleUncertainty
float32 locationUncertainty
string map

float64 lastLaserRunTime
float64 laserRunTime
int32 laserNumObservedPoints
int32 laserNumCorrespondences
float32 laserStage0Weights
float32 laserStageRWeights
float32 laserMeanSqError

float64 lastPointCloudRunTime
float64 pointCloudRunTime
int32 pointCloudNumObservedPoints
int32 pointCloudNumCorrespondences
float32 pointCloudStage0Weights
float32 pointCloudStageRWeights
float32 pointCloudMeanSqError

"""
  __slots__ = ['mission_id','currentTask','currentSubTask','currentNavigationSubTask','timeBlocked','taskDuration','subTaskDuration','navigationSubTaskDuration','navigationTimeRemaining','timeToDeadline','currentDestination','fromLocation','toLocation','objectToFind','carryingObject','navigating','taskCompleted','successValue','paused','owner']
  _slot_types = ['int32','string','string','string','float32','float32','float32','float32','float32','float32','cobot_msgs/CobotLocalizationMsg','string','string','string','bool','bool','bool','int32','bool','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       mission_id,currentTask,currentSubTask,currentNavigationSubTask,timeBlocked,taskDuration,subTaskDuration,navigationSubTaskDuration,navigationTimeRemaining,timeToDeadline,currentDestination,fromLocation,toLocation,objectToFind,carryingObject,navigating,taskCompleted,successValue,paused,owner

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(CobotTaskPlannerMsg, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.mission_id is None:
        self.mission_id = 0
      if self.currentTask is None:
        self.currentTask = ''
      if self.currentSubTask is None:
        self.currentSubTask = ''
      if self.currentNavigationSubTask is None:
        self.currentNavigationSubTask = ''
      if self.timeBlocked is None:
        self.timeBlocked = 0.
      if self.taskDuration is None:
        self.taskDuration = 0.
      if self.subTaskDuration is None:
        self.subTaskDuration = 0.
      if self.navigationSubTaskDuration is None:
        self.navigationSubTaskDuration = 0.
      if self.navigationTimeRemaining is None:
        self.navigationTimeRemaining = 0.
      if self.timeToDeadline is None:
        self.timeToDeadline = 0.
      if self.currentDestination is None:
        self.currentDestination = cobot_msgs.msg.CobotLocalizationMsg()
      if self.fromLocation is None:
        self.fromLocation = ''
      if self.toLocation is None:
        self.toLocation = ''
      if self.objectToFind is None:
        self.objectToFind = ''
      if self.carryingObject is None:
        self.carryingObject = False
      if self.navigating is None:
        self.navigating = False
      if self.taskCompleted is None:
        self.taskCompleted = False
      if self.successValue is None:
        self.successValue = 0
      if self.paused is None:
        self.paused = False
      if self.owner is None:
        self.owner = ''
    else:
      self.mission_id = 0
      self.currentTask = ''
      self.currentSubTask = ''
      self.currentNavigationSubTask = ''
      self.timeBlocked = 0.
      self.taskDuration = 0.
      self.subTaskDuration = 0.
      self.navigationSubTaskDuration = 0.
      self.navigationTimeRemaining = 0.
      self.timeToDeadline = 0.
      self.currentDestination = cobot_msgs.msg.CobotLocalizationMsg()
      self.fromLocation = ''
      self.toLocation = ''
      self.objectToFind = ''
      self.carryingObject = False
      self.navigating = False
      self.taskCompleted = False
      self.successValue = 0
      self.paused = False
      self.owner = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      buff.write(_get_struct_i().pack(self.mission_id))
      _x = self.currentTask
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.currentSubTask
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.currentNavigationSubTask
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_6fd5f().pack(_x.timeBlocked, _x.taskDuration, _x.subTaskDuration, _x.navigationSubTaskDuration, _x.navigationTimeRemaining, _x.timeToDeadline, _x.currentDestination.timeStamp, _x.currentDestination.x, _x.currentDestination.y, _x.currentDestination.angle, _x.currentDestination.angleUncertainty, _x.currentDestination.locationUncertainty))
      _x = self.currentDestination.map
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2d2i3f2d2i3f().pack(_x.currentDestination.lastLaserRunTime, _x.currentDestination.laserRunTime, _x.currentDestination.laserNumObservedPoints, _x.currentDestination.laserNumCorrespondences, _x.currentDestination.laserStage0Weights, _x.currentDestination.laserStageRWeights, _x.currentDestination.laserMeanSqError, _x.currentDestination.lastPointCloudRunTime, _x.currentDestination.pointCloudRunTime, _x.currentDestination.pointCloudNumObservedPoints, _x.currentDestination.pointCloudNumCorrespondences, _x.currentDestination.pointCloudStage0Weights, _x.currentDestination.pointCloudStageRWeights, _x.currentDestination.pointCloudMeanSqError))
      _x = self.fromLocation
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.toLocation
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.objectToFind
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_3BiB().pack(_x.carryingObject, _x.navigating, _x.taskCompleted, _x.successValue, _x.paused))
      _x = self.owner
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.currentDestination is None:
        self.currentDestination = cobot_msgs.msg.CobotLocalizationMsg()
      end = 0
      start = end
      end += 4
      (self.mission_id,) = _get_struct_i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.currentTask = str[start:end].decode('utf-8')
      else:
        self.currentTask = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.currentSubTask = str[start:end].decode('utf-8')
      else:
        self.currentSubTask = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.currentNavigationSubTask = str[start:end].decode('utf-8')
      else:
        self.currentNavigationSubTask = str[start:end]
      _x = self
      start = end
      end += 52
      (_x.timeBlocked, _x.taskDuration, _x.subTaskDuration, _x.navigationSubTaskDuration, _x.navigationTimeRemaining, _x.timeToDeadline, _x.currentDestination.timeStamp, _x.currentDestination.x, _x.currentDestination.y, _x.currentDestination.angle, _x.currentDestination.angleUncertainty, _x.currentDestination.locationUncertainty,) = _get_struct_6fd5f().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.currentDestination.map = str[start:end].decode('utf-8')
      else:
        self.currentDestination.map = str[start:end]
      _x = self
      start = end
      end += 72
      (_x.currentDestination.lastLaserRunTime, _x.currentDestination.laserRunTime, _x.currentDestination.laserNumObservedPoints, _x.currentDestination.laserNumCorrespondences, _x.currentDestination.laserStage0Weights, _x.currentDestination.laserStageRWeights, _x.currentDestination.laserMeanSqError, _x.currentDestination.lastPointCloudRunTime, _x.currentDestination.pointCloudRunTime, _x.currentDestination.pointCloudNumObservedPoints, _x.currentDestination.pointCloudNumCorrespondences, _x.currentDestination.pointCloudStage0Weights, _x.currentDestination.pointCloudStageRWeights, _x.currentDestination.pointCloudMeanSqError,) = _get_struct_2d2i3f2d2i3f().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.fromLocation = str[start:end].decode('utf-8')
      else:
        self.fromLocation = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.toLocation = str[start:end].decode('utf-8')
      else:
        self.toLocation = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.objectToFind = str[start:end].decode('utf-8')
      else:
        self.objectToFind = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.carryingObject, _x.navigating, _x.taskCompleted, _x.successValue, _x.paused,) = _get_struct_3BiB().unpack(str[start:end])
      self.carryingObject = bool(self.carryingObject)
      self.navigating = bool(self.navigating)
      self.taskCompleted = bool(self.taskCompleted)
      self.paused = bool(self.paused)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.owner = str[start:end].decode('utf-8')
      else:
        self.owner = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      buff.write(_get_struct_i().pack(self.mission_id))
      _x = self.currentTask
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.currentSubTask
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.currentNavigationSubTask
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_6fd5f().pack(_x.timeBlocked, _x.taskDuration, _x.subTaskDuration, _x.navigationSubTaskDuration, _x.navigationTimeRemaining, _x.timeToDeadline, _x.currentDestination.timeStamp, _x.currentDestination.x, _x.currentDestination.y, _x.currentDestination.angle, _x.currentDestination.angleUncertainty, _x.currentDestination.locationUncertainty))
      _x = self.currentDestination.map
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2d2i3f2d2i3f().pack(_x.currentDestination.lastLaserRunTime, _x.currentDestination.laserRunTime, _x.currentDestination.laserNumObservedPoints, _x.currentDestination.laserNumCorrespondences, _x.currentDestination.laserStage0Weights, _x.currentDestination.laserStageRWeights, _x.currentDestination.laserMeanSqError, _x.currentDestination.lastPointCloudRunTime, _x.currentDestination.pointCloudRunTime, _x.currentDestination.pointCloudNumObservedPoints, _x.currentDestination.pointCloudNumCorrespondences, _x.currentDestination.pointCloudStage0Weights, _x.currentDestination.pointCloudStageRWeights, _x.currentDestination.pointCloudMeanSqError))
      _x = self.fromLocation
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.toLocation
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.objectToFind
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_3BiB().pack(_x.carryingObject, _x.navigating, _x.taskCompleted, _x.successValue, _x.paused))
      _x = self.owner
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.currentDestination is None:
        self.currentDestination = cobot_msgs.msg.CobotLocalizationMsg()
      end = 0
      start = end
      end += 4
      (self.mission_id,) = _get_struct_i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.currentTask = str[start:end].decode('utf-8')
      else:
        self.currentTask = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.currentSubTask = str[start:end].decode('utf-8')
      else:
        self.currentSubTask = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.currentNavigationSubTask = str[start:end].decode('utf-8')
      else:
        self.currentNavigationSubTask = str[start:end]
      _x = self
      start = end
      end += 52
      (_x.timeBlocked, _x.taskDuration, _x.subTaskDuration, _x.navigationSubTaskDuration, _x.navigationTimeRemaining, _x.timeToDeadline, _x.currentDestination.timeStamp, _x.currentDestination.x, _x.currentDestination.y, _x.currentDestination.angle, _x.currentDestination.angleUncertainty, _x.currentDestination.locationUncertainty,) = _get_struct_6fd5f().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.currentDestination.map = str[start:end].decode('utf-8')
      else:
        self.currentDestination.map = str[start:end]
      _x = self
      start = end
      end += 72
      (_x.currentDestination.lastLaserRunTime, _x.currentDestination.laserRunTime, _x.currentDestination.laserNumObservedPoints, _x.currentDestination.laserNumCorrespondences, _x.currentDestination.laserStage0Weights, _x.currentDestination.laserStageRWeights, _x.currentDestination.laserMeanSqError, _x.currentDestination.lastPointCloudRunTime, _x.currentDestination.pointCloudRunTime, _x.currentDestination.pointCloudNumObservedPoints, _x.currentDestination.pointCloudNumCorrespondences, _x.currentDestination.pointCloudStage0Weights, _x.currentDestination.pointCloudStageRWeights, _x.currentDestination.pointCloudMeanSqError,) = _get_struct_2d2i3f2d2i3f().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.fromLocation = str[start:end].decode('utf-8')
      else:
        self.fromLocation = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.toLocation = str[start:end].decode('utf-8')
      else:
        self.toLocation = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.objectToFind = str[start:end].decode('utf-8')
      else:
        self.objectToFind = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.carryingObject, _x.navigating, _x.taskCompleted, _x.successValue, _x.paused,) = _get_struct_3BiB().unpack(str[start:end])
      self.carryingObject = bool(self.carryingObject)
      self.navigating = bool(self.navigating)
      self.taskCompleted = bool(self.taskCompleted)
      self.paused = bool(self.paused)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.owner = str[start:end].decode('utf-8')
      else:
        self.owner = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_i = None
def _get_struct_i():
    global _struct_i
    if _struct_i is None:
        _struct_i = struct.Struct("<i")
    return _struct_i
_struct_2d2i3f2d2i3f = None
def _get_struct_2d2i3f2d2i3f():
    global _struct_2d2i3f2d2i3f
    if _struct_2d2i3f2d2i3f is None:
        _struct_2d2i3f2d2i3f = struct.Struct("<2d2i3f2d2i3f")
    return _struct_2d2i3f2d2i3f
_struct_6fd5f = None
def _get_struct_6fd5f():
    global _struct_6fd5f
    if _struct_6fd5f is None:
        _struct_6fd5f = struct.Struct("<6fd5f")
    return _struct_6fd5f
_struct_3BiB = None
def _get_struct_3BiB():
    global _struct_3BiB
    if _struct_3BiB is None:
        _struct_3BiB = struct.Struct("<3BiB")
    return _struct_3BiB
