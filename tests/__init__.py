import unittest
import serializers
from serializers.serializer import Serializer
from serializers.attribute import Attribute, ValueAttribute


class BaseModel():

  def __init__( self ):
    self.string_var  = "string"
    self.int_var     = 6
    self.arr_var     = [1, 2, "string"]
    self.dict_var    = { 'key' : 'value' }
    self.keyed_var   = "poops"

  def func_var( self ):
    return "funk"

class OtherModel():

  def __init__( self ):
    self.attr       = "string"
    self.lol        = 6
    self.something  = [1, 2, "string"]
    self.wonderful  = { 'key' : 'value' }
    self.here       = "poops"

  def func( self ):
    return "lol"

class ComplexModel():

  def __init__( self ):
    self.base   = BaseModel()
    self.others = [ OtherModel(), OtherModel() ]


class BaseSerializer(Serializer):
  pass

BaseSerializer.attribute( 'string_var' )  \
              .attribute( 'int_var' )     \
              .attribute( 'dict_var' )    \
              .attribute( 'arr_var' )     \
              .attribute( 'keyed_var', { 'key': 'serialized_name' } ) \
              .attribute( 'func_var' )

class OtherSerializer(Serializer):
  pass

OtherSerializer.attributes( 'attr',
                            'lol',
                            'something',
                            'func',
                            'here' ) \
               .attribute( 'wonderful' )
              

class ComplexSerializer(Serializer):
  pass

ComplexSerializer.has_one( 'base', { 'serializer': BaseSerializer } )
ComplexSerializer.has_many( 'others', { 'serializer': OtherSerializer } )


class MethodizedSerializer(Serializer):

  @classmethod
  def custom_field( self, object, args = {} ):
    return object.here

  @classmethod
  def custom_field_with_args( self, object, args = {} ):
    ret = "object.here:" + object.here
    if args:
      ret += ", args['lol']:" + args.get('lol')

    return ret

  @classmethod
  def keyed_custom_field_with_args( self, object, args = {} ):
    return "lol"

MethodizedSerializer.attributes(  'custom_field',
                                  'custom_field_with_args' ) \
                    .attribute(   'keyed_custom_field_with_args', { 'key' : 'kek' } )
