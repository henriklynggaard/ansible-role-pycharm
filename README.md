Pycharm
=========

This role installs Pycharm and configured plugins. It has been tested on Linux Mint 18 but should wokr on most 
distributions. By default it installs Pycharm community edition 2017.1.1 and no additional plugins

By default Pycharm is installed under the user's home directory and _become_ is not needed.

Requirements
------------

None


Role Variables
--------------

    pycharm_version: 2017.1.1
    pycharm_edition: community
    pycharm_download_mirror: https://download.jetbrains.com/python/
    pycharm_plugin_download_mirror: "https://plugins.jetbrains.com/plugin/download?updateId="
    pycharm_plugins: []
    pycharm_download_directory: /tmp
    pycharm_install_directory: "{{ ansible_env['HOME'] }}/Tools"

    pycharm_install_file: "pycharm-{{ pycharm_edition}}-{{ pycharm_version }}.tar.gz"
    pycharm_download_url: "{{ pycharm_download_mirror }}{{ pycharm_install_file }}"
    pycharm_desktop_file_directory: "{{ ansible_env['HOME'] }}/.local/share/applications"
    pycharm_desktop_file_location: "{{ pycharm_desktop_file_directory }}//pycharm-{{ pycharm_edition }}-{{ pycharm_version }}.desktop"


pycharm_plugins is a list of names which get appended to pycharm_plugin_download_mirror to form a full download  


Dependencies
------------

None

Example 
-------

__Example playbook__


    - hosts: localhost
      connection: local
    
    roles:
      - henriklyngaard.pycharm
      
__Exmaple inventory for plugins__

The below IDs have been found by going to https://plugins.jetbrains.com/pycharm and searching for the plugin. 
Once found copy the link location for the desired version and use the _updateId=XXXXX_ part at the end        
      
    pycharm_plugins:
      # ignore 1.7.6
      - 32828
      # bash support 1.6.5.171
      - 31610
      # ansible 0.9.4
      - 27616
      # docker 2.5.3
      - 33621
      # markdown 2017.1.20170302
      - 33092      
      
 Alternatively upload the required plugins to a webserver and adjust _pycharm_plugin_download_mirror_ and 
 _pycharm_plugins_ accordingly
      
      
License
-------

MIT

Change log
----------

* 1.1: Create the desktop file directory in case we are the first
* 1.0: Initial version
