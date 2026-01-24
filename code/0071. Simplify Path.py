class Solution(object):
    def simplifyPath(self, path):
        seg_path = path.split("/")
        new_path = []
        for node in seg_path:
            if not node or node == ".":
                continue
            elif node == "..":
                if len(new_path)>0:
                    new_path.pop()
            else:
                new_path.append("/" + node)
        if not new_path:
            new_path = "/"
        return "".join(new_path)
