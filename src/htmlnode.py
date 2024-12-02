class HtmlNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        result = ""
        if self.props:
            for attribute in self.props:
                result += f" {attribute}={self.props[attribute]}"
        return result

    def __repr__(self):
        return f"HtmlNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

    def __eq__(self, other):
        return (
                self.tag == other.tag
                and self.value == other.value
                and self.children == other.children
                and self.props == other.props
        )


class LeafNode(HtmlNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError
        if not self.tag:
            return str(self.value)

        if self.props:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"


class ParentNode(HtmlNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        html_line = ""
        if not self.tag:
            raise ValueError("missing tag")
        if not self.children:
            raise ValueError("missing children")

        for child in self.children:
            html_line += child.to_html()
        return f"<{self.tag}>{html_line}</{self.tag}>"
