"""Godot 2.x PCK lister/extractor (format version 0)."""
import struct, sys, os, fnmatch

def read_index(path):
    with open(path, "rb") as f:
        assert f.read(4) == b"GDPC"
        ver, major, minor, rev = struct.unpack("<4I", f.read(16))
        f.read(16 * 4)
        (count,) = struct.unpack("<I", f.read(4))
        files = []
        for _ in range(count):
            (ln,) = struct.unpack("<I", f.read(4))
            name = f.read(ln).rstrip(b"\0").decode("utf-8")
            ofs, size = struct.unpack("<QQ", f.read(16))
            f.read(16)
            files.append((name, ofs, size))
    return (ver, major, minor, rev), files

def main():
    pck, cmd = sys.argv[1], sys.argv[2]
    hdr, files = read_index(pck)
    if cmd == "list":
        out = sys.argv[3]
        with open(out, "w", encoding="utf-8") as o:
            o.write("# pck %s files=%d\n" % (hdr, len(files)))
            for n, ofs, size in files:
                o.write("%d\t%s\n" % (size, n))
        print(hdr, len(files))
    elif cmd == "extract":
        outdir = sys.argv[3]
        pats = sys.argv[4:]
        n_out = 0
        with open(pck, "rb") as f:
            for n, ofs, size in files:
                if not any(fnmatch.fnmatch(n, p) for p in pats):
                    continue
                rel = n.replace("res://", "")
                dst = os.path.join(outdir, rel)
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                f.seek(ofs)
                with open(dst, "wb") as o:
                    o.write(f.read(size))
                n_out += 1
        print("extracted", n_out)

if __name__ == "__main__":
    main()
