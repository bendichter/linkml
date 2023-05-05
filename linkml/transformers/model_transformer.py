from abc import abstractmethod
from dataclasses import dataclass
from typing import Any

from linkml_runtime import SchemaView
from linkml_runtime.linkml_model import SlotDefinition, ClassDefinitionName


@dataclass
class ModelTransformer:
    """
    Base class for all model transformers
    """
    schemaview: SchemaView = None

    @abstractmethod
    def transform(
            self, tgt_schema_name: str = None, top_class: ClassDefinitionName = None
    ) -> Any:
        raise NotImplementedError

    def unfold_slot_range(self, slot: SlotDefinition):
        union_ranges = []
        for x in slot.any_of + slot.exactly_one_of:
            if x.range:
                union_ranges.append(x.range)
        if not union_ranges:
            union_ranges.append(slot.range)
        

