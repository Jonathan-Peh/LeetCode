class Solution(object):
    def fullJustify(self, words, maxWidth):
        text = []
        line = []
        unjust_length = -1
        for w in words:
            if unjust_length + 1 + len(w) <= maxWidth:
                line.append(w)
                unjust_length += 1 + len(w)
            else:
                leftover = maxWidth - unjust_length
                if len(line) > 1:
                    even_space = leftover//(len(line)-1) + 1 # + 1 because all already have default one space
                    uneven_space = leftover%(len(line)-1)
                    just_line = ""
                    for i in range(len(line)):
                        just_line += line[i]
                        if i < len(line)-1:
                            just_line += " "*even_space
                            if i < uneven_space:
                                just_line += " "
                else:
                    just_line = line[0] + " "*leftover

                text.append(just_line)

                line = [w]
                unjust_length = len(w)

        leftover = maxWidth - unjust_length
        text.append(" ".join(line) + " "*leftover)

        return text
