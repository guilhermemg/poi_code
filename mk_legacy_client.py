#!/usr/bin/env python

import os_client_config

auth_url = 'http://localhost:5000/v3'
project_name = 'demo'
username = 'admin'
password = 'nomoresecret'
region_name = 'RegionOne'

def make_nova_client():
    legacy_client = os_client_config.make_client(
	'compute',
        auth_url=auth_url,
        username=username,
        password=password,
        project_name=project_name,
        region_name=region_name)
    return legacy_client

def make_glance_client():
    legacy_client = os_client_config.make_client(
        'image',
        auth_url=auth_url,
        username=username,
        password=password,
        project_name=project_name,
        region_name=region_name)
    return legacy_client

def make_neutron_client():
    legacy_client = os_client_config.make_client(
        'network',
        auth_url=auth_url,
        username=username,
        password=password,
        project_name=project_name,
        region_name=region_name)
    return legacy_client    

def make_keystone_client():
    legacy_client = os_client_config.make_client(
        'identity',
        auth_url=auth_url,
        username=username,
        password=password,
        project_name=project_name,
        region_name=region_name)
    return legacy_client
