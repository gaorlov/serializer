from association import Association

class HasOneAssociation(Association):

    def value_for( self, object ):
        assoc = getattr( object, self.name )
        return self.__dict_for( assoc )