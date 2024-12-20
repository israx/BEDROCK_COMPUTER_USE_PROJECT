import boto3
import json

def read_image(file_path):
    with open(file_path, 'rb') as f:
        return f.read()

def main():
    # Initialize the Bedrock client
    bedrock = boto3.client('bedrock-runtime')

    # Read the image file
    image_data = read_image('test_images/console.png')

    # Prepare the request
    request = {
        'modelId': 'anthropic.claude-3-5-sonnet-20241022-v2:0',
        'messages': [
            {
                'role': 'user',
                'content': [
                    {
                        'text': 'Go to the bedrock console'
                    },
                    {
                        'image': {
                            'format': 'png',
                            'source': {
                                'bytes': image_data
                            }
                        }
                    }
                ]
            }
        ],
        'additionalModelRequestFields': {
            "tools": [
                {
                    "type": "computer_20241022",
                    "name": "computer",
                    "display_height_px": 768,
                    "display_width_px": 1024,
                    "display_number": 0
                },
                {
                    "type": "bash_20241022",
                    "name": "bash",
                },
                {
                    "type": "text_editor_20241022",
                    "name": "str_replace_editor",
                }
            ],
            "anthropic_beta": ["computer-use-2024-10-22"]
        },
        'toolConfig': {
            'tools': [
                {
                    'toolSpec': {
                        'name': 'get_weather',
                        'inputSchema': {
                            'json': {
                                'type': 'object'
                            }
                        }
                    }
                }
            ]
        }
    }

    # Call the Bedrock Converse API
    response = bedrock.converse(**request)

    # Print the response
    print(json.dumps(response, indent=4))

if __name__ == "__main__":
    main()
