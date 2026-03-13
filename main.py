"""
AI Chat Assistant — Interactive CLI
=====================================
Main entry point with a rich terminal interface.
Commands: /help, /clear, /mode, /chain, /eval, /status, /exit
"""

import sys
from colorama import init, Fore, Style

from agent.chat_agent import ChatAgent
from prompts.system_prompt import ROLE_CONFIGS
import config

# Initialize colorama for Windows ANSI support
init(autoreset=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  DISPLAY HELPERS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BANNER = f"""
{Fore.CYAN}{'━' * 60}
  🤖  AI Chat Assistant — Prompt Engineered
{'━' * 60}{Style.RESET_ALL}
{Fore.WHITE}  Model       : {config.MODEL_NAME}
  Provider    : Google Gemini (Free Tier)
  Memory      : {config.MEMORY_WINDOW_SIZE}-turn sliding window
  Chaining    : {"ON" if config.ENABLE_PROMPT_CHAINING else "OFF"}
  Evaluation  : {"ON" if config.ENABLE_SELF_EVALUATION else "OFF"}
{Fore.YELLOW}
  Commands:
    /help       Show this help message
    /clear      Clear conversation memory
    /mode <r>   Switch role (default, coder, tutor, analyst, creative)
    /chain      Toggle prompt chaining on/off
    /eval       Toggle self-evaluation on/off
    /status     Show current agent configuration
    /exit       Exit the assistant
{Fore.CYAN}{'━' * 60}{Style.RESET_ALL}
"""

HELP_TEXT = f"""
{Fore.YELLOW}Available Commands:{Style.RESET_ALL}
  {Fore.GREEN}/help{Style.RESET_ALL}         Show this help message
  {Fore.GREEN}/clear{Style.RESET_ALL}        Clear conversation memory
  {Fore.GREEN}/mode <role>{Style.RESET_ALL}  Switch role: {', '.join(ROLE_CONFIGS.keys())}
  {Fore.GREEN}/chain{Style.RESET_ALL}        Toggle prompt chaining on/off
  {Fore.GREEN}/eval{Style.RESET_ALL}         Toggle self-evaluation on/off
  {Fore.GREEN}/status{Style.RESET_ALL}       Show current agent configuration
  {Fore.GREEN}/exit{Style.RESET_ALL}         Exit the assistant
"""


def print_role_name(role: str):
    """Print the current role banner."""
    name = ROLE_CONFIGS.get(role, ROLE_CONFIGS["default"])["role_name"]
    print(f"\n{Fore.MAGENTA}[Role: {name}]{Style.RESET_ALL}")


def print_response(result: dict):
    """Pretty-print the agent's response with optional metadata."""
    # Main response
    print(f"\n{Fore.GREEN}🤖 Assistant:{Style.RESET_ALL}")
    print(f"{result['response']}")

    # Chain metadata (if prompt chaining was used)
    if result.get("chain_metadata"):
        steps = result["chain_metadata"].get("chain_steps", [])
        classification = result["chain_metadata"].get("classification", {})
        print(
            f"\n{Fore.BLUE}  ⛓  Chain steps: {' → '.join(steps)}"
            f"  |  Intent: {classification.get('intent', '?')}"
            f"  |  Complexity: {classification.get('complexity', '?')}"
            f"{Style.RESET_ALL}"
        )

    # Evaluation scores (if self-evaluation was used)
    if result.get("evaluation"):
        ev = result["evaluation"]
        score = ev.get("overall_score", "?")
        retried = " (retried)" if result.get("retried") else ""
        print(
            f"{Fore.BLUE}  📊  Quality: {score}/1.0{retried}"
            f"  |  Relevance: {ev.get('relevance', '?')}"
            f"  |  Accuracy: {ev.get('accuracy', '?')}"
            f"  |  Clarity: {ev.get('clarity', '?')}"
            f"{Style.RESET_ALL}"
        )


def print_status(status: dict):
    """Print the current agent status."""
    print(f"\n{Fore.CYAN}━━━ Agent Status ━━━━━━━━━━━━━━━━━━━━{Style.RESET_ALL}")
    for key, value in status.items():
        print(f"  {Fore.WHITE}{key:20s}{Style.RESET_ALL}: {value}")
    print(f"{Fore.CYAN}{'━' * 40}{Style.RESET_ALL}")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  MAIN LOOP
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def main():
    # ── Validate API key ─────────────────────────────────────
    if not config.GOOGLE_API_KEY or config.GOOGLE_API_KEY == "your-google-api-key-here":
        print(f"\n{Fore.RED}❌  Error: GOOGLE_API_KEY not set.{Style.RESET_ALL}")
        print(f"   1. Get a free key at: {Fore.YELLOW}https://aistudio.google.com/apikey{Style.RESET_ALL}")
        print(f"   2. Copy {Fore.YELLOW}.env.example{Style.RESET_ALL} → "
              f"{Fore.YELLOW}.env{Style.RESET_ALL} and add your API key.\n")
        sys.exit(1)

    # ── Initialize agent ─────────────────────────────────────
    agent = ChatAgent()
    print(BANNER)
    print_role_name(agent.role)

    # ── Chat loop ────────────────────────────────────────────
    while True:
        try:
            user_input = input(f"\n{Fore.YELLOW}You:{Style.RESET_ALL} ").strip()
        except (EOFError, KeyboardInterrupt):
            print(f"\n{Fore.CYAN}Goodbye! 👋{Style.RESET_ALL}\n")
            break

        if not user_input:
            continue

        # ── Handle commands ──────────────────────────────────
        if user_input.startswith("/"):
            cmd_parts = user_input.split(maxsplit=1)
            cmd = cmd_parts[0].lower()

            if cmd == "/exit":
                print(f"\n{Fore.CYAN}Goodbye! 👋{Style.RESET_ALL}\n")
                break

            elif cmd == "/help":
                print(HELP_TEXT)

            elif cmd == "/clear":
                agent.clear_memory()
                print(f"{Fore.GREEN}✅ Conversation memory cleared.{Style.RESET_ALL}")

            elif cmd == "/mode":
                if len(cmd_parts) < 2:
                    print(f"{Fore.YELLOW}Usage: /mode <role>{Style.RESET_ALL}")
                    print(f"  Available: {', '.join(ROLE_CONFIGS.keys())}")
                else:
                    role = cmd_parts[1].strip().lower()
                    try:
                        agent.set_role(role)
                        print(f"{Fore.GREEN}✅ Switched to role: "
                              f"{ROLE_CONFIGS[role]['role_name']}{Style.RESET_ALL}")
                        print_role_name(role)
                    except ValueError as e:
                        print(f"{Fore.RED}❌ {e}{Style.RESET_ALL}")

            elif cmd == "/chain":
                state = agent.toggle_chaining()
                label = "ON" if state else "OFF"
                print(f"{Fore.GREEN}✅ Prompt chaining: {label}{Style.RESET_ALL}")

            elif cmd == "/eval":
                state = agent.toggle_evaluation()
                label = "ON" if state else "OFF"
                print(f"{Fore.GREEN}✅ Self-evaluation: {label}{Style.RESET_ALL}")

            elif cmd == "/status":
                print_status(agent.get_status())

            else:
                print(f"{Fore.RED}Unknown command: {cmd}. "
                      f"Type /help for options.{Style.RESET_ALL}")

            continue

        # ── Normal conversation ──────────────────────────────
        try:
            print(f"\n{Fore.BLUE}⏳ Thinking...{Style.RESET_ALL}", end="", flush=True)
            result = agent.chat(user_input)
            # Clear the "Thinking..." line
            print("\r" + " " * 30 + "\r", end="")
            print_response(result)

        except Exception as e:
            print(f"\n{Fore.RED}❌ Error: {e}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}   Check your API key and network connection.{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
