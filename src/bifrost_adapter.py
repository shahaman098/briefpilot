import os
import json
import logging
import urllib.request
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)

class BifrostGatewayAdapter:
    """
    Adapter for routing LLM synthesis requests through Maxim AI's Bifrost Gateway
    (https://github.com/maximhq/bifrost) for sub-millisecond routing, rate limit
    governance, and enterprise observability.
    """
    def __init__(
        self,
        base_url: Optional[str] = None,
        api_key: Optional[str] = None,
        model: Optional[str] = None
    ):
        self.base_url = (base_url or os.getenv("BIFROST_BASE_URL", "http://localhost:8080/v1")).rstrip("/")
        self.api_key = api_key or os.getenv("BIFROST_API_KEY", "")
        self.model = model or os.getenv("BIFROST_MODEL", "gemini-3.5-flash")

    def is_available(self) -> bool:
        """Check if local or remote Bifrost gateway is responding."""
        try:
            req = urllib.request.Request(f"{self.base_url}/health", method="GET")
            with urllib.request.urlopen(req, timeout=1.5) as resp:
                return resp.status == 200
        except Exception:
            return False

    def route_completion(self, system_prompt: str, user_prompt: str) -> Optional[str]:
        """
        Routes the prompt through Bifrost OpenAI-compatible endpoint.
        Returns synthesized text or None if gateway is unreachable.
        """
        if not self.is_available():
            logger.info("Bifrost gateway not active; falling back to direct provider API.")
            return None

        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "temperature": 0.2
        }

        headers = {
            "Content-Type": "application/json"
        }
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"

        try:
            req = urllib.request.Request(
                f"{self.base_url}/chat/completions",
                data=json.dumps(payload).encode("utf-8"),
                headers=headers,
                method="POST"
            )
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data["choices"][0]["message"]["content"]
        except Exception as e:
            logger.warning(f"Bifrost completion error: {e}")
            return None
