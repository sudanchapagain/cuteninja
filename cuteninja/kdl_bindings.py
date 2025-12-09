class KdlParseError(Exception):
    """Error raised when KDL parsing fails."""


try:
    import kdl_rs

    def parse(source: str):
        """parse KDL source using kdl_rs_py."""
        return kdl_rs.parse(source)

    Document = kdl_rs.Document
    Node = kdl_rs.Node

except ImportError:

    def parse(source: str):
        """parse KDL source: requires kdl_rs_py to be installed."""
        raise NotImplementedError("kdl_rs_py not installed")

    class Document:
        """Document class: requires kdl_rs_py to be installed."""

        def __init__(self):
            raise NotImplementedError("kdl_rs_py not installed")

    class Node:
        """Node class: requires kdl_rs_py to be installed."""

        pass


__all__ = ["parse", "Document", "Node", "KdlParseError"]
