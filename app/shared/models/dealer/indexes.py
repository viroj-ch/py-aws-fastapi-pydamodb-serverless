from pynamodb.attributes import UnicodeAttribute
from pynamodb.indexes import GlobalSecondaryIndex, IncludeProjection


class DealerStatusPriorityIdIndex(GlobalSecondaryIndex):
    class Meta:
        index_name = 'dealerStatus-priorityId-index'
        projection = IncludeProjection(['dealerNameThai', 'taxId'])

    dealerStatus = UnicodeAttribute(hash_key=True)
    priorityId = UnicodeAttribute(range_key=True)
