#!/usr/bin/python
# encoding: utf-8
"""
@author: lwqhp
Contact: 
@file: base.py
@time:2024/2/2 10:07
"""
import os
from typing import Optional
import pathlib
from pydantic import BaseModel

class LogSettings(BaseModel):
    LEVEL: Optional[str] = 'DEBUG'
    PATH: str =pathlib.Path(__file__).resolve().parent.parent.joinpath('logs', 'xiaogpt.log')
    STDOUT: Optional[bool] = True
    ROTATION: Optional[str] = '00:00'
    RETENTION: Optional[str] = '30 days'
    COMPRESSION: Optional[str] = None

class BaseConfig():
    API_NAME = "小爱智能音箱"
    TIMEOUT = 120
    BASEDIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    DEBUG = False
