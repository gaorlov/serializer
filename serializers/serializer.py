from serializers.attribute import ValueAttribute
from serializers.association import HasOneAssociation, HasManyAssociation

from future.utils import with_metaclass

import json

class SerializerMeta(type):
  def __init__(cls, name, bases, dct):
    super(SerializerMeta, cls).__init__(name, bases, dct)
    cls._attributes = {}

class Serializer(with_metaclass(SerializerMeta, object)):

  _attributes = {}

  def __init__( self, item, args = {} ):
    self.item = item
    self.args = args

  def to_dict( self ):
    blob = {}
    for attribute in self.__class__._attributes.values( ):
      blob[ attribute.key( ) ] = attribute.value_for( self.item, self.args )

    return blob

  def to_json( self ):
    return json.dumps( self.to_dict(), sort_keys=True )

  # class methods

  @classmethod
  def attribute( cls, name, options = {} ):
    cls.__add_attribute( name, options )
    
    return cls

  @classmethod
  def attributes( cls, *attrs ):
    for attr in attrs:
      cls.__add_attribute( attr )
    
    return cls

  @classmethod
  def has_one( cls, name, options = {} ):
    if options.get( 'serializer', None ) == None:
      raise Exception("You must specify a serializer for {cls}.{name}".format(cls=cls, name=name))

    cls.__add_association( HasOneAssociation, name, options )

  @classmethod
  def has_many( cls, name, options = {} ):
    if options.get( 'serializer', None ) == None:
      raise Exception("You must specify a serializer for {cls}.{name}".format(cls=cls, name=name))

    cls.__add_association( HasManyAssociation, name, options )

  # private

  @classmethod
  def __add_attribute( cls, name, options = {} ):
    cls._attributes[ name ] = ValueAttribute( cls, name, options )

  @classmethod
  def __add_association( cls, association, name, options = {} ):
    cls._attributes[ name ] = association( cls, name, options )
