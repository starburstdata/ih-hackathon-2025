from InlineAgent.agent import InlineAgent

import asyncio

instruction = """
You are a friendly assistant that is responsible manipulating a data structure.
The format of the data structure is: `(id, name, type, path, [nested])` where: V=VARCHAR, B=BIGINT, A=ARRAY.
An example data structure is:
```
[(1,"specversion","V","/specversion"),(2,"id","V","/id"),(3,"source","V","/source"),(4,"type","V","/type"),(5,"time","V","/time"),(7,"duration_millis","B","/data/durationMillis"),(8,"cluster_id","V","/data/clusterId"),(9,"account_id","V","/data/accountId"),(10,"deployment_id","V","/data/deploymentId"),(11,"cloud_region_id","V","/data/cloudRegionId"),(12,"payment_tier","V","/data/paymentTier"),(13,"variant","V","/data/variant"),(14,"role","V","/data/role"),(15,"node_instance_type","V","/data/nodeInstanceType"),(16,"pod_name","V","/data/podName"),(17,"pod_ip","V","/data/podIp"),(18,"catalog_metrics","A","/data/catalogMetrics",[(21,"catalog_id","V","/catalogId"),(22,"catalog_name","V","/catalogName"),(23,"intra_region_read_bytes","B","/intraRegionReadBytes"),(24,"intra_region_write_bytes","B","/intraRegionWriteBytes"),(25,"cross_region_read_bytes","B","/crossRegionReadBytes"),(26,"cross_region_write_bytes","B","/crossRegionWriteBytes"),(27,"private_link_read_bytes","B","/privateLinkReadBytes"),(28,"private_link_write_bytes","B","/privateLinkWriteBytes")])]
```
The user may ask you to:
1. Add a new field to the data structure.
2. Remove a field from the data structure.
3. Rename a field in the data structure.
4. Change the type of a field in the data structure.
5. Add a nested field to the data structure.
6. Remove a nested field from the data structure.
7. Rename a nested field in the data structure.
8. Change the type of a nested field in the data structure.

You should always return the updated data structure in the same format as above. The data structure will
be used by a downstream system, so it is important to maintain the format and structure.
"""

# Step 3: Define agent
agent = InlineAgent(
    foundation_model="arn:aws:bedrock:us-west-2:310018062324:inference-profile/us.anthropic.claude-sonnet-4-20250514-v1:0",
    instruction=instruction,
    agent_name="Icehouse",
    profile="hackathon",
)

input_text = """
In the following data structure, remove the fields specversion, id, and source:
```
[(1,"specversion","V","/specversion"),(2,"id","V","/id"),(3,"source","V","/source"),(4,"type","V","/type"),(5,"time","V","/time"),(7,"duration_millis","B","/data/durationMillis"),(8,"cluster_id","V","/data/clusterId"),(9,"account_id","V","/data/accountId"),(10,"deployment_id","V","/data/deploymentId"),(11,"cloud_region_id","V","/data/cloudRegionId"),(12,"payment_tier","V","/data/paymentTier"),(13,"variant","V","/data/variant"),(14,"role","V","/data/role"),(15,"node_instance_type","V","/data/nodeInstanceType"),(16,"pod_name","V","/data/podName"),(17,"pod_ip","V","/data/podIp"),(18,"catalog_metrics","A","/data/catalogMetrics",[(21,"catalog_id","V","/catalogId"),(22,"catalog_name","V","/catalogName"),(23,"intra_region_read_bytes","B","/intraRegionReadBytes"),(24,"intra_region_write_bytes","B","/intraRegionWriteBytes"),(25,"cross_region_read_bytes","B","/crossRegionReadBytes"),(26,"cross_region_write_bytes","B","/crossRegionWriteBytes"),(27,"private_link_read_bytes","B","/privateLinkReadBytes"),(28,"private_link_write_bytes","B","/privateLinkWriteBytes")])]
```
"""
# Step 4: Invoke agent
asyncio.run(agent.invoke(input_text=input_text))
