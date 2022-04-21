[![CI tests](https://github.com/scicore-unibas-ch/ansible-role-biomedit-transfers-tool/actions/workflows/ci_tests.yml/badge.svg)](https://github.com/scicore-unibas-ch/ansible-role-biomedit-transfers-tool/actions/workflows/ci_tests.yml)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-scicore.biomedit_transfers_tool-blue.svg)](https://galaxy.ansible.com/scicore/biomedit_transfers_tool)


ansible-role-biomedit-transfers-tool (SETT)
=========

Install the BiomedIT transfer tool (SETT) in a virtualenv.

Tested on Centos7


Role Variables
--------------

```
# SETT tool will be installed in a virtualenv in this path
biomedit_transfers_tool_venv_path: "/opt/sett"

# should we install the epel-release rpm to enable EPEL yum repo?
biomedit_transfers_tool_install_epel: yes

# should we create a file in /etc/profile.d/ to add the binaries to PATH?
biomedit_transfers_tool_add_to_path: yes
```

License
-------

BSD

Author Information
------------------

Pablo Escobar
