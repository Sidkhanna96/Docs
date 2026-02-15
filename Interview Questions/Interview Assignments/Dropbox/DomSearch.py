"""
Dropbox

Search the DOM

Usually only asked in interviews for frontend positions.

Given the root tag of a DOM and a CSS selector (like 'div > span > href'), return
all tags in the DOM that would be selected by the selector.


Most people fail to consider the following case
div (1) > div (2) > div (3) > span (4) > div (5) > span (6) > href (7) > span (8) > href (9) > href (10)
You should return tags 7, 9, and 10.

As you iterate over the DOM tree and you find a match in the CSS sequence, you should proceed as if (1) you are taking
the tag, and (2) as if you are omitting the tag.

"""

from collections import deque


class DOMSearch:
    def __init__(self):
        pass

    def searchDOM(self, node, cssSelector):
        tags = cssSelector.split(">")

        queue = deque([(node, 0)])

        while queue:
            node, tagIndex = queue.popleft()

            for neighbors in node.neighbors:
                if node.tag == tags[tagIndex]:
                    queue.append([(neighbors, tagIndex + 1)])

                queue.append()
