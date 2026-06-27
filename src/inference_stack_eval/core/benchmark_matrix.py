from __future__ import annotations

BENCHMARK_WORKLOADS = [
    {
        "workload": "short_chat",
        "input_shape": "short prompt, short history",
        "output_shape": "100-500 tokens",
        "stress_point": "TTFT and scheduler overhead",
    },
    {
        "workload": "long_context_rag",
        "input_shape": "8k-64k prompt with retrieved context",
        "output_shape": "300-1,000 tokens",
        "stress_point": "prefill time and KV-cache pressure",
    },
    {
        "workload": "structured_json",
        "input_shape": "schema-heavy prompt",
        "output_shape": "validated JSON",
        "stress_point": "guided decoding and retry behavior",
    },
    {
        "workload": "tool_calling_agents",
        "input_shape": "stable tool schema plus dynamic state",
        "output_shape": "tool calls and reasoning text",
        "stress_point": "prefix reuse and traceability",
    },
    {
        "workload": "batch_generation",
        "input_shape": "many parallel offline requests",
        "output_shape": "variable length",
        "stress_point": "throughput and fairness under load",
    },
    {
        "workload": "repeated_prefix",
        "input_shape": "stable policy/tools with changing user input",
        "output_shape": "variable length",
        "stress_point": "cache hit rate and prefill amortization",
    },
]
