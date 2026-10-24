import json
import logging
import yaml
import xml.etree.ElementTree as ET
import csv

logger = logging.getLogger(__name__)

def parse_json(file_path: str):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except (FileNotFoundError, IOError) as e:
        logger.error(f"Error parsing JSON file: {e}")
        return []

def parse_yaml(file_path: str):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        logger.info("PARSE_YAML_SUCCESS")
        return data if data is not None else []
    except (FileNotFoundError, yaml.YAMLError) as e:
        logger.error(f"PARSE_YAML_ERROR: {e}")
        return []

def parse_csv(file_path: str):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            data = list(reader)
        logger.info("PARSE_CSV_SUCCESS")
        return data
    except (FileNotFoundError, IOError) as e:
        logger.error(f"PARSE_CSV_ERROR: {e}")
        return []

def parse_xml(file_path: str):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        logger.info("PARSE_XML_SUCCESS")
        return root
    except (FileNotFoundError, ET.ParseError) as e:
        logger.error(f"PARSE_XML_ERROR: {e}")
        return []
    