import pytest

from lab_serializer.serializers.json_serializer import Json
from lab_serializer.serializers.xml_serializer import Xml

'''
Primitives testing section
'''


def test_primitive_int_json():
    value = 3456324324324324324324324325465436375687980907656789
    serializer = Json()
    packed = serializer.dumps(value)
    assert value == serializer.loads(packed)


def test_primitive_float_json():
    value = 3456324324324324324324324325.465436375687980907656789
    serializer = Json()
    packed = serializer.dumps(value)
    assert value == serializer.loads(packed)


def test_primitive_str_json():
    value = "some simple test"
    serializer = Json()
    packed = serializer.dumps(value)
    assert value == serializer.loads(packed)


def test_primitive_bool_json():
    serializer = Json()
    packedTrue = serializer.dumps(True)
    packedFalse = serializer.dumps(False)
    assert True == serializer.loads(packedTrue)
    assert False == serializer.loads(packedFalse)


def test_primitive_none_json():
    value = None
    serializer = Json()
    packed = serializer.dumps(value)
    assert value == serializer.loads(packed)


def test_primitive_int_xml():
    value = 3456324324324324324324324325465436375687980907656789
    serializer = Xml()
    packed = serializer.dumps(value)
    assert value == serializer.loads(packed)


def test_primitive_float_xml():
    value = 3456324324324324324324324325.465436375687980907656789
    serializer = Xml()
    packed = serializer.dumps(value)
    assert value == serializer.loads(packed)


def test_primitive_str_xml():
    value = "some simple test"
    serializer = Xml()
    packed = serializer.dumps(value)
    assert value == serializer.loads(packed)


def test_primitive_bool_xml():
    serializer = Xml()
    packedTrue = serializer.dumps(True)
    packedFalse = serializer.dumps(False)
    assert True == serializer.loads(packedTrue)
    assert False == serializer.loads(packedFalse)


def test_primitive_none_xml():
    value = None
    serializer = Xml()
    packed = serializer.dumps(value)
    assert value == serializer.loads(packed)


'''
Collections testing section
Empty collections
'''


def test_empty_list_json():
    value = []
    serializer = Json()
    packed = serializer.dumps(value)
    assert value == serializer.loads(packed)


def test_empty_tuple_json():
    value = ()
    serializer = Json()
    packed = serializer.dumps(value)
    assert value == serializer.loads(packed)


def test_empty_dict_json():
    value = {}
    serializer = Json()
    packed = serializer.dumps(value)
    assert value == serializer.loads(packed)


def test_empty_set_json():
    value = set()
    serializer = Json()
    packed = serializer.dumps(value)
    assert value == serializer.loads(packed)


def test_empty_list_xml():
    value = []
    serializer = Xml()
    packed = serializer.dumps(value)
    assert value == serializer.loads(packed)


def test_empty_tuple_xml():
    value = ()
    serializer = Xml()
    packed = serializer.dumps(value)
    assert value == serializer.loads(packed)


def test_empty_dict_xml():
    value = {}
    serializer = Xml()
    packed = serializer.dumps(value)
    assert value == serializer.loads(packed)


def test_empty_set_xml():
    value = set()
    serializer = Xml()
    packed = serializer.dumps(value)
    assert value == serializer.loads(packed)


'''
Collections testing section
Simple collections
'''


def test_simple_list_json():
    value = [None, 'fldfkndsfdsfm', 34.0023442, True, 'wejwie', False]
    serializer = Json()
    packed = serializer.dumps(value)
    assert value == serializer.loads(packed)


def test_simple_tuple_json():
    value = (None, 'fldfkndsfdsfm', 34.0023442, True, 'wejwie', False)
    serializer = Json()
    packed = serializer.dumps(value)
    assert value == serializer.loads(packed)


def test_simple_dict_json():
    value = {'key1': 'value1', 2: True, '???': None}
    serializer = Json()
    packed = serializer.dumps(value)
    assert value == serializer.loads(packed)


def test_simple_set_json():
    value = set([None, 'fldfkndsfdsfm', 34.0023442, True, 'wejwie', False])
    serializer = Json()
    packed = serializer.dumps(value)
    assert value == serializer.loads(packed)


def test_simple_list_xml():
    value = [None, 'fldfkndsfdsfm', 34.0023442, True, 'wejwie', False]
    serializer = Xml()
    packed = serializer.dumps(value)
    assert value == serializer.loads(packed)


def test_simple_tuple_xml():
    value = (None, 'fldfkndsfdsfm', 34.0023442, True, 'wejwie', False)
    serializer = Xml()
    packed = serializer.dumps(value)
    assert value == serializer.loads(packed)


def test_simple_dict_xml():
    value = {'key1': 'value1', 2: True, '???': None}
    serializer = Xml()
    packed = serializer.dumps(value)
    assert value == serializer.loads(packed)


def test_simple_set_xml():
    value = set([None, 'fldfkndsfdsfm', 34.0023442, True, 'wejwie', False])
    serializer = Xml()
    packed = serializer.dumps(value)
    assert value == serializer.loads(packed)


'''
Collections testing section
Complex collections
'''


def test_complex_json():
    value = [None, {'key1': 'value1', 2: True, '???': None},
             set([None, 'fldfkndsfdsfm', 34.0023442, True, 'wejwie', False]),
             [{'key': ['value1', 'value2']}, (None, 'fldfkndsfdsfm', 34.0023442, True, 'wejwie', False)]]
    serializer = Json()
    packed = serializer.dumps(value)
    assert value == serializer.loads(packed)


def test_complex_xml():
    value = [None, {'key1': 'value1', 2: True, '???': None},
             set([None, 'fldfkndsfdsfm', 34.0023442, True, 'wejwie', False]),
             [{'key': ['value1', 'value2']}, (None, 'fldfkndsfdsfm', 34.0023442, True, 'wejwie', False)]]
    serializer = Xml()
    packed = serializer.dumps(value)
    assert value == serializer.loads(packed)


'''
Functions testing section
'''


def no_arg_func():
    return 'hello'


def test_no_arg_func_json():
    serializer = Json()
    packed = serializer.dumps(no_arg_func)
    assert no_arg_func() == serializer.loads(packed)()


def test_no_arg_func_xml():
    serializer = Xml()
    packed = serializer.dumps(no_arg_func)
    assert no_arg_func() == serializer.loads(packed)()


def arg_n_kwarg_func(pos1, pos2, kwarg1=True, kwarg2=True):
    return pos1, pos2, kwarg1, kwarg2


def test_arg_n_kwarg_func_json():
    serializer = Json()
    packed = serializer.dumps(arg_n_kwarg_func)
    assert arg_n_kwarg_func('first', 'second', kwarg2=False, kwarg1=True) == serializer.loads(packed)('first', 'second',
                                                                                                      kwarg2=False,
                                                                                                      kwarg1=True)


def test_arg_n_kwarg_func_xml():
    serializer = Xml()
    packed = serializer.dumps(arg_n_kwarg_func)
    assert arg_n_kwarg_func('first', 'second', kwarg2=False, kwarg1=True) == serializer.loads(packed)('first', 'second',
                                                                                                      kwarg2=False,
                                                                                                      kwarg1=True)


def rec_func(value):
    return value + rec_func(value - 1) if value != 0 else 0


def test_rec_func_json():
    serializer = Json()
    packed = serializer.dumps(rec_func)
    assert rec_func(5) == serializer.loads(packed)(5)


def test_rec_func_xml():
    serializer = Xml()
    packed = serializer.dumps(rec_func)
    assert rec_func(5) == serializer.loads(packed)(5)


import math


def closure_and_module_func(value_to_closure: int):
    closured_value = value_to_closure

    def closured_func(another_value: int):
        return math.cos(closured_value + another_value)

    return closured_func


def test_closure_and_module_func_json():
    serializer = Json()
    packed = serializer.dumps(closure_and_module_func(4))
    assert closure_and_module_func(4)(5) == serializer.loads(packed)(5)


def test_closure_and_module_func_xml():
    serializer = Xml()
    packed = serializer.dumps(closure_and_module_func(4))
    assert closure_and_module_func(4)(5) == serializer.loads(packed)(5)


some_module_lambda = lambda x: math.sin(x)


def test_lambda_w_module_json():
    serializer = Json()
    packed = serializer.dumps(some_module_lambda)
    assert some_module_lambda(-1) == serializer.loads(packed)(-1)


def test_lambda_w_module_xml():
    serializer = Xml()
    packed = serializer.dumps(some_module_lambda)
    assert some_module_lambda(-1) == serializer.loads(packed)(-1)


class Iter:
    def __init__(self):
        self.data = ['some', {'keys': 'and', None: 'values'}]
        self.iterator = iter(self.data)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterator)


def test_iter_json():
    serializer = Json()
    packed = serializer.dumps(Iter())
    unpacked = serializer.loads(packed)
    assert next(unpacked) == Iter().data[0]


def test_iter_xml():
    serializer = Xml()
    packed = serializer.dumps(Iter())
    unpacked = serializer.loads(packed)
    assert next(unpacked) == Iter().data[0]


'''
Class&object testing section
'''


class ClassWithDecorator:
    some_field = 1111

    def decorator_func(func):
        def wrapper(self):
            return f'wrapped {func(self)}'

        return wrapper

    @decorator_func
    def to_be_decorated(self):
        return f'to be decorated with field {self.some_field}'


def test_class_w_decorator_json():
    serializer = Json()
    packed = serializer.dumps(ClassWithDecorator)
    deser_class = serializer.loads(packed)
    deser_obj = deser_class()
    assert deser_obj.to_be_decorated() == ClassWithDecorator().to_be_decorated()


def test_class_w_decorator_xml():
    serializer = Xml()
    packed = serializer.dumps(ClassWithDecorator)
    deser_class = serializer.loads(packed)
    deser_obj = deser_class()
    assert deser_obj.to_be_decorated() == ClassWithDecorator().to_be_decorated()


def test_class_object_dynamic_field_json():
    serializer = Json()
    packed = serializer.dumps(ClassWithDecorator)
    deser_class = serializer.loads(packed)
    deser_obj = deser_class()
    true_obj = ClassWithDecorator()
    deser_obj.some_field = 'dsfdsfds'
    true_obj.some_field = 'dsfdsfds'
    assert deser_obj.to_be_decorated() == true_obj.to_be_decorated()


def test_class_object_dynamic_field_xml():
    serializer = Xml()
    packed = serializer.dumps(ClassWithDecorator)
    deser_class = serializer.loads(packed)
    deser_obj = deser_class()
    true_obj = ClassWithDecorator()
    deser_obj.some_field = 'dsfdsfds'
    true_obj.some_field = 'dsfdsfds'
    assert deser_obj.to_be_decorated() == true_obj.to_be_decorated()


class ClassWithStaticMethod:

    @staticmethod
    def get_data(data):
        return f'got data: {data}'


def test_class_w_static_json():
    serializer = Json()
    packed = serializer.dumps(ClassWithStaticMethod)
    deser_class = serializer.loads(packed)
    data_sample = [1, 23.4, (True, None)]
    assert ClassWithStaticMethod.get_data(data_sample) == deser_class.get_data(data_sample)


def test_class_w_static_xml():
    serializer = Xml()
    packed = serializer.dumps(ClassWithStaticMethod)
    deser_class = serializer.loads(packed)
    data_sample = [1, 23.4, (True, None)]
    assert ClassWithStaticMethod.get_data(data_sample) == deser_class.get_data(data_sample)


class ClassWithClassMethod:
    @classmethod
    def get_data(cls):
        return 'this is class method'


def test_class_w_cmethod_json():
    serializer = Json()
    packed = serializer.dumps(ClassWithClassMethod)
    deser_class = serializer.loads(packed)
    assert ClassWithClassMethod.get_data() == deser_class.get_data()


def test_class_w_cmethod_xml():
    serializer = Xml()
    packed = serializer.dumps(ClassWithClassMethod)
    deser_class = serializer.loads(packed)
    assert ClassWithClassMethod.get_data() == deser_class.get_data()


class FirstParent:
    some_field = 'sss'

    def __init__(self, data):
        self.some_field = data

    def some_method(self, value):
        return value


class SecondParent:
    another_field = 'sss'

    def __init__(self, data):
        self.another_field = data

    def another_method(self, value):
        return value


class Child(FirstParent, SecondParent):
    def join_fields(self):
        return "".join([self.some_field, self.another_field])


def test_class_inheritance_json():
    serializer = Json()
    packed = serializer.dumps(Child)
    deser_class = serializer.loads(packed)
    deser_obj = deser_class('weeee')
    true_obj = Child('weeee')
    assert true_obj.join_fields() == deser_obj.join_fields()


def test_class_inheritance_xml():
    serializer = Xml()
    packed = serializer.dumps(Child)
    deser_class = serializer.loads(packed)
    deser_obj = deser_class('weeee')
    true_obj = Child('weeee')
    assert true_obj.join_fields() == deser_obj.join_fields()


def test_class_mro_json():
    serializer = Json()
    packed = serializer.dumps(Child)
    deser_class = serializer.loads(packed)
    assert str(Child.__mro__) == str(deser_class.__mro__)


def test_class_mro_xml():
    serializer = Xml()
    packed = serializer.dumps(Child)
    deser_class = serializer.loads(packed)
    assert str(Child.__mro__) == str(deser_class.__mro__)


'''
Scope testing section
'''

some_global_var = 1111


def global_func():
    global some_global_var
    return f'glob: {some_global_var}'


def test_global_json():
    serializer = Json()
    packed = serializer.dumps(global_func)
    deser_func = serializer.loads(packed)
    some_global_var = 324324
    assert global_func() == deser_func()


def test_global_xml():
    serializer = Xml()
    packed = serializer.dumps(global_func)
    deser_func = serializer.loads(packed)
    some_global_var = 324324
    assert global_func() == deser_func()


def non_local_func_out():
    var = 1234567890

    def non_local_func_in():
        nonlocal var
        return var + 1

    return non_local_func_in


def test_global_json():
    serializer = Json()
    packed = serializer.dumps(non_local_func_out)
    deser_func = serializer.loads(packed)

    assert non_local_func_out()() == deser_func()()


def test_global_xml():
    serializer = Xml()
    packed = serializer.dumps(non_local_func_out)
    deser_func = serializer.loads(packed)

    assert non_local_func_out()() == deser_func()()
