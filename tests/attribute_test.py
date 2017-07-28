from serializer.serializer import Serializer
from tests import BaseModel, BaseSerializer, AdvancedSerializer

from nose.tools import assert_true, assert_equals

class TestAttribute():
  def setup( self ):
    self.obj = BaseModel() 


  def test_attribute_to_dict( self ):
    obj_dict = BaseSerializer( self.obj ).to_dict()

    assert_true( isinstance( obj_dict, dict ) )

    assert_equals( obj_dict['string_var'], "string" )
    assert_equals( obj_dict['int_var'], 6 )
    assert_equals( obj_dict['arr_var'], [1, 2, "string"] )
    assert_equals( obj_dict['dict_var'], { 'key' : 'value' } )
    assert_equals( obj_dict['serialized_name'], "poops" )
    assert_equals( obj_dict['func_var'], "funk" )


  def test_attribute_to_json( self ):
    obj_json = BaseSerializer( self.obj ).to_json()

    assert_equals( obj_json, '{"arr_var": [1, 2, "string"], "func_var": "funk", "dict_var": {"key": "value"}, "string_var": "string", "int_var": 6, "serialized_name": "key"}' )

  def test_attributes_to_dict( self ):
    obj_dict = AdvancedSerializer( self.obj ).to_dict()

    assert_true( isinstance( obj_dict, dict ) )

    assert_equals( obj_dict['string_var'], "string" )
    assert_equals( obj_dict['int_var'], 6 )
    assert_equals( obj_dict['arr_var'], [1, 2, "string"] )
    assert_equals( obj_dict['dict_var'], { 'key' : 'value' } )
    assert_equals( obj_dict['func_var'], "funk" )

  def test_attributes_to_json( self ):
    assert_equals( AdvancedSerializer( self.obj ).to_json(), '{"arr_var": [1, 2, "string"], "func_var": "funk", "dict_var": {"key": "value"}, "string_var": "string", "int_var": 6}' )
