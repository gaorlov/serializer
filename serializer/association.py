from attribute import Attribute

class Association(Attribute):
  def __init__( self, name, options = {} ):
    super( Attribute, self).__init__( name, options )
    self.serializer = options[ 'serializer' ]

  #private

  def __dict_for( self, object ):
    return self.serializer( object ).to_dict()