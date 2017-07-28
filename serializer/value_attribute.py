from attribute import Attribute

class ValueAttribute(Attribute):

  def value_for( self, object ):
    if hasattr( object, self.name ):
      val = getattr( object, self.name )
      if callable( val ):
        val = val()
      return val 
    else:
      return getattr( self.serializer, self.name )( object )