"""Lyzr Agent adapter for portfolio-project-agent"""

def export_lyzr_agent():
    return {
        "agent_name": "portfolio-project-agent",
        "agent_description": (
            "AI companion for Chithra R's Professional Portfolio Project -- a glassmorphism "
            "dark-mode website with IntersectionObserver scroll-reveal animations, CSS "
            "variables, floating blob backgrounds, and responsive hamburger navigation."
        ),
        "system_prompt": (
            "You are portfolio-project-agent. Explain Chithra R's portfolio design and "
            "implementation. Use glassmorphism-design-guide for CSS design questions, "
            "scroll-animation-explainer for IntersectionObserver and transition questions, "
            "and portfolio-structure-walkthrough for section layout questions. "
            "Ground all answers in the committed source files."
        ),
        "tools": [
            {"name": "design-inspector", "type": "code-analysis"},
            {"name": "animation-navigator", "type": "code-analysis"},
            {"name": "section-retriever", "type": "data-retrieval"}
        ],
        "model_config": {"model": "gemini-2.0-flash", "temperature": 0.2}
    }
