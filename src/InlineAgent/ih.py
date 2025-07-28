from InlineAgent.agent import InlineAgent
from flask import Flask, request, jsonify
import asyncio

instruction = """
You are a friendly assistant that is responsible manipulating a JSON data structure.
An example data structure is:
```
[
            {
                "trinoColumnName": "specversion",
                "parseProperties": {
                    "@type": "json",
                    "relativeJsonPointer": "/specversion",
                    "parseParameters": {
                        "varchar.type": "scalar"
                    }
                },
                "trinoType": {
                    "typeId": "VARCHAR",
                    "typeParameters": {}
                },
                "required": false,
                "nestedColumns": []
            },
            {
                "trinoColumnName": "id",
                "parseProperties": {
                    "@type": "json",
                    "relativeJsonPointer": "/id",
                    "parseParameters": {
                        "varchar.type": "scalar"
                    }
                },
                "trinoType": {
                    "typeId": "VARCHAR",
                    "typeParameters": {}
                },
                "required": false,
                "nestedColumns": []
            },
            {
                "trinoColumnName": "source",
                "parseProperties": {
                    "@type": "json",
                    "relativeJsonPointer": "/source",
                    "parseParameters": {
                        "varchar.type": "scalar"
                    }
                },
                "trinoType": {
                    "typeId": "VARCHAR",
                    "typeParameters": {}
                },
                "required": false,
                "nestedColumns": []
            },
            {
                "trinoColumnName": "type",
                "parseProperties": {
                    "@type": "json",
                    "relativeJsonPointer": "/type",
                    "parseParameters": {
                        "varchar.type": "scalar"
                    }
                },
                "trinoType": {
                    "typeId": "VARCHAR",
                    "typeParameters": {}
                },
                "required": false,
                "nestedColumns": []
            },
            {
                "trinoColumnName": "time",
                "parseProperties": {
                    "@type": "json",
                    "relativeJsonPointer": "/time",
                    "parseParameters": {
                        "varchar.type": "scalar"
                    }
                },
                "trinoType": {
                    "typeId": "VARCHAR",
                    "typeParameters": {}
                },
                "required": false,
                "nestedColumns": []
            },
            {
                "trinoColumnName": "cloud_region_id",
                "parseProperties": {
                    "@type": "json",
                    "relativeJsonPointer": "/data/cloudRegionId",
                    "parseParameters": {
                        "varchar.type": "scalar"
                    }
                },
                "trinoType": {
                    "typeId": "VARCHAR",
                    "typeParameters": {}
                },
                "required": false,
                "nestedColumns": []
            },
            {
                "trinoColumnName": "account_id",
                "parseProperties": {
                    "@type": "json",
                    "relativeJsonPointer": "/data/accountId",
                    "parseParameters": {
                        "varchar.type": "scalar"
                    }
                },
                "trinoType": {
                    "typeId": "VARCHAR",
                    "typeParameters": {}
                },
                "required": false,
                "nestedColumns": []
            },
            {
                "trinoColumnName": "payment_tier",
                "parseProperties": {
                    "@type": "json",
                    "relativeJsonPointer": "/data/paymentTier",
                    "parseParameters": {
                        "varchar.type": "scalar"
                    }
                },
                "trinoType": {
                    "typeId": "VARCHAR",
                    "typeParameters": {}
                },
                "required": false,
                "nestedColumns": []
            },
            {
                "trinoColumnName": "service_name",
                "parseProperties": {
                    "@type": "json",
                    "relativeJsonPointer": "/data/serviceName",
                    "parseParameters": {
                        "varchar.type": "scalar"
                    }
                },
                "trinoType": {
                    "typeId": "VARCHAR",
                    "typeParameters": {}
                },
                "required": false,
                "nestedColumns": []
            },
            {
                "trinoColumnName": "task_source_type",
                "parseProperties": {
                    "@type": "json",
                    "relativeJsonPointer": "/data/taskSourceType",
                    "parseParameters": {
                        "varchar.type": "scalar"
                    }
                },
                "trinoType": {
                    "typeId": "VARCHAR",
                    "typeParameters": {}
                },
                "required": false,
                "nestedColumns": []
            },
            {
                "trinoColumnName": "live_table_id",
                "parseProperties": {
                    "@type": "json",
                    "relativeJsonPointer": "/data/liveTableId",
                    "parseParameters": {
                        "varchar.type": "scalar"
                    }
                },
                "trinoType": {
                    "typeId": "VARCHAR",
                    "typeParameters": {}
                },
                "required": false,
                "nestedColumns": []
            },
            {
                "trinoColumnName": "live_table_instance_id",
                "parseProperties": {
                    "@type": "json",
                    "relativeJsonPointer": "/data/liveTableInstanceId",
                    "parseParameters": {
                        "varchar.type": "scalar"
                    }
                },
                "trinoType": {
                    "typeId": "VARCHAR",
                    "typeParameters": {}
                },
                "required": false,
                "nestedColumns": []
            },
            {
                "trinoColumnName": "reserved_compute_unit_millis",
                "parseProperties": {
                    "@type": "json",
                    "relativeJsonPointer": "/data/reservedComputeUnitMillis",
                    "parseParameters": {}
                },
                "trinoType": {
                    "typeId": "BIGINT",
                    "typeParameters": {}
                },
                "required": false,
                "nestedColumns": []
            },
            {
                "trinoColumnName": "reserved_cpu_millis",
                "parseProperties": {
                    "@type": "json",
                    "relativeJsonPointer": "/data/reservedCpuMillis",
                    "parseParameters": {}
                },
                "trinoType": {
                    "typeId": "BIGINT",
                    "typeParameters": {}
                },
                "required": false,
                "nestedColumns": []
            },
            {
                "trinoColumnName": "reserved_memory_millis",
                "parseProperties": {
                    "@type": "json",
                    "relativeJsonPointer": "/data/reservedMemoryMillis",
                    "parseParameters": {}
                },
                "trinoType": {
                    "typeId": "BIGINT",
                    "typeParameters": {}
                },
                "required": false,
                "nestedColumns": []
            },
            {
                "trinoColumnName": "actual_compute_unit_millis",
                "parseProperties": {
                    "@type": "json",
                    "relativeJsonPointer": "/data/actualComputeUnitMillis",
                    "parseParameters": {}
                },
                "trinoType": {
                    "typeId": "BIGINT",
                    "typeParameters": {}
                },
                "required": false,
                "nestedColumns": []
            },
            {
                "trinoColumnName": "actual_cpu_millis",
                "parseProperties": {
                    "@type": "json",
                    "relativeJsonPointer": "/data/actualCpuMillis",
                    "parseParameters": {}
                },
                "trinoType": {
                    "typeId": "BIGINT",
                    "typeParameters": {}
                },
                "required": false,
                "nestedColumns": []
            },
            {
                "trinoColumnName": "actual_memory_millis",
                "parseProperties": {
                    "@type": "json",
                    "relativeJsonPointer": "/data/actualMemoryMillis",
                    "parseParameters": {}
                },
                "trinoType": {
                    "typeId": "BIGINT",
                    "typeParameters": {}
                },
                "required": false,
                "nestedColumns": []
            },
            {
                "trinoColumnName": "duration_millis",
                "parseProperties": {
                    "@type": "json",
                    "relativeJsonPointer": "/data/durationMillis",
                    "parseParameters": {}
                },
                "trinoType": {
                    "typeId": "BIGINT",
                    "typeParameters": {}
                },
                "required": false,
                "nestedColumns": []
            }
        ]
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
be used by a downstream system, so it is important to maintain the format and structure. Respond with the 
updated data structure only, without any additional text or explanation.
"""

# Step 3: Define agent
agent = InlineAgent(
    foundation_model="arn:aws:bedrock:us-west-2:310018062324:inference-profile/us.anthropic.claude-sonnet-4-20250514-v1:0",
    instruction=instruction,
    agent_name="Icehouse",
    profile="hackathon",
)

# Initialize Flask app
app = Flask(__name__)

@app.route('/invoke', methods=['POST'])
def invoke_agent():
    """
    Invoke the Icehouse agent with user input text and return the result.
    Expects raw text in the request body.
    """
    try:
        # Get input text from request body as raw string
        input_text = request.get_data(as_text=True)
        if not input_text or input_text.strip() == '':
            return jsonify({'error': 'Missing input text in request body'}), 400
        
        # Invoke the agent with the provided input text
        result = asyncio.run(agent.invoke(input_text=input_text))

        return result
    except Exception as e:
        return jsonify({
            'error': f'Agent invocation failed: {str(e)}',
            'status': 'error'
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint.
    """
    return jsonify({
        'status': 'healthy',
        'agent': 'Icehouse Data Structure Agent'
    })

@app.route('/', methods=['GET'])
def root():
    """
    Root endpoint with API information.
    """
    return jsonify({
        'message': 'Icehouse Data Structure Agent API',
        'endpoints': {
            'POST /invoke': 'Invoke the agent with input text (raw text in request body)',
            'GET /health': 'Health check',
            'GET /': 'API information'
        }
    })

if __name__ == '__main__':
    # Run the Flask development server
    app.run(host='0.0.0.0', port=8000, debug=True)
