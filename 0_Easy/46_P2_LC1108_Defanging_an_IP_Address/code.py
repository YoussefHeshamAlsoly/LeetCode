def defangIPaddr(address):
    """
    :type address: str
    :rtype: str
    """
    address = address.split(".")
    return "[.]".join(address)

