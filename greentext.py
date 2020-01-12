import znc


def apply_greentext(message):
    if message.s.startswith(">"):
        message.s = "\00303" + message.s


class greentext(znc.Module):
    def OnChanMsg(self, nick, channel, message):
        apply_greentext(message)
        return znc.CONTINUE

    def OnUserMsg(self, target, message):
        apply_greentext(message)
        return znc.CONTINUE
