from datetime import datetime
import logging
import json

from sqlalchemy.event import listens_for

from src.models import LOG_FILENAME


logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)


def make_dump(row):
    return json.dumps(
        {k: v.strftime("%Y-%m-%d %H:%M:%S") if isinstance(v, datetime) else v
         for k, v in row.__dict__.items() if k[0] != '_'}
    )


def log_insert(mapper, connection, target):
    dump = make_dump(target)
    logging.info(f'Insert into table {target.__tablename__} values {dump}')


def log_update(mapper, connection, target):
    dump = make_dump(target)
    logging.info(f'Update from table {target.__tablename__} values {dump}')


def log_delete(mapper, connection, target):
    dump = make_dump(target)
    logging.info(f'delete from table {target.__tablename__} values {dump}')


ACTIONS = {
    'after_insert': log_insert,
    'after_update': log_update,
    'after_delete': log_delete
}


def loging_models(*models):
    for event, function in ACTIONS.items():
        for model in models:
            listens_for(model, event)(function)
