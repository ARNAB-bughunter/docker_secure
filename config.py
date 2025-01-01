import yaml
import os


def parse_yaml(file):
    ''' Parse yaml file into dict '''
    try:
        info = yaml.safe_load(open(file))
        return info
    except Exception as e:
        print(e)
        print("Unable to find file....... ")
        return False


def get_corpus():
    info = parse_yaml('corpus.yaml')
    if info:
        try:
            return info
        except Exception:
            print("Unable to find corpus path..... ")
            return False
    else:
        return False


def get_host():
    # info = parse_yaml('config.yaml')
    # if info:
    #     try:
    #         return info['host']
    try:
        return os.environ.get('date_parser_host')
    except Exception:
        print("Unable to find date_parser host..... ")
        return False
    # else:
    #     return False


def get_port():
    # info = parse_yaml('config.yaml')
    # if info:
    #     try:
    #         return info['dev_port']
    try:
        return os.environ.get('date_parser_port')
    except Exception:
        print("Unable to find date_parser port..... ")
        return False
    # else:
    #     return False
