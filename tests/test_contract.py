import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]
PACKAGE = 'transition_grant_review'

def read_csv(name):
    with (ROOT / 'data' / name).open(encoding='utf-8', newline='') as handle:
        return list(csv.DictReader(handle))

def read_json(name):
    return json.loads((ROOT / 'data' / name).read_text(encoding='utf-8'))

class ContractTests(unittest.TestCase):
    def test_package_name_and_data_directory(self):
        self.assertTrue(PACKAGE)
        self.assertTrue((ROOT / 'data').is_dir())

    def test_application_ids_are_unique(self):
        rows = read_csv('applications.csv')
        self.assertTrue(len({row['application_id'] for row in rows}) == len(rows))

    def test_rejected_evidence_is_preserved(self):
        rows = read_csv('evidence.csv')
        self.assertTrue(next(row for row in rows if row['evidence_id'] == 'E03')['check_status'] == 'rejected')
