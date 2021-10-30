# -*- coding: utf-8 -*-
"""BioImageIT formats reader service provider.

This module implement the runner service provider

Classes
-------
RunnerServiceProvider

"""
from ._plugins import ImagetiffServiceBuilder, MovietxtServiceBuilder


class ObjectFactory:
    """Agnostic factory

    Implements the factory design pattern

    """
    def __init__(self):
        self._builders = {}

    def register_builder(self, key, builder):
        """Add a new service builder to the factory"""
        self._builders[key] = builder

    def create(self, key, **kwargs):
        """Create a new service builder"""
        builder = self._builders.get(key)
        if not builder:
            raise ValueError(key)
        return builder(**kwargs)


class FormatsReaderServiceProvider(ObjectFactory):
    """Service provider for the formats readers"""
    def get(self, service_id, **kwargs):
        return self.create(service_id, **kwargs)


formatsServices = FormatsReaderServiceProvider()
formatsServices.register_builder('imagetiff', ImagetiffServiceBuilder())
formatsServices.register_builder('movietxt', MovietxtServiceBuilder())
