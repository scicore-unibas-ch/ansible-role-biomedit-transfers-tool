import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_sett_executable(host):
    f = host.file('/opt/sett/bin/sett')
    assert f.exists
    assert f.is_file


def test_sett_gui_executable(host):
    f = host.file('/opt/sett/bin/sett-gui')
    assert f.exists
    assert f.is_file
