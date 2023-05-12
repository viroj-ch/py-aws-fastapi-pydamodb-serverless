from pynamodb.attributes import (NumberAttribute, UnicodeAttribute)
from pynamodb.models import Model

from .indexes import DealerStatusPriorityIdIndex


class DealerModel(Model):
    class Meta:
        table_name = 'dev-bay-idisburse-dealer'
        region = 'ap-southeast-1'

    dealerStatusPriorityIdIndex = DealerStatusPriorityIdIndex()

    dealerCode = UnicodeAttribute(hash_key=True)
    createdDate = UnicodeAttribute(null=True)
    modifiedDate = UnicodeAttribute(null=True)
    dealerNameThai = UnicodeAttribute()
    dealerStatus = UnicodeAttribute()
    priorityId = UnicodeAttribute()
    priorityLevel = NumberAttribute(default=0)
    taxId = UnicodeAttribute()
