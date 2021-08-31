import collections
import logging

logger = logging.getLogger(__name__)


def get_all_entities_of_annotation(data):
    result = {}
    if 'data' in data:
        data = data['data']
        result_gold = _get_entities_of_annotation(data['gold'])
        result_computed = _get_entities_of_annotation(data['computed'])
        result = collections.defaultdict(set)
        _add_entities(result, result_gold)
        _add_entities(result, result_computed)
    return result


def _add_entities(result, entities):
    for entity in entities:
        result[entity].update(entities[entity])


def _get_entities_of_annotation(entities):
    result = collections.defaultdict(set)
    for entity_key in entities:
        for entity in entities[entity_key]:
            if 'annotations' in entity:
                for annotation in entity['annotations']:
                    if 'type' in annotation and 'entity' in annotation:
                        result[annotation['type']].add(annotation['entity'])
                    else:
                        logger.error('annotations has wrong format. Missing type or entity.')
    return result
