class KdlParseError(Exception):
    """Error raised when KDL parsing fails."""


try:
    import ckdl

    def parse(source: str):
        """parse KDL source using ckdl."""
        return ckdl.parse(source)

    Document = ckdl.Document
    Node = ckdl.Node

except ImportError:

    def parse(source: str):
        """parse KDL source: requires ckdl to be installed."""
        raise NotImplementedError("ckdl not installed")

    class Document:
        """Document class: requires kdl_rs_py to be installed."""

        def __init__(self):
            raise NotImplementedError("kdl_rs_py not installed")

    class Node:
        """Node class: requires kdl_rs_py to be installed."""

        pass


__all__ = ["parse", "Document", "Node", "KdlParseError"]
