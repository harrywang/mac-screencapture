---
name: screencapture
description: Take screenshots and screen recordings on macOS. Capture full screen, specific windows, or regions. Convert to gif. Use when the user wants to capture, screenshot, record, or gif their screen.
---

# Screen Capture

Take screenshots and screen recordings on macOS using the `screencapture` CLI.

## Quick Reference

| Task | Command |
|------|---------|
| Full screen | `screencapture /path/to/file.png` |
| Specific window | `screencapture -l <windowID> /path/to/file.png` |
| Region | `screencapture -R x,y,w,h /path/to/file.png` |
| Interactive select | `screencapture -i /path/to/file.png` |
| Video (timed) | `screencapture -v -V <seconds> /path/to/file.mov` |
| Video of window | `screencapture -v -V <seconds> -l <windowID> /path/to/file.mov` |
| No sound | add `-x` |
| With cursor | add `-C` |
| To clipboard | add `-c` (no filename) |
| Delay | `-T <seconds>` |
| Format | `-t jpg` / `-t png` / `-t pdf` |

## Finding Window IDs

Use the bundled helper to find window IDs:

```bash
swift "${CLAUDE_SKILL_DIR}/scripts/get-window-id.swift" "AppName"
```

Output: `windowID  ownerName  windowTitle  x,y,width,height`

Example:
```bash
swift "${CLAUDE_SKILL_DIR}/scripts/get-window-id.swift" "Ghostty"
# 21680  Ghostty  My Window Title  361,200,800,632
```

## Converting to GIF

Use ffmpeg to convert .mov recordings to gif:

```bash
ffmpeg -i recording.mov -vf "fps=12,scale=800:-1:flags=lanczos" -loop 0 output.gif -y
```

Adjust parameters:
- `fps=12` — frame rate (lower = smaller file, choppier)
- `scale=800:-1` — width in pixels, height auto
- `-loop 0` — loop forever

## Cropping Video Before GIF Conversion

If you recorded full screen but only want a portion:

```bash
ffmpeg -i fullscreen.mov -vf "crop=w:h:x:y,fps=12,scale=800:-1:flags=lanczos" -loop 0 output.gif -y
```

Note: for Retina displays, multiply point coordinates by 2 for pixel coordinates.

## Creating Before/After Comparison Images

Use Python with Pillow to combine screenshots:

```bash
pip3 install Pillow --user 2>/dev/null
python3 "${CLAUDE_SKILL_DIR}/scripts/before-after.py" before.png after.png output.png
```

## Instructions

When the user asks to take a screenshot or recording:

1. Determine what to capture (full screen, window, or region)
2. If capturing a specific window, use the `get-window-id.swift` helper to find the window ID
3. Run the appropriate `screencapture` command
4. If they want a gif, convert with ffmpeg (install via `brew install ffmpeg` if needed)
5. Show the result using the Read tool

## Requirements

- **macOS only** — `screencapture` is a macOS built-in
- **ffmpeg** — needed for gif conversion (`brew install ffmpeg`)
- **Screen Recording permission** — may be needed for video capture
