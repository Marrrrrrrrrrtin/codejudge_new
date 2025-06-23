single_step_prompt = []


dual_step_prompt = {
    "compare_prompt": [
        [#0
            {
                "role": "system", 
                "content": """
                You are a strict code judger. You will be provided with a problem statement and a code snippet that supposedly addresses the problem in {{LANGUAGE}}.
                Your task is to check if the code snippet covers the required functionalities. 
                Do not provide a corrected version. Please analysis step by step
                Evaluation Steps:
                1. Read the problem statement carefully and identify the required functionalities of the implementation. You can refer to the example and reference answer to understand the problem better.
                2. Carefully check input constraints, such as whether the input must be non-negative, within a certain range, or a non-empty string.
                3. Only use the information from the problem description and program. Be accurate and do not assume extra details. Do not evaluate based on function naming conventions.
                4. Unless explicitly stated in the problem, do NOT evaluate time complexity.
                5. Read the code snippet and analyze its logic. Check if the code snippet covers all the required functionalities of the problem.
                6. Analyze the code step by step and line by line.
                7. Finally, conclude your evaluation.
                """
            }, 
            {
                "role": "user", 
                "content": "Problem Statement: \"\"\"\nImplement a function `summarize_transactions(txns)` that takes in a list of transaction records `txns`. Each record is a dictionary with keys:\n- \"id\": a unique transaction identifier (string).\n- \"amount\": a float, positive for credit, negative for debit.\n- \"tags\": a list of strings (optional).\n\nYour function must:\n1. If `txns` is empty, return `None`.\n2. Validate that every \"amount\" is a float or int; if any record has a non-numeric amount, raise a `TypeError`.\n3. Compute:\n   - `total_change`: the sum of all amounts.\n   - `num_transactions`: the total number of records.\n   - `tag_counts`: a dict mapping each tag to its total occurrences across all transactions (ignore missing or empty tags).\n4. Return a tuple `(total_change, num_transactions, tag_counts)`.\n\nExamples:\n>>> summarize_transactions([\n...   {\"id\":\"t1\",\"amount\":100.0,\"tags\":[\"food\",\"grocery\"]},\n...   {\"id\":\"t2\",\"amount\":-20,\"tags\":[\"transport\"]},\n...   {\"id\":\"t3\",\"amount\":50.5}\n... ]) == (130.5, 3, {\"food\":1,\"grocery\":1,\"transport\":1})\n>>> summarize_transactions([]) is None\n\"\"\"\nCode Snippet: \"\"\"python\ndef summarize_transactions(txns):\n    total = 0\n    counts = {}\n    for t in txns:\n        total += t[\"amount\"]\n        for tag in t[\"tags\"]:\n            counts[tag] = counts.get(tag, 0) + 1\n    return (total, len(txns), counts)\n\nI really appreciate your help!\n\"\"\""
            },
            {
                "role": "assistant",
                "content": "1. **Empty input**\n   - Requirement: return `None` if `txns` is empty.\n   - Snippet: enters the `for` loop zero times, but then does `return (total, len(txns), counts)`, i.e. `(0, 0, {})`, not `None`. ❌\n\n2. **Type validation**\n   - Requirement: raise `TypeError` if any `amount` is not an `int` or `float`.\n   - Snippet: directly adds `t[\"amount\"]`, without checking type. Non-numeric values would either silently convert or trigger a different error. ❌\n\n3. **Missing tags handling**\n   - Requirement: ignore missing or empty `\"tags\"`.\n   - Snippet: does `for tag in t[\"tags\"]` unconditionally, so if `\"tags\"` is absent it raises `KeyError`. ❌\n\n4. **Summation logic**\n   - Requirement: accumulate into a `float` total.\n   - Snippet: initializes `total = 0` (an `int`), then adds possibly floats; that works but doesn't enforce float semantics. (Not a functional error, but deviates from reference type.) ⚠️\n\n5. **Counting transactions**\n   - Requirement: `num_transactions = len(txns)`.\n   - Snippet: correctly returns `len(txns)` as the second element. ✔️\n\n6. **Step-by-step code analysis**\n   - Line 1: defines the function signature.\n   - Line 2: sets `total = 0`.\n   - Line 3: sets up `counts = {}`.\n   - Lines 4–7: iterates every record `t`, adds `t[\"amount\"]` to `total`, then iterates `t[\"tags\"]` (assumes tags always present).\n   - Line 8: returns `(total, len(txns), counts)` without any of the required guards.\n\n**Conclusion:**\nThe snippet fails to handle empty input, type-check amounts, or cope with missing `\"tags\"`. It only correctly counts the number of transactions. It does **not** cover all required functionalities. 🚫"
            }, 
            {
                "role": "user", 
                "content": "Problem Statement: \"\"\"\n{{PROBLEM}}\n{{EXAMPLE}}\n\"\"\"\nCode Snippet: \"\"\"{{LANGUAGE}}\n{{CODE1}}\n\nI really appreciate your help!\n\"\"\""
            }, 
            {
                "role": "assistant", 
                "content": "Evaluation:\n"
            }
        ],
        [#1
            {
                "role": "system", 
                "content": """
                You are a strict code judger. You will be provided with a problem statement and a code snippet that supposedly addresses the problem in {{LANGUAGE}}.
                Your task is to check if the code snippet covers the required functionalities. 
                Do not provide a corrected version. Please analysis step by step
                Evaluation Steps:
                1. Read the problem statement carefully and identify the required functionalities of the implementation. You can refer to the example and reference answer to understand the problem better.
                2. Carefully check input constraints, such as whether the input must be non-negative, within a certain range, or a non-empty string.
                3. Only use the information from the problem description and program. Be accurate and do not assume extra details. Do not evaluate based on function naming conventions.
                4. Unless explicitly stated in the problem, do NOT evaluate time complexity.
                5. Read the code snippet and analyze its logic. Check if the code snippet covers all the required functionalities of the problem. Check the syntax of the code snippet.
                6. Analyze the code step by step and line by line.
                7. Consider about edge cases. 
                8. Finally, conclude your evaluation.
                """
            }, 
            {
                "role": "user", 
                "content": "Problem Statement: \"\"\"\n{{PROBLEM}}\n{{EXAMPLE}}\n\"\"\"\nCode Snippet: \"\"\"{{LANGUAGE}}\n{{CODE1}}\n\nI really appreciate your help!\n\"\"\""
            }, 
            {
                "role": "assistant", 
                "content": "Evaluation:\n"
            }
        ],
        [#2
            {
                "role": "system", 
                "content": "You are a strict code judger. You will be provided with a problem statement and a code snippet that supposedly addresses the problem in {{LANGUAGE}}.\nYour task is to check if the code snippet covers the required functionalities. Do not provide a corrected version. Please analysis step by step. Finally, conclude your evaluation."
            }, 
            {
                "role": "user", 
                "content": "Problem Statement: \"\"\"\n{{PROBLEM}}\n{{EXAMPLE}}\n\"\"\"\nCode Snippet: \"\"\"{{LANGUAGE}}\n{{CODE1}}\n\nI really appreciate your help!\n\"\"\""
            }, 
            {
                "role": "assistant", 
                "content": "Evaluation:\n"
            }
        ]
    ],


    "analyze_prompt": [
        [
            {
                "role": "system",
                "content": "You will be provided with an analysis result of a code snippet.\nIf the analysis believes that the code snippet is correct, output: \"Yes\". Otherwise, output: \"No\"."
            },
            {
                "role": "user",
                "content": "Analysis Result:\"\"\"\n{{MISTAKES}}\n\"\"\""
            },
            {
                "role": "assistant",
                "content": "Final Answer (Yes or No):\n"
            }
        ]
]
}
