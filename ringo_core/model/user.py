#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Modul for Users"""
import sqlalchemy as sa
from ringo_core.lib.security import encrypt_password
from ringo_core.lib.db import Base
from ringo_core.model.base import BaseItem, BaseFactory


class UserFactory(BaseFactory):

    """Factory for user objects"""

    def create(self, name, password):
        """Will create a new :class:`User` object. The password will be
        encrypted.

        :name: Name of the new user. Used as for the username on
        authentification.
        :password: Unencrypted password of the new user.
        :returns: :class:`User` object.

        """
        encrypted_password = encrypt_password(password)
        return User(name, encrypted_password)


class User(BaseItem, Base):
    """User class"""
    __tablename__ = "users"

    name = sa.Column("name", sa.String, nullable=False)
    """Username of the user."""
    password = sa.Column("password", sa.String, nullable=False)
    """Encrypted password of the user."""

    def __init__(self, name, password):
        """TODO: to be defined1.
        :name: Name of the user used as username
        :password: Encrypted password of the user
        """
        super(User, self).__init__()

        self.name = name
        self.password = password

    @classmethod
    def get_factory(cls, db):
        return UserFactory(User, db)
