#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

def make_icon(size, path):
    img = Image.new('RGB', (size, size), '#0f172a')
    draw = ImageDraw.Draw(img)
    
    # Circle background
    margin = size * 0.1
    draw.ellipse([margin, margin, size-margin, size-margin], fill='#1e293b')
    
    # Baseball stitching lines (simple circle)
    lw = max(2, size // 40)
    cx, cy, r = size//2, size//2, size*0.3
    draw.ellipse([cx-r, cy-r, cx+r, cy+r], outline='#e2e8f0', width=lw)
    
    # ⚾ emoji-style stitches
    draw.arc([cx-r*0.5, cy-r, cx+r*0.5, cy+r], -30, 30, fill='#ef4444', width=lw)
    draw.arc([cx-r*0.5, cy-r, cx+r*0.5, cy+r], 150, 210, fill='#ef4444', width=lw)
    
    img.save(path, 'PNG')
    print(f"Created {path}")

os.makedirs('/home/claude/mlb-tracker/public', exist_ok=True)
make_icon(192, '/home/claude/mlb-tracker/public/icon-192.png')
make_icon(512, '/home/claude/mlb-tracker/public/icon-512.png')
