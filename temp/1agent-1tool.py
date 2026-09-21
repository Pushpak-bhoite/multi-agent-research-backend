
stp - 1 ==========search agent working======= 
query:-------------> Impact of AI agents on software engineering jobs 2023

search results:=====>

{
    'messages': [
        HumanMessage(
            content='Find recent, reliable and detailed information about: Impact of AI agents on software engineering jobs',
            additional_kwargs={},
            response_metadata={},
            id='20cd89d9-515a-4659-bd66-e148104418e5'
        ),
        AIMessage(
            content='',
            additional_kwargs={'refusal': None},
            response_metadata={
                'token_usage': {
                    'completion_tokens': 24,
                    'prompt_tokens': 73,
                    'total_tokens': 97,
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
                'system_fingerprint': 'fp_2e30314e0f',
                'id': 'chatcmpl-EQ74fCQQLvHAohM2vH49WnCtCJJPl',
                'service_tier': 'default',
                'finish_reason': 'tool_calls',
                'logprobs': None
            },
            id='lc_run--01a0bde7-0268-7560-a423-86886da944c5-0',
            tool_calls=[
                {
                    'name': 'web_search',
                    'args': {'query': 'Impact of AI agents on software engineering jobs 2023'},
                    'id': 'call_poQBLaBrHZfeygXId4xsGa6W',
                    'type': 'tool_call'
                }
            ],
            invalid_tool_calls=[],
            usage_metadata={
                'input_tokens': 73,
                'output_tokens': 24,
                'total_tokens': 97,
                'input_token_details': {'audio': 0, 'cache_read': 0},
                'output_token_details': {'audio': 0, 'reasoning': 0}
            }
        ),
        ToolMessage(
            content='Title: Impact of AI on the 2025 Software Engineering Job Market\nURL: 
https://www.sundeepteki.org/advice/impact-of-ai-on-the-2025-software-engineering-job-market\nSnippet: that is down 25% from 2023 levels. The data collectively 
points to a clear and concerning trend: the primary entry points into the software engineering profession are narrowing.  1.2 Codified vs. Tacit Programming 
Knowledge\u200b    The quantitative data from the Stanford study begs a crucial question: w\n-----\nTitle: How AI Agents Are Transforming Software Engineering 
...\nURL: https://www.computer.org/csdl/magazine/co/2025/05/10970187/260SnIeoUUM\nSnippet: []( Stokel-Walker. “_Why it sucks to be a junior developer right 
now._” LeadDev. Accessed: Oct.15, 2024. [Online]. Available: \n   []( Technologies. “_AI: Transforming the future of manual software testing._” Medium. 
Sep.2023. Accessed: Oct.15, 2024. [Online]. Available: \n   []( Wright, “_GitHub Copi\n-----\nTitle: As AI agents accelerate coding, what is the future of 
...\nURL: https://x.com/AndrewYNg/status/2043742105852621052?lang=en\nSnippet: lead to massive unemployment, perhaps even rioting in the streets — won’t be 
nearly as bad as dire forecasts by pundits, especially pundits who are trying to paint a picture of how powerful their AI technology is. Among professions, AI 
is accelerating software engineering most, given the rise of cod\n-----\nTitle: The Impact of AI on Engineering Jobs\nURL: 
https://www.intuit.com/blog/innovative-thinking/ai-impact-engineering-jobs\nSnippet: AI’s ongoing evolution could put certain engineering roles at risk. That 
includes entry-level positions centered on straightforward or routine tasks. Think roles like CAD technicians, QA/test engineers focused on manual testing, or 
junior software developers handling routine coding tasks.\n\nAt the sa\n-----\nTitle: What is the future of software engineering with AI?\nURL: 
https://www.linkedin.com/posts/christopherwalton_ai-agents-engineering-activity-7372323946601517056-w7DS\nSnippet: code, provisioning and deploying systems, 
and monitoring and root-causing issues.The role of the software engineer will then shift to identifying requirements, prompting agents to perform tasks, and 
auditing outputs from the agents.In essence, a software engineer will manage a team of AI agents to p',
            name='web_search',
            id='a05141ee-805b-4615-86cf-4a1aeff44dbf',
            tool_call_id='call_poQBLaBrHZfeygXId4xsGa6W'
        ),
        AIMessage(
            content="Here are some recent and reliable sources discussing the impact of AI agents on software engineering jobs:\n\n1. **Impact of AI on the 
2025 Software Engineering Job Market**\n   - **URL**: 
[sundeepteki.org](https://www.sundeepteki.org/advice/impact-of-ai-on-the-2025-software-engineering-job-market)\n   - **Snippet**: This article discusses a 
concerning trend where the primary entry points into the software engineering profession are narrowing, with a projected 25% decrease in job availability by 
2025 compared to 2023 levels.\n\n2. **How AI Agents Are Transforming Software Engineering**\n   - **URL**: 
[computer.org](https://www.computer.org/csdl/magazine/co/2025/05/10970187/260SnIeoUUM)\n   - **Snippet**: This piece explores the transformation of software 
engineering roles due to AI, emphasizing the shift in responsibilities and the evolving nature of coding tasks.\n\n3. **As AI Agents Accelerate Coding, What is
the Future of Software Engineering?**\n   - **URL**: [x.com](https://x.com/AndrewYNg/status/2043742105852621052?lang=en)\n   - **Snippet**: This discussion 
highlights the acceleration of software engineering by AI, suggesting that while there are fears of massive unemployment, the actual impact may be less severe 
than predicted.\n\n4. **The Impact of AI on Engineering Jobs**\n   - **URL**: 
[intuit.com](https://www.intuit.com/blog/innovative-thinking/ai-impact-engineering-jobs)\n   - **Snippet**: The article outlines how AI's evolution could 
threaten certain engineering roles, particularly entry-level positions that involve routine tasks, such as junior software developers and QA/test 
engineers.\n\n5. **What is the Future of Software Engineering with AI?**\n   - **URL**: 
[linkedin.com](https://www.linkedin.com/posts/christopherwalton_ai-agents-engineering-activity-7372323946601517056-w7DS)\n   - **Snippet**: This post discusses
the future role of software engineers as they transition to managing AI agents, focusing on identifying requirements and auditing outputs rather than 
traditional coding tasks.\n\nThese sources provide a comprehensive overview of the current landscape and future implications of AI in software engineering.",
            additional_kwargs={'refusal': None},
            response_metadata={
                'token_usage': {
                    'completion_tokens': 479,
                    'prompt_tokens': 640,
                    'total_tokens': 1119,
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
                'system_fingerprint': 'fp_2e30314e0f',
                'id': 'chatcmpl-EQ74jAVFWXvRCrGh8F96djKPX7Itm',
                'service_tier': 'default',
                'finish_reason': 'stop',
                'logprobs': None
            },
            id='lc_run--01a0bde7-15a6-7da0-9821-d03784977adb-0',
            tool_calls=[],
            invalid_tool_calls=[],
            usage_metadata={
                'input_tokens': 640,
                'output_tokens': 479,
                'total_tokens': 1119,
                'input_token_details': {'audio': 0, 'cache_read': 0},
                'output_token_details': {'audio': 0, 'reasoning': 0}
            }
        )
    ]
}

state['search_result']:====>
 Here are some recent and reliable sources discussing the impact of AI agents on software engineering jobs:

1. **Impact of AI on the 2025 Software Engineering Job Market**
   - **URL**: (https://www.sundeepteki.org/advice/impact-of-ai-on-the-2025-software-engineering-job-market)
   - **Snippet**: This article discusses a concerning trend where the primary entry points into the software engineering profession are narrowing, with a 
projected 25% decrease in job availability by 2025 compared to 2023 levels.

2. **How AI Agents Are Transforming Software Engineering**
   - **URL**: (https://www.computer.org/csdl/magazine/co/2025/05/10970187/260SnIeoUUM)
   - **Snippet**: This piece explores the transformation of software engineering roles due to AI, emphasizing the shift in responsibilities and the evolving 
nature of coding tasks.

3. **As AI Agents Accelerate Coding, What is the Future of Software Engineering?**
   - **URL**: (https://x.com/AndrewYNg/status/2043742105852621052?lang=en)
   - **Snippet**: This discussion highlights the acceleration of software engineering by AI, suggesting that while there are fears of massive unemployment, the
actual impact may be less severe than predicted.

4. **The Impact of AI on Engineering Jobs**
   - **URL**: (https://www.intuit.com/blog/innovative-thinking/ai-impact-engineering-jobs)
   - **Snippet**: The article outlines how AI's evolution could threaten certain engineering roles, particularly entry-level positions that involve routine 
tasks, such as junior software developers and QA/test engineers.

5. **What is the Future of Software Engineering with AI?**
   - **URL**: (https://www.linkedin.com/posts/christopherwalton_ai-agents-engineering-activity-7372323946601517056-w7DS)
   - **Snippet**: This post discusses the future role of software engineers as they transition to managing AI agents, focusing on identifying requirements and 
auditing outputs rather than traditional coding tasks.

These sources provide a comprehensive overview of the current landscape and future implications of AI in software engineering.
INFO:     127.0.0.1:58164 - "POST /api/research HTTP/1.1" 200 OK
