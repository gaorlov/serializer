import unittest
import serializer
from serializer.serializer import Serializer
from serializer.value_attribute import ValueAttribute
from serializer.attribute import Attribute


class BaseModel():

  def __init__( self ):
    self.string_var  = "string"
    self.int_var     = 6
    self.arr_var     = [1, 2, "string"]
    self.dict_var    = { 'key' : 'value' }
    self.keyed_var   = "poops"

  def func_var( self ):
    return "funk"

class BaseSerializer(Serializer):
  from serializer.serializer import Serializer as s

  s.attribute( 'string_var' )
  s.attribute( 'int_var' )
  s.attribute( 'dict_var' )
  s.attribute( 'arr_var' )
  s.attribute( 'keyed_var', { 'key': 'serialized_name' } )
  s.attribute( 'func_var' )

class AdvancedSerializer(Serializer):
  from serializer.serializer import Serializer as s

  s.attributes( 'string_var',
                'int_var',
                'dict_var',
                'arr_var',
                'func_var' )