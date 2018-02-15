# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from cobot_msgs/CobotHumanClassified.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg

class CobotHumanClassified(genpy.Message):
  _md5sum = "59f9df57cd1e9989aabf745f443495cc"
  _type = "cobot_msgs/CobotHumanClassified"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int32 id
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
  __slots__ = ['id','age','confidence','position','velocity','orientation','intention']
  _slot_types = ['int32','int32','float32','geometry_msgs/Point32','geometry_msgs/Point32','float32','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       id,age,confidence,position,velocity,orientation,intention

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(CobotHumanClassified, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.id is None:
        self.id = 0
      if self.age is None:
        self.age = 0
      if self.confidence is None:
        self.confidence = 0.
      if self.position is None:
        self.position = geometry_msgs.msg.Point32()
      if self.velocity is None:
        self.velocity = geometry_msgs.msg.Point32()
      if self.orientation is None:
        self.orientation = 0.
      if self.intention is None:
        self.intention = ''
    else:
      self.id = 0
      self.age = 0
      self.confidence = 0.
      self.position = geometry_msgs.msg.Point32()
      self.velocity = geometry_msgs.msg.Point32()
      self.orientation = 0.
      self.intention = ''

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
      _x = self
      buff.write(_get_struct_2i8f().pack(_x.id, _x.age, _x.confidence, _x.position.x, _x.position.y, _x.position.z, _x.velocity.x, _x.velocity.y, _x.velocity.z, _x.orientation))
      _x = self.intention
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
      if self.position is None:
        self.position = geometry_msgs.msg.Point32()
      if self.velocity is None:
        self.velocity = geometry_msgs.msg.Point32()
      end = 0
      _x = self
      start = end
      end += 40
      (_x.id, _x.age, _x.confidence, _x.position.x, _x.position.y, _x.position.z, _x.velocity.x, _x.velocity.y, _x.velocity.z, _x.orientation,) = _get_struct_2i8f().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.intention = str[start:end].decode('utf-8')
      else:
        self.intention = str[start:end]
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
      _x = self
      buff.write(_get_struct_2i8f().pack(_x.id, _x.age, _x.confidence, _x.position.x, _x.position.y, _x.position.z, _x.velocity.x, _x.velocity.y, _x.velocity.z, _x.orientation))
      _x = self.intention
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
      if self.position is None:
        self.position = geometry_msgs.msg.Point32()
      if self.velocity is None:
        self.velocity = geometry_msgs.msg.Point32()
      end = 0
      _x = self
      start = end
      end += 40
      (_x.id, _x.age, _x.confidence, _x.position.x, _x.position.y, _x.position.z, _x.velocity.x, _x.velocity.y, _x.velocity.z, _x.orientation,) = _get_struct_2i8f().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.intention = str[start:end].decode('utf-8')
      else:
        self.intention = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2i8f = None
def _get_struct_2i8f():
    global _struct_2i8f
    if _struct_2i8f is None:
        _struct_2i8f = struct.Struct("<2i8f")
    return _struct_2i8f
