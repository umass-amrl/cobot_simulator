# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from cobot_msgs/CobotHumansClassified.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import cobot_msgs.msg

class CobotHumansClassified(genpy.Message):
  _md5sum = "ac643b370a6778e9d3b4cde7634f85cc"
  _type = "cobot_msgs/CobotHumansClassified"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """CobotHumanClassified[] classified_humans


================================================================================
MSG: cobot_msgs/CobotHumanClassified
int32 id
int32 age
float32 confidence
geometry_msgs/Point32 position
geometry_msgs/Point32 velocity
float32 orientation
string intention

================================================================================
MSG: geometry_msgs/Point32
# This contains the position of a point in free space(with 32 bits of precision).
# It is recommeded to use Point wherever possible instead of Point32.  
# 
# This recommendation is to promote interoperability.  
#
# This message is designed to take up less space when sending
# lots of points at once, as in the case of a PointCloud.  

float32 x
float32 y
float32 z"""
  __slots__ = ['classified_humans']
  _slot_types = ['cobot_msgs/CobotHumanClassified[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       classified_humans

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(CobotHumansClassified, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.classified_humans is None:
        self.classified_humans = []
    else:
      self.classified_humans = []

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
      length = len(self.classified_humans)
      buff.write(_struct_I.pack(length))
      for val1 in self.classified_humans:
        _x = val1
        buff.write(_get_struct_2if().pack(_x.id, _x.age, _x.confidence))
        _v1 = val1.position
        _x = _v1
        buff.write(_get_struct_3f().pack(_x.x, _x.y, _x.z))
        _v2 = val1.velocity
        _x = _v2
        buff.write(_get_struct_3f().pack(_x.x, _x.y, _x.z))
        buff.write(_get_struct_f().pack(val1.orientation))
        _x = val1.intention
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
      if self.classified_humans is None:
        self.classified_humans = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.classified_humans = []
      for i in range(0, length):
        val1 = cobot_msgs.msg.CobotHumanClassified()
        _x = val1
        start = end
        end += 12
        (_x.id, _x.age, _x.confidence,) = _get_struct_2if().unpack(str[start:end])
        _v3 = val1.position
        _x = _v3
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _get_struct_3f().unpack(str[start:end])
        _v4 = val1.velocity
        _x = _v4
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _get_struct_3f().unpack(str[start:end])
        start = end
        end += 4
        (val1.orientation,) = _get_struct_f().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.intention = str[start:end].decode('utf-8')
        else:
          val1.intention = str[start:end]
        self.classified_humans.append(val1)
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
      length = len(self.classified_humans)
      buff.write(_struct_I.pack(length))
      for val1 in self.classified_humans:
        _x = val1
        buff.write(_get_struct_2if().pack(_x.id, _x.age, _x.confidence))
        _v5 = val1.position
        _x = _v5
        buff.write(_get_struct_3f().pack(_x.x, _x.y, _x.z))
        _v6 = val1.velocity
        _x = _v6
        buff.write(_get_struct_3f().pack(_x.x, _x.y, _x.z))
        buff.write(_get_struct_f().pack(val1.orientation))
        _x = val1.intention
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
      if self.classified_humans is None:
        self.classified_humans = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.classified_humans = []
      for i in range(0, length):
        val1 = cobot_msgs.msg.CobotHumanClassified()
        _x = val1
        start = end
        end += 12
        (_x.id, _x.age, _x.confidence,) = _get_struct_2if().unpack(str[start:end])
        _v7 = val1.position
        _x = _v7
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _get_struct_3f().unpack(str[start:end])
        _v8 = val1.velocity
        _x = _v8
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _get_struct_3f().unpack(str[start:end])
        start = end
        end += 4
        (val1.orientation,) = _get_struct_f().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.intention = str[start:end].decode('utf-8')
        else:
          val1.intention = str[start:end]
        self.classified_humans.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2if = None
def _get_struct_2if():
    global _struct_2if
    if _struct_2if is None:
        _struct_2if = struct.Struct("<2if")
    return _struct_2if
_struct_3f = None
def _get_struct_3f():
    global _struct_3f
    if _struct_3f is None:
        _struct_3f = struct.Struct("<3f")
    return _struct_3f
_struct_f = None
def _get_struct_f():
    global _struct_f
    if _struct_f is None:
        _struct_f = struct.Struct("<f")
    return _struct_f