# Serializer

This is an attempt at a simple Python port of [ActiveModel::Serializer](https://github.com/rails-api/active_model_serializers). It's a bit minimal at the moment, but any contributions are welcome.

## Installation

You can install this using `pip` as:

    $ pip install serializer

## Usage


### Example

```python
  class Model():

    def __init__( self ):
      self.string_var  = "string"
      self.int_var     = 6
      self.arr_var     = [1, 2, "string"]
      self.dict_var    = { 'key' : 'value' }
      self.keyed_var   = "poops"

    def func_var( self ):
      return "funk"
  

  class ModelSerializer(Serializer):
    pass

  ModelSerializer.attribute( 'string_var' )  \
                .attribute( 'int_var' )     \
                .attribute( 'dict_var' )    \
                .attribute( 'arr_var' )     \
                .attribute( 'keyed_var', { 'key': 'serialized_name' } ) \
                .attribute( 'func_var' )

  ModelSerializer( Model() ).to_json() # => '{  "arr_var": [1, 2, "string"], 
                                       #        "func_var": "funk", 
                                       #        "dict_var": {"key": "value"}, 
                                       #        "string_var": "string", 
                                       #        "int_var": 6, 
                                       #        "serialized_name": "poops"
                                       #     }'

```

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/gaorlov/serializer.


## License

The gem is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).

