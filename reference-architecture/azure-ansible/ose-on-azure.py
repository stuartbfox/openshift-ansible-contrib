#!/usr/bin/env python
# vim: sw=2 ts=2

import click
from jinja2 import Environment, FileSystemLoader
import os
import sys
import json
import types
from copy import deepcopy

@click.command()

### Cluster options
@click.option('--console-port', default='443', type=click.IntRange(1,65535), help='OpenShift web console port',
              show_default=True)
@click.option('--deployment-type', default='openshift-enterprise', help='OpenShift deployment type',
              show_default=True)

### Azure options
@click.option('--group-name', default='OpenShift-Infra', help='Azure Resource Group name',
              show_default=True)
@click.option('--region', default='westus', help='Azure Region',
              show_default=True)
@click.option('--vars-file', default='vars/main.yaml',
            help="Location of environment specific variables, either fully qualified or relative to the playbooks directory",
            show_default=True)

def launch_refarch_env(group_name=None,
                       region=None,
                       create_rg=None,
                       create_vnet=None,
                       create_storage=None,
                       create_private=None,
                       create_public=None,
                       vnet_cidr=None,
                       public_cidr=None,
                       private_cidr=None,
                       ssh_key=None,
                       vars_file=None):

  playbooks = ['playbooks/infrastructure.yaml']
  #playbooks = ['playbooks/infrastructure.yaml', 'playbooks/openshift-install.yaml']:

  for playbook in playbooks:


    command=('ansible-playbook -i nventory/azure/hosts/azure_rm.py -e \'\
    console_port=%s \
    deployment_type=%s \
    group_name=%s \
    region=%s \
    create_rg=%s \
    create_vnet=%s \
    create_storage=%s \
    create_private=%s \
    create_public=%s \
    vnet_cidr=%s \
    public_cidr=%s \
    private_cidr=%s \
    ssh_key=%s \
    vars_file=%s  \' %s') % (
                      console_port,
                      deployment_type,
                      group_name,
                      region,
                      create_rg,
                      create_vnet,
                      create_storage,
                      create_private,
                      create_public,
                      vnet_cidr,
                      public_cidr,
                      private_cidr,
                      ssh_key,
                      vars_file,
                      playbook)

    if verbose > 0:
      command += " -" + "".join(['vvv']*verbose)
      click.echo('We are running: %s' % command)

if __name__ == '__main__':
  launch_refarch_env()
