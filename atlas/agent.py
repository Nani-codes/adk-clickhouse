
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters


root_agent = LlmAgent(
    model='gemini-2.0-flash',
    name='clikchouse_agent',
    description='A ClickHouse agent that can help you to retrieve data from ClickHouse',
    instruction='You are a ClickHouse agent. You can help users to retrieve data from ClickHouse. You can use the tools provided to interact with ClickHouse.',
    tools=[
        MCPToolset(
            connection_params=StdioServerParameters(
                command='uv',
                args=[
                        "run",
                        "--with",
                        "mcp-clickhouse",
                        "--python",
                        "3.13",
                        "mcp-clickhouse"
                    ],
                env={
                        "CLICKHOUSE_HOST": "",
                        "CLICKHOUSE_USER": "",
                        "CLICKHOUSE_PASSWORD": "",
                        "CLICKHOUSE_PORT": "8443",
                        "CLICKHOUSE_SECURE": "true",
                        "CLICKHOUSE_VERIFY": "true",
                        "CLICKHOUSE_CONNECT_TIMEOUT": "30",
                        "CLICKHOUSE_SEND_RECEIVE_TIMEOUT": "30"
                    }
            ),
            # Optional: Filter which tools from the MCP server are exposed
            # tool_filter=['list_directory', 'read_file']
        )
    ],
)
