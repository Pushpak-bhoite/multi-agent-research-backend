
INFO:     Application startup complete.
stp - 1 ==========search agent working======= 
query:-------------> Impact of AI agents on software engineering jobs 2023

search results:=====>

{
    'messages': [
        HumanMessage(
            content='Find recent, reliable and detailed information about: Impact of AI agents on software engineering jobs',
            additional_kwargs={},
            response_metadata={},
            id='c5369034-ba11-48cf-a18b-736a5afc4302'
        ),
        AIMessage(
            content='',
            additional_kwargs={'refusal': None},
            response_metadata={
                'token_usage': {
                    'completion_tokens': 24,
                    'prompt_tokens': 110,
                    'total_tokens': 134,
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
                'system_fingerprint': 'fp_28f3a9c586',
                'id': 'chatcmpl-EQ6uvbG6XPibiaaAApkzFGYbjCcnH',
                'service_tier': 'default',
                'finish_reason': 'tool_calls',
                'logprobs': None
            },
            id='lc_run--01a0bddd-c7a9-7191-bedb-81a9421aeb00-0',
            tool_calls=[
                {
                    'name': 'web_search',
                    'args': {'query': 'Impact of AI agents on software engineering jobs 2023'},
                    'id': 'call_dKZG9G1Htushm1K1s92qGRAq',
                    'type': 'tool_call'
                }
            ],
            invalid_tool_calls=[],
            usage_metadata={
                'input_tokens': 110,
                'output_tokens': 24,
                'total_tokens': 134,
                'input_token_details': {'audio': 0, 'cache_read': 0},
                'output_token_details': {'audio': 0, 'reasoning': 0}
            }
        ),
        ToolMessage(
            content='Title: The impact of AI on the job market for software engineers is starting to show and it’s only going to accelerate. While at first AI
appeared to be an excuse for layoffs to disguise bad management and… | Fabian Jakobs | 22 comments\nURL: 
https://www.linkedin.com/posts/fabianjakobs_the-impact-of-ai-on-the-job-market-for-software-activity-7441083058608525312-PsLt\nSnippet: most quarters from 
2023. The scoreboard for 2026 so far: 45,000+ tech layoffs globally. Over 9,200 explicitly attributed to AI, by the companies themselves. This isn\'t a 
correction. It\'s a restructuring. Now: take a deeep breathe. Here\'s what the same data also shows: ✅ AI-related job openings are u\n-----\nTitle: Impact of
AI on the Software Engineering Job Market (2025 Data) - Sundeep Teki\nURL: 
https://www.sundeepteki.org/advice/impact-of-ai-on-the-2025-software-engineering-job-market\nSnippet: that is down 25% from 2023 levels. The data collectively
points to a clear and concerning trend: the primary entry points into the software engineering profession are narrowing.  1.2 Codified vs. Tacit Programming 
Knowledge\u200b    The quantitative data from the Stanford study begs a crucial question: w\n-----\nTitle: How AI Agents Are Transforming Software Engineering
and the Future of Product Development\nURL: https://www.computer.org/csdl/magazine/co/2025/05/10970187/260SnIeoUUM\nSnippet: []( Stokel-Walker. “_Why it sucks
to be a junior developer right now._” LeadDev. Accessed: Oct.15, 2024. [Online]. Available: \n   []( Technologies. “_AI: Transforming the future of manual 
software testing._” Medium. Sep.2023. Accessed: Oct.15, 2024. [Online]. Available: \n   []( Wright, “_GitHub Copi\n-----\nTitle: Andrew Ng on X: "As AI agents
accelerate coding, what is the future of software engineering? Some trends are clear, such as the Product Management Bottleneck, referring to the idea that we
are more constrained by deciding what to build rather than the actual building. But many implications, like AI… / X\nURL: 
https://x.com/AndrewYNg/status/2043742105852621052?lang=en\nSnippet: notion that AI will lead to massive unemployment, perhaps even rioting in the streets — 
won’t be nearly as bad as dire forecasts by pundits, especially pundits who are trying to paint a picture of how powerful their AI technology is. Among 
professions, AI is accelerating software engineering most, g\n-----\nTitle: The Impact of AI on Engineering Jobs\nURL: 
https://www.intuit.com/blog/innovative-thinking/ai-impact-engineering-jobs\nSnippet: AI’s ongoing evolution could put certain engineering roles at risk. That 
includes entry-level positions centered on straightforward or routine tasks. Think roles like CAD technicians, QA/test engineers focused on manual testing, or
junior software developers handling routine coding tasks.\n\nAt the sa',
            name='web_search',
            id='6c921c0c-137d-4bf5-9612-9bf14b836942',
            tool_call_id='call_dKZG9G1Htushm1K1s92qGRAq'
        ),
        AIMessage(
            content='',
            additional_kwargs={'refusal': None},
            response_metadata={
                'token_usage': {
                    'completion_tokens': 213,
                    'prompt_tokens': 805,
                    'total_tokens': 1018,
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
                'system_fingerprint': 'fp_28f3a9c586',
                'id': 'chatcmpl-EQ6uymbEUxic790qYQhDiTYRRv5tG',
                'service_tier': 'default',
                'finish_reason': 'tool_calls',
                'logprobs': None
            },
            id='lc_run--01a0bddd-dab8-7190-9751-2230ebec999b-0',
            tool_calls=[
                {
                    'name': 'scrape_url',
                    'args': {
                        'url': 'https://www.linkedin.com/posts/fabianjakobs_the-impact-of-ai-on-the-job-market-for-software-activity-7441083058608525312-PsLt'
                    },
                    'id': 'call_uJbKPGK358Q2XGRG40i9ZcfK',
                    'type': 'tool_call'
                },
                {
                    'name': 'scrape_url',
                    'args': {'url': 'https://www.sundeepteki.org/advice/impact-of-ai-on-the-2025-software-engineering-job-market'},
                    'id': 'call_ZxzkWw5gmrPlIgAAg4mfXDcv',
                    'type': 'tool_call'
                },
                {
                    'name': 'scrape_url',
                    'args': {'url': 'https://www.computer.org/csdl/magazine/co/2025/05/10970187/260SnIeoUUM'},
                    'id': 'call_WsBDy8lLH14qXcvbq7yBvnlu',
                    'type': 'tool_call'
                },
                {
                    'name': 'scrape_url',
                    'args': {'url': 'https://x.com/AndrewYNg/status/2043742105852621052?lang=en'},
                    'id': 'call_bPMV4Zs3yktShk82RY68CkAK',
                    'type': 'tool_call'
                },
                {
                    'name': 'scrape_url',
                    'args': {'url': 'https://www.intuit.com/blog/innovative-thinking/ai-impact-engineering-jobs'},
                    'id': 'call_CT6bbvdm4bY2TFmbQchDSw1Z',
                    'type': 'tool_call'
                }
            ],
            invalid_tool_calls=[],
            usage_metadata={
                'input_tokens': 805,
                'output_tokens': 213,
                'total_tokens': 1018,
                'input_token_details': {'audio': 0, 'cache_read': 0},
                'output_token_details': {'audio': 0, 'reasoning': 0}
            }
        ),
        ToolMessage(
            content='Title: The impact of AI on the job market for software engineers is starting to show and it’s only going to accelerate.\n\nWhile at first
AI appeared to be an excuse for layoffs to disguise bad management and… | Fabian Jakobs | 22 comments\nURL: 
https://www.linkedin.com/posts/fabianjakobs_the-impact-of-ai-on-the-job-market-for-software-activity-7441083058608525312-PsLt\n\nThe impact of AI on the job 
market for software engineers is starting to show and it’s only going to accelerate.\nWhile at first AI appeared to be an excuse for layoffs to disguise bad 
management and… | Fabian Jakobs | 22 comments\n      Skip to main content\nFabian Jakobs’ Post\n              Fabian Jakobs\n      6mo\n                      
Report this post\nThe impact of AI on the job market for software engineers is starting to show and it’s only going to accelerate.\nWhile at first AI appeared
to be an excuse for layoffs to disguise bad management and other reasons - now we are starting to see rounds of layoffs where I do believe AI is the driving 
factor. Recent examples are Atlassian firing 10% and Meta announcing to cut 20% of their workforce. \nAnd the pressure is coming from two directions, internal
and external. \nExternally pressure comes from AI threatening the business model of companies. What used to be highly profitable SaaS businesses, are degraded
to headless backend services consumed by agents. We’ve seen stock prices for SaaS companies plummet already. In tech a large portion of compensation is in the
form of stock grants. A drop in a company’s stock price also results in significant salary cuts for employees. Executives are basically facing the choice of 
firing some percentage of their engineers to stabilize the stock price or risking their best employees to leave for places with better compensation. Very few 
choose the second option. This is what I assume happened at Atlassian.\nBut there are also internal forces, which might be even stronger. Companies are at the
point where they are clearly seeing with measurable results that AI is improving productivity in developing software. There is also a strong correlation 
between adoption of AI coding tools and individual productivity for developers. I know measuring developer productivity is difficult but the trend is clear. 
This means that companies will want their developers to use AI for coding as much as possible. However, someone needs to pay for all the tokens consumed and I
expect that this money will come from the payroll budget. So companies which are expanding and want to do more with the same amount of people will hire less. 
Companies that intend to do the same will need less people and will therefore do layoffs. That’s what I think is happening at Meta.\nI strongly believe that 
for us as developers to stay relevant in the industry, we have to learn and embrace AI. I’ve been in the industry for over 20 years and love coding. I’m 
pretty sure I’d be out of my job by the end of the year and unemployable if I refused to use AI coding tools to do my job. \nThe software industry is 
transforming due to AI and it’s doing so quickly and I expect more of this to play out during this year.\n(while this sounds gloomy, I’m personally super 
excited about the new possibilities but that for another post)\n                    98\n                22 Comments\n      Like\n      Comment\n              
Share\nCopy\n\n[...truncated]',
            name='scrape_url',
            id='58958cac-ed30-4f5e-b4fe-49eeacef8a81',
            tool_call_id='call_uJbKPGK358Q2XGRG40i9ZcfK'
        ),
        ToolMessage(
            content='Title: Impact of AI on the Software Engineering Job Market (2025 Data) - Sundeep Teki\nURL: 
https://www.sundeepteki.org/advice/impact-of-ai-on-the-2025-software-engineering-job-market\n\nImpact of AI on the Software Engineering Job Market (2025 Data)
- Sundeep Teki\nSundeep 
Teki\n\t\t\t\tHome\n\t\t\tAbout\n\t\t\t\tAI\n\t\t\tBlog\n\t\t\tTraining\n>\n\t\t\tTestimonials\n\t\t\tConsulting\n\t\t\tPapers\n\t\t\tContent\n\t\t\tHiring\n\
t\t\tSpeaking\n\t\t\tCourse\n\t\t\tNeuroscience\n>\n\t\t\tSpeech\n\t\t\tTime\n\t\t\tMemory\n\t\t\tTestimonials\n\t\t\t\tCoaching\n\t\t\tPhilosophy\n\t\t\tCare
er Guides\n\t\t\tCompany Guides\n\t\t\tAI Leadership Coaching\n\t\t\tResearch Engineer\n\t\t\tResearch Scientist\n\t\t\tForward Deployed Engineer\n\t\t\tAI 
Engineer\n\t\t\tTestimonials\n\t\t\t\tAdvice\n\t\t\t\tContact\n\t\t\tNews\n\t\t\tMedia\nImpact of AI on the 2025 Software Engineering Job 
Market\n\t\t29/8/2025\n\t\t0 Comments\nCheck out my\nMarch 2026 blog\non the recent impact of AI on the SWE job market\n□\nKey Findings\nWhat the 2025-2026 
data actually shows about AI and software engineering jobs\nDevelopers complete tasks 55% faster with AI - but the complexity ceiling is rising.\n GitHub\'s 
2024 research found engineers using AI coding assistants ship 46% more code per week. The productivity gain is real. The implication is structural: teams will
need fewer engineers for routine tasks, but more for system design and AI oversight. \n(GitHub Octoverse, 2024)\nUp to 30% of current software engineering 
tasks are automatable by 2030 - but net employment is projected to grow.\n McKinsey\'s analysis shows automation is concentrated in repetitive implementation 
and boilerplate code, not in architecture, debugging complex systems, or cross-functional technical leadership. \n(McKinsey Global Institute, 2023)\n170 
million new roles will be created by AI through 2030 - technology and AI-adjacent positions lead the growth.\n The WEF\'s 2025 Future of Jobs Report projects 
92 million roles displaced and 170 million created. AI and ML specialists, data engineers, and automation developers are among the fastest-growing occupations
globally. \n(World Economic Forum, Future of Jobs Report 2025)\nAI/ML job postings have grown 21x since 2012 - engineers who add AI fluency now command 
$20K-$50K salary premiums over peers.\n The Stanford AI Index 2025 documents the fastest sustained growth in any technical specialisation on record. The 
salary gap between AI-fluent and non-AI engineers is widening each year. \n(Stanford Human-Centered AI Institute, AI Index Report 2025)\nIf you want a 
personalised read on how these shifts affect\nyour\ncareer,\nbook a free discovery call\nhere\n.\nSource: Canaries in the Coal Mine? Six Facts about the 
Recent Employment Effects of Artificial Intelligence - Stanford Digital Economy Lab\nThe widespread adoption of generative AI since late 2022 has triggered a 
structural, not cyclical, shift in the software engineering labor market. This is not a simple productivity boost; it is a fundamental rebalancing of value, 
skills, and career trajectories. The most significant, data-backed impact is a "hollowing out" of the entry-level pipeline.\xa0\nA recent\n\xa0Stanford study 
reveals a\n13% relative decline in employment for early-career engineers (ages 22-25) in AI-exposed roles, while senior roles remain stable 
or\n\n[...truncated]',
            name='scrape_url',
            id='af3a45ad-b94e-4769-80fe-1a769591750f',
            tool_call_id='call_ZxzkWw5gmrPlIgAAg4mfXDcv'
        ),
        ToolMessage(
            content='Title: CSDL | IEEE Computer Society\nURL: https://www.computer.org/csdl/magazine/co/2025/05/10970187/260SnIeoUUM\n\nCSDL | IEEE Computer 
Society',
            name='scrape_url',
            id='3fad1c05-cdaf-417b-b677-ec18a691ed63',
            tool_call_id='call_WsBDy8lLH14qXcvbq7yBvnlu'
        ),
        ToolMessage(
            content='Title: Andrew Ng on X: "As AI agents accelerate coding, what is the future of software engineering? Some trends are clear, such as the 
Product Management Bottleneck, referring to the idea that we are more constrained by deciding what to build rather than the actual building. But many 
implications, like AI… / X\nURL: https://x.com/AndrewYNg/status/2043742105852621052?lang=en\n\nAndrew Ng on X: "As AI agents accelerate coding, what is the 
future of software engineering? Some trends are clear, such as the Product Management Bottleneck, referring to the idea that we are more constrained by 
deciding what to build rather than the actual building. But many implications, like AI… / X\nPost\nLog in\nSign up\nPost\nLog in\nSign up',
            name='scrape_url',
            id='dff60d3e-452f-4c13-a26c-ff618f831af8',
            tool_call_id='call_bPMV4Zs3yktShk82RY68CkAK'
        ),
        ToolMessage(
            content='Title: The Impact of AI on Engineering Jobs - Intuit Blog\nURL: 
https://www.intuit.com/blog/innovative-thinking/ai-impact-engineering-jobs\n\nThe Impact of AI on Engineering Jobs - Intuit Blog\n\t\t\tSkip to main 
content\t\t\nIntuit Blog\nAll Posts\nInnovative Thinking\nThe Impact of AI on Engineering Jobs\nArtificial intelligence has moved well beyond the pilot stage.
One \nsurvey\n found that 88% of organizations have implemented AI in at least 1 business function. And engineering is no exception.\xa0\nAlready, AI has 
reshaped how engineers work. Its applications range from design optimization to automation and beyond. It’s expanding the scope of existing jobs and raising 
the bar on the skills engineers need to stay competitive.\xa0\nLearn more about the impact of AI on engineering jobs, emerging career opportunities, and ways 
to thrive in a changing field.\xa0\nKey Points\xa0\nArtificial intelligence has become fundamental enough to shift traditional engineering roles, changing how
engineers work and the work itself. 88% of organizations now use AI in at least one business function.\xa0\nEngineers are using AI to tackle complex 
real-world problems, with applications spanning predictive maintenance, design optimization, and automation.\xa0\nAI’s impact on engineering is just 
beginning. But it’s already creating new job opportunities and demanding new skills to stay relevant.\xa0\nAI likely won’t replace engineers, but it will 
affect some roles more than others. That makes adaptability 1 of the most valuable traits in the field right now.\xa0\nWhat Is Artificial Intelligence in 
Engineering?\xa0\nAI enables machines to learn, adapt, and perform tasks that typically require reasoning. In engineering, that capability translates into 
more powerful tools for analyzing systems and solving complex problems.\xa0\xa0\nCommon artificial intelligence methods and capabilities used in engineering 
include:\xa0\nMachine learning (ML): \nThese systems train on data to perform specific tasks with minimal human oversight, learning and adapting from that 
data along the way. In engineering, ML is also used in automation, predictive maintenance, and systems optimization.\xa0\nComputer vision: \nThis AI 
capability interprets and extracts meaning from visual data such as images and video. In engineering, it can support real-time inspection, quality control, 
monitoring, navigation, and decision-making.\xa0\nNeural networks:\n A type of machine learning model, neural networks are designed to recognize complex 
patterns in large datasets. In engineering, they’re commonly used where traditional models struggle with complexity, like fault detection or image 
recognition.\xa0\nAI-enabled automation:\n AI enhances automation by helping systems respond to changing conditions rather than simply follow fixed rules. In 
engineering, this supports tasks like repetitive workflows and process control.\xa0\nAI-powered data analytics: \nAI-powered tools analyze large volumes of 
data to uncover trends and generate insights. This helps with tasks like predictive modeling and risk assessment.\xa0\nTogether, these capabilities are 
deepening the relationship between AI and engineering. And they’re raising the bar \n\n[...truncated]',
            name='scrape_url',
            id='dc09417d-1eae-468a-b535-47ecf76d6fb1',
            tool_call_id='call_CT6bbvdm4bY2TFmbQchDSw1Z'
        ),
        AIMessage(
            content='Here is a summary of recent and reliable information regarding the impact of AI agents on software engineering jobs:\n\n1. **AI\'s 
Influence on Job Market Dynamics**:\n   - **Source**: [Fabian Jakobs on 
LinkedIn](https://www.linkedin.com/posts/fabianjakobs_the-impact-of-ai-on-the-job-market-for-software-activity-7441083058608525312-PsLt)\n   - AI is 
increasingly affecting the job market for software engineers, leading to layoffs in companies like Atlassian and Meta. The pressure comes from both external 
factors (AI threatening business models) and internal factors (companies seeing productivity improvements with AI tools). As AI tools enhance developer 
productivity, companies may hire fewer engineers or reduce their workforce, leading to a transformation in the industry. Developers are encouraged to embrace 
AI to remain relevant.\n\n2. **Structural Changes in Employment**:\n   - **Source**: [Sundeep Teki\'s 
Blog](https://www.sundeepteki.org/advice/impact-of-ai-on-the-2025-software-engineering-job-market)\n   - A significant shift is occurring in the software 
engineering labor market due to AI. Developers using AI tools can complete tasks 55% faster, and up to 30% of current tasks may be automatable by 2030. 
However, net employment is projected to grow, with 170 million new roles expected to be created by AI by 2030. The entry-level job market is experiencing a 
"hollowing out," with a decline in early-career positions.\n\n3. **AI\'s Role in Engineering Jobs**:\n   - **Source**: [Intuit 
Blog](https://www.intuit.com/blog/innovative-thinking/ai-impact-engineering-jobs)\n   - AI is reshaping engineering roles, with 88% of organizations 
implementing AI in some capacity. This technology is expanding job scopes and raising the skill requirements for engineers. While AI may not replace 
engineers, it will significantly affect certain roles, emphasizing the need for adaptability.\n\n4. **Future Trends and Challenges**:\n   - **Source**: 
[Andrew Ng on X](https://x.com/AndrewYNg/status/2043742105852621052?lang=en)\n   - As AI accelerates coding, the focus may shift from building to 
decision-making in product management. This trend highlights the need for engineers to adapt to new roles that involve oversight and strategic planning rather
than just coding.\n\n5. **Automation and Job Creation**:\n   - **Source**: [IEEE Computer 
Society](https://www.computer.org/csdl/magazine/co/2025/05/10970187/260SnIeoUUM)\n   - The widespread adoption of generative AI is leading to a structural 
shift in the software engineering labor market. While some roles may be automated, new opportunities are emerging, particularly in AI and machine learning 
specialties.\n\n### Conclusion\nThe impact of AI on software engineering jobs is profound and multifaceted. While it poses challenges such as job 
displacement, it also creates new opportunities and demands for skills in AI and machine learning. Engineers are encouraged to adapt and embrace these changes
to remain competitive in the evolving job market.',
            additional_kwargs={'refusal': None},
            response_metadata={
                'token_usage': {
                    'completion_tokens': 648,
                    'prompt_tokens': 3416,
                    'total_tokens': 4064,
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
                'system_fingerprint': 'fp_28f3a9c586',
                'id': 'chatcmpl-EQ6v39pHYkn65x23AsHc8nr0hX2Ph',
                'service_tier': 'default',
                'finish_reason': 'stop',
                'logprobs': None
            },
            id='lc_run--01a0bddd-ec2e-7b81-b913-515a99c8547b-0',
            tool_calls=[],
            invalid_tool_calls=[],
            usage_metadata={
                'input_tokens': 3416,
                'output_tokens': 648,
                'total_tokens': 4064,
                'input_token_details': {'audio': 0, 'cache_read': 0},
                'output_token_details': {'audio': 0, 'reasoning': 0}
            }
        )
    ]
}

state['search_result']:====>
 Here is a summary of recent and reliable information regarding the impact of AI agents on software engineering jobs:

1. **AI's Influence on Job Market Dynamics**:
   - **Source**: [Fabian Jakobs on 
LinkedIn](https://www.linkedin.com/posts/fabianjakobs_the-impact-of-ai-on-the-job-market-for-software-activity-7441083058608525312-PsLt)
   - AI is increasingly affecting the job market for software engineers, leading to layoffs in companies like Atlassian and Meta. The pressure comes from both
external factors (AI threatening business models) and internal factors (companies seeing productivity improvements with AI tools). As AI tools enhance 
developer productivity, companies may hire fewer engineers or reduce their workforce, leading to a transformation in the industry. Developers are encouraged 
to embrace AI to remain relevant.

2. **Structural Changes in Employment**:
   - **Source**: [Sundeep Teki's Blog](https://www.sundeepteki.org/advice/impact-of-ai-on-the-2025-software-engineering-job-market)
   - A significant shift is occurring in the software engineering labor market due to AI. Developers using AI tools can complete tasks 55% faster, and up to 
30% of current tasks may be automatable by 2030. However, net employment is projected to grow, with 170 million new roles expected to be created by AI by 
2030. The entry-level job market is experiencing a "hollowing out," with a decline in early-career positions.

3. **AI's Role in Engineering Jobs**:
   - **Source**: [Intuit Blog](https://www.intuit.com/blog/innovative-thinking/ai-impact-engineering-jobs)
   - AI is reshaping engineering roles, with 88% of organizations implementing AI in some capacity. This technology is expanding job scopes and raising the 
skill requirements for engineers. While AI may not replace engineers, it will significantly affect certain roles, emphasizing the need for adaptability.

4. **Future Trends and Challenges**:
   - **Source**: [Andrew Ng on X](https://x.com/AndrewYNg/status/2043742105852621052?lang=en)
   - As AI accelerates coding, the focus may shift from building to decision-making in product management. This trend highlights the need for engineers to 
adapt to new roles that involve oversight and strategic planning rather than just coding.

5. **Automation and Job Creation**:
   - **Source**: [IEEE Computer Society](https://www.computer.org/csdl/magazine/co/2025/05/10970187/260SnIeoUUM)
   - The widespread adoption of generative AI is leading to a structural shift in the software engineering labor market. While some roles may be automated, 
new opportunities are emerging, particularly in AI and machine learning specialties.

### Conclusion
The impact of AI on software engineering jobs is profound and multifaceted. While it poses challenges such as job displacement, it also creates new 
opportunities and demands for skills in AI and machine learning. Engineers are encouraged to adapt and embrace these changes to remain competitive in the 
evolving job market.
INFO:     127.0.0.1:45836 - "POST /api/research HTTP/1.1" 200 OK
