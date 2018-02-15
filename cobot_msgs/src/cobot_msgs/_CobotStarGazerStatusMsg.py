# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from cobot_msgs/CobotStarGazerStatusMsg.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import cobot_msgs.msg
import genpy
import std_msgs.msg

class CobotStarGazerStatusMsg(genpy.Message):
  _md5sum = "dda64f5e584fbd9a49bc5cbcdd254136"
  _type = "cobot_msgs/CobotStarGazerStatusMsg"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """Header header
CobotStarGazerMarkerStatusMsg[] active
CobotStarGazerMsg lastSGMsg


================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: cobot_msgs/CobotStarGazerMarkerStatusMsg
uint16 id
CobotStarGazerMarkerMsg lastMsg
time firstSeen
uint16 count

================================================================================
MSG: cobot_msgs/CobotStarGazerMarkerMsg
uint16 ID
float32 rawX
float32 rawY
float32 rawOrientation

string map
float32 robotX
float32 robotY
float32 robotOrientation

================================================================================
MSG: cobot_msgs/CobotStarGazerMsg
Header header
CobotStarGazerMarkerMsg[] markers
"""
  __slots__ = ['header','active','lastSGMsg']
  _slot_types = ['std_msgs/Header','cobot_msgs/CobotStarGazerMarkerStatusMsg[]','cobot_msgs/CobotStarGazerMsg']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,active,lastSGMsg

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(CobotStarGazerStatusMsg, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.active is None:
        self.active = []
      if self.lastSGMsg is None:
        self.lastSGMsg = cobot_msgs.msg.CobotStarGazerMsg()
    else:
      self.header = std_msgs.msg.Header()
      self.active = []
      self.lastSGMsg = cobot_msgs.msg.CobotStarGazerMsg()

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
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.active)
      buff.write(_struct_I.pack(length))
      for val1 in self.active:
        buff.write(_get_struct_H().pack(val1.id))
        _v1 = val1.lastMsg
        _x = _v1
        buff.write(_get_struct_H3f().pack(_x.ID, _x.rawX, _x.rawY, _x.rawOrientation))
        _x = _v1.map
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = _v1
        buff.write(_get_struct_3f().pack(_x.robotX, _x.robotY, _x.robotOrientation))
        _v2 = val1.firstSeen
        _x = _v2
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        buff.write(_get_struct_H().pack(val1.count))
      _x = self
      buff.write(_get_struct_3I().pack(_x.lastSGMsg.header.seq, _x.lastSGMsg.header.stamp.secs, _x.lastSGMsg.header.stamp.nsecs))
      _x = self.lastSGMsg.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.lastSGMsg.markers)
      buff.write(_struct_I.pack(length))
      for val1 in self.lastSGMsg.markers:
        _x = val1
        buff.write(_get_struct_H3f().pack(_x.ID, _x.rawX, _x.rawY, _x.rawOrientation))
        _x = val1.map
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1
        buff.write(_get_struct_3f().pack(_x.robotX, _x.robotY, _x.robotOrientation))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.active is None:
        self.active = None
      if self.lastSGMsg is None:
        self.lastSGMsg = cobot_msgs.msg.CobotStarGazerMsg()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.active = []
      for i in range(0, length):
        val1 = cobot_msgs.msg.CobotStarGazerMarkerStatusMsg()
        start = end
        end += 2
        (val1.id,) = _get_struct_H().unpack(str[start:end])
        _v3 = val1.lastMsg
        _x = _v3
        start = end
        end += 14
        (_x.ID, _x.rawX, _x.rawY, _x.rawOrientation,) = _get_struct_H3f().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v3.map = str[start:end].decode('utf-8')
        else:
          _v3.map = str[start:end]
        _x = _v3
        start = end
        end += 12
        (_x.robotX, _x.robotY, _x.robotOrientation,) = _get_struct_3f().unpack(str[start:end])
        _v4 = val1.firstSeen
        _x = _v4
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 2
        (val1.count,) = _get_struct_H().unpack(str[start:end])
        self.active.append(val1)
      _x = self
      start = end
      end += 12
      (_x.lastSGMsg.header.seq, _x.lastSGMsg.header.stamp.secs, _x.lastSGMsg.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.lastSGMsg.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.lastSGMsg.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.lastSGMsg.markers = []
      for i in range(0, length):
        val1 = cobot_msgs.msg.CobotStarGazerMarkerMsg()
        _x = val1
        start = end
        end += 14
        (_x.ID, _x.rawX, _x.rawY, _x.rawOrientation,) = _get_struct_H3f().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.map = str[start:end].decode('utf-8')
        else:
          val1.map = str[start:end]
        _x = val1
        start = end
        end += 12
        (_x.robotX, _x.robotY, _x.robotOrientation,) = _get_struct_3f().unpack(str[start:end])
        self.lastSGMsg.markers.append(val1)
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
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.active)
      buff.write(_struct_I.pack(length))
      for val1 in self.active:
        buff.write(_get_struct_H().pack(val1.id))
        _v5 = val1.lastMsg
        _x = _v5
        buff.write(_get_struct_H3f().pack(_x.ID, _x.rawX, _x.rawY, _x.rawOrientation))
        _x = _v5.map
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = _v5
        buff.write(_get_struct_3f().pack(_x.robotX, _x.robotY, _x.robotOrientation))
        _v6 = val1.firstSeen
        _x = _v6
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        buff.write(_get_struct_H().pack(val1.count))
      _x = self
      buff.write(_get_struct_3I().pack(_x.lastSGMsg.header.seq, _x.lastSGMsg.header.stamp.secs, _x.lastSGMsg.header.stamp.nsecs))
      _x = self.lastSGMsg.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.lastSGMsg.markers)
      buff.write(_struct_I.pack(length))
      for val1 in self.lastSGMsg.markers:
        _x = val1
        buff.write(_get_struct_H3f().pack(_x.ID, _x.rawX, _x.rawY, _x.rawOrientation))
        _x = val1.map
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1
        buff.write(_get_struct_3f().pack(_x.robotX, _x.robotY, _x.robotOrientation))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.active is None:
        self.active = None
      if self.lastSGMsg is None:
        self.lastSGMsg = cobot_msgs.msg.CobotStarGazerMsg()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.active = []
      for i in range(0, length):
        val1 = cobot_msgs.msg.CobotStarGazerMarkerStatusMsg()
        start = end
        end += 2
        (val1.id,) = _get_struct_H().unpack(str[start:end])
        _v7 = val1.lastMsg
        _x = _v7
        start = end
        end += 14
        (_x.ID, _x.rawX, _x.rawY, _x.rawOrientation,) = _get_struct_H3f().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v7.map = str[start:end].decode('utf-8')
        else:
          _v7.map = str[start:end]
        _x = _v7
        start = end
        end += 12
        (_x.robotX, _x.robotY, _x.robotOrientation,) = _get_struct_3f().unpack(str[start:end])
        _v8 = val1.firstSeen
        _x = _v8
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 2
        (val1.count,) = _get_struct_H().unpack(str[start:end])
        self.active.append(val1)
      _x = self
      start = end
      end += 12
      (_x.lastSGMsg.header.seq, _x.lastSGMsg.header.stamp.secs, _x.lastSGMsg.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.lastSGMsg.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.lastSGMsg.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.lastSGMsg.markers = []
      for i in range(0, length):
        val1 = cobot_msgs.msg.CobotStarGazerMarkerMsg()
        _x = val1
        start = end
        end += 14
        (_x.ID, _x.rawX, _x.rawY, _x.rawOrientation,) = _get_struct_H3f().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.map = str[start:end].decode('utf-8')
        else:
          val1.map = str[start:end]
        _x = val1
        start = end
        end += 12
        (_x.robotX, _x.robotY, _x.robotOrientation,) = _get_struct_3f().unpack(str[start:end])
        self.lastSGMsg.markers.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_H = None
def _get_struct_H():
    global _struct_H
    if _struct_H is None:
        _struct_H = struct.Struct("<H")
    return _struct_H
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_H3f = None
def _get_struct_H3f():
    global _struct_H3f
    if _struct_H3f is None:
        _struct_H3f = struct.Struct("<H3f")
    return _struct_H3f
_struct_3f = None
def _get_struct_3f():
    global _struct_3f
    if _struct_3f is None:
        _struct_3f = struct.Struct("<3f")
    return _struct_3f
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
