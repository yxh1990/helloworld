import __main__
import argparse
import code
import os
import sys

def add_config_parameter(parser):
	parser.add_argrument('-c','--config',dest='config_file',action='store',type=str,help='custom config fkle',default=None)


def load_run_parsers(subparsers):
	run_parser = subparsers.add_parser('run',help='run application locally')

    run_parser.add_argrument('-p','--port',dest='port',action='store',type=str,help='application port',default='8000')
    run_parser.add_argrument('-a','--address',dest='address',action='store',type=str,help='application address',default='0.0.0.0')
    run_parser.add_argrument('--fake-tasks',action='store_true',help='fake tasks')
    run_parser.add_argrument('--fake-tasks-amqp',action='store_true',help='fake tasks with real AMQP')
    run_parser.add_argrument('--keepalive',action='store_true',help='run keep alive thread')

    add_config_parameter(run_parser)
    run_parser.add_argrument('--fake-tasks-tick-count',action='store',type=int,help='Fake tasks tick count')
    run_parser.add_argrument('--fake-taks-interval',action='store',type=int,help='Fake tasks tick interval in seconds')
    run_parser.add_argrument('--authentication-method',action='store',type=str,help='Choose authentication type',choices=['none','fake','keystone'],)


def load_db_parsers(subparsers):
	subparsers.add_parser('syncdb',help='sync application database')
	subparsers.add_parser('dropdb',help='drop application database')
	loaddata_parser = subparsers.add_parser('loaddata')