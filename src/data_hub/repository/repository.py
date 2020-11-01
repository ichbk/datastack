from typing import Dict, Tuple
from data_hub.dataset.factory import BaseDatasetFactory
from data_hub.dataset.iterator import DatasetIteratorIF
from data_hub.exception import DatasetNotFoundError
from data_hub.dataset.meta import IteratorMeta


class DatasetRepository:
    def __init__(self):
        self._base_factory_dict: Dict[str, BaseDatasetFactory] = dict()

    def get(self, identifier: str, split: str) -> Tuple[DatasetIteratorIF, IteratorMeta]:
        if identifier not in self._base_factory_dict.keys():
            raise DatasetNotFoundError
        return self._base_factory_dict[identifier].get_dataset_iterator(split)

    def register(self, identifier: str, dataset_factory: BaseDatasetFactory):
        self._base_factory_dict[identifier] = dataset_factory
