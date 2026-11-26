"""Decode Godot 2.x PHashTranslation (.xl) using a known key list. Smaz codebook is read from the game exe."""
import struct, sys, json, re

def smaz_table(exe=None):
    import os
    return [s.encode('latin-1') for s in json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'smaz_rcb.json')))]

def smaz_decompress(data, rcb):
    out = bytearray(); i = 0
    while i < len(data):
        c = data[i]
        if c == 254:
            out.append(data[i+1]); i += 2
        elif c == 255:
            n = data[i+1] + 1
            out += data[i+2:i+2+n]; i += 2 + n
        else:
            out += rcb[c]; i += 1
    return bytes(out)

class R:
    def __init__(s, b): s.b = b; s.p = 0
    def u32(s):
        v = struct.unpack_from("<I", s.b, s.p)[0]; s.p += 4; return v
    def u64(s):
        v = struct.unpack_from("<Q", s.b, s.p)[0]; s.p += 8; return v
    def ustr(s):
        n = s.u32(); v = s.b[s.p:s.p+n]; s.p += n; return v.rstrip(b"\0").decode("utf-8")

def load_xl(path):
    r = R(open(path, "rb").read())
    assert r.b[:4] == b"RSRC"; r.p = 4
    be, real64, vmaj, vmin, vfmt = r.u32(), r.u32(), r.u32(), r.u32(), r.u32()
    rtype = r.ustr(); r.u64(); r.p += 14 * 4
    strs = [r.ustr() for _ in range(r.u32())]
    for _ in range(r.u32()): r.ustr(); r.ustr()
    ints = [(r.ustr(), r.u64()) for _ in range(r.u32())]
    r.p = ints[0][1]
    t = r.ustr(); props = {}
    for _ in range(r.u32()):
        name = strs[r.u32()]; vt = r.u32()
        if vt == 32:
            n = r.u32(); props[name] = struct.unpack_from("<%dI" % n, r.b, r.p); r.p += 4 * n
        elif vt == 31:
            n = r.u32(); props[name] = r.b[r.p:r.p+n]; r.p += n + ((4 - n % 4) % 4)
        elif vt == 5:
            props[name] = r.ustr()
        elif vt == 34:
            props[name] = [r.ustr() for _ in range(r.u32())]
        else:
            raise Exception("variant %d for %s" % (vt, name))
    return props

def gd_hash(d, s):
    if d == 0: d = 0x1000193
    for c in s:
        d = ((d * 0x1000193) & 0xFFFFFFFF) ^ c
    return d

class XL:
    def __init__(s, path, rcb):
        p = load_xl(path); s.ht = p["hash_table"]; s.bt = p["bucket_table"]; s.st = p["strings"]; s.rcb = rcb
    def count(s):
        n = 0
        for p in set(s.ht):
            if p != 0xFFFFFFFF: n += s.bt[p]
        return n
    def get(s, key):
        k = key.encode("utf-8")
        p = s.ht[gd_hash(0, k) % len(s.ht)]
        if p == 0xFFFFFFFF: return None
        size, func = s.bt[p], s.bt[p+1]
        h = gd_hash(func, k)
        for i in range(size):
            e = p + 2 + i * 4
            if s.bt[e] == h:
                ofs, cs, us = s.bt[e+1], s.bt[e+2], s.bt[e+3]
                raw = s.st[ofs:ofs+cs]
                if cs != us: raw = smaz_decompress(raw, s.rcb)
                return raw.rstrip(b"\0").decode("utf-8")
        return None
