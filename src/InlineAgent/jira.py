from mcp import StdioServerParameters

from InlineAgent.tools import MCPStdio
from InlineAgent.action_group import ActionGroup
from InlineAgent.agent import InlineAgent

# Step 1: Define MCP stdio parameters
server_params = StdioServerParameters(
    command="npx",
    args=["-y","mcp-remote","https://mcp.atlassian.com/v1/sse"],
)


async def main():
    # Step 2: Create MCP Client
    time_mcp_client = None
    
    try:
        time_mcp_client = await MCPStdio.create(server_params=server_params)

        # Step 3: Define an action group
        time_action_group = ActionGroup(
            name="JiraActionGroup",
            description="Helps user interact with Jira projects and issues.",
            mcp_clients=[time_mcp_client],
        )

        # Step 4: Invoke agent
        await InlineAgent(
            # Step 4.1: Provide the model (using inference profile ARN)
            foundation_model="arn:aws:bedrock:us-west-2:310018062324:inference-profile/us.anthropic.claude-sonnet-4-20250514-v1:0",
            # Step 4.2: Concise instruction
            instruction="""You are a friendly assistant that is responsible for resolving user queries. You can make multiple calls to the MCP service to resolve user queries.""",
            # Step 4.3: Provide the agent name and action group
            agent_name="jira_agent",
            action_groups=[time_action_group],
            profile="hackathon",
        ).invoke(
            input_text="Show me all the jira projects I have access to"
        )

    except Exception as e:
        print(f"Error occurred: {e}")
        raise
    finally:
        # Ensure proper cleanup even if an error occurs
        if time_mcp_client is not None:
            try:
                await time_mcp_client.cleanup()
            except Exception as cleanup_error:
                print(f"Warning: Error during cleanup: {cleanup_error}")
                # Don't re-raise cleanup errors to avoid masking the original error


if __name__ == "__main__":
    import asyncio
    import sys
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        sys.exit(0)
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)
