from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a:int, b:int) -> int:
    """return sum of two integers

    Args:
        a (int): first int
        b (int): second int

    Returns:
        int: sum of two given ints
    """
    return a+b

@mcp.tool()
def multiple(a:int, b:int) -> int:
    """return multiplication of two integers

    Args:
        a (int): first int
        b (int): second int

    Returns:
        int: multiple of two given ints
    """
    return a*b


# The transport=stdio argument tells the server to use the standard input/output (stdin and stdout)
# to receive and respond to tool function calls

if __name__ == "__main__":
    mcp.run(transport="stdio")