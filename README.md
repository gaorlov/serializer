# Serializers

[![Build Status](https://travis-ci.org/gaorlov/serializer.svg?branch=master)](https://travis-ci.org/gaorlov/serializer)

This is an attempt at a simple Python port of [ActiveModel::Serializers](https://github.com/rails-api/active_model_serializers). It's a bit minimal at the moment, but any contributions are welcome.

## Installation

All you have to do is run:

    $ pip install serializers

## Usage

If you have an object that you want to render as JSON and don't necessarily want to render all of it, or want to modify the shape of the object. You could certainly do all of that specification in the object, but that is not great separation of concerns and can get tedious.

### Single Object Serialization

Usually you would define one or more serializer per object class:

```python
  class MyObjectSerialzer( Serializer ):
    pass

  # NOTE: feel free to reach out if you have a way to move this into the class definition

  MyObjectSerializer.attribute( 'attribute_name' )
  MyObjectSerializer.attribute( 'internal_name', { 'key' : 'public_name'} )
  MyObjectSerializer.attributes( 'list', 'of', 'attributes' )
```

and then in your rendering, you would init a new serializer with the object you want serialized:

```python
  obj = MyObject( ) # whatever this is
  json = MyObjectSerializer( obj ).to_json()

  return json # or whatever your rendering logic is
```

You can also render the object to a dictionary, if you want

```python
  serializer = MyObjectSerialzier( obj )
  obj_dict   = serializer.to_dict()
```

### ComplexObjectSerialization

If you have an object that has subobjects you want custom serialized, you can define serializer relationships. 

```python

  ChildSerializer( Serializer ):
    pass
  
  ChildSerializer.attriutes( 'name', 'ordinal')


  ParentSerializer( Serializer ):
    pass

  ParentSerializer.attribute( 'name' )
  ParentSerializer.has_many( 'children', { 'serializer' : ChildSerializer } )


  parent = Parent( 'Bob' )
  parent.children = [ Child( 'Jim', 'first' ), Child( 'Jamie', 'second' ) ]

  ParentSerializer( parent ).to_json()  # =>  { "name": "Bob",
                                        #       "children": [
                                        #         { "name": "Jim",
                                        #           "ordinal": "first"
                                        #         },
                                        #         { "name": "Jamie",
                                        #           "ordinal": "second"
                                        #         },
                                        #       ]
                                        #     }
```
### Optional Parameter Passing & Serializer Methods

Because the serializer object is now the external interface definition for your object separate from it, it makes sense you would be able to define custom serialization methods for your objects. And you can. 

```python
  class PersonSerializer(Serializer):

    @classmethod
    def formatted_name( cls, item, args ):
      return f"{item.title} {item.first_name} {item.last_name} {item.suffix}"

    # in case you were wondering about the args in that method, that's so that you can pass in additional data into the serializer
    @classmethod
    def timezones_from_you( cls, item, args ):
      zone = timezone( args.get('timezone', "UTC") )
      
      return item.timezone - zone

  PersonSerializer.attributes(  'formatted_name ',
                                'timezones_from_you' )
```

With this, you can, in your controller, do

```python
  def show( self, args ):
    person = Person.find( args[ 'person_id' ] )
    return PersonSerializer( person, args ).to_json()
```

which should render something along the lines of

```json
{ "formatted_name" : "Mr. Bob Dobalina Sr. III",
  "timezones_from_you": -3 }
```


  

### Example

```python
  class Model():

    def __init__( self ):
      self.public_data = "stuff here"
      self.secret      = "magic secrets no one should ever see"
      self.rename_me   = "i have been renamed!"

    def func( self ):
      return "reslt of a function"

    # if you are using SQL Alchemy
    children = relationship("Child")
  

  class ModelSerializer(Serializer):
    pass

  ModelSerializer.attributes( 'public_data', 'func' )
                 .attribute( 'rename_me', { 'key': 'reanamed_var' } ) \
                 .has_many( 'children', { 'serializer' : ChildSerializer } )

  ModelSerializer( Model() ).to_json() # => '{  "func" : "reslt of a function"
                                       #        "public_data": "stuff here",
                                       #        "reanamed_var": "i have been renamed!"
                                       #        "children": [
                                       #          { "name": "Jim",
                                       #            "ordinal": "first"
                                       #          },
                                       #          { "name": "Jamie",
                                       #            "ordinal": "second"
                                       #         },
                                       #       ]
                                       #     }'

```

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/gaorlov/serializer.


## License

The gem is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).


