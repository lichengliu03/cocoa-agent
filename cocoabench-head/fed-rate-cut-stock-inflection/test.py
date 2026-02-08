"""
Test function for fed-rate-cut-stock-inflection.

Evaluates the count of stocks aligned with the Fed rate cut event.
"""

import json
import re

# Ground truth value
EXPECTED_ANSWER = "2"


def _extract_answer_from_text(text: str) -> str | None:
    """Extract answer from <answer>...</answer> tags."""
    # Try to find answer in <answer> tags
    answer_pattern = re.compile(r'<answer>(.*?)</answer>', re.IGNORECASE | re.DOTALL)
    match = answer_pattern.search(text)
    if match:
        return match.group(1).strip()
    return None


def _extract_answer_from_conversation(conversation: list) -> str | None:
    """Extract answer from conversation history."""
    # First, check assistant messages with tool_calls for task_complete with result parameter
    for message in reversed(conversation or []):
        if not isinstance(message, dict):
            continue
        if message.get("role") == "assistant" and message.get("tool_calls"):
            # Check if any tool call is task_complete with result
            for tc in message.get("tool_calls", []):
                if not isinstance(tc, dict):
                    continue
                func = tc.get("function", {})
                if func.get("name") == "task_complete":
                    # Extract result from tool call arguments
                    try:
                        args_str = func.get("arguments", "{}")
                        args = json.loads(args_str) if isinstance(args_str, str) else args_str
                        if "result" in args:
                            result_str = args["result"]
                            # Try to extract answer from result
                            answer = _extract_answer_from_text(result_str)
                            if answer:
                                return answer
                    except (json.JSONDecodeError, Exception):
                        pass

    # Search through assistant messages in reverse order for answer in content
    for message in reversed(conversation or []):
        if not isinstance(message, dict):
            continue
        if message.get("role") != "assistant":
            continue
        content = message.get("content") or ""
        answer = _extract_answer_from_text(content)
        if answer:
            return answer
    return None


def _normalize_answer(answer: str) -> str:
    """Normalize answer for comparison (strip whitespace)."""
    return answer.strip()


def test(result: dict) -> dict:
    """
    Test executor result.

    Args:
        result: Result dict from TaskExecutor.run_task()

    Returns:
        Test dict with metrics and pass/fail status
    """
    conversation = result.get("conversation") or []
    task_completed = result.get("status") == "success"

    # First, check if task_result is directly provided in result dict
    task_result = result.get("task_result")
    output_answer = None
    if task_result:
        # Try to extract answer from task_result
        output_answer = _extract_answer_from_text(task_result)

    # If not found in task_result, extract from conversation
    if not output_answer:
        output_answer = _extract_answer_from_conversation(conversation)

    if not output_answer:
        return {
            "passed": False,
            "feedback": "No valid answer found in assistant responses. Expected format: <answer>N</answer> where N is 0, 1, 2, or 3",
            "details": {
                "task_completed": task_completed,
                "conversation_length": len(conversation),
            },
        }

    # Normalize answers for comparison
    normalized_output = _normalize_answer(output_answer)
    normalized_expected = _normalize_answer(EXPECTED_ANSWER)

    # Check if answer matches
    answer_correct = normalized_output == normalized_expected

    # Additional validation: answer should be a valid integer 0-3
    try:
        answer_int = int(normalized_output)
        valid_range = 0 <= answer_int <= 3
    except ValueError:
        valid_range = False

    passed = task_completed and answer_correct

    feedback_parts = []
    feedback_parts.append(f"Found answer: {output_answer}")

    if not valid_range:
        feedback_parts.append(f"✗ Answer must be an integer between 0 and 3, got '{output_answer}'")
    else:
        feedback_parts.append(
            f"{'✓' if answer_correct else '✗'} Stock count: got '{output_answer}', expected '{EXPECTED_ANSWER}'."
        )

    if not task_completed:
        feedback_parts.append("✗ Task status is not success.")

    return {
        "passed": passed,
        "feedback": "\n".join(feedback_parts),
        "details": {
            "task_completed": task_completed,
            "output_answer": output_answer,
            "answer_correct": answer_correct,
            "expected_answer": EXPECTED_ANSWER,
            "valid_range": valid_range,
        },
    }
