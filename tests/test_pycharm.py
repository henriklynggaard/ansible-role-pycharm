import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


desktop_file_location = "/root/.local/share/applications/pycharm-community-2017.1.5.desktop"


def test_desktop_file_exists(File):
    f = File(desktop_file_location)

    assert f.exists
    assert f.is_file


def test_desktop_file_contains_fullpath(File):
    f = File(desktop_file_location)

    assert f.contains("/root/Tools/pycharm-community-2017.1.5/bin/pycharm.png")
    assert f.contains("/root/Tools/pycharm-community-2017.1.5/bin/pycharm.sh")


def test_desktop_file_contains_right_name(File):
    f = File(desktop_file_location)

    assert f.contains("PyCharm Community Edition 2017.1.5")


def test_start_file_exists(File):
    f = File('/root/Tools/pycharm-community-2017.1.5/bin/pycharm.sh')

    assert f.exists
    assert f.is_file
