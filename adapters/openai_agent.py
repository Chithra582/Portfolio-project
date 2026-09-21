"""OpenAI Agents SDK adapter for portfolio-project-agent"""

SYSTEM_PROMPT = """You are portfolio-project-agent, the AI companion for Chithra R's
professional portfolio website. Explain the glassmorphism design system, IntersectionObserver
scroll-reveal animations, and portfolio section structure. Ground all answers in index.html,
style.css, and script.js. Never claim Tailwind, React, or GSAP are used."""

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "design_inspector",
            "description": "Inspect CSS glassmorphism design properties and variables",
            "parameters": {
                "type": "object",
                "properties": {
                    "property": {"type": "string"},
                    "element": {"type": "string"}
                }
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "animation_navigator",
            "description": "Navigate scroll-reveal and animation systems",
            "parameters": {
                "type": "object",
                "properties": {
                    "animation_type": {"type": "string", "enum": ["scroll-reveal","blob","hamburger","navbar-scroll"]},
                    "detail_level": {"type": "string", "enum": ["summary","full"]}
                }
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "section_retriever",
            "description": "Retrieve portfolio section HTML structure and content",
            "parameters": {
                "type": "object",
                "properties": {
                    "section": {"type": "string", "enum": ["home","about","skills","projects","experience","contact","navbar","all"]}
                },
                "required": ["section"]
            }
        }
    }
]

def export_openai_spec():
    return {"system_prompt": SYSTEM_PROMPT, "tools": TOOLS, "model": "gpt-4o-mini"}
