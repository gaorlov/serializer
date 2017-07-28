from association import Association

class HasManyAssociation(Association):

    def value_for( self, object ):
        assocs = getattr( object, self.name )
        return map( lambda ( self, obj ) : self.__dict_for( obj ), assocs )
