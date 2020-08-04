def flatten_json(nested_json):
    """
        Flatten json object with nested keys into a single level.
        Args:
            object: A nested json object.
        Returns:
            The flattened json object if successful, None otherwise.
    """
    out = {}

    def flatten(object, name=''):
        if type(object) is dict:
            for element in object:
                flatten(object[element], name + element + '/')
        elif type(object) is list:
            i = 0
            for element in object:
                flatten(element, name + str(i) + '/')
                i += 1
        else:
            out[name[:-1]] = object

    flatten(nested_json)
    return out