class Serializer

    __attributes = {}

    def __init__( self, object ):
        self.object = object


    def to_dict( self ):
        blob = {}
        for attribute in self.__class__.__attributes.values():
            blob[ attribute.key() ] = attribute.value_for( self.object )

        return blob

    def to_json( self ):
        return json.dumps(self.to_dict())

    # class methods

    @classmethod
    def attribute( cls, name, options = {} ):
        cls.__add_attribute( name, options )

    @classmethod
    def attributes( cls, attrs ):
        for attr in attrs:
            cls.__add_attribute( attr )

    @classmethod
    def has_one( cls, association, options = {} )
        if !options['serializer']
            raise SerializerException("You must specify a serializer for %s.%s" % cls, association)

        cls.__add_association( association, HasOneAssociation, options )

    @classmethod
    def has_one( cls, association, options = {} )
        if !options['serializer']
            raise SerializerException("You must specify a serializer for %s.%s" % cls, association)

        cls.__add_association( association, HasManyAssociation, options )

    # private

    @classmethod
    def __add_attribute( cls, name, options = {} )
        cls.__attributes[ name ] = ValueAttribute( name, options )

    def __add_association( cls, name, association, options = {} )
        cls.__attributes[ name ] = association( name, options )

class Attribute():

    def __init__( self, name, options = {} ):
        self.name = name
        self.options = options

    def key( self ):
        return options.get('key', self.name)

class ValueAttribute(Attribute):

    def value_for( self, object ):
        return getattr( object, self.name )

class Association(Attribute):
    def __init__( self, name, options = {} ):
        super( name, options )
        self.serializer = options[ 'serializer' ]

    #private

    def __dict_for( self, object ):
        return self.serializer( object ).to_dict()

class HasOneAssociation(Association):

    def value_for( self, object ):
        assoc = getattr( object, self.name )
        return self.__dict_for( assoc )

class HasManyAssociation(Association):

    def value_for( self, object ):
        assocs = getattr( object, self.name )
        return map( lambda ( self, obj ) : self.__dict_for( obj ), assocs )
