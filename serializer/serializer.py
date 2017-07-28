from value_attribute import ValueAttribute
from has_one_association import HasOneAssociation
from has_many_association import HasManyAssociation
import json

class Serializer(object):

  __attributes = {}

  def __init__( self, object ):
    self.object = object


  def to_dict( self ):
    blob = {}
    for attribute in self.__class__.__attributes.values( ):
      blob[ attribute.key( ) ] = attribute.value_for( self.object )

    return blob

  def to_json( self ):
    return json.dumps(self.to_dict())

  # class methods

  @classmethod
  def attribute( cls, name, options = {} ):
    cls.__add_attribute( name, options )

  @classmethod
  def attributes( cls, *attrs ):
    for attr in attrs:
      cls.__add_attribute( attr )

  @classmethod
  def has_one( cls, association, options = {} ):
    if options['serializer'] == None:
      raise SerializerException("You must specify a serializer for %s.%s" % cls, association)

    cls.__add_association( association, HasOneAssociation, options )

  @classmethod
  def has_one( cls, association, options = {} ):
    if options['serializer'] == None:
      raise SerializerException("You must specify a serializer for %s.%s" % cls, association)

    cls.__add_association( association, HasManyAssociation, options )

  # private

  @classmethod
  def __add_attribute( cls, name, options = {} ):
    cls.__attributes[ name ] = ValueAttribute( cls, name, options )

  def __add_association( cls, name, association, options = {} ):
    cls.__attributes[ name ] = association( name, options )