"""
Handlers to communicate with database
"""

from database import database
from decorators import require_json
from utils import json_result, json_error


@require_json(require_data=False)
def get_all(**kwargs):
    return json_result(database.get_all())


@require_json()
def get_by_name(data=None, **kwargs):
    """
    We are searching by name case-insensitive
    """
    if len(data.split()) > 1:
        return json_error("Data must be one word!")

    return json_result(database.get_by_name(data))


@require_json()
def get_by_miRNA_s(data=None, **kwargs):
    """
    We are searching by only first two nucleotides of endogenous miRNA
    """
    if len(data) != 2:
        return json_error("Data must have 2 characters!")

    return json_result(database.get_by_miRNA_s(data))


get_all.methods = ['POST']
get_by_name.methods = ['POST']
get_by_miRNA_s.methods = ['POST']
