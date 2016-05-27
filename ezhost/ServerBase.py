# -*- coding: utf-8 -*-
"""
Base class for all server class
"""
from fabric.api import env

from ezhost.ServerAbstract import ServerAbstract
from ezhost.ServerLists import ServerLists
from ezhost.ServerLamp import ServerLamp

class ServerBase(ServerAbstract):
    def __init__(self, args, configure_obj):
        self.args = args
        self.configure_obj = configure_obj

        # set server type
        self.server_type = args.server
        
        # parser parameters
        self._parse_parameters()

        # initial host 
        self.init_host()

        # install 
        self.install()

    def install(self):
        """
            install the server
        """
        try:
            server = ServerLists(self.server_type)
            eval(server.name)().install()
        except Exception as e:
            raise e
       

    def _parse_parameters(self):
        # set args from commmand parser
        if self.configure_obj is None:
            self.host_string = args.host
            self.host_user = args.user
            self.host_passwd = args.passwd
            self.host_keyfile = args.keyfile

        # set args from config file parser
        else:
            try:
                self.host_string = self.configure_obj['host']
                self.host_user = self.configure_obj['user']
            except Exception as e:
                raise KeyError('Lack of required host information. Please check whether you have set host address or login user.')
           
            try:
                self.host_keyfile = self.configure_obj['keyfile']
            except Exception as e:
                self.host_keyfile = None

            if self.host_keyfile is None:
                try:
                    self.host_passwd = self.configure_obj['passwd']
                except Exception as e:
                    raise KeyError('Lack of required host information. Please check whether you have set login password or keyfile.')


            

    def init_host(self):
        """
            Initial  host 
        """
        env.host_string = self.host_string
        env.user = self.host_user
        env.password = self.host_passwd
        env.key_filename = self.host_keyfile