class Attribute(object):

  def __init__( self, serializer, name, options = {} ):
    self.name = name
    self.options = options
    self.serializer = serializer

  def key( self ):
    return self.options.get('key', self.name)