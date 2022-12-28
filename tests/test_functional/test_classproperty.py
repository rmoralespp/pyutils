# -*- coding: utf-8 -*-
import pytest

import pymince.functional


def test_with_method():
    class MyClass:
        @pymince.functional.classproperty
        def name(self):
            return self._name

    with pytest.raises(AttributeError):
        assert MyClass.name


def test_from_cls():
    class MyClass:
        _foo = "var"

        @pymince.functional.classproperty
        def foo(cls):
            return cls._foo

    assert MyClass.foo == "var"


def test_from_obj():
    class MyClass:
        _foo = "var"

        @pymince.functional.classproperty
        def foo(cls):
            return cls._foo

    obj = MyClass()
    assert obj.foo == "var"


def test_with_params():
    class MyClass:
        @pymince.functional.classproperty
        def foo(cls, *args, **kwargs):
            return args, kwargs

    with pytest.raises(TypeError):
        assert MyClass.foo("a", b="b")
