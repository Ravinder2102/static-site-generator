from enum import Enum

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'

def block_to_block_type(block: str) -> BlockType:
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if line.startswith(">"):
                return BlockType.QUOTE
            return BlockType.PARAGRAPH
    if block.startswith("- "):
        for line in lines:
            if line.startswith("- "):
                return BlockType.UNORDERED_LIST
            return BlockType.PARAGRAPH
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if line.startswith(f"{i}. "):
                return BlockType.ORDERED_LIST
            i += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
