/python /home/am-lp-53/Desktop/MyFolder/Multi-Agent-AI-Researcher/multi-agent-research-backend/practice/project-1-langgraph/main.py
Enter a message: what is 2+2 
state==========>
[
    HumanMessage(content='what is 2+2 ',
                 additional_kwargs={},
                 response_metadata={}, 
                 id='535da45e-cdd1-40e5-88fb-2ee5516e4a37'),
    AIMessage(
        content='2 + 2 equals 4.',
        additional_kwargs={'refusal': None}, 
        response_metadata={ 
            'token_usage': {
                'completion_tokens': 8,
                'prompt_tokens': 14,
                'total_tokens': 22,
                'completion_tokens_details': { 
                    'accepted_prediction_tokens': 0,
                    'audio_tokens': 0,
                    'reasoning_tokens': 0,
                    'rejected_prediction_tokens': 0,
                    'text_tokens': None
                },
                'prompt_tokens_details': {'audio_tokens': 0, 'cache_write_tokens': None, 'cached_tokens': 0, 'image_tokens': None, 'text_tokens': None}
            },
            'model_provider': 'openai',
            'model_name': 'gpt-4o-mini-2024-07-18',
            'system_fingerprint': 'fp_f51aa69871',
            'id': 'chatcmpl-EQGDzRBP9LTYtGfFJdaX50zhtKgrh',
            'service_tier': 'default',
            'finish_reason': 'stop',
            'logprobs': None
        },
        id='lc_run--01a0bfff-bb95-7222-959c-96a5c3575d37-0',
        tool_calls=[],
        invalid_tool_calls=[],
        usage_metadata={
            'input_tokens': 14,
            'output_tokens': 8,
            'total_tokens': 22,
            'input_token_details': {'audio': 0, 'cache_read': 0},
            'output_token_details': {'audio': 0, 'reasoning': 0}
        }
    )
]
state[-1]==========> 2 + 2 equals 4.
(multi-agent-research-backend) ➜  multi-agent-research-backend git:(main) ✗ /home/am-lp-53/Desk
top/MyFolder/Multi-Agent-AI-Researcher/multi-agent-research-backend/.venv/bin/python /home/am-l
p-53/Desktop/MyFolder/Multi-Agent-AI-Researcher/multi-agent-research-backend/practice/project-1
-langgraph/main.py