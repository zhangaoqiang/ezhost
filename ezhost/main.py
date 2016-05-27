#!/usr/bin/python
"""
This module contains `main` method plus related subroutines.
`main` is executed as the command line ``ezhost`` program and takes care of
parsing options and commands

The other callables defined in this module are internal only. Anything useful
to individuals leveraging Fabric as a library, should be kept elsewhere.
"""
import argparse, configparser
from ezhost.ServerBase import ServerBase

def main():
    """
        Check args
    """

    configure_obj = None
    try:
        parser = argparse.ArgumentParser(description='Easy to install server.')
        parser.add_argument(
            '-s', 
            '--server', 
            help='what kind of server you want to install',  
            required=True
        )
        parser.add_argument(
            '-c', 
            '--config', 
            help='config file path of your host informations', 
        )
        parser.add_argument(
            '-H', 
            '--host', 
            help='host server address', 
        )
        parser.add_argument(
            '-U', 
            '--user', 
            help='host server login user', 
        )
        parser.add_argument(
            '-P', 
            '--passwd', 
            help='host server login password', 
        )
        parser.add_argument(
            '-K', 
            '--keyfile', 
            help='host server key file path', 
        )

        args = parser.parse_args()
    except Exception as e:
        parser.print_help()

    # if config file and host both not provide, throw a error
    try:
        if args.config is None and args.host is None:
            raise ValueError('You have to setup your host information through -c(--config) or -H(--host)')
    except Exception as e:
        print(e)
        return

    # check user and passwd
    try:
        if args.host is not None:
            if (args.user and (args.passwd or args.keyfile) ) is None:
                raise ValueError('Lack of required host information. Please check whether you have set login user, login password or keyfile.')
    except Exception as e:
        print(e)
        return

    # if exist config file, read configuration from file
    try:
        if args.config is not None:
            # init configuration parser
            configure = configparser.ConfigParser()
            configure.read(args.config)

            # check key exist
            if 'ezhost' in configure:
                configure_obj = configure['ezhost']
            else:
                raise KeyError('Can not found ezhost configuration informations.')
    except Exception as e:
        print(e)
        return

    # init server
    ServerBase(args, configure_obj)

