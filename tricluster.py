
def get_clusters(FCP: list, min_support_count = 1, min_size = 2) ->list:
    """Returns a list of tri-clusters from the given list of FCPs"""
    
    return [fcp.toJSON(include_object=True)
     for fcp in FCP if fcp.support_count() >= min_support_count and fcp.size() >= min_size]