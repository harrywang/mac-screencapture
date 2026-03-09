# macOS Screen Capture Skill

An [agent skill](https://agentskills.io) that gives AI coding agents the ability to take screenshots, record screen video, create GIFs, and build before/after comparison images on macOS.

Works with Claude Code, Cursor, Windsurf, and other AI coding agents that support the Agent Skills standard.

## Install

```bash
npx skills add harrywang/mac-screencapture
```

## What it does

Provides a complete reference and helper scripts for macOS `screencapture`:

- **Screenshots** — full screen, specific window, region, or interactive selection
- **Video recording** — timed recordings of full screen or specific windows
- **GIF conversion** — convert recordings to GIF via ffmpeg
- **Before/after images** — combine two screenshots into a comparison image

## Bundled scripts

### `get-window-id.swift`

Find window IDs by app name (needed for window-specific captures):

```bash
swift scripts/get-window-id.swift "Ghostty"
# 21680  Ghostty  My Window  361,200,800,632
```

### `before-after.py`

Create comparison images from two screenshots:

```bash
python3 scripts/before-after.py before.png after.png output.png
python3 scripts/before-after.py before.png after.png output.png --label-before "Old" --label-after "New"
```

## Quick reference

| Task | Command |
|------|---------|
| Full screen | `screencapture file.png` |
| Specific window | `screencapture -l <windowID> file.png` |
| Region | `screencapture -R x,y,w,h file.png` |
| Video (5s) | `screencapture -v -V 5 file.mov` |
| Video of window | `screencapture -v -V 5 -l <windowID> file.mov` |
| Convert to GIF | `ffmpeg -i file.mov -vf "fps=12,scale=800:-1:flags=lanczos" -loop 0 out.gif -y` |

## Requirements

- macOS (uses `screencapture` built-in)
- ffmpeg for GIF conversion (`brew install ffmpeg`)
- Pillow for before/after images (`pip3 install Pillow`)
- Screen Recording permission may be needed for video

## License

MIT
