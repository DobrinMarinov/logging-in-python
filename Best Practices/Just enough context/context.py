import logging

def do_service_lookup(service_address):
    try:
        raise Exception('Connection refused.')

    except:
        logging.exception('Exception in: %s' % service_address)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    do_service_lookup('10.0.0.15')
