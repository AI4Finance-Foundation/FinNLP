"""Regression tests for the Stocknet dataset loader."""

import importlib.util
import json
import os
import sys
import tempfile
import types
import unittest
from pathlib import Path


MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "finnlp"
    / "data_sources"
    / "datasets"
    / "load_dataset.py"
)


def load_module():
    """Load the loader with a minimal local substitute for optional datasets."""
    fake_datasets = types.ModuleType("datasets")
    fake_datasets.Dataset = types.SimpleNamespace(from_pandas=lambda dataframe: dataframe)

    original_datasets = sys.modules.get("datasets")
    sys.modules["datasets"] = fake_datasets
    try:
        spec = importlib.util.spec_from_file_location("finnlp_load_dataset", MODULE_PATH)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    finally:
        if original_datasets is None:
            del sys.modules["datasets"]
        else:
            sys.modules["datasets"] = original_datasets

    return module


class LoadDatasetTests(unittest.TestCase):
    def test_stocknet_loader_reads_each_date_file_once(self):
        module = load_module()

        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_path = Path(temporary_directory)
            work_directory = temporary_path / "one" / "two" / "three"
            data_directory = temporary_path / "stocknet-dataset" / "tweet" / "raw" / "AAPL"
            work_directory.mkdir(parents=True)
            data_directory.mkdir(parents=True)
            (data_directory / "2024-01-01.json").write_text(
                json.dumps({"id": "first"}) + "\n", encoding="utf-8"
            )
            (data_directory / "2024-01-02.json").write_text(
                json.dumps({"id": "second"}) + "\n", encoding="utf-8"
            )

            original_directory = os.getcwd()
            try:
                os.chdir(work_directory)
                dataset = module.load_dataset("Stocknet")
            finally:
                os.chdir(original_directory)

        self.assertEqual(sorted(dataset["id"].tolist()), ["first", "second"])


if __name__ == "__main__":
    unittest.main()
