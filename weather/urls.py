#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 15:36:29 2021

@author: alexisng
"""

from django.urls import path 
from . import views
urlpatterns = [
   
    path('', views.index),
    ]