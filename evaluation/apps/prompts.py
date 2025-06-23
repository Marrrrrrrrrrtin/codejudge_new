single_step_prompt = []


dual_step_prompt = {
    "compare_prompt": [
        [#0
            {
                "role": "system",
                "content": """\
You will be provided with an algorithm contest problem. This problem will contain four parts: the problem statement, input description, output description, and several input-output pair examples.
Then, you will be provided with a code snippet that supposedly addresses the problem in Python.
Your task is to check if the code snippet covers the required functionalities. Only output the evaluation, do not provide a corrected version.
""",
            },
            {
                "role": "user",
                "content": """\
Problem Statement: \"\"\"
{{PROBLEM}}
\"\"\"
Code Snippet: \"\"\"python
{{CODE1}}
\"\"\"

There are also constraints on the input range  (e.g. 1 <= n <= 10^6), and programs running longer than 10 seconds will be treated as having timeout errors. Therefore, the correct code snippet needs to have both the correct logic and time complexity.
Read the code snippet carefully and analyze it. Check if the code snippet covers all the required functionalities of the problem.
"""
            },
            {
                "role": "assistant",
                "content": """\
Evaluation:
"""
            }
        ],
        [#1
            {
                "role": "system",
                "content": """\
You will be provided with an algorithm contest problem. This problem will contain four parts: the problem statement, input description, output description, and several input-output pair examples.
Then, you will be provided with a code snippet that supposedly addresses the problem in Python, and a reference answer.
Your task is to check if the code snippet covers the required functionalities. Only output the evaluation, do not provide a corrected version.
""",
            },
            {
                "role": "user",
                "content": """\
Problem Statement: \"\"\"
{{PROBLEM}}
\"\"\"
Reference Solution: \"\"\"{{LANGUAGE}}
{{CODE2}}
\"\"\"
Code Snippet: \"\"\"{{LANGUAGE}}
{{CODE1}}
\"\"\"

There are also constraints on the input range  (e.g. 1 <= n <= 10^6), and programs running longer than 10 seconds will be treated as having timeout errors. Therefore, the correct code snippet needs to have both the correct logic and appropriate time complexity. However, it's not necessary to compare the efficiency of the code snippet to the reference code.
Read the code snippet carefully and analyze it. Check if the code snippet covers all the required functionalities of the problem.
"""
            },
            {
                "role": "assistant",
                "content": """\
Evaluation:
"""
            }
        ],
        [#2
            {
                "role": "system",
                "content": """\
You will be provided with a problem statement and a code snippet that supposedly addresses the problem.
Your task is to check if the code snippet covers the required functionalities.
If the code snippet is correct, output your reason.
If the code snippet is incorrect, list the mistakes and explain the reasons.
""",
            },
            {
                "role": "user",
                "content": """\
Problem Statement: \"\"\"
{{PROBLEM}}
\"\"\"
Code Snippet: \"\"\"Python
{{CODE1}}
\"\"\"
"""
            },
            {
                "role": "assistant",
                "content": """\
Evaluation:
"""
            }
        ],
        [
            {
                "role": "system",
                "content": """\
You will be provided with a problem statement, a code snippet that supposedly addresses the problem, and a reference solution.
The reference solution is used to help you understand the problem, do not directly compare the code snippet to the reference code.
Your task is to check if the code snippet covers the required functionalities.
If the code snippet is correct, output your reason.
If the code snippet is incorrect, list the mistakes and explain the reasons.
""",
            },
            {
                "role": "user",
                "content": """\
Problem Statement: \"\"\"
{{PROBLEM}}
\"\"\"
Reference Solution: \"\"\"Python
{{CODE2}}
\"\"\"
Code Snippet: \"\"\"Python
{{CODE1}}
\"\"\"
"""
            },
            {
                "role": "assistant",
                "content": """\
Evaluation:
"""
            }
        ],
    ],
    "analyze_prompt": [
        [
            {
                "role": "system",
                "content": """\
You will be provided with an analysis result of a code snippet.
If the analysis believes that the code snippet is correct, output: "Yes". Otherwise, output: "No".
""",
            },
            {
                "role": "user",
                "content": """\
Analysis Result:\"\"\"
{{MISTAKES}}
\"\"\"
"""
            },
            {
                "role": "assistant",
                "content": """\
Final Answer (Yes or No):
"""
            }
        ],
    ],
}
