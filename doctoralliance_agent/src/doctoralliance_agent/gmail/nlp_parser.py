def parse_reply(text: str) -> dict:
    out = {}
    for line in text.splitlines():
        if ':' in line:
            k,v = line.split(':',1)
            out[k.strip()] = v.strip()
    return out
