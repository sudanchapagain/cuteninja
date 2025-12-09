import re
from typing import Tuple, Dict


class JinjaProcessor:
    def __init__(self):
        self.token_map: Dict[str, str] = {}
        self.token_counter = 0

    def extract_jinja(self, source: str) -> Tuple[str, Dict[str, str]]:
        self.token_map = {}
        self.token_counter = 0

        # pattern to match Jinja syntax: {{ }}, {% %}, {# #}
        pattern = r"(\{\{.*?\}\}|\{%.*?%\}|\{#.*?#\})"

        def replace_jinja(match):
            token = match.group(0)
            placeholder = f"__JINJA_{self.token_counter}__"
            self.token_map[placeholder] = token
            self.token_counter += 1

            # If the token contains newlines then wrap it as a KDL text node
            if "\n" in token:
                return f'- "{placeholder}"'
            return placeholder

        # replace all Jinja blocks with placeholders
        cleaned = re.sub(pattern, replace_jinja, source, flags=re.DOTALL)

        # handle standalone single-line Jinja blocks
        lines = cleaned.split("\n")
        final_lines = []

        for line in lines:
            stripped = line.strip()
            # check if line is only a placeholder (i.e. standalone block)
            if re.fullmatch(r"__JINJA_\d+__", stripped):
                # to KDL text node
                indent = len(line) - len(line.lstrip())
                final_lines.append(" " * indent + f'- "{stripped}"')
            else:
                final_lines.append(line)

        return "\n".join(final_lines), self.token_map

    def restore_jinja(self, html: str, token_map: Dict[str, str]) -> str:
        result = html
        for placeholder, token in token_map.items():
            result = result.replace(placeholder, token)
        return result

    def get_source_map(self) -> Dict[str, str]:
        return self.token_map
