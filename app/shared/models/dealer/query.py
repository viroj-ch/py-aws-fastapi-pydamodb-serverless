from .dealer import DealerModel


def query_by_dealer_status_and_priority_id(dealer_status: str, priority_id: str, limit: int):
    results = DealerModel.dealerStatusPriorityIdIndex.query(
        dealer_status,
        DealerModel.priorityId == priority_id,
        limit=limit
    )
    return [result.attribute_values for result in results]


def query_by_dealer_code(dealer_code: str):
    try:
        return DealerModel.get(dealer_code).attribute_values
    except DealerModel.DoesNotExist:
        return None
