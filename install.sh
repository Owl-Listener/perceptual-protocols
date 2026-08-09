#!/bin/sh
# install.sh — copy perceptual protocol templates into a project.
#
# This is a convenience, not a dependency. It copies markdown files and does
# nothing else: no network calls, no package manager, no config written, no
# state kept. Copying the files by hand is the canonical path and always works.
#
#   ./install.sh --list
#   ./install.sh --into ~/projects/my-app vocab voice tokens
#   ./install.sh --into ~/projects/my-app all
#
set -eu

SRC=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)

# name : source template : installed filename
PROTOCOLS="
vocab:vocab-protocol/VOCAB.md:vocab.md
motion:motion-protocol/MOTION.md:motion.md
voice:voice-protocol/VOICE.md:voice.md
sound:listen-protocol/SOUND.md:sound.md
tokens:tokens-protocol/TOKENS.md:tokens.md
"

usage() {
	cat <<'EOF'
Usage: ./install.sh --into <dir> <protocol>...
       ./install.sh --list

Options:
  --into <dir>   Project directory to install into. Required.
  --force        Overwrite files that already exist.
  --list         List the protocols available to install.
  -h, --help     Show this message.

Protocols:
  vocab motion voice sound tokens
  all            Install every protocol above.

Each protocol installs one lowercase markdown file into <dir>. Fill it in,
then point your agent at it. There is no build step and nothing to run.
EOF
}

list_protocols() {
	echo "Available protocols:"
	echo "$PROTOCOLS" | while IFS=: read -r name src dest; do
		[ -n "$name" ] || continue
		printf '  %-8s -> %-10s (from %s)\n' "$name" "$dest" "$src"
	done
	echo
	echo "Not installable as templates: mood, listen, situation, trace, critique."
	echo "Those are authored from your own references via a prompt rather than"
	echo "filled in from a blank file — see each protocol's PROMPT.md."
}

lookup() {
	echo "$PROTOCOLS" | while IFS=: read -r name src dest; do
		[ "$name" = "$1" ] || continue
		echo "$src:$dest"
	done
}

INTO=""
FORCE=0
WANTED=""

while [ $# -gt 0 ]; do
	case "$1" in
		--into)
			[ $# -ge 2 ] || { echo "install.sh: --into needs a directory" >&2; exit 2; }
			INTO="$2"; shift 2 ;;
		--force) FORCE=1; shift ;;
		--list) list_protocols; exit 0 ;;
		-h|--help) usage; exit 0 ;;
		-*) echo "install.sh: unknown option '$1'" >&2; usage >&2; exit 2 ;;
		*) WANTED="$WANTED $1"; shift ;;
	esac
done

if [ -z "$INTO" ]; then
	echo "install.sh: --into <dir> is required" >&2
	usage >&2
	exit 2
fi

if [ -z "${WANTED# }" ]; then
	echo "install.sh: name at least one protocol, or 'all'" >&2
	usage >&2
	exit 2
fi

if [ ! -d "$INTO" ]; then
	echo "install.sh: '$INTO' is not a directory" >&2
	exit 1
fi

# Note: the guard below must be `|| continue` rather than `&& printf`. The
# last line of $PROTOCOLS is empty, so an `&&` list would leave the while
# loop — and therefore this assignment — with status 1, which `set -e` turns
# into a silent early exit that installs nothing.
case " $WANTED " in
	*" all "*)
		WANTED=$(echo "$PROTOCOLS" | while IFS=: read -r name _rest; do
			[ -n "$name" ] || continue
			printf '%s ' "$name"
		done) ;;
esac

status=0
for name in $WANTED; do
	pair=$(lookup "$name")
	if [ -z "$pair" ]; then
		echo "install.sh: unknown protocol '$name' (try --list)" >&2
		status=1
		continue
	fi

	src="$SRC/${pair%%:*}"
	dest="$INTO/${pair##*:}"

	if [ ! -f "$src" ]; then
		echo "install.sh: missing template $src" >&2
		status=1
		continue
	fi

	if [ -e "$dest" ] && [ "$FORCE" -eq 0 ]; then
		echo "skip    ${pair##*:} (already exists — pass --force to overwrite)"
		continue
	fi

	cp "$src" "$dest"
	echo "install ${pair##*:}"
done

echo
if [ "$status" -eq 0 ]; then
	echo "Done. Fill in the files you installed, then tell your agent to read them."
else
	echo "Finished with errors — see above."
fi
exit $status
